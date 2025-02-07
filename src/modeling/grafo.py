from matplotlib import pyplot as plt
from unidecode import unidecode
import networkx as nx
from pyprojroot.here import here
import geopandas as gpd
from tqdm.notebook import tqdm
import pandas

# pandas.set_option('expand_frame_repr', False)
# read here(data/gadm41_PRT_2.json) (geojson)
concelhos = gpd.read_file(here('data/gadm41_PRT_2.json')) # https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_PRT_2.json.zip


def shared_border(a, b):
  return a.touches(b) | a.intersects(b)


def transform_concelhos(x):
  return unidecode(x).upper().replace(' ', '').replace('-', '')


zip_codes = {}

G = nx.Graph()
for index, row in concelhos.iterrows():
  if row['NAME_1'] == 'Azores' or row['NAME_1'] == 'Madeira':
    continue
  G.add_node(transform_concelhos(row['NAME_2']), pos=(row.geometry.centroid.x, row.geometry.centroid.y))
  zip_codes[row["CC_2"]] = transform_concelhos(row['NAME_2'])

for i, row1 in tqdm(concelhos.iterrows()):
  for j, row2 in concelhos.iterrows():
    # ignore azores e madeira
    if row1['NAME_1'] == 'Azores' or row1['NAME_1'] == 'Madeira':
      continue
    if i != j and shared_border(row1.geometry, row2.geometry):
      G.add_edge(transform_concelhos(row1['NAME_2']), transform_concelhos(row2['NAME_2']))

if __name__ == '__main__':
  pos = nx.get_node_attributes(G, 'pos')
  nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3, font_size=7)
  plt.show()

  # write geopandas as csv without geometries
  # concelhos.drop(columns=['geometry']).to_csv(here('data/temp.csv'))


# apply
def smallest_path(start, end):
  return nx.shortest_path(G, start, end)

# search torres
concelhos[concelhos['NAME_2'].str.contains('Torres')]