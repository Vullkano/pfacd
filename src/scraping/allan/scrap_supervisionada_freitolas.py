from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv

# Caminho para o chromedriver
driver_path = "/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument(f"executable_path={driver_path}")

driver = webdriver.Chrome(options=options)

def syngenta_temp_vento():
    url = "https://www.syngenta.pt/service/previsao-do-tempo"
    driver.get(url)
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
    try:

        cookie_consent_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Autorizar todos os Cookies']"))
        )
        cookie_consent_button.click()

        for city in citys:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "edit-syn-weather-search-box"))
            )

            search_box.clear()

            for char in city:
                search_box.send_keys(char)
                time.sleep(0.2)  #


            try:
                suggestion_menu = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "ui-menu ui-widget ui-widget-content ui-autocomplete ui-front"))
                )
                first_suggestion = WebDriverWait(suggestion_menu, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "ui-menu-item"))
                )
                first_suggestion.click()
            except Exception as e:
                print(f"Error with suggestions for {city}: {e}")
                continue

            # Esperar pelo carregamento dos dados do tempo
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "weather-graph-chart-wrapper"))
            )

            # Obter o HTML da página
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            valore = []
            date_element = soup.find_all('div', class_='daily-weather-widget')
            for i in date_element:
                if i.find('div', class_='weather-date tw-text-xl', string='17-06'):
                    valore.append(city)
                    weather_values = i.find_all('div', class_='wrapper')

                    for value in weather_values:
                        valore.append(value.get_text(strip=True))

                    with open("dados_para_previs.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(valore)
                else:
                    print("Data específica não encontrada.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

syngenta_temp_vento()
