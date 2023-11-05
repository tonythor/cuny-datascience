library(httr)
library(jsonlite)
library(dplyr)
library(uuid)

library(tidyr)


get_data <- function(suffix, type = "json", persist = FALSE) {
  base_url <- "http://api.nobelprize.org/v1/"
  full_url <- paste0(base_url, suffix)
  accept_header <- ifelse(type == "json", "application/json", "text/csv")
  response <- GET(full_url, accept(accept_header))
  if (status_code(response) == 200) {
    content_data <- content(response, "text", encoding = "UTF-8")

    # If persist is TRUE, save the raw output to the file system
    if (persist) {
      file_name <- paste0("nogit_", 
            UUIDgenerate(), "_", suffix, 
            ifelse(type == "json", ".json", ".csv"))
      print(sprintf("FileName %s", file_name))
      write(content_data, file_name)
    }

    # Process and return the data
    if (type == "json") {
      return(fromJSON(content_data))
    } else if (type == "csv") {
      return(read.csv(text = content_data, stringsAsFactors = FALSE))
    } else {
      stop("Type must be either 'json' or 'csv'.")
    }
  } else {
    stop("Failed to retrieve data: ", status_code(response))
  }
}


countries <- get_data(suffix = "country.csv", type = "csv", persist = FALSE)
people <-  get_data(suffix = "prize.json", type = "json", persist = FALSE) %>%
  { flatten(. $prizes) } %>%
  unnest(laureates)
