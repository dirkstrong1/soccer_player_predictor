# install necessary packages ----
library(ggplot2)
library(ggradar)
suppressPackageStartupMessages(library(dplyr))
library(scales)

#load necessary data
shooting <= read_csv('shooting.csv')

# data processing ----
shooting_radar <- shooting %>%
  #as_tibble(rownames = 'Player Name') %>%
  mutate_at(vars(-'Player Name'),function(x) x/100)%>%
  head(3)

# visualization radar plot ----
ggradar(shooting_radar) +
  ggsave("shooting_radar_plot.png")






