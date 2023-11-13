library(tidyverse)
library(caret)
library(quanteda)
library(dplyr)
library(future)
library(future.apply)
library(e1071)

proj_path <- paste0(getwd(), "/data607-data-acquisition-and-management/projects/spam-classifier/")

# Function to load files into a dataframe
load_files_to_df <- function(file_path, file_count = 150) {
  file_names <- list.files(path = file_path, full.names = TRUE, pattern = "^\\d+.*")
  file_names <- head(file_names, file_count)
  text_data <- set_names(file_names, nm = basename(file_names)) %>%
    map_df(~tibble(name = .y, data = read_file(.x)), .y = names(.))
  return(text_data)
}

preprocess_and_create_dfm <- function(df, cache_filename = "dfm_cache.rds") {
  f_cache <- paste0(proj_path, cache_filename)

  if (file.exists(f_cache)) {
    print(paste0("Returning ", cache_filename, " from file system"))
    return(readRDS(f_cache))
  } else {
    # Set up future to use a multisession - this will enable parallel processing
    plan(multisession, workers = 4)

    # Preprocessing text data in parallel
    clean_data <- future.apply::future_sapply(df$data, FUN = function(text) {
      text %>%
        str_replace_all("^(From|Return-Path|Received|Message-ID):.*", "") %>%
        str_replace_all("\\n", " ") %>%
        str_squish()
    }, USE.NAMES = FALSE)

    # Tokenizing and creating a DFM (Document-Feature Matrix)
    tokens <- tokens(clean_data, what = "word", remove_punct = TRUE, remove_symbols = TRUE)
    tokens <- tokens_remove(tokens, stopwords("en"))

    # Creating the DFM
    dfm <- dfm(tokens)
    message("Saving DFM to cache...")
    saveRDS(dfm, f_cache)

    return(dfm)
  }
}

# Example usage:

# file_count = 150 -> 52 seconds 
# file_count = 250 -> 2 minutes and 41 seconds

mail <- load_files_to_df(paste0(proj_path, "nogit_easy_ham/"), file_count = 100)
spam <- load_files_to_df(paste0(proj_path, "nogit_spam/"), file_count = 100)

# Combine datasets and add labels
all_mail <- bind_rows(
  mail %>% mutate(label = 1),
  spam %>% mutate(label = 0)
) %>% sample_frac(size = 1)

# Split into training and testing sets
split_index <- createDataPartition(all_mail$label, p = 0.8, list = FALSE)
train_set <- all_mail[split_index, ]
test_set <- all_mail[-split_index, ]


# Preprocess the training set and create a DFM
train_set_dfm <- preprocess_and_create_dfm(train_set, cache_filename = "train_set_dfm.rds")

# Extract the feature names from the training set's DFM
train_featnames <- featnames(train_set_dfm)

# Convert the training DFM to a data frame after extracting feature names
train_set_dfm <- convert(train_set_dfm, to = "data.frame")
train_set_dfm$label <- train_set$label

test_set_dfm <- preprocess_and_create_dfm(test_set,  cache_filename = "test_set_dfm.rds")

# Align the test set DFM with the training set DFM feature names
# The dfm_select() function will be applied only if test_set_dfm is a dfm object.
# The valuetype = "fixed" ensures that the exact feature names are matched.
test_set_dfm <- dfm_select(test_set_dfm, pattern = train_featnames, valuetype = "fixed")

# Convert the test DFM to a data frame after aligning the features
# This convert() call should happen only once.
test_set_dfm <- convert(test_set_dfm, to = "data.frame")

# Add the label column to the test data frame
# This step is done after the test_set_dfm is confirmed to be a data frame.
test_set_dfm$label <- test_set$label

# Convert the 'label' column to a factor
train_set_dfm$label <- factor(train_set_dfm$label)

# Train the model on the training DFM

#caret
#model <- train(label ~ ., data = train_set_dfm, method = "naive_bayes")
#e1071
model <- naiveBayes(x = train_set_dfm[, -which(colnames(train_set_dfm) == "label")], y = train_set_dfm$label)

# Convert the 'label' column in the test set to a factor as well
test_set_dfm$label <- factor(test_set_dfm$label)

# Predict on the test DFM
predictions <- predict(model, test_set_dfm)
predictions <- predict(model, test_set_dfm[, -which(colnames(test_set_dfm) == "label")])


# Evaluate the model's performance
conf_mat <- confusionMatrix(predictions, test_set_dfm$label)
print(conf_mat)