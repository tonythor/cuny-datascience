library(readr)
setwd("/Users/afraser/Documents/src/cuny-datascience/bridge/R/")
sales <- read_csv("../../data/scatter_data.csv")
sales$Order_Total <- as.numeric(gsub('\\$|,', '', sales$Order_Total))
sales$CountXTotal <- as.numeric(gsub('\\$|,', '', sales$CountXTotal))
# View(sales)
colnames(sales)

# labels = c("Female", "Male")

plot(sales$Item_Count_25, sales$Order_Total)
