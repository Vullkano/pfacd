library(tidyverse)
library(conflicted)
library(here)
library(readxl)
library(janitor)
read_xlsx(here("data", "QuebrasJuntoInc.xlsx")) %>% clean_names() -> df

df %>% tabyl(mes, ano) %>% adorn_totals("row") %>% adorn_totals("col")
df %>% tabyl(nivel_de_tensao, decisao) %>% adorn_totals("row") %>% adorn_totals("col")
df %>%
  ggplot(aes(mes %>% as.factor, ano %>% as.factor)) +
  geom_jitter(size=1) +
  theme_minimal() +
  labs(title = "Jitterplot de Quebras por Mês e Ano", x = "Mês", y = "Ano")

