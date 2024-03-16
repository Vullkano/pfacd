from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import math
import time


driver_path = "/chromedriver"
options = webdriver.ChromeOptions()
options.binary_location = '/path/to/chrome/binary'
options.add_argument(f"executable_path={driver_path}")
driver = webdriver.Chrome(options=options)
driver.get("https://www.docsumo.com/free-tools/extract-tables-from-pdf-images")

caminho_arquivo = '/caminho/para/o/seu/arquivo.pdf'

botao_enviar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
botao_enviar.send_keys(caminho_arquivo)


WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.XPATH, "//div[contains(text(), 'Uploading...')]"))
)

botao_baixar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='sb1d9 sRnVG DGd4r pZGKy']"))
)

botao_baixar.click()

time.sleep(10)
botao_baixar1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "div[@class='PS1_9'][2]/button"))
)
botao_baixar1.click()
driver.quit()