calc_streak <- function(x) {
  if (!is.atomic(x)) {
    x <- x[, 1]
  }
  if (any(!x %in% c("H", "M"))) {
    stop("Input should only contain hits (\"H\") and misses (\"M\")")
  }
  y <- rep(0, length(x))
  y[x == "H"] <- 1
  y <- c(0, y, 0)
  wz <- which(y == 0)
  streak <- diff(wz) - 1
  return(data.frame(length = streak))
}