library(tidyverse)
library(caret)
library(quanteda)
library(future)
library(future.apply)
library(quanteda.textmodels)

class_dir <- "/data607-data-acquisition-and-management/projects/"
proj_path <- paste0(getwd(), class_dir,  "spam-classifier/")

load_files_to_df <- function(file_path, file_count = 1) {
  file_names <- list.files(path = file_path, full.names = TRUE, pattern = "^\\d+.*")
  message(paste0("## loading ", file_count, " files from path ", file_path))
  file_names <- head(file_names, file_count)
  text_data <- set_names(file_names, nm = basename(file_names)) %>%
    map_df(~tibble(name = .y, data = read_file(.x)), .y = names(.))
  return(text_data)
}

preprocess_and_create_dfm <- function(df, cache_filename = "dfm_cache.rds") {
  f_cache <- paste0(proj_path, cache_filename)

  message("### preprocessing ...")
  message("#### setting up parallel text processing ...")
  plan(multisession, workers = 4)
  message("#### cleaning ...")
  clean_data <- future.apply::future_sapply(df$data, FUN = function(text) {
    text %>%
      # str_replace_all("^(From|Return-Path|Received|Message-ID):.*", "") %>%
      str_replace_all("\\n", " ") %>%
      str_squish()
  }, USE.NAMES = FALSE)

  message("#### tokenizing and creating dfm/document feature matrix ... ")
  tokens <- tokens(clean_data, what = "word", 
    remove_punct = TRUE, remove_symbols = TRUE)
  tokens <- tokens_remove(tokens, stopwords("en"))

  dfm <- dfm(tokens)

  message("#### removing sparse terms ...")
  dfm <- dfm_trim(dfm, sparsity = .95)
  # message("## caching dfm ...")
  # saveRDS(dfm, f_cache)
  return(dfm)
}

message("## Loading email files")
mail <- load_files_to_df(paste0(proj_path,
  "nogit_easy_ham/"), file_count = 100)
spam <- load_files_to_df(paste0(proj_path, 
  "nogit_spam/"), file_count = 100)
# Combine datasets and add labels
all_mail <- bind_rows(
  mail %>% mutate(label = 1),
  spam %>% mutate(label = 0)
) %>% sample_frac(size = 1)

message("## Split into test and training")
split_index <- createDataPartition(all_mail$label, p = 0.8, list = FALSE)
train_set <- all_mail[split_index, ]
test_set <- all_mail[-split_index, ]

message("## Building training dataset")
train_set_dfm <- preprocess_and_create_dfm(train_set, 
  cache_filename = "train_set_dfm.rds")
message("## Building test dataset")
test_set_dfm <- preprocess_and_create_dfm(test_set, 
  cache_filename = "test_set_dfm.rds")
test_set_dfm <- dfm_match(test_set_dfm, featnames(train_set_dfm))

message("## Modeling and predicting")
model <- textmodel_nb(train_set_dfm, y = factor(train_set$label))
predictions <- predict(model, newdata = test_set_dfm)
true_labels <- factor(test_set$label)
conf_mat <- confusionMatrix(predictions, true_labels)
print(conf_mat)