library(fpp3)
library(patchwork)
library(lubridate)
library(scales)
library(stringr)
library(forecast)
options(scipen=999)
data(gafa_stock)


# section 9.1 
google_2018 <- gafa_stock |>
  filter(Symbol == "GOOG", year(Date) == 2018)

google_2018 |> 
  autoplot(Close) +
  labs(y = "Closing Stock($USD)")

#ACF  
google_2018 |> 
  ACF(Close) |>
  autoplot()


## stabilize data
data(PBS)
a10 <- PBS |> 
  filter(ATC2 == "A10") |>
  summarize(Cost = sum(Cost) / 1e6)
#graph this, needs transformations! 
a10 |> autoplot(Cost) 
# first graph , stabilzie the variance, the peaks and valleys.
a10 |> autoplot(log(Cost))
# but still have trend and seasonality.
# remove seasonality 
a10 |> autoplot(log(Cost) |> difference(12))


# now we do one, but still has trend after we take the seasonaltiy difference
h02 <- PBS |>
  filter (ATC2 == "H02") |> 
  summarise (Cost = sum(Cost) /  1e6)

h02 |>  autoplot(Cost)
h02 |> autoplot(log(Cost))
                          # seasonal diff 
h02 |> autoplot(log(Cost) |> difference(12))
                          #  seasonal diff  + first order diff
h02 |> autoplot(log(Cost) |> difference(12) |> difference(1))


#9.5 

egy <- global_economy |>
  filter(Code == "EGY")
egy |> autoplot(Exports) +
labs(y = "% of gdp", title ="Egyption Exports")
View(egy)


fit <- egy |> model(ARIMA(Exports))
report(fit)

gg_tsresiduals(fit)
# > report(fit)
# Series: Exports 
# Model: ARIMA(2,0,1) w/ mean 

# Coefficients:
#          ar1      ar2      ma1  constant
#       1.6764  -0.8034  -0.6896    2.5623
# s.e.  0.1111   0.0928   0.1492    0.1161

# sigma^2 estimated as 8.046:  log likelihood=-141.57
# AIC=293.13   AICc=294.29   BIC=303.43
# > 

fit |> forecast(h=10) |> autoplot(global_economy) + 
labs(y="% of GDP", title = "Egypt Exports")


fit <- egy |> 
model(
  ar4 = ARIMA(Exports ~ pdq(p=4, d=0, q=0)),
  auto = ARIMA(Exports)
)
glance (fit)

# > glance (fit)
# # A tibble:
# #   2 × 9
#   Country          .model sigma2 log_lik   AIC  AICc   BIC ar_roots  ma_roots 
#   <fct>            <chr>   <dbl>   <dbl> <dbl> <dbl> <dbl> <list>    <list>   
# 1 Egypt, Arab Rep. ar4      7.88   -141.  293.  295.  305. <cpl [4]> <cpl [0]>
# 2 Egypt, Arab Rep. auto     8.05   -142.  293.  294.  303. <cpl [2]> <cpl [1]>
# > 


# Easily create acf and pacf plot()
egy |>
gg_tsdisplay (Exports, plot_type = "partial")


# 9.9 Seasonal ARIMA

leisure <- us_employment |> 
  filter(Title == "Leisure and Hospitality", year(Month) > 2000) |>
  mutate(Employed = Employed / 1000) |>
  select(Month, Employed)

autoplot(leisure, Employed) + labs(title = "US Employment, l&h", y = "People/MIllions")

# very seasonal, and with Trend
leisure |> 
  gg_tsdisplay(difference(Employed, 12), plot_type="partial", lag=36) +
    labs(title = "seasonality differenced" , y = "")
  

leisure |> 
  gg_tsdisplay(difference(Employed, 12) |> difference() , plot_type="partial", lag=36) +
    labs(title = "seasonality differenced" , y = "")
  

fit <- leisure |>
  model (
    arima012011 = ARIMA (Employed ~ pdq (0, 1, 2) + PDQ(0, 1, 1)),
    arima210011 = ARIMA (Employed ~ pdq (2, 1, 0) + PDQ(0, 1, 1)),
    auto = ARIMA (Employed, stepwise = FALSE, approx = FALSE))

# > glance(fit) |> arrange(AICc)
# # A tibble: 3 × 8
#   .model       sigma2 log_lik   AIC  AICc   BIC ar_roots   ma_roots  
#   <chr>         <dbl>   <dbl> <dbl> <dbl> <dbl> <list>     <list>    
# 1 auto        0.00142    395. -780. -780. -763. <cpl [14]> <cpl [12]>
# 2 arima210011 0.00145    392. -776. -776. -763. <cpl [2]>  <cpl [12]>
# 3 arima012011 0.00146    391. -775. -775. -761. <cpl [0]>  <cpl [14]>

fit |> 
  pivot_longer(everything(),
    names_to = "Model name",
    values_to = "orders"
  )
# # A mable: 3 x 2
# # Key:     Model name [3]
#   `Model name`                    orders
#   <chr>                          <model>
# 1 arima012011  <ARIMA(0,1,2)(0,1,1)[12]>
# 2 arima210011  <ARIMA(2,1,0)(0,1,1)[12]>
# 3 auto         <ARIMA(2,1,0)(1,1,1)[12]>


fit |> select(auto) |> 
  gg_tsresiduals(lag=36)

# There is one outof bounds spike in this grap. So let's do a ljung box test.
augment(fit) |> 
  filter(.model == "auto") |> 
  features(.innov, ljung_box, lag=24, dof=4)

# dof is four because
# AUTO  ARIMA(2,1,0)(1,1,1) = 
# AUTO  ARIMA(2,-,-)(1,-,1) = (2 + 1+ 1 = 4) 

# # A tibble: 1 × 3
#   .model lb_stat lb_pvalue
#   <chr>    <dbl>     <dbl>
# 1 auto      16.6     0.680

# P value is good, not enough to tip it into significant reigon. So good.  ? WTF?

forecast(fit, h=36) |> 
  filter(.model == "auto") |> 
  autoplot(leisure) + 
  labs(title = "US Employment, L&H", y = "People/Millions")


# next example
h02 <- PBS |>
  filter(ATC2 == "H02") |> 
  summarise(Cost = sum(Cost)/1e6)

h02 |> autoplot(Cost)
h02 |> autoplot(log(Cost)) # box cox tranformation we'll use b/c stabilize the variance
h02 |> autoplot(log(Cost) |> difference(12)) ## take out seasonality, yearly data.  <- closer to stationary!
#data looks stationary enough, let's plut it acf and pacf.
h02 |> gg_tsdisplay(difference(log(Cost), 12),
  lag_max = 35, plot_type ="partial"
)



fit <- h02 |> 
  model(
    bestmostgood = ARIMA(log(Cost)),
    auto  = ARIMA (log(Cost), stepwise = FALSE, approx = FALSE),
    aut2  = ARIMA (log(Cost), stepwise = FALSE, approx = FALSE, order_constraint = p + q + P + Q <=9),
    guess = ARIMA(log(Cost) ~ 0 + pdq(3,0,1) + PDQ(0,1,2)))

# > report(fit) 
# # A tibble: 4 × 8
#   .model        sigma2 log_lik   AIC  AICc   BIC ar_roots   ma_roots  
#   <chr>          <dbl>   <dbl> <dbl> <dbl> <dbl> <list>     <list>    
# 1 bestmostgood 0.00439    245. -483. -483. -470. <cpl [2]>  <cpl [12]>
# 2 auto         0.00420    251. -488. -487. -465. <cpl [2]>  <cpl [15]>
# 3 aut2         0.00405    254. -489. -487. -456. <cpl [28]> <cpl [25]>
# 4 guess        0.00428    250. -486. -485. -463. <cpl [3]>  <cpl [25]>
# Warning message:

report(fit["bestmostgood"])
gg_tsresiduals(fit["best"])

augment(fit["best"]) |> 
  features(.innov, ljung_box, lag=36, dof=6)

augment(fit["best"]) |> 
  features(.innov, ljung_box, lag=36, dof=6)

report(fit["aut2"])

# > 
# report(fit["aut2"]) 
# Series: Cost 
# Model: ARIMA(4,1,1)(2,1,2)[12] 
# Transformation: log(Cost) 

# Coefficients:
#           ar1     ar2     ar3      ar4      ma1    sar1     sar2     sma1
#       -0.0425  0.2098  0.2017  -0.2273  -0.7424  0.6213  -0.3832  -1.2019
# s.e.   0.2167  0.1813  0.1144   0.0810   0.2074  0.2421   0.1185   0.2491
#         sma2
#       0.4959
# s.e.  0.2135

# sigma^2 estimated as 0.004049:  log likelihood=254.31
# AIC=-488.63   AICc=-487.4   BIC=-456.1
# > 

# This is how you run a ljung box test to see if your model is ok.
# It's this lb_pvalue. If it's greater than .1 it's ok.

# > augment(fit["aut2"]) |> 
#   features(.innov, ljung_box, lag=36, dof=9) 
# # A tibble: 1 × 3
#   .model lb_stat lb_pvalue
#   <chr>    <dbl>     <dbl>
# 1 aut2      36.5     0.106
# > 


# > report(fit["bestmostgood"]) 
# Series: Cost 
# Model: ARIMA(2,1,0)(0,1,1)[12] 
# Transformation: log(Cost) 

# Coefficients:
#           ar1      ar2     sma1
#       -0.8491  -0.4207  -0.6401
# s.e.   0.0712   0.0714   0.0694

# sigma^2 estimated as 0.004387:  log likelihood=245.39
# AIC=-482.78   AICc=-482.56   BIC=-469.77


# > report(fit["auto"])
# Series: Cost 
# Model: ARIMA(2,1,3)(0,1,1)[12] 
# Transformation: log(Cost) 

# Coefficients:
#           ar1      ar2     ma1     ma2      ma3     sma1
#       -1.0194  -0.8351  0.1717  0.2578  -0.4206  -0.6528
# s.e.   0.1648   0.1203  0.2079  0.1177   0.1060   0.0657

# sigma^2 estimated as 0.004203:  log likelihood=250.8
# AIC=-487.6 


h02 <- PBS |>
  filter(ATC2 == "H02") |> 
  summarise(Cost = sum(Cost)/1e6)
fit <- h02 |>
  filter_index (~ "2006 Jun") |> model (
    ARIMA(log(Cost) ~ 0 + pdq (3, 0, 0) + PDQ(2, 1, 0)),
    ARIMA(log(Cost) ~ 0 + pdq (3, 0, 1) + PDQ(2, 1, 0)),
    ARIMA(log(Cost) ~ 0 + pdq (3, 0, 2) + PDQ(2, 1, 0)),
    ARIMA(log(Cost) ~ 0 + pdq (3, 0, 1) + PDQ(1, 1, 0))
)

fit |> forecast(h="2 years") |> accuracy((h02))




#9.10 compare arima to ETS
aus_economy <- global_economy |>
  filter (Code == "AUS") |>
  mutate (Population = Population / 1e6)

aus_economy |>
  slice(-n()) |>
  stretch_tsibble(.init = 10) |>
  model (
    ets = ETS(Population),
    arima = ARIMA(Population)) |>
  forecast(h = 1) |>
  accuracy(aus_economy) |>
  select(.model, ME:RMSSE)

#   # A tibble: 2 × 8
#   .model     ME   RMSE    MAE   MPE  MAPE  MASE RMSSE
#   <chr>   <dbl>  <dbl>  <dbl> <dbl> <dbl> <dbl> <dbl>
# 1 arima  0.0420 0.194  0.0789 0.277 0.509 0.317 0.746
# 2 ets    0.0202 0.0774 0.0543 0.112 0.327 0.218 0.298
# > 

## So ETS is a lot better, let's predict.
aus_economy |>
  model(ETS(Population)) |>
  forecast(h = "5 years") |>
  autoplot(aus_economy) +
    labs(title = "Australian population", y = "People (millions) ")


## One more example 
## YOu can't choose between these two unless you try on the test set.
## calculate differently, one AICc is not the same scale. 
cement <- aus_production |>
  select(Cement) |>
  filter_index("1988 Q1" ~ .)
train <- cement |> filter_index(. ~ "2007 Q4")
fit <- train |>
  model (
    arima = ARIMA(Cement),
    ets = ETS(Cement)
  )

fit |> select(arima) |> report()

# > fit |> select(arima) |> report()
# Series: Cement 
# Model: ARIMA(1,0,1)(2,1,1)[4] w/ drift 

# Coefficients:
#          ar1      ma1   sar1     sar2     sma1  constant
#       0.8886  -0.2366  0.081  -0.2345  -0.8979    5.3884
# s.e.  0.0842   0.1334  0.157   0.1392   0.1780    1.4844

# sigma^2 estimated as 11456:  log likelihood=-463.52
# AIC=941.03   AICc=942.68   BIC=957.35

fit |> select(ets) |> report()
# > fit |> select(ets) |> report()
# Series: Cement 
# Model: ETS(M,N,M) 
#   Smoothing parameters:
#     alpha = 0.7533714 
#     gamma = 0.0001000093 

#   Initial states:
#      l[0]     s[0]    s[-1]    s[-2]     s[-3]
#  1694.712 1.031179 1.045209 1.011424 0.9121874

#   sigma^2:  0.0034

#      AIC     AICc      BIC 
# 1104.095 1105.650 1120.769 

fit |>
  select(arima) |>
  augment() |> 
  features(.innov, ljung_box, lag = 16, dof = 6)
#   .model lb_stat lb_pvalue
#   <chr>    <dbl>     <dbl>
# 1 arima     6.37     0.783


fit |>
  select(ets) |>
  augment() |> 
  features(.innov, ljung_box, lag = 16)
# A tibble: 1 × 3
#   .model lb_stat lb_pvalue
#   <chr>    <dbl>     <dbl>
# 1 ets       10.0     0.865

# now let's compare them on real data.
fit |>
  forecast(h="2 years 6 months") |> 
  accuracy(cement) |>
  select(-ME, -MPE, -ACF1)
# # A tibble: 2 × 7
#   .model .type  RMSE   MAE  MAPE  MASE RMSSE
#   <chr>  <chr> <dbl> <dbl> <dbl> <dbl> <dbl>
# 1 arima  Test   216.  186.  8.68  1.27  1.26
# 2 ets    Test   222.  191.  8.85  1.30  1.29

