library(fpp3)
library(patchwork)
library(USgas)
library(lubridate)
library(scales)
options(scipen = 999)
data(global_economy)


### 8.1 simple exponential smoothing 

algeria_economy <- global_economy |>
  filter(Country == "Algeria")


fit <- algeria_economy |> # fit:mable
  model(ANN = ETS(Exports ~ error("A") + trend("N") + season("N")))

report(fit)

# It builds the alpha for you!

# > report(fit)
# Series: Exports
# Model: ETS(A,N,N)
#   Smoothing parameters:
#     alpha = 0.8399875

#   Initial states:
#    l[0]
#  39.539

#   sigma^2:  35.6301

#      AIC     AICc      BIC
# 446.7154 447.1599 452.8968
# >

# you can also autoplot: 
components(fit) |> autoplot()

fit |>
  forecast(h=5) |>
  autoplot(algeria_economy) + labs (y = "% of GDP", title = "Exports: Algeria")

# 8.2 Exponential smoothing, with trend

aus_economy <- global_economy |>
  filter(Code =="AUS") |> 
  mutate(Pop = Population / 1e6) # to millions! 

fit <- aus_economy |> ## ------------------___  <- see the capital A here?
  model(AAN = ETS(Pop ~ error("A") + trend("A") + season("N")))

report(fit)
# > report(fit)
# Series: Pop 
# Model: ETS(A,A,N) 
#   Smoothing parameters:
#     alpha = 0.9999     <-- ALPHA!
#     beta  = 0.3266366  <-- BETA!! 

#   Initial states:
#      l[0]      b[0]
#  10.05414 0.2224818

#   sigma^2:  0.0041

#       AIC      AICc       BIC 
# -76.98569 -75.83184 -66.68347 
# > 

components(fit) |> autoplot()

components(fit) |> 
  left_join(fitted(fit), by = c("Country", ".model", "Year"))

# # A dable: 59 x 8 [1Y]
# # Key:     Country, .model [1]
# # :        Pop = lag(level, 1) + lag(slope, 1) +
# #   remainder
#    Country   .model  Year   Pop level slope remainder .fitted
#    <fct>     <chr>  <dbl> <dbl> <dbl> <dbl>     <dbl>   <dbl>
#  1 Australia AAN     1959  NA    10.1 0.222 NA           NA  
#  2 Australia AAN     1960  10.3  10.3 0.222 -0.000145    10.3
#  3 Australia AAN     1961  10.5  10.5 0.217 -0.0159      10.5
#  4 Australia AAN     1962  10.7  10.7 0.231  0.0418      10.7
#  5 Australia AAN     1963  11.0  11.0 0.223 -0.0229      11.0
#  6 Australia AAN     1964  11.2  11.2 0.221 -0.00641     11.2
#  7 Australia AAN     1965  11.4  11.4 0.221 -0.000314    11.4
#  8 Australia AAN     1966  11.7  11.7 0.235  0.0418      11.6
#  9 Australia AAN     1967  11.8  11.8 0.206 -0.0869      11.9
# 10 Australia AAN     1968  12.0  12.0 0.208  0.00350     12.0
# # ℹ 49 more rows
# # ℹ Use `print(n = ...)` to see more rows

# now we can forecast
fit |>
  forecast(h = 10) |>
  autoplot(aus_economy) +
  labs(y = "millions", title = "Population: Australia")

# Additave Damped 
fit <- aus_economy |> ## ------------------___  <- see the D?
  model(AAN = ETS(Pop ~ error("A") + trend("Ad") + season("N"))) 

fit |> 
  forecast(h = 30) |>
  autoplot(aus_economy)


## Now let' put them all together


aus_economy <- global_economy |>
  filter(Code =="AUS") |> 
  mutate(Pop = Population / 1e6) # to millions!



library(fpp3)
data(global_economy)

aus_economy <- global_economy |>
  filter(Code =="AUS") |> 
  mutate(Pop = Population / 1e6) # to millions!



fit <- aus_economy |>
  filter(Year <= 2010) |>
  model(
    ses =    ETS(Pop ~ error("A") + trend("N")  + season("N")),
    holt =   ETS(Pop ~ error("A") + trend("A")  + season("N")),
    damped = ETS(Pop ~ error("A") + trend("Ad") + season("N"))
  )

tidy(fit)
accuracy(fit)

# > accuracy(fit)
# # A tibble: 3 × 11
#   Country   .model .type       ME   RMSE    MAE    MPE  MAPE  MASE RMSSE    ACF1
#   <fct>     <chr>  <chr>    <dbl>  <dbl>  <dbl>  <dbl> <dbl> <dbl> <dbl>   <dbl>
# 1 Australia ses    Train… 0.231   0.242  0.231  1.48   1.48  0.980 0.990  0.267 
# 2 Australia holt   Train… 0.00716 0.0646 0.0451 0.0336 0.289 0.192 0.264  0.0504
# 3 Australia damped Train… 0.0157  0.0665 0.0466 0.0883 0.300 0.198 0.272 -0.0334
# > 

#8.3 Holt's trend and seasonality

data(tourism)
aus_holidays3 <- tourism |>
  filter(Purpose == "Holiday") |>
  summarise(Trips = sum(Trips))

fit3 <- aus_holidays3 |>
  model(
      additive      =  ETS(Trips ~ error("A") + trend("A")  + season("A")),
      multiplicative = ETS(Trips ~ error("M") + trend("N")  + season("M")))
fc3 <- fit3 |> forecast() 

tidy(fit3) |>
  spread(.model, estimate)
# A tibble: 9 × 3
#   term     additive multiplicative
#   <chr>       <dbl>          <dbl>
# 1 alpha    0.236          0.358   
# 2 b[0]   -37.4           NA       
# 3 beta     0.0298        NA       
# 4 gamma    0.000100       0.000969
# 5 l[0]  9899.          9667.      
# 6 s[-1] -684.             0.927   
# 7 s[-2] -290.             0.968   
# 8 s[-3] 1512.             1.16    
# 9 s[0]  -538.             0.943   

## ONe more exam[mple

data(pedestrian)
sth_cross_ped <- pedestrian |>
  filter(
    Date >= "2016-07-01",
    Sensor == "Southern Cross Station"
  ) |>
  index_by(Date) |>
  summarise(Count = sum(Count) / 1000) 

sth_cross_ped |>
  filter(Date <= "2016-07-31") |> 
  model(hw = ETS(Count ~ error("M") + trend("Ad") + season("M"))) |>
  forecast(h = "2 weeks") |> 
  autoplot(sth_cross_ped |> filter(Date <= "2016-08-14")) +
    labs(
      title = "Daily Traffic Southern Cross",
      y = "Pedestrians ('000)"
    )


#8.6
fit <- global_economy |>
  mutate(Pop = Population / 1e6) |>
  model(ets = ETS(Pop))

fit

# > fit
# # A mable: 263 x 2
# # Key:     Country [263]
#    Country                      ets
#    <fct>                    <model>
#  1 Afghanistan         <ETS(A,A,N)>
#  2 Albania             <ETS(M,A,N)>
#  3 Algeria             <ETS(M,A,N)>
#  4 American Samoa      <ETS(M,A,N)>
#  5 Andorra             <ETS(M,A,N)>
#  6 Angola              <ETS(M,A,N)>
#  7 Antigua and Barbuda <ETS(M,A,N)>
#  8 Arab World          <ETS(M,A,N)>
#  9 Argentina           <ETS(A,A,N)>
# 10 Armenia             <ETS(M,A,N)>
# # ℹ 253 more rows

fit |>
  forecast(h=5 )

# > fit |>
# +   forecast(h=5 )
# # A fable: 1,315 x 5 [1Y]
# # Key:     Country, .model [263]
#    Country     .model  Year             Pop .mean
#    <fct>       <chr>  <dbl>          <dist> <dbl>
#  1 Afghanistan ets     2018    N(36, 0.012) 36.4 
#  2 Afghanistan ets     2019    N(37, 0.059) 37.3 
#  3 Afghanistan ets     2020     N(38, 0.16) 38.2 
#  4 Afghanistan ets     2021     N(39, 0.35) 39.0 
#  5 Afghanistan ets     2022     N(40, 0.64) 39.9 
#  6 Albania     ets     2018 N(2.9, 0.00012)  2.87
#  7 Albania     ets     2019  N(2.9, 0.0006)  2.87
#  8 Albania     ets     2020  N(2.9, 0.0017)  2.87
#  9 Albania     ets     2021  N(2.9, 0.0036)  2.86
# 10 Albania     ets     2022  N(2.9, 0.0066)  2.86
# # ℹ 1,305 more rows

aus_holidays <- tourism |> 
  filter(Purpose == "Holiday") |>
  summarise(Trips = sum(Trips))

fit4 <- aus_holidays |>
  model(ets = ETS(Trips))|>
  report()

# > fit <- aus_holidays |>
# +   model(ets = ETS(Trips))|>
# +   report()
# Series: Trips 
# Model: ETS(M,N,M) 
#   Smoothing parameters:
#     alpha = 0.3578226 
#     gamma = 0.0009685565 

#   Initial states:
#      l[0]      s[0]     s[-1]    s[-2]    s[-3]
#  9666.501 0.9430367 0.9268433 0.968352 1.161768

#   sigma^2:  0.0022

#      AIC     AICc      BIC 
# 1331.372 1332.928 1348.046 

comp_fit4 <- components(fit4)
autoplot(comp_fit4) + labs(title = "ETS(M,N,M) components")

residuals(fit)
residuals(fit, type="response")

fit4 |> augment()
# > fit4 |> augment()
# A tsibble: 80 x 6 [1Q]
# Key:       .model [1]
#    .model Quarter  Trips .fitted .resid   .innov
#    <chr>    <qtr>  <dbl>   <dbl>  <dbl>    <dbl>
#  1 ets    1998 Q1 11806.  11230.  576.   0.0513 
#  2 ets    1998 Q2  9276.   9532. -257.  -0.0269 
#  3 ets    1998 Q3  8642.   9036. -393.  -0.0435 
#  4 ets    1998 Q4  9300.   9050.  249.   0.0275 
#  5 ets    1999 Q1 11172.  11260.  -88.0 -0.00781
#  6 ets    1999 Q2  9608.   9358.  249.   0.0266 
#  7 ets    1999 Q3  8914.   9042. -129.  -0.0142 
#  8 ets    1999 Q4  9026.   9154. -129.  -0.0140 
#  9 ets    2000 Q1 11071.  11221. -150.  -0.0134 
# 10 ets    2000 Q2  9196.   9308. -111.  -0.0120 


# 8.7 
data(PBS)
h02 <- PBS |>
  filter(ATC2 == "H02") |>
  summarise(Cost = sum(Cost))

h02 |> autoplot(Cost)

## Let it choose for you!
h02 |> 
  model(ETS(Cost)) |>
    report()
# > h02 |> 
# +   model(ETS(Cost)) |>
# +     report()
# Series: Cost 
# Model: ETS(M,Ad,M)     ###> this is what it's suggesting
#   Smoothing parameters:
#     alpha = 0.3071016 
#     beta  = 0.0001006793  |- not much of a slope!
#     gamma = 0.0001007181  |-
#     phi   = 0.977528 

#   Initial states:
#      l[0]    b[0]      s[0]     s[-1]     s[-2]     s[-3]     s[-4]    s[-5]
#  417268.7 8205.82 0.8716807 0.8259747 0.7562808 0.7733338 0.6872373 1.283821
#     s[-6]    s[-7]    s[-8]    s[-9]   s[-10]    s[-11]
#  1.324616 1.180067 1.163601 1.104801 1.047963 0.9806235

#   sigma^2:  0.0046  ## veriance of epsilon 

#      AIC     AICc      BIC 
# 5515.212 5518.909 5574.938 
# ----------- | the corrected version for small samples. 

## Chose it yourself! 
h02 |>
  model(ETS(Cost ~ error("A") + trend("A") + season("A"))) |>
  report()
# > h02 |>
# +   model(ETS(Cost ~ error("A") + trend("A") + season("A"))) |>
# +   report()
# Series: Cost 
# Model: ETS(A,A,A) 
#   Smoothing parameters:
#     alpha = 0.1702163 
#     beta  = 0.006310854 
#     gamma = 0.4545987 

#   Initial states:
#      l[0]     b[0]      s[0]     s[-1]     s[-2]     s[-3]     s[-4]    s[-5]
#  409705.9 9097.111 -99075.37 -136602.3 -191496.1 -174530.8 -241436.7 210643.8
#     s[-6]    s[-7]    s[-8]    s[-9]  s[-10]    s[-11]
#  244644.2 145368.2 130569.6 84457.69 39131.7 -11673.71

#   sigma^2:  3498869384

#      AIC     AICc      BIC 
# 5585.278 5588.568 5641.686 
# --------| <- AICc is much bigger, so not as good as a model

# Let's compare 
h02 |>
  model(
    auto = ETS(Cost), 
    AAA  = ETS(Cost ~ error("A") + trend("A") + season("A"))
  ) |>
  accuracy()

# > h02 |>
# +   model(
# +     auto = ETS(Cost), 
# +     AAA  = ETS(Cost ~ error("A") + trend("A") + season("A"))
# +   ) |>
# +   accuracy()
# # A tibble: 2 × 10
#   .model .type        ME   RMSE    MAE     MPE  MAPE  MASE RMSSE    ACF1
#   <chr>  <chr>     <dbl>  <dbl>  <dbl>   <dbl> <dbl> <dbl> <dbl>   <dbl>
# 1 auto   Training  2461. 51102. 38649. -0.0127  4.99 0.638 0.689 -0.0958
# 2 AAA    Training -5780. 56784. 43378. -1.30    6.05 0.716 0.766  0.0258
# ---------------------------|    <- much better!! 
