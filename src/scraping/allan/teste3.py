import requests
from bs4 import BeautifulSoup
import pandas as pd

# Função para converter texto para float ou zero se não for possível
def to_float(text):
    try:
        return float(text)
    except ValueError:
        return 0.0

# Função para extrair dados da página de clima
def extract_weather_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraindo o distrito
    district_div = soup.find('div', class_='hh1')
    district = district_div.find('h1').text.strip() if district_div else 'Desconhecido'

    # Extração das linhas da tabela
    rows = soup.find_all('tr')
    temperature, humidity, wind_speed, precipitation = [], [], [], []

    for row in rows:
        cells = row.find_all('td')
        if cells:
            label = cells[0].text.lower()
            data = [to_float(cell.text) for cell in cells[1:]]
            
            if 'temperatura' in label:
                temperature = data
                max_temp = max(temperature)
                min_temp = min(temperature)
                med_temp = sum(temperature) / len(temperature) if temperature else 0.0
            elif 'humidade relativa' in label:
                humidity = data
                med_humid = sum(humidity) / len(humidity) if humidity else 0.0
            elif 'intensidade média do vento' in label:
                wind_speed = data
                med_wind = sum(wind_speed) / len(wind_speed) if wind_speed else 0.0
            elif 'precipitação' in label:
                precipitation = data
                med_precipita = sum(precipitation) / len(precipitation) if precipitation else 0.0

            # Verificação dos comprimentos das listas
            print(f"Temperaturas: {len(temperature)}")
            print(f"Humidades: {len(humidity)}")
            print(f"Intensidade do Vento: {len(wind_speed)}")
            print(f"Precipitação: {len(precipitation)}")

            # Garantir que todas as listas tenham o mesmo tamanho
            min_length = min(len(temperature), len(humidity), len(wind_speed), len(precipitation))
            temperature = temperature[:min_length]
            humidity = humidity[:min_length]
            wind_speed = wind_speed[:min_length]
            precipitation = precipitation[:min_length]

            return {
                'Distrito': district,
                'Temperatura': temperature,
                'Humidade': humidity,
                'Intensidade do Vento': wind_speed,
                'Precipitação': precipitation
            }

def search_district_weather(district):
    url = f"https://www.weatheronline.pt/cgi-bin/suchen?LANG=pt&ORT={district}"
    return extract_weather_data(url)

# Lista de distritos
citys = [
    "Aveiro",
    "Beja",
    "Braga",
    "Bragança",
    "Castelo Branco",
    "Coimbra",
    "Évora",
    "Faro",
    "Guarda",
    "Leiria",
    "Lisboa",
    "Portalegre",
    "Porto",
    "Santarém",
    "Setúbal",
    "Viana do Castelo",
    "Vila Real",
    "Viseu"
]


all_districts_data = []

for district in citys:
    print(f"Coletando dados para o distrito de {district}...")
    try:
        data = search_district_weather(district)
        all_districts_data.append(data)
    except Exception as e:
        print(f"Erro ao coletar dados para o distrito de {district}: {e}")

# Criar DataFrame a partir dos dados coletados
df = pd.DataFrame(all_districts_data)

# Salvar os dados em um arquivo CSV
csv_filename = "dados_climaticos_distritos_PT.csv"
df.to_csv(csv_filename, index=False)
print(f"Dados salvos em '{csv_filename}' com sucesso!")
