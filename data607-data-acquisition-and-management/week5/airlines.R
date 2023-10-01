library(tidyverse)

source_file_path <- sys.frame(1)$ofile
dirname(source_file_path)
setwd(dirname(source_file_path))

data <- read.table("airlines.csv", header = TRUE, sep = ",",
                   stringsAsFactors = FALSE, fill = TRUE, 
                   na.strings = c("NA", "")) #<- straight into NA
# > data
#         X     X.1 Los.Angeles Phoenix San.Diego San.Francisco Seattle
# 1  ALASKA on time         497     221       212           503    1841
# 2    <NA> delayed          62      12        20           102     305
# 3    <NA>    <NA>          NA      NA        NA            NA      NA
# 4 AM WEST on time         694    4840       383           320     201
# 5    <NA> delayed         117     415        65           129      61

data_cleaned <- data %>%
  rename(Airline = X, Status = X.1) %>% # Rename columns
  fill(Airline, .direction = "down") %>%
  filter(!is.na(Status)) # Remove rows where Status is NA

#   Airline  Status Los.Angeles Phoenix San.Diego San.Francisco Seattle
# 1  ALASKA on time         497     221       212           503    1841
# 2  ALASKA delayed          62      12        20           102     305
# 3 AM WEST on time         694    4840       383           320     201
# 4 AM WEST delayed         117     415        65           129      61

gathered <- data_cleaned %>%
  gather(key = "City", value = "Flights", -Airline, -Status)

# > gathered
#    Airline  Status          City Flights
# 1   ALASKA on time   Los.Angeles     497
# 2   ALASKA delayed   Los.Angeles      62
# 3  AM WEST on time   Los.Angeles     694
# 4  AM WEST delayed   Los.Angeles     117
# 5   ALASKA on time       Phoenix     221
# 6   ALASKA delayed       Phoenix      12
# 7  AM WEST on time       Phoenix    4840
# 8  AM WEST delayed       Phoenix     415
# 9   ALASKA on time     San.Diego     212
# 10  ALASKA delayed     San.Diego      20
# 11 AM WEST on time     San.Diego     383
# 12 AM WEST delayed     San.Diego      65
# 13  ALASKA on time San.Francisco     503
# 14  ALASKA delayed San.Francisco     102
# 15 AM WEST on time San.Francisco     320
# 16 AM WEST delayed San.Francisco     129
# 17  ALASKA on time       Seattle    1841
# 18  ALASKA delayed       Seattle     305
# 19 AM WEST on time       Seattle     201
# 20 AM WEST delayed       Seattle      61

spread <- gathered %>%
    spread(key = Status, value = Flights)

# > spread
#    Airline          City delayed on time
# 1   ALASKA   Los.Angeles      62     497
# 2   ALASKA       Phoenix      12     221
# 3   ALASKA     San.Diego      20     212
# 4   ALASKA San.Francisco     102     503
# 5   ALASKA       Seattle     305    1841
# 6  AM WEST   Los.Angeles     117     694
# 7  AM WEST       Phoenix     415    4840
# 8  AM WEST     San.Diego      65     383
# 9  AM WEST San.Francisco     129     320
# 10 AM WEST       Seattle      61     201