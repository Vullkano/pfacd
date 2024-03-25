import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_csv('dados_melhorzim.csv')
# print(a.describe())
# print(a.info())
# print(a.head())
# print(a.dtypes)


# a.plot(kind='bar', x='Unnamed: 0', y='2')
# plt.show()

# a.plot(kind='scatter', x='Unnamed: 0', y='Unnamed: 0')
# plt.show()

# a['22'].value_counts().plot(kind='pie')
# plt.show()

nan_counts = a.isna().sum()
nan_counts.plot(kind='bar')
plt.xlabel('Colunas')
plt.ylabel('Quantidade de NaN')
plt.title('Quantidade de NaN por Coluna')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()