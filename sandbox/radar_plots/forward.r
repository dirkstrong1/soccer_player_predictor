# install necessary packages ----
library(ggplot2)
library(ggradar)
suppressPackageStartupMessages(library(dplyr))
library(scales)

#load necessary data
forward <= read_csv('forward.csv')

# data processing ----
forward_radar <- forward %>%
  mutate_at(vars(-'Player Name'),function(x) x/100)%>%
  tail(3)

# visualization radar plot ----
ggradar(forward_radar) +
  ggsave("forward_radar_plot.png")