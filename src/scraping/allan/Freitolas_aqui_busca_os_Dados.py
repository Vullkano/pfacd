from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


driver_path = "caminho_para_seu_chromedriver"
options = webdriver.ChromeOptions()
options.add_argument(f"executable_path={driver_path}")

driver = webdriver.Chrome(options=options)

try:
    
    driver.get("https://www.weatheronline.pt/weather/maps/forecastmaps?LANG=pt&CONT=ptpt")

    
    consent_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.fc-cta-consent'))
    )
    consent_button.click()

    
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
        
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ORT"]'))
        )
        input_box.clear()
        input_box.send_keys(district)
        input_box.send_keys(Keys.RETURN)

        time.sleep(5)

        
        link_list = driver.find_elements(By.CSS_SELECTOR, 'ul.hor_list_z li a')
        if len(link_list) > 3:
            link_list[3].click()

        time.sleep(5)

       
        try:
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#dismiss-button'))
            )
            close_button.click()
        except Exception as e:
            print("Erro ao tentar fechar o anúncio:", e)

        
        link_list2 = driver.find_elements(By.CSS_SELECTOR, 'ul.e_hor li a')
        if len(link_list2) > 3:
            link_list2[3].click()

        time.sleep(10)  

        
        response = requests.get(driver.current_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        
        district_div = soup.find('div', class_='hh1')
        district_name = district_div.find('h1').text.strip() if district_div else 'Desconhecido'

        
        rows = soup.find_all('tr')
        temperature, humidity, wind_speed, precipitation = [], [], [], []

        def to_float(text):
            try:
                return float(text)
            except ValueError:
                return 0.0

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

        
        min_length = min(len(temperature), len(humidity), len(wind_speed), len(precipitation))
        temperature = temperature[:min_length]
        humidity = humidity[:min_length]
        wind_speed = wind_speed[:min_length]
        precipitation = precipitation[:min_length]

        
        all_districts_data.append({
            'Distrito': district_name,
            'Temperatura': temperature,
            'Humidade': humidity,
            'Intensidade do Vento': wind_speed,
            'Precipitação': precipitation
        })

   
    df = pd.DataFrame(all_districts_data)

   
    csv_filename = "dados_climaticos_distritos_PT.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Dados salvos em '{csv_filename}' com sucesso!")

finally:
    
    driver.quit()
