1+1
x <-"2 Dozen"
print(x)
"tony" -> y
print(y)

assign("t", 26)
print(t) 

#remove a variable from memory
rm(t)


## basic typing
class(y)
is.numeric(1)
l<-5
2*l

nchar(123444)

# subtract integers as days!
date1 <- as.Date(('2021-01-30'))
print(date1 - 40)


FALSE * 5

## boolians are called logicals, so .is_logical is a thing.
2 == 3
2 == 2

x <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
## automatically does for each.
x * 2

# ranges
y <- 1:10
y + x


#Basic array access
q <- c("Hockey", "Football", "Baseball", "Curling", "Rugby", "Lacrosse", "Basketball", "Tennis", "Cricket", "Soccer")
q[2:length(q)-1]

# key value pairs
d <- c("One" = "apple", "Two" = "orange")
d["Two"]

## like 'distinct' 
q2 <- c("Hockey", "Hockey", "Baseball", "Curling", "Rugby", "Lacrosse", "Basketball", "Tennis", "Cricket", "Soccer")
q2Factor = as.factor(q2)
print(q2Factor)

#getting function documentation 
?`mean`
# seraches for all things iwth mean in them
apropos("mea")

f <- c("Tony", NA)
is.na(f[1])


x <- 10:1 
y <- -4:5 
q <- c("Hockey", "Football", "Baseball", "Curling", "Rugby","Lacrosse", "Basketball", "Tennis", "Cricket", "Soccer")
theDF <- data.frame("count" = x, "other"= y, "sport" = q) 
theDF

theDF[1,]

theDF$Sport

## Load data into dataframe, use sqldf to query it.
mcsv <- "http://www.jaredlander.com/data/Tomato%20First.csv"
tomato <- read.csv(mcsv)
head(tomato)
library(sqldf)
x = sqldf("select * from tomato where source like '%gostino%'")


## functions, and default parameters
say.hello <- function(fName ="tony")
{
  sprintf("Yolo %s", fName)
}
say.hello()
say.hello("jake")

say.hello("rif")
