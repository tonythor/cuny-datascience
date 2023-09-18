# Practical R Cheat Sheet
By Tony Fraser

### dplyr basics
```r
library(dplyr)
# Basic SQL Operations
df_select <- df %>% select(column1, column2) # SELECT
df_where <- df %>% filter(column1 == "value") # WHERE
df_orderby <- df %>% arrange(column1) # ORDER BY


 # GROUP BY & HAVING
df_groupby <- df %>% 
  group_by(column1) %>%
  summarise(avg_col2 = mean(column2)) %>%
  filter(avg_col2 > value)

# GROUP BY AND COUNT
grouped_data <- accidents %>%
  filter(!is.na(BOROUGH) & `CONTRIBUTING FACTOR VEHICLE 1` != "unspecified") %>%
  group_by(BOROUGH, `CONTRIBUTING FACTOR VEHICLE 1`, `VEHICLE TYPE CODE 1`) %>%
  summarise(count = n()) %>%
  arrange(-count)

## Between
accidents_zoomed <-   accidents %>% 
  filter(
    between(LATITUDE, latitude_center - radius_constant_latitude, latitude_center + radius_constant_latitude) &
    between(LONGITUDE, longitude_center - radius_constant_longitude, longitude_center + radius_constant_longitude)
  ) %>% 
  slice(1:record_count)

#JOINS 
df_join <- df1 %>% 
  left_join(df2, by = c("column" = "column"))
result <- employees %>%
  left_join(dayWorkers, by = c("employeeId" = "emp_id"))


df_limit <- df %>% slice_head(n = 10) # LIMIT

# Functions & Operations
df_avg <- df %>% summarise(avg_col1 = mean(column1)) # Aggregate Functions

# String functions in dplyr might need additional packages like stringr.
# Date functions can vary depending on the class of the date in the dataframe.

# Modifying Data Frames
# In dplyr, operations are non-mutative by default. You'd need to overwrite
# the dataframe or assign to a new one.
df <- df %>% add_row(column1 = "value1", column2 = "value2") # INSERT
df <- df %>% mutate(column1 = ifelse(column2 == "value", "new_value", column1)) # UPDATE
df <- df %>% filter(column1 != "value") # DELETE

# Miscellaneous
df_value <- df %>% filter(column1 == value) # Using R Variables in Queries
df_na <- df %>% filter(is.na(column1)) # Handling NA

# if one column has a string add another
df_new <- df %>%
  mutate(newColumn = if_else(str_detect(oldColumn, "appletv"), "appleTV", "notAppleTv"))
```


### gt basics
```r
library(dplyr)
library(gt)

by_borough <- accidents %>%
  filter(!is.na(BOROUGH) & nchar(BOROUGH) > 0 & `CONTRIBUTING FACTOR VEHICLE 1` != "unspecified") %>%
  group_by(`VEHICLE TYPE CODE 1`, BOROUGH) %>%
  summarise(count = n(), .groups = "drop") %>%
  mutate(`VEHICLE TYPE CODE 1` = ifelse(count < 5, "Other", `VEHICLE TYPE CODE 1`),
         `VEHICLE TYPE CODE 1` = ifelse(nchar(`VEHICLE TYPE CODE 1`) < 1, "unspecified", `VEHICLE TYPE CODE 1`)) %>%
  arrange(`VEHICLE TYPE CODE 1`, -count)

by_borough_table <- by_borough %>%
  gt() %>%
  tab_style(
    style = cell_text(align = "left"),
    locations = cells_body(columns = c(`VEHICLE TYPE CODE 1`, BOROUGH, count))
  ) %>%
  cols_label(
    `VEHICLE TYPE CODE 1` = "Vehicle Code",
    BOROUGH = "Borough",
    count = "Accident Count"
  ) %>%
  tab_style(
    style = cell_text(weight = "bold", size = "large"),
    locations = cells_column_labels(columns = c(`VEHICLE TYPE CODE 1`, BOROUGH, count))
  )

by_borough_table

```
## R
```r
#long strings
long_string <- paste("This is a very long string",
                     "that I want to break across two lines.")
long_string <- "This is a very long string \
that I want to break across two lines."

str1 <- "tony"
str2 <- "fraser"
combined_str <- paste(str1, str2)

str1 <- "tony"
str2 <- "fraser"
combined_str <- sprintf("%s%s", str1, str2)


library(glue)

str1 <- "tony"
str2 <- "fraser"
combined_str <- glue("{str1}{str2}")

## this is where we are going supposedly, anonymous lambda funcitons, but we're not there yet.
# to_vector <- function(input_string) {
#   cleaned_string <- input_string |> 
#     \(x) gsub("\\[\\d+\\]|\\\"", "", x) |>
#     \(x) gsub(" {2,}|\n", "", x)
#   return(cleaned_string)
# }



library(magrittr)
cleaned_string <- input_string %>%
  { gsub("\\[\\d+\\]|\\\"", "", .) } %>%
  { gsub(" {2,}|\n", "", .) }

## the extraction operator -- this is a list.
> v
[[1]]
 [1] " bell pepper"            "bilberry"               
 [3] "blackberry"              "blood orange"           
 [5] " blueberry"              "cantaloupe"             
 [7] "chili pepper cloudberry" " elderberry"            
 [9] "lime"                    "lychee"                 
[11] "mulberry"                " olive"                 
[13] "salal berry"            


> `[[`(v,1) [1]
[1] " bell pepper"


# REGEX 
library(stringr)
text_string <- "aaabbbcccdddxxx111222"
regex_pattern <- "(.)\\1\\1"
matches <- str_match_all(text_string, regex_pattern)
first_match <- matches[[1]][1, 1]
second_match <- matches[[1]][2, 1]
third_match <- matches[[1]][3, 1]

```


## Quarto
https://quarto.org/docs/computations/execution-options.html


