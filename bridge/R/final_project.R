# What was the makeup of the lifeboats between the titanic and the lusitania?
library(sqldf)
library(dplyr)
library(stringr)
library(tidyr)
library(ggplot2)


lf = 'https://raw.githubusercontent.com/tonythor/cuny-datascience/develop/bridge/R/data/lusitania_manifest.csv'
tf = 'https://raw.githubusercontent.com/tonythor/cuny-datascience/develop/bridge/R/data/titanic_lifeboats.csv'

titanic <- read.csv(tf)
lusitania <- read.csv(lf)

titanic[c('last_name', 'first_name')]<- str_split_fixed(titanic$name, ',', 2)
replacements  = c('Miss.'='','Master.'='', 'Mrs.'='', 'Mister.'='', 'Mr.'='')
titanic$first_name<- str_replace_all(titanic$first_name, replacements )
titanic <- dplyr::rename(titanic, c("gender" = "sex"), c("lifeboat" = "boat"))
titanic_boat= c("titanic")
titanic$boat = titanic_boat
titanic <- titanic %>% mutate_at(c('age'), ~replace_na(.,0))
titanic <- titanic %>%   mutate(age = as.numeric(age))


titanic_clean <- titanic %>% select(boat,last_name, first_name, survived, gender, age, lifeboat)


lusitania_boat= c("lusitania")
lusitania$boat = lusitania_boat
lusitania <- dplyr::rename(lusitania, c("first_name" = "Personal.name"), 
                           c("last_name" = "Family.name"),
                           c("lifeboat" = "Lifeboat"),
                           c("age" = "Age"),
                           c("gender" = "Sex"))

lusitania <- lusitania %>%  mutate(age = as.numeric(age))
lusitania <- lusitania %>% mutate_at(c('age'), ~replace_na(.,0))

# 1 Lost, 1193, Not on board 1, Saved 763, Saved (died from trauma) 4
lusitania = lusitania %>% mutate(survived = case_when(grepl("Saved", Fate) ~ 1,.default = 0)) 

lusitania$gender <- tolower(lusitania$gender)
lusitania$last_name <- str_to_title(lusitania$last_name)
lusitania_clean <- lusitania %>% select(boat,last_name, first_name, survived, gender, age, lifeboat)
boats = union(lusitania_clean,titanic_clean)



ggplot(data=boats %>% filter(age >1),aes(x=age, fill = boat)) +
  geom_histogram(bins=25) +
  ylab("Total Passengers") + xlab ("Age")
ggplot(data=boats %>% filter(survived == 1) %>% filter(age >1) ,aes(x=age, fill = boat)) +
  geom_histogram(bins=25) +
  ylab("Survivers") + xlab ("Age")

# Titanic 14/15 April 1912  1490-1635 deaths / 2224 people 1550/2224 = 70% 
# Lusitania by german U Boat: May 7, 1915, 761 deaths /(1266+696 = 1962 people) = 38%


