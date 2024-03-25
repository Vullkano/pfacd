import pandas as pd
import csv

data = []
with open('output.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

df = pd.DataFrame(data)

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

df.to_csv('dados_melhorzim.csv', index=True)