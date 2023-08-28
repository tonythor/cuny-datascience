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


parse_fw <- function(filename) {
  # header <- c("name","number","quickid", "initials", "nickname")

  lines <- readLines(filename)


  # first remover all the lines that are just hypens, we'll put
  # what remains in filtered_lines. As well, we'll chop off hte two
  # first lines, which we know are headers.
  filtered_lines <- c()
  line_counter <- 1
  for (line in lines[seq(3, length(lines))]) {
    if(! str_detect(line, "----")){
      filtered_lines[line_counter] <- line
      line_counter <- line_counter + 1
    }
  }

  ## now break things apart.

  odd_numbers   <- seq(1, length(filtered_lines), 2)
  even_numbers  <- seq(2, length(filtered_lines), 2)


  top_lines <-  filtered_lines[1]
  # bottom_lines <- filtered_lines(seq(even_numbers))
  # now we break into two dataframes. 



  # header_lines <- lines[seq(0,1)]
  # data_lines <- lines[seq(2, length(lines))]
  # widths <- c(4,6,2)
  # detail_df <- read.fwf(textConnection(data_lines), widths = widths, stringsAsFactors = FALSE, header = FALSE)

  # return(top_lines)

}
df <- parse_fw("simp.txt")
# ddf(df)
# for (l in df) {
#   print(l)
# }

# glimpse(df)
# print(df)
