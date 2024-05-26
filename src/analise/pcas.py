import pandas as pd
from pyarrow import feather
from pyprojroot.here import here
from sklearn.preprocessing import StandardScaler
from pca import pca
import janitor # necessary
eventos_inputation_complete = feather.read_feather(here("data/before_pcas.feather"))

eventos_inputation_complete = eventos_inputation_complete.select_columns("tiepi_mt_min_", "saifi_mt_#_", "saidi_mt_min_", "end_mwh_", "saifi_bt_#_", "saidi_bt_min_")

scaler = StandardScaler()
scaler.fit(eventos_inputation_complete)
eventos_inputation_complete_scaled = pd.DataFrame(scaler.transform(eventos_inputation_complete), columns=eventos_inputation_complete.columns)

model = pca(n_components=5)
model.fit_transform(eventos_inputation_complete_scaled)
model.plot()[0].show()
# 2 is best

model = pca(n_components=2)
model.fit_transform(eventos_inputation_complete_scaled)
# write these pcas results
eventos_pcas = model.results
# caguei nos pcas
eventos_pcas.to_feather(here("data/eventos_pcas.feather"))