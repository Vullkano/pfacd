# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from io import BytesIO 
import requests
import math
import time
import pdfplumber
import csv


# driver_path = "/chromedriver"
# options = webdriver.ChromeOptions()
# options.binary_location = '/path/to/chrome/binary'
# options.add_argument(f"executable_path={driver_path}")
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.docsumo.com/free-tools/extract-tables-from-pdf-images")

# #caminho_arquivo = '/caminho/para/o/seu/arquivo.pdf'

# botao_enviar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
# botao_enviar.send_keys(caminho_arquivo)


# WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(text(), 'Uploading...')]")))

# botao_baixar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='sb1d9 sRnVG DGd4r pZGKy']")))

# botao_baixar.click()

# time.sleep(10)
# botao_baixar1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "div[@class='PS1_9'][2]/button")))
# botao_baixar1.click()
# driver.quit()

with open('links_eredes.txt', 'r') as txt:
    links = ["https://www.e-redes.pt"+line.strip() for line in txt]

url = ["https://www.e-redes.pt/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Temporal%20Regi%C3%A3o%20Sul%202022.pdf"]
blabl = 0
space = ["  ","   ","  ","  ","   "]

for link in url:
    response = requests.get(link)
    a = link.split("/")[-1]
    if response.status_code == 200:
        with pdfplumber.open(BytesIO(response.content)) as pdf:
            with open('output.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                
                for i, page in enumerate(pdf.pages):
                    tables = page.extract_tables()
                    for table in tables:
                        for row in table:
                            if blabl == 0:
                                row.append('freguesia')
                                writer.writerow(row)
                                blabl += 1
                            else:
                                row.append(f'{a}')
                                writer.writerow(row)
                        writer.writerow(space)
                            
    else:
        print("Falha ao baixar o PDF")