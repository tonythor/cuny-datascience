library(readr)
# setwd("/Users/afraser/Documents/src/cuny-datascience/bridge/R/")
tips <- read_csv("data/tips.csv")
View(tips)
# print(tips$total_bill)
plot(tips$total_bill, tips$tip)
print(sd(tips$total_bill))

length(combn(20,5))

hist(tips$total_bill, breaks=20)



# tips$total_bill, 
