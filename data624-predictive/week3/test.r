library(fpp3)

## GDP per capita
global_economy %>%
  filter(Country == "Australia") %>%
  autoplot(GDP / Population)

## Retail CPI
print_retail <- aus_retail %>%
  filter(Industry == "Newspaper and book retailing") %>%
  group_by(Industry) %>%
  index_by(Year = year(Month)) %>%
  summarise(Turnover = sum(Turnover))

aus_economy <- global_economy %>%
  filter(Code == "AUS")

print_retail %>%
  left_join(aus_economy, by = c("Year" = "Year")) %>%
  mutate(Adjusted_turnover = Turnover / CPI * 100) %>%
  pivot_longer(c(Turnover, Adjusted_turnover), values_to = "Turnover") %>%
  mutate(name = factor(name, levels = c("Turnover", "Adjusted_turnover"))) %>%
  ggplot(aes(x = Year, y = Turnover)) +
    geom_line() +
    facet_grid(name ~ ., scales = "free_y") +
    labs(title = "Turnover: Australian print media industry", y = "$AU")

## Food retailing
food <- aus_retail %>%
  filter(Industry == "Food retailing") %>%
  summarise(Turnover = sum(Turnover))

food %>%
  autoplot(Turnover) +
  labs(y = "Turnover ($AUD)")

food %>%
  features(Turnover, features = guerrero) %>%
  autoplot(box_cox(Turnover, lambda = 0.0524)) +
  labs(y = "Box-Cox transformed turnover")



food <- aus_retail |>
    filter(Industry == "Food retailing") |>
    summarise(Turnover = sum(Turnover))

food |> autoplot() 
food |> autoplot(sqrt(Turnover)) + labs(y = "sqr root")
food |> autoplot(Turnover^(1/3)) + labs(y = "cube root")
food |> autoplot(log(Turnover)) + labs(y = "turnover root")

 

library(fpp3)
us_retail_employment <- us_employment %>%
  filter(year(Month) >= 1990, Title == "Retail Trade") %>%
  select(-Series_ID)

us_retail_employment |>
  model(STL(Employed ~ season(window = 15) + trend(window = 15), robust=FALSE)) |>
  components() |>
  autoplot() + labs(title="STL Decomp: US Retail")