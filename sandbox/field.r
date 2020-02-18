# install necessary packages ----
library(ggplot2)
library(ggradar)
suppressPackageStartupMessages(library(dplyr))
library(scales)

#load necessary data
#field_radar = read_csv('write_data/field_radar.csv')

# data processing ----
field_radar <- field_radar %>%
  #as_tibble(rownames = 'classification') %>%
  mutate_at(vars(-'classification'),function(x) x/100)%>%
  head(5)

# visualization radar plot ----
ggradar(field_radar) +
  ggsave("fifa_radar_plot.png")

