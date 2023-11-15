library(tidyverse)
library(caret)
library(quanteda)
library(dplyr)
library(future)
library(future.apply)
library(e1071)
library(tm)

proj_path <- paste0(getwd(), "/data607-data-acquisition-and-management/projects/spam-classifier/")


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

  if (file.exists(f_cache)) {
    message(paste0("Returning ", cache_filename, " from file system"))
    return(readRDS(f_cache))
  } else {
    message("#### cache does not exist: building new ...")
    # Set up future to use a multisession - this will enable parallel processing
    plan(multisession, workers = 4)
    # Preprocessing text data in parallel
    message("#### cleaning ...")
    clean_data <- future.apply::future_sapply(df$data, FUN = function(text) {
      text %>%
        str_replace_all("^(From|Return-Path|Received|Message-ID):.*", "") %>%
        str_replace_all("\\n", " ") %>%
        str_squish()
    }, USE.NAMES = FALSE)

    # Tokenizing and creating a DFM (Document-Feature Matrix)
    message("#### tokenizing ...")
    tokens <- tokens(clean_data, what = "word", remove_punct = TRUE, remove_symbols = TRUE)
    tokens <- tokens_remove(tokens, stopwords("en"))

    dfm <- dfm(tokens)

    sparse_threshold <- 0.01
    message("## removing sparse terms ...")
    dfm <- dfm_trim(dfm, sparsity = sparse_threshold) # remove sparse terms. 
    message("## caching dfm ...")
    saveRDS(dfm, f_cache)

    return(dfm)
  }
}

# Example usage:

# file_count = 150 -> 52 seconds 
# file_count = 250 -> 2 minutes and 41 seconds

message("## Loading files")
mail <- load_files_to_df(paste0(proj_path, "nogit_easy_ham/"), file_count = 300)
spam <- load_files_to_df(paste0(proj_path, "nogit_spam/"), file_count = 300)

# Combine datasets and add labels
all_mail <- bind_rows(
  mail %>% mutate(label = 1),
  spam %>% mutate(label = 0)
) %>% sample_frac(size = 1)

# Split into training and testing sets
split_index <- createDataPartition(all_mail$label, p = 0.8, list = FALSE)
train_set <- all_mail[split_index, ]
test_set <- all_mail[-split_index, ]

message("## Building training dataset")
# Preprocess the training set and create a DFM
train_set_dfm <- preprocess_and_create_dfm(train_set, cache_filename = "train_set_dfm.rds")

# Extract the feature names from the training set's DFM
train_featnames <- featnames(train_set_dfm)

# Convert the training DFM to a data frame after extracting feature names
train_set_dfm <- convert(train_set_dfm, to = "data.frame")
train_set_dfm$label <- train_set$label

message("## Building test dataset")
test_set_dfm <- preprocess_and_create_dfm(test_set,  cache_filename = "test_set_dfm.rds")


test_set_dfm <- dfm_select(test_set_dfm, pattern = train_featnames, valuetype = "fixed")

test_set_dfm <- convert(test_set_dfm, to = "data.frame")

test_set_dfm$label <- test_set$label

train_set_dfm$label <- factor(train_set_dfm$label)
test_set_dfm$label <- factor(test_set_dfm$label)

message("## Train the model, using e1071")
model <- naiveBayes(x = train_set_dfm[, -which(colnames(train_set_dfm) == "label")], y = train_set_dfm$label)

# Predict on the test DFM
# predictions <- predict(model, test_set_dfm)
message("## Build predictions")
predictions <- predict(model, test_set_dfm[, -which(colnames(test_set_dfm) == "label")])

# Evaluate the model's performance
conf_mat <- confusionMatrix(predictions, test_set_dfm$label)
message(conf_mat)