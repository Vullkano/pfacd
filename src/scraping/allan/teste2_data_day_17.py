import requests
from bs4 import BeautifulSoup
import csv
import re

def syngenta_temp_vento():
    citys = [
        "Aveiro, Portugal",
        "Beja, Portugal",
        "Braga, Portugal",
        "Bragança, Portugal",
        "Castelo Branco, Portugal",
        "Coimbra, Portugal",
        "Évora, Portugal",
        "Faro, Portugal",
        "Guarda, Portugal",
        "Leiria, Portugal",
        "Lisboa, Portugal",
        "Portalegre, Portugal",
        "Porto, Portugal",
        "Santarém, Portugal",
        "Setúbal, Portugal",
        "Viana do Castelo, Portugal",
        "Vila Real, Portugal",
        "Viseu, Portugal"
    ]

    headers = {
        'accept': '*/*',
        'accept-language': 'pt-BR,pt;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'cf_clearance=7MrPEUbnLONYGJSpDN9L_rW5Cv_FtbzoevKw9c6YfE0-1718580161-1.0.1.1-cmZ9rwM5jhj15kgzgVvtNHYi6b.sikEvRYiXkYMFj3e2PpV_UkvHpTodHJHKB8UYM7yvnb_og3g5F0oorYmOag; SSESS01050bbd327529cb5f3bde04c42f63a8=h%2CdKHTJ7P96poqVzQjD4wA3vB3dGG2MXwLq22OLl3cTMfXCG; __cf_bm=zG_TyPYcho52PAA8V7GfSoLasoXddCDJqqkuAUw1AFs-1718581603-1.0.1.1-_.Js4oTulCNCnmE._iWfUmU8jeTGvVIDPDIQaNWTdVIEzZJd0ZNhVBY2Pexkh5aGs1.UdtFypvTjaR0CH5s4mA',
        'origin': 'https://www.syngenta.pt',
        'priority': 'u=1, i',
        'referer': 'https://www.syngenta.pt/service/previsao-do-tempo',
        'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': 'Linux',
        'sec-ch-ua-platform-version': '6.1.0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    base_url = 'https://www.syngenta.pt/ajax/weather/services/weather-widgets-update'

    for city in citys:
        try:
            data = {
                'locationName': city,
                'synWeatherSettings[fromDate]': '2024-06-17T00:00:00',
                'synWeatherSettings[sprayWindowHourlyEnabled]': '1',
                'synWeatherSettings[showEightHourlyImages]': '1',
                'synWeatherSettings[showPredictability]': '1',
                'synWeatherSettings[showMoreDays]': 'false',
                'synWeatherSettings[toDate]': 'today + 7 days - 1 second',
                'widgets[]': 'weather-widget-1718581609::weather_graph',
                'widgets[]': 'weather-widget-1718580407--2::weather_daily',
                'widgets[]': 'weather-widget-1718580407--4::weather_hourly'
            }

            response = requests.post(base_url, headers=headers, data=data)
            response.raise_for_status()

            # Parsing da resposta JSON
            response_data = response.json()

            # Verificar a estrutura da resposta
            if 'locationName' not in response_data:
                print(f"Erro: 'locationName' não encontrado na resposta para {city}")
                continue

            # Extrair os dados necessários
            city_name = response_data['locationName']
            weather_data = response_data['weatherData']

            # Escrever os dados em um arquivo CSV
            filename = f'dados_para_previs_{re.sub("[^a-zA-Z0-9]+", "_", city_name.lower())}.csv'
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['City', 'Date', 'Temperature', 'Precipitation', 'Wind'])

                for data in weather_data:
                    date = data['date']
                    temperature = data['temperature']
                    precipitation = data['precipitation']
                    wind = data['wind']

                    writer.writerow([city_name, date, temperature, precipitation, wind])

            print(f"Dados salvos para {city_name} em {filename}")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dados para {city}: {e}")

syngenta_temp_vento()
