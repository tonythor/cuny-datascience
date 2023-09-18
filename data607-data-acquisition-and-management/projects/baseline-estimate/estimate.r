library(tidyverse)

# Sample data
critic_ratings <- tribble(
  ~Critic, ~CaptainAmerica, ~Deadpool, ~Frozen, ~JungleBook, ~PitchPerfect2, ~StarWarsForce,
  "Burton", NA, NA, 4, 4, NA, NA,
  "Charley", 4, 5, 4, 3, 2, 3,
  "Dan", NA, 5, NA, NA, NA, 5,
  "Dieudonne", 5, 4, NA, NA, NA, 5,
  "Matt", 4, NA, 2, 2, 5, NA,
  "Mauricio", 4, NA, 3, 3, 4, NA,
  "Max", 4, 4, 4, 2, 2, 4,
  "Nathan", NA, NA, NA, NA, NA, 4,
  "Param", 4, 4, 1, NA, NA, 5,
  "Parshu", 4, 3, 5, 5, 2, 3,
  "Prashanth", 5, 5, 5, 5, NA, 4,
  "Shipra", NA, NA, 4, 5, NA, 3,
  "Sreejaya", 5, 5, 5, 4, 4, 5,
  "Steve", 4, NA, NA, NA, NA, 4,
  "Vuthy", 4, 5, 3, 3, 3, NA,
  "Xingjia", NA, NA, 5, 5, NA, NA
)

# Compute everything in one pipeline for the main table
critic_ratings <- critic_ratings %>%
  bind_rows(
    summarise(., across(where(is.numeric), mean, na.rm = TRUE), Critic = "col_average")
  ) %>%
  rowwise() %>%
  mutate(row_average = mean(c_across(where(is.numeric)), na.rm = TRUE)) %>%
  ungroup() %>%
  mutate(row_average = if_else(Critic == "col_average", NA_real_, row_average))

# Compute the two summary variables separately
average_of_col_avg <- critic_ratings %>%
  filter(Critic != "col_average") %>%
  summarise(avg = mean(row_average, na.rm = TRUE)) %>%
  pull(avg)

average_of_row_avg <- critic_ratings %>%
  filter(Critic == "col_average") %>%
  summarise(avg = mean(c_across(where(is.numeric)), na.rm = TRUE)) %>%
  pull(avg)


print(sprintf("average_of_col_avg %s", average_of_col_avg))
print(sprintf("average_of_row_avg %s", average_of_row_avg))

