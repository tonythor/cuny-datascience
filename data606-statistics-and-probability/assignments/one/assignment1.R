# First load data.
library(sqldf)
library(dplyr)
library(stringr)
library(tidyr)
library(ggplot2)

g_repo = "https://raw.githubusercontent.com/tonythor/cuny-datascience/develop/" 
lf =  paste(g_repo,"data/lusitania_manifest.csv", sep = "")
tf =  paste(g_repo,"data/titanic_lifeboats.csv", sep="")
titanic <- read.csv(tf)
lusitania <- read.csv(lf)

## Clean and standardize the titanic data set
titanic[c('last_name', 'first_name')]<- str_split_fixed(titanic$name, ',', 2)
replacements  = c('Miss.'='','Master.'='', 'Mrs.'='', 'Mister.'='', 'Mr.'='')
titanic$first_name<- str_replace_all(titanic$first_name, replacements )
titanic <- dplyr::rename(titanic, c("gender" = "sex"), c("lifeboat" = "boat"))
titanic_boat= c("titanic")
titanic$boat = titanic_boat
titanic <- titanic %>% mutate_at(c('age'), ~replace_na(.,0))
titanic <- titanic %>%   mutate(age = as.numeric(age))
# Could be any column name to filter not. Last row is empty and needs to be dropped. 
titanic <- titanic %>% filter(!last_name=='')
titanic_clean <- titanic %>% select(boat,last_name, first_name, 
                                    survived, gender, age, lifeboat)
## Clean and standardize the Lusitania data set
lusitania_boat= c("lusitania")
lusitania$boat = lusitania_boat
lusitania <- dplyr::rename(lusitania, c("first_name" = "Personal.name"), 
                           c("last_name" = "Family.name"),
                           c("lifeboat" = "Lifeboat"),
                           c("age" = "Age"),
                           c("gender" = "Sex"))
lusitania <- lusitania %>%  mutate(age = as.numeric(age))
lusitania <- lusitania %>% mutate_at(c('age'), ~replace_na(.,0))
lusitania = lusitania %>% mutate(survived = case_when(grepl("Saved", Fate) ~ 1,
                                                      .default = 0)) 
lusitania$gender <- tolower(lusitania$gender)
lusitania$last_name <- str_to_title(lusitania$last_name)
lusitania_clean <- lusitania %>% select(boat,last_name, first_name, survived, 
                                        gender, age, lifeboat)
## uninion the data sets into one, add a numerical categorical flag for gender
boats = union(lusitania_clean,titanic_clean)
# par(mar = c(4, 4, .1, .1))
ggplot(data=boats %>% filter(age > 1) ,aes(x=age, fill = boat)) +
  geom_histogram(bins=25, show.legend = FALSE) +
  ylim(0, 325) +
  xlim(0, 90) + 
  scale_y_continuous(n.breaks = 15) +
  scale_x_continuous(n.breaks = 10) +
  ylab("All Passangeers") + xlab ("Age")
ggplot(data=boats %>% filter(survived == 1) %>% filter(age >1) ,aes(x=age, fill = boat)) +
  geom_histogram(bins=25) +
  ylim(0, 325) +
  xlim(0, 90) + 
  scale_x_continuous(n.breaks = 10) +
  ylab("Survivors") + xlab ("Age")

#survived, by boat / gender!  
sbb  =  boats %>% filter(survived == 1)  %>%  group_by(boat,gender) %>%
  summarise(total_count=n(), .groups = 'drop') 
# agg, get boat totals  
sbb_agg = sbb %>% group_by(boat) %>% summarise(sum=sum(total_count), 
                                               .groups = 'drop')
survivers_lus = sbb_agg %>% filter(boat=="lusitania") %>% select("sum")
survivers_tit = sbb_agg %>% filter(boat=="titanic") %>% select("sum")

sbb = sbb %>% mutate(survivors = case_when(grepl("titanic", boat) 
                                           ~ survivers_tit, .default = survivers_lus)) 
sbb <- sbb %>% mutate(survivorship_percentage = (total_count / survivors$sum) * 100)

g <- ggplot(sbb, aes(x=boat,  y=survivorship_percentage))
g + geom_col(aes(fill = gender)) +  ylab("Survivorship Percentage") + xlab ("Boat")
print("here")
