library(sqldf, dplyr, stringr)

#7. BONUS – place the original .csv in a github file and have R read from the link.
titanic_dataset <- "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic <- read.csv(titanic_dataset)
titanic

#3. Create new column names for the new data frame.
titanic <- dplyr::rename(titanic, c("PassengerClass" = "Pclass"), c("Gender" = "Sex"))
titanic[c('LastName', 'FirstName')]<- str_split_fixed(titanic$Name, ',', 2)


#2. Create a new data frame with a subset of the columns and rows. Make sure to rename it.
titanic_children = sqldf("select  Survived, PassengerClass, LastName, FirstName,
                         Gender, Age from titanic where age < 18 order by PassengerClass, Age desc")

#1 Use the summary function to gain an overview of the data set. Then display the mean and 
#  median for at least two attributes.
summary(titanic_children)
sprintf("P Class : mean:%s median:%s", round(mean(titanic_children$PassengerClass), digits=5), 
        round(median(titanic_children$PassengerClass),digits=5))
sprintf("Survived: mean:%s median:%s", round(mean(titanic_children$Survived), digits=5), 
        round(mean(titanic_children$Survived), digits=5))


# This is what I was wondering. Miss and master were terms used to refer to children. However,
# I noticed Mrs. in here and went looking into that. Mrs. definitely implies marriage, and the age
# of consent was considerably lower back then. https://chnm.gmu.edu/cyh/primary-sources/24.html 

titanic_children = titanic_children %>%
  mutate(PossiblyMarried = case_when(
    grepl("Mrs.", FirstName) ~ "True",
    grepl("Mister.", FirstName ) ~ "True",
    grepl("Mr.", FirstName ) ~ "True",
    .default = ""
  ))

#5 For at least 3 values in a column please rename so that every value in that column is renamed.
replacements  = c('Miss.'='','Master.'='', 'Mrs.'='', 'Mister.'='', 'Mr.'='')
titanic_children$FirstName<- str_replace_all(titanic_children$FirstName, replacements )

# The first name column is pretty long, let's truncate it.
titanic_children = titanic_children %>% mutate(FirstName = str_trunc(FirstName, width = 10))

#6. Display enough rows to see examples of all of steps 1-5 above.
head(titanic_children) 


titanic_children = titanic_children %>% mutate(FirstName = str_trunc(FirstName, width = 10))

