
library("fpp3")

gdpcc <-global_economy |>
  mutate(GDP_per_capita = GDP/Population) |>
  select(Year, Country, GDP, Population, GDP_per_capita)

# gdpcc
g <- gdpcc

g %>%
  filter(Country == "Sweden") %>%
  autoplot(GDP_per_capita) +
   labs(title = "GDP Sweden", y = "USD")


fit <- gdpcc |> 
    model(trend_model = TSLM(GDP_per_capita ~ trend()))

fit  # <- is a mable

fit |> forecast(h = "3 years")  ## <- generates a fable, a forecast table

# shows three records per country, three years fo forecast
# # A fable: 789 x 5 [1Y]
# # Key:     Country, .model [263]
#    Country        .model       Year   GDP_per_capita  .mean
#    <fct>          <chr>       <dbl>           <dist>  <dbl>
#  1 Afghanistan    trend_model  2018     N(526, 9653)   526.
#  2 Afghanistan    trend_model  2019     N(534, 9689)   534.
#  3 Afghanistan    trend_model  2020     N(542, 9727)   542.


fit |>
  forecast(h = "3 years") %>%
  filter(Country == "Sweden") %>%
  autoplot(g) +
  labs(title = "Forecasted GDP per Capita for Sweden", y = "USD")


## 5.2
bricks <- aus_production |>
  filter_index("1970 Q1" ~ "2004 Q4") |>
  select(Bricks)

bricks |> model(MEAN(Bricks))

bricks |> model(NAIVE(Bricks))

bricks |> model(SNAIVE(Bricks ~ lag("year")))

bricks |> model(RW(Bricks ~ drift()))

# Set training data from 1992 to 2006
train <- aus_production |>
  filter_index("1992 Q1" ~ "2006 Q4")
# Fit the models
beer_fit <- train |>
  model(
    Mean = MEAN(Beer),
    `Naïve` = NAIVE(Beer),
    `Seasonal naïve` = SNAIVE(Beer)
  )
# Generate forecasts for 14 quarters
beer_fc <- beer_fit |> forecast(h = 14)
# Plot forecasts against actual values
beer_fc |>
  autoplot(train, level = NULL) +
  autolayer(
    filter_index(aus_production, "2007 Q1" ~ .),
    colour = "black"
  ) +
  labs(
    y = "Megalitres",
    title = "Forecasts for quarterly beer production"
  ) +
  guides(colour = guide_legend(title = "Forecast"))


###### Brick Example
## returns a MABLE with four columns
brick_fit <- aus_production |>
filter(!is.na(Bricks)) |>
model(
  seasonal_naive = SNAIVE(Bricks),
  naive = NAIVE(Bricks),
  drift = RW(Bricks ~ drift()), 
  mean = MEAN(Bricks) 
)
brick_fit

## fable, forecasting table
brick_fc <- brick_fit |>
  forecast(h = "5 years")

brick_fc |>
    autoplot(aus_production, level=NULL) +
    labs(title = "clay bricks in AU", y = "millions of bricks") +
    guides(colour = guide_legend(title = "Forecast"))


## Facebook Stock
fb_stock <- gafa_stock |>
    filter (Symbol == "FB") |>
    mutate(trading_day = row_number()) |>
    update_tsibble(index=trading_day, regular= TRUE)

fb_stock |>
    model(
    "naive" = NAIVE(Close),
    "drift" = RW(Close ~ drift()), 
    "mean" = MEAN(Close) 
    ) |>
    forecast(h = 42) |>
    autoplot(fb_stock, level=NULL) +
        labs(title = "FB Closing Price", y="$US") + 
        guides(colour = guide_legend(title="Forecast"))


## 5.4 
fb_stock |> autoplot(Close)
fit <- fb_stock |> model(NAIVE(Close))
augment(fit)

augment(fit) |>
ggplot(aes(x = trading_day)) +
 geom_line(aes(y=Close, colour="Data")) +
 geom_line(aes(y = .fitted, colour="Fitted"))

## now let's plot differneces 
augment(fit) |>
filter(trading_day > 1100) |>
ggplot(aes(x = trading_day)) +
 geom_line(aes(y=Close, colour="Data")) +
 geom_line(aes(y = .fitted, colour="Fitted"))

#plot the residuals
augment(fit) |>
 autoplot(.resid) + 
 labs(y = "US$", ittle = "RESID from NAÏVE method")

library(ggplot2)
 ## histogram of the residuals
augment(fit) |>
 ggplot(aes(x = .resid)) + 
 geom_histogram(bins=150) + 
labs(title = "Histogram of residuals")


## look at ACF of residuals
augment(fit) |>
ACF(.resid) |>
autoplot() + 
labs(title = "ACF of Residual")

#All together!!!
gg_tsresiduals(fit)



augment(fit) |>
features(.resid, ljung_box, lag =10)


# 5.5
#Do the prediction
aus_production |> 
    filter(!is.na(Bricks)) |>
    model(seasonal_naive = SNAIVE(Bricks)) |>
    forecast(h = "5 years") 

#To get the interval, use the hilo function
aus_production |> 
    filter(!is.na(Bricks)) |>
    model(seasonal_naive = SNAIVE(Bricks)) |>
    forecast(h = "5 years") |>
    hilo(level = 95)


#To extract interval
aus_production |> 
    filter(!is.na(Bricks)) |>
    model(seasonal_naive = SNAIVE(Bricks)) |>
    forecast(h = "5 years") |>
    hilo(level = 95) |>
    mutate(lower = `95%`$lower, upper = `95%`$upper)


# 5.6
eggs <- prices |>
    filter(!is.na(eggs))
    select(eggs)

eggs |> autoplot() + 
 labs(title = "Annual Egg prices U$")

#ok use drift and create a model
fit <- eggs |> 
    model(RW(log(eggs) ~ drift()))
fit 

#now forecast 
fc <- fit |>
    forecast(h=50)

fc |> autoplot(eggs) + 
 labs(title = "Annual egg prices",
  y = "US$(adjusted for inflation)")

fc |> autoplot(eggs, level=90, point_forecast = lst(mean, median)) + 
 labs(title = "Annual egg prices",
  y = "US$(adjusted for inflation)")

# 5.7  forecasting with decomp
us_retail_employment <- us_employment |> 
    filter(year(Month) > 1990, Title == "Retail Trade") |>
    select(-Series_ID)

us_retail_employment

dcmp <- us_retail_employment |> 
    model(STL(Employed)) |> 
    components() |>
    select(-.model)
dcmp 

dcmp |>
    model(NAIVE(season_adjust)) |>
    forecast() |> 
    autoplot(dcmp) +
    labs(title = "Naive forecasts of seasonally adjusted data")

us_retail_employment |> 
    model(stlf = decomposition_model(
        STL(Employed ~ trend(window=7), robust=TRUE),
        NAIVE(season_adjust)
    )) |>
    forecast() |>
    autoplot(us_retail_employment)

fit_dcmp <- us_retail_employment |> 
    model(stlf = decomposition_model(
        STL(Employed ~ trend(window=7), robust=TRUE),
        NAIVE(season_adjust)
    ))

fit_dcmp |>
  forecast() |>
  autoplot(us_retail_employment)+
  labs(y = "Number of people",
       title = "US retail employment")

# dont forget about this charting thing.
fit_dcmp |> gg_tsresiduals()

## 5.8 Evaluating point forecast accuracy 
recent_production <- aus_production |> 
    filter(year(Quarter) >= 1992)

train <- recent_production |>
  filter(year(Quarter) <= 2007)

beer_fit <- train |>  # mable object
  model(
    Mean = MEAN(Beer),
    Naive = NAIVE(Beer),
    Seasonal_naive = SNAIVE(Beer),
    Drift = RW(Beer ~ drift()))

beer_fc <- beer_fit |>
  forecast(h = 10)

accuracy(beer_fit) |>
    arrange(.model) |> 
    select(.model, .type, RMSE, MAE, MAPE, MASE, RMSSE)

#   .model         .type     RMSE   MAE  MAPE  MASE RMSSE
#   <chr>          <chr>    <dbl> <dbl> <dbl> <dbl> <dbl>
# 1 Drift          Training  65.9  55.2 12.2   3.79  3.86
# 2 Mean           Training  43.9  35.6  7.95  2.45  2.57
# 3 Naive          Training  65.9  55.1 12.2   3.78  3.86
# 4 Seasonal_naive Training  17.1  14.6  3.37  1     1   
# 
# Seasonal_naive is best!! 


recent_production <- aus_production |>
  filter(year(Quarter) >= 1992)

accuracy(beer_fc, recent_production) |>
    arrange(.model) |>
    select(.model, .type, RMSE, MAE, MAPE, MASE, RMSSE)
# A tibble: 4 × 7
#   .model         .type  RMSE   MAE  MAPE  MASE RMSSE
#   <chr>          <chr> <dbl> <dbl> <dbl> <dbl> <dbl>
# 1 Drift          Test   82.6  75.7 18.7  5.20  4.84 
# 2 Mean           Test   37.2  34.3  8.23 2.35  2.18 
# 3 Naive          Test   78.6  71.2 17.6  4.89  4.60 
# 4 Seasonal_naive Test   12.7  10.8  2.57 0.742 0.746


#5.9
library("fpp3")
google_stock <- gafa_stock |> 
  filter(Symbol == "GOOG", year(Date) >= 2015) |>
  mutate(day = row_number()) |>
  update_tsibble(index = day, regular=TRUE)
google_2015 <- google_stock |> 
  filter(Symbol == "GOOG", year(Date) == 2015)
google_jan_2016 <- google_stock |> 
  filter(Symbol == "GOOG", yearmonth(Date) == yearmonth("2016-01"))


google_fit <- google_2015 |>
  model(
    Mean = MEAN(Close),
    Naive = NAIVE(Close),
    Drift = RW(Close ~ drift()))

google_fc <- google_fit |>
  forecast(google_jan_2016)

## MEAN
google_fc |>
  filter(.model == "Mean") |>
  autoplot(bind_rows(google_2015, google_jan_2016))  +
    labs(y = "$US", title="Google closing stock prices: Mean Forecasts") + 
    guides(color = guide_legend(title = "Forecast")) + ylim(439,880)

## NAIVE
google_fc |>
  filter(.model == "Naive") |>
  autoplot(bind_rows(google_2015, google_jan_2016))  +
    labs(y = "$US", title="Google closing stock prices: Mean Forecasts") + 
    guides(color = guide_legend(title = "Forecast")) + ylim(439,880)


# lets do the quantile scoring now
google_fc |> 
    filter(.model == "Naive", Date =="2016-01-04") |>
    accuracy(google_stock, list(qs=quantile_score), probs=0.1)

google_fc |> 
    filter(.model == "Naive", Date =="2016-01-04") |>
    accuracy(google_stock, list(qs=quantile_score), probs=0.9)

google_fc |> 
    filter(.model == "Naive", Date =="2016-01-04") |>
    accuracy(google_stock, list(winkler = winkler_score), level= 80)

#CRPS Continuous Ranked Probability Score
google_fc |> 
  accuracy(google_stock, list(crps=CRPS))

  #5.10
  ## Facebook Stock
fb_stock <- gafa_stock |>
  filter (Symbol == "FB") |>
  mutate(trading_day = row_number()) |>
  update_tsibble(index=trading_day, regular= TRUE)

fb_stretch <- fb_stock |> 
  stretch_tsibble(.init = 3, .step = 1) |> 
  filter(.id != max(.id))

## this a mable
fit_cv <- fb_stretch |>
  model(RW(Close ~ drift()))

## Now pipe it into forecast
fc_cv <- fit_cv |>
  forecast(h = 1)

## Now we pipe it into accuracy 
fc_cv |> accuracy(fb_stock)

# training_set
fb_stock |> model(RW(Close ~ drift())) |>
    accuracy() 

# # A tibble: 1 × 11
#   .model      Symbol .type      ME  RMSE   MAE     MPE  MAPE  MASE RMSSE    ACF1
#   <chr>       <chr>  <chr>   <dbl> <dbl> <dbl>   <dbl> <dbl> <dbl> <dbl>   <dbl>
# 1 RW(Close ~… FB     Test  -0.0529  2.42  1.47 -0.0607  1.27  1.00  1.00 -0.0208
# > fb_stock |> model(RW(Close ~ drift())) |>
#     accuracy()  
# # A tibble: 1 × 11
#   Symbol .model       .type    ME  RMSE   MAE      MPE  MAPE  MASE RMSSE    ACF1
#   <chr>  <chr>        <chr> <dbl> <dbl> <dbl>    <dbl> <dbl> <dbl> <dbl>   <dbl>
# 1 FB     RW(Close ~ … Trai…     0  2.41  1.46 -0.00571  1.26 0.998  1.00 -0.0205
# > 