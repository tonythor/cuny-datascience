library(RSQLite)
library(readr)
# Load the RSQLite Library

# data("mtcars")
# mtcars$car_names <- rownames(mtcars)
# rownames(mtcars) <- c()
# head(mtcars)
# # Create a connection to our new database, CarsDB.db
# # you can check that the .db file has been created on your working directory
# conn <- dbConnect(RSQLite::SQLite(), "CarsDB.db")


## build people datframe.

people <- read_csv(I("person_id,relationship,first_name,last_name
1,family,tony,fraser
2,family,tori,rivera
3,family,grayson,fraser
4,friend,jaime,shannon
5,friend,randy,frey
6,friend,rich,kurtzer
7,friend,renee,wasco
8,friend,tim,abrahamson
9,friend,mermaid,murmylo,
10,family,lyndon,fraser"), show_col_types = FALSE)


generated_observation_count <- 10
mystartnumber <- 1
result <- replicate(generated_observation_count, {
  numbers <- sample(1:5, 5, replace = TRUE)
  current_line <- paste(c(mystartnumber, numbers), collapse = ",")
  mystartnumber <<- mystartnumber + 1
  current_line
}, simplify = FALSE)


result <- as.character(result)

# Convert the result list to a dataframe
df <- as.data.frame(do.call(rbind, strsplit(result, ",")))

# Rename columns
colnames(df) <- c("person_id", "AvatarII", "Barbie", "Oppenheimer", "Guardians3", "SpiderverseII")

# Make sure to convert the character columns back to numeric
# df <- mutate(df, across(everything(), as.numeric))

