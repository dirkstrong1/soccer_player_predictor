# install necessary packages ----
library(ggplot2)
library(ggradar)
suppressPackageStartupMessages(library(dplyr))
library(scales)

#load necessary data
field_radar <= read_csv('field_radar.csv')

# data processing ----
fifa_radar <- fifa_radar %>%
  #as_tibble(rownames = 'classification') %>%
  mutate_at(vars(-'classification'),function(x) x/100)%>%
  head(28)

# visualization radar plot ----
ggradar(field_radar) +
  ggsave("field_radar_plot.png")
