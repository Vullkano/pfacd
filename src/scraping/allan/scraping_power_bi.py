from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import requests
from bs4 import BeautifulSoup
import math
import time


driver_path = "/chromedriver"
options = webdriver.ChromeOptions()
options.binary_location = '/path/to/chrome/binary'
options.add_argument(f"executable_path={driver_path}")
driver = webdriver.Chrome(options=options)


def powerbi():
    url = "https://app.powerbi.com/view?r=eyJrIjoiZGIyYzlkYTEtYzVhMS00MTkxLWE5OGEtOWQzZTRlMThmM2NkIiwidCI6ImIwMzU0MDBkLTE3NzYtNDYyZi04YjIxLTYxMTYzYWI0MDNkZiIsImMiOjl9"
    driver.get(url)
    time.sleep(5)
    links = []
    wait = WebDriverWait(driver, 2)
    for i in range(1):
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
    #     div_total = soup.find('div', {'class': 'col-md-4 df-total'})
    #     total_publicacoes = int(div_total.get_text().split()[-1])
    #     total_paginas = math.ceil(total_publicacoes / 10)
    #     divs = soup.find_all('div', {'class': 'row title df-mb-10'})
    #     for div in divs:
    #         link = div.find('a')['href']
    #         links.append(link)
    #     active_li = element.find_element(By.XPATH, "//ul[@class='paginationTop']/li[@class='active']")
    #     next_li = active_li.find_element(By.XPATH, "./following-sibling::li[1]")
    #     next_li.click()
    # element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    # html = driver.page_source

    # soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # div_total = soup.find('div', {'class': 'col-md-4 df-total'})
    # total_publicacoes = int(div_total.get_text().split()[-1])
    # total_paginas = math.ceil(total_publicacoes / 10)
    # divs = soup.find_all('div', {'class': 'row title df-mb-10'})
    # for div in divs:
    #     link = div.find('a')['href']
    #     links.append(link)


    driver.quit()
    # with open('links.txt', 'w') as file:
    #     for word in links:
    #         file.write(word + '\n')

powerbi()