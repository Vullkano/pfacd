from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import time

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

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Modo não headless
        page = browser.new_page()
        url = "https://www.syngenta.pt/service/previsao-do-tempo"
        page.goto(url)
        
        try:
            # Esperar e clicar no botão de consentimento de cookies
            page.wait_for_selector("button:text('Autorizar todos os Cookies')", timeout=20000)
            page.click("button:text('Autorizar todos os Cookies')")
            print("Cookies consentidos.")

            for city in citys:
                # Esperar a caixa de pesquisa
                page.wait_for_selector("#edit-syn-weather-search-box", timeout=20000)
                search_box = page.locator("#edit-syn-weather-search-box")
                print(f"Buscando por cidade: {city}")
                search_box.fill(city)
                time.sleep(1)  # Pequena pausa para garantir que o campo esteja preenchido
                
                # Esperar a sugestão aparecer e clicar na primeira sugestão
                page.wait_for_selector(".ui-menu-item", timeout=20000)
                page.click(".ui-menu-item")
                time.sleep(2)  # Esperar os resultados carregarem

                # Aguarda o carregamento do gráfico do tempo
                page.wait_for_selector(".weather-graph-chart-wrapper", timeout=20000)

                html = page.content()
                soup = BeautifulSoup(html, 'html.parser')

                valore = []
                date_element = soup.find_all('div', class_='daily-weather-widget')
                for i in date_element:
                    if i.find('div', class_='weather-date tw-text-xl', string='17-06'):
                        valore.append(city)
                        weather_values = i.find_all('div', class_='wrapper')

                        for value in weather_values:
                            valore.append(value.get_text(strip=True))

                        with open("dados_para_previs.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(valore)
                    else:
                        print(f"Data específica não encontrada para {city}")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            browser.close()

syngenta_temp_vento()
