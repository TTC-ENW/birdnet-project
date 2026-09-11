# Explore birdnet prediction data

library(dplyr)
library(lubridate)
library(stringr)
library(birdnetTools)


dat <- read.csv("outputs/results.csv")

dat <- dat |>
  mutate(
    filename = basename(input),
    station = str_extract(filename, "^[^_]+"),
    datetime = ymd_hms(
      str_extract(filename, "\\d{8}_\\d{6}"),
      tz = "America/Edmonton"
    )
  )
