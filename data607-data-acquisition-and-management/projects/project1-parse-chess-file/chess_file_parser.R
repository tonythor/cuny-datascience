library(stringr)
# library(sqldf)
# library(dplyr)
# library(tidyr)
# library(ggplot2)
# library(tidyverse)


ddf <- function(df) {
  for (line in df) {
    print(line)
  }
}



file_to_single_row_records <- function(file_name) {
  lines <- readLines(file_name)
  # first, there's a bunch of lines in these files that are all hypens.
  # let's get rid of those, and at teh same time we'll chop off the two
  # top lines, which are static column headers.

  filtered_lines <- c()
  line_counter <- 1
  for (line in lines[seq(4, length(lines))]) {
    if (!str_detect(line, "----")) {
      filtered_lines[line_counter] <- gsub(" *\\| *", "|", str_trim(str_squish(line), side = "both"))
      line_counter <- line_counter + 1
    }
  }

  # Sweet.
  # now we have to deal with this crazy formatting, basically one record
  # spans across two rows one on top of the other. Logically, let's call
  # them "top_of_record" and "bottom_of_record", then we'll move them side
  # by side and collapse them onto a single line. 

  odd_numbers <- seq(1, length(filtered_lines), 2)
  even_numbers <- seq(2, length(filtered_lines), 2)

  top_of_record <- filtered_lines[even_numbers]
  bottom_of_record <- filtered_lines[odd_numbers]

  # now let's put them side by side and merge them together!
  single_row_records <- paste(bottom_of_record, top_of_record)

  # records look like this now, perfect.
  # [1] "1|GARY HUA|6.0|W 39|W 21|W 18|W 14|W 7|D 12|D 4| ON|15445895 / R: 1794 ->1817|N:2|W|B|W|B|W|B|W|"
  # [1] "2|DAKSHESH DARURI|6.0|W 63|W 58|L 4|W 17|W 16|W 20|W 7| MI|14598900 / R: 1553 ->1663|N:2|B|W|B|W|B|W|B|"
  # [1] "3|ADITYA BAJAJ|6.0|L 8|W 61|W 25|W 21|W 11|W 13|W 12| MI|14959604 / R: 1384 ->1640|N:2|W|B|W|B|W|B|W|"
  # [1] "4|PATRICK H SCHILLING|5.5|W 23|D 28|W 2|W 26|D 5|W 19|D 1| MI|12616049 / R: 1716 ->1744|N:2|W|B|W|B|W|B|B|"
  return(single_row_records)
}



file_name <- "act.txt"
file_name_csv <- str_replace(file_name, "txt", "csv")
single_row_record_array <- file_to_single_row_records(file_name)

# Split each entry in the array
split_data <- lapply(single_row_record_array, function(x) strsplit(x, split = "\\|")[[1]])
df <- as.data.frame(do.call(rbind, split_data), stringsAsFactors = FALSE)
cols <- c("pair", "name", "total", "round1", "round2", "round3", "round4", "round5",
          "round6", "round7", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
colnames(df) <-  cols

write.csv(df, file = file_name_csv, append = FALSE, quote = FALSE, row.names = FALSE )

print(head(df))


