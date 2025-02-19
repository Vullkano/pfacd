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


def freitola():
    url = "https://www.gee.gov.pt/pt/publicacoes/estatisticas-tematicas/estatisticas-regionais"
    driver.get(url)
    links = []
    wait = WebDriverWait(driver, 0.5)
    for i in range(35):
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        div_total = soup.find('div', {'class': 'col-md-4 df-total'})
        total_publicacoes = int(div_total.get_text().split()[-1])
        total_paginas = math.ceil(total_publicacoes / 10)
        divs = soup.find_all('div', {'class': 'row title df-mb-10'})
        for div in divs:
            link = div.find('a')['href']
            links.append(link)
        active_li = element.find_element(By.XPATH, "//ul[@class='paginationTop']/li[@class='active']")
        next_li = active_li.find_element(By.XPATH, "./following-sibling::li[1]")
        next_li.click()
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    div_total = soup.find('div', {'class': 'col-md-4 df-total'})
    total_publicacoes = int(div_total.get_text().split()[-1])
    total_paginas = math.ceil(total_publicacoes / 10)
    divs = soup.find_all('div', {'class': 'row title df-mb-10'})
    for div in divs:
        link = div.find('a')['href']
        links.append(link)


    driver.quit()
    with open('links.txt', 'w') as file:
        for word in links:
            file.write(word + '\n')


def plancholas():
    links = []
    html = """<div class="view-content row">
      <div data-drupal-views-infinite-scroll-content-wrapper="" class="views-infinite-scroll-content-wrapper clearfix">    <div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Temporal Região Sul 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Temporal%20Regi%C3%A3o%20Sul%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Temporal Região Sul 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div>
    <div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Dezembro 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Dezembro%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Dezembro 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div>
    <div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Novembro 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Novembro%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Novembro 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div>
    <div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Outubro 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Outubro%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Outubro 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div>
<div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Setembro 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Setembro%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Setembro 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Agosto%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Agosto 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jul 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Julho 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Julho%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Julho 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Junho 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Junho%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Junho 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Maio 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Maio%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Maio 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Abril 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Abril%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Abril 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Depressão Efrain 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Depress%C3%A3o%20Efrain%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Depressão Efrain 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Março 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Mar%C3%A7o%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Março 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Rio Atmosférico (2021)</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Rio%20Atmosf%C3%A9rico%20%282021%29.pdf" type="application/pdf">Evento Excecional Tabela Decisão Rio Atmosférico (2021).pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Deslastre de Frequência (2021)</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Deslastre%20de%20Frequ%C3%AAncia%20%282021%29.pdf" type="application/pdf">Evento Excecional Tabela Decisão Deslastre de Frequência (2021).pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Depressão Hortense (2021)</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Depress%C3%A3o%20Hortense%20%282021%29.pdf" type="application/pdf">Evento Excecional Tabela Decisão Depressão Hortense (2021).pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Fevereiro 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Fevereiro%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Fevereiro 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2022</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Janeiro 2022</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Janeiro%202022.pdf" type="application/pdf">Evento Excecional Tabela Decisão Janeiro 2022.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Dezembro 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Dezembro%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Dezembro 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Novembro 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Novembro%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Novembro 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Outubro 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Outubro%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Outubro 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Setembro 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Setembro%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Setembro 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto 2021.pdf </div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Agosto%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Agosto 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jul 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Julho 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Julho%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Julho 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Junho 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Junho%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Junho 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Maio 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Maio%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Maio 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Abril 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Abril%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Abril 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Março</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_mar_2019.pdf" type="application/pdf">Tabela decisão_mar_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Março 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Mar%C3%A7o%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Março 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Fevereiro 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Fevereiro%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Fevereiro 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2021</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Janeiro 2021</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Janeiro%202021.pdf" type="application/pdf">Evento Excecional Tabela Decisão Janeiro 2021.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Dezembro 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Dezembro%202020_0.pdf" type="application/pdf">Evento Excecional Tabela Decisão Dezembro 2020_0.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Novembro 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20nov%202020.pdf" type="application/pdf">Tabela de decisão - nov 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Outubro 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Outubro%202020.pdf" type="application/pdf">Evento Excecional Tabela Decisão Outubro 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Setembro 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20set%202020.pdf" type="application/pdf">Tabela de decisão - set 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20ago%202020.pdf" type="application/pdf">Tabela de decisão - ago 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jul 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Julho 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20jul%202020.pdf" type="application/pdf">Tabela de decisão - jul 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Junho 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20jun%202020.pdf" type="application/pdf">Tabela de decisão - jun 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Maio 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20mai%202020.pdf" type="application/pdf">Tabela de decisão - mai 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Abril 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20abr%202020.pdf" type="application/pdf">Tabela de decisão - abr 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Depressão 01 e 02 Março (2020)</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20depress%C3%A3o%2001%20e%2002%20de%20mar%C3%A7o.pdf" type="application/pdf">Tabela de decisão - depressão 01 e 02 de março.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Março 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20mar%202020.pdf" type="application/pdf">Tabela de decisão - mar 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Fevereiro 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20fev%202020.pdf" type="application/pdf">Tabela de decisão - fev 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Depressão Glória (2020)</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20depress%C3%A3o%20Gl%C3%B3ria.pdf" type="application/pdf">Tabela de decisão - depressão Glória.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2020</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Janeiro 2020</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20jan%202020.pdf" type="application/pdf">Tabela de decisão - jan 2020.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Dezembro 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_dez_2019.pdf" type="application/pdf">Tabela decisão_dez_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Depressão Elsa e Fabien</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_depress%C3%A3o%20Elsa%20e%20Fabien.pdf" type="application/pdf">Tabela decisão_depressão Elsa e Fabien.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Novembro 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_nov_2019.pdf" type="application/pdf">Tabela decisão_nov_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Outubro 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_out_2019.pdf" type="application/pdf">Tabela decisão_out_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Setembro 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_set_2019.pdf" type="application/pdf">Tabela decisão_set_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Tempestade DEA</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_Tempestade%20DEA.pdf" type="application/pdf">Tabela decisão_Tempestade DEA.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_ago_2019.pdf" type="application/pdf">Tabela decisão_ago_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Junho 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_jun_2019_0.pdf" type="application/pdf">Tabela decisão_jun_2019_0.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Maio 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_mai_2019.pdf" type="application/pdf">Tabela decisão_mai_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Abril 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_abr_2019.pdf" type="application/pdf">Tabela decisão_abr_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Fevereiro 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_fev_2019.pdf" type="application/pdf">Tabela decisão_fev_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Depressão Helena</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_depress%C3%A3o%20Helena.pdf" type="application/pdf">Tabela decisão_depressão Helena.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2019</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Janeiro 2019</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_jan_2019.pdf" type="application/pdf">Tabela decisão_jan_2019.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 2 Dezembro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%202%20Dezembro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 2 Dezembro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Dezembro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%20Dezembro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD Dezembro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 3 Novembro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%203%20Novembro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 3 Novembro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 2 Novembro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%202%20Novembro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 2 Novembro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Novembro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%20Novembro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD Novembro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 4 Outubro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%204%20Outubro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 4 Outubro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Setembro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/1.%20Tabela%20de%20decis%C3%A3o%20-%20EDP_D%20-%20Setembro%202018.pdf" type="application/pdf">1. Tabela de decisão - EDP_D - Setembro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 3 Setembro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%203%20Setembro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 3 Setembro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 2 Setembro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%202%20Setembro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 2 Setembro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Agosto 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/1.%20Tabela%20de%20decis%C3%A3o%20-%20EDP_D%20-%20Agosto%202018.pdf" type="application/pdf">1. Tabela de decisão - EDP_D - Agosto 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 3 Agosto 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%203%20Agosto%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 3 Agosto 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 2 Agosto 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%202%20Agosto%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 2 Agosto 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão IGI Agosto 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20IGI%20Agosto%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão IGI Agosto 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jul 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 3 Julho 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%203%20Julho%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 3 Julho 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 3 Junho 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2021-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%203%20Junho%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 3 Junho 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 2 Maio 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/2.%20Tabela%20de%20decis%C3%A3o%20-%20EDP_D%20-%20Maio%202018.pdf" type="application/pdf">2. Tabela de decisão - EDP_D - Maio 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 3 Maio 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%203%20Maio%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 3 Maio 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Maio 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/1.%20Tabela%20de%20decis%C3%A3o%20EDP_D%20-%20Maio%202018.pdf" type="application/pdf">1. Tabela de decisão EDP_D - Maio 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 2 Abril 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/2.%20Tabela%20de%20decis%C3%A3o%20EDP_D%20-%20Abril%202018.pdf" type="application/pdf">2. Tabela de decisão EDP_D - Abril 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 3 Abril 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%203%20Abril%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 3 Abril 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Abril 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/1.%20Tabela%20Decis%C3%A3o%20-%20EDPD%20abril%202018.pdf" type="application/pdf">1. Tabela Decisão - EDPD abril 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Março 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/1.%20Tabela%20de%20Decis%C3%A3o%20-%20EDP_D_Mar%C3%A7o_2018.pdf" type="application/pdf">1. Tabela de Decisão - EDP_D_Março_2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 4 Março 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%204%20Mar%C3%A7o%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 4 Março 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 3 Março 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/3.%20Tabela%20de%20decis%C3%A3o%20EDP_D%20-%20Mar%C3%A7o%202018.pdf" type="application/pdf">3. Tabela de decisão EDP_D - Março 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 2 Março 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/2.%20Tabela%20Decis%C3%A3o%20-%20EDPD%20mar%C3%A7o%202018.pdf" type="application/pdf">2. Tabela Decisão - EDPD março 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão IGI Março 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20IGI%20Mar%C3%A7o%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão IGI Março 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Fevereiro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/1.%20Tabela%20de%20Decis%C3%A3o%20-%20EDP_D_Fevereiro_2018.pdf" type="application/pdf">1. Tabela de Decisão - EDP_D_Fevereiro_2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão IGI Fevereiro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20IGI%20Fevereiro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão IGI Fevereiro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 2 Fevereiro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/2.%20Tabela%20de%20decis%C3%A3o%20EDP_D%20-%20Fevereiro%202018.pdf" type="application/pdf">2. Tabela de decisão EDP_D - Fevereiro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 4 Janeiro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-06/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20EDPD%204%20Janeiro%202018.pdf" type="application/pdf">Evento Excecional Tabela Decisão EDPD 4 Janeiro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 3 Janeiro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/3.Tabela%20de%20decis%C3%A3o%20EDP_D%20-%20Janeiro%202018.pdf" type="application/pdf">3.Tabela de decisão EDP_D - Janeiro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD 2 Janeiro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/2.%20Tabela%20Decis%C3%A3o%20-%20EDPD%20janeiro%202018.pdf" type="application/pdf">2. Tabela Decisão - EDPD janeiro 2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2018</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Janeiro 2018</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/1.%20Tabela%20de%20Decis%C3%A3o%20-%20EDP_D_Janeiro_2018.pdf" type="application/pdf">1. Tabela de Decisão - EDP_D_Janeiro_2018.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão XLS Dezembro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-vnd-openxmlformats-officedocument-spreadsheetml-sheet file--x-office-spreadsheet"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20Dezembro.xlsx" type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">Tabela Decisão Dezembro.xlsx</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão IGI Dezembro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/IGI_2017_DEZ_TC_001.pdf" type="application/pdf">IGI_2017_DEZ_TC_001.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão XLS 2 Dezembro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-vnd-openxmlformats-officedocument-spreadsheetml-sheet file--x-office-spreadsheet"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20Dezembro_2.xlsx" type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">Tabela Decisão Dezembro_2.xlsx</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDP Distribuição Novembro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-vnd-openxmlformats-officedocument-spreadsheetml-sheet file--x-office-spreadsheet"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDP%20Distribui%C3%A7%C3%A3o_nov_2017.xlsx" type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">Tabela decisão - EDP Distribuição_nov_2017.xlsx</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Novembro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-vnd-openxmlformats-officedocument-spreadsheetml-sheet file--x-office-spreadsheet"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20Novembro.xlsx" type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">Tabela Decisão Novembro.xlsx</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Via Norte Outubro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/EDPD_2017_OUT_T_001_Via%20Norte.pdf" type="application/pdf">EDPD_2017_OUT_T_001_Via Norte.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDP Distribuição XLS Outubro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-vnd-openxmlformats-officedocument-spreadsheetml-sheet file--x-office-spreadsheet"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDP%20Distribui%C3%A7%C3%A3o_out_2017.xlsx" type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">Tabela decisão - EDP Distribuição_out_2017.xlsx</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Via Leiria Outubro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/EDPD_2017_OUT_T_001_Via%20Leiria.pdf" type="application/pdf">EDPD_2017_OUT_T_001_Via Leiria.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Outubro XLS 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-vnd-openxmlformats-officedocument-spreadsheetml-sheet file--x-office-spreadsheet"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20Outubro.xlsx" type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">Tabela Decisão Outubro.xlsx</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Via Norte Outubro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/EDPD_2017_OUT_T_001_Via%20Norte.pdf" type="application/pdf">EDPD_2017_OUT_T_001_Via Norte.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDP Distribuição XLS Outubro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-vnd-openxmlformats-officedocument-spreadsheetml-sheet file--x-office-spreadsheet"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDP%20Distribui%C3%A7%C3%A3o_out_2017.xlsx" type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">Tabela decisão - EDP Distribuição_out_2017.xlsx</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão XLS Setembro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-vnd-openxmlformats-officedocument-spreadsheetml-sheet file--x-office-spreadsheet"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDP%20Distribui%C3%A7%C3%A3o_set_2017.xlsx" type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">Tabela decisão - EDP Distribuição_set_2017.xlsx</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão XLS 2 Setembro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-vnd-openxmlformats-officedocument-spreadsheetml-sheet file--x-office-spreadsheet"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20Setembro.xlsx" type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet">Tabela Decisão Setembro.xlsx</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Setembro 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20EDPD%20-%20Setembro%202017.pdf" type="application/pdf">Tabela de decisão EDPD - Setembro 2017.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão XLS Agosto 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20Agosto.pdf" type="application/pdf">Tabela Decisão Agosto.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20EDPD%20-%20Agosto%202017.pdf" type="application/pdf">Tabela de decisão EDPD - Agosto 2017.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão XLS 2 Agosto 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20Agosto_3.pdf" type="application/pdf">Tabela Decisão Agosto_3.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto 2017 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20EDPD%20-%20Agosto%202017_2.pdf" type="application/pdf">Tabela de decisão EDPD - Agosto 2017_2.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jul 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Julho 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20EDPD%20-%20Julho%202017.pdf" type="application/pdf">Tabela de decisão EDPD - Julho 2017.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Junho 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20EDP%20Distribui%C3%A7%C3%A3o%20-%20Junho%202017.pdf" type="application/pdf">Tabela de decisão EDP Distribuição - Junho 2017.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão XLS Junho 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20Junho_.pdf" type="application/pdf">Tabela Decisão Junho_.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Maio 2017 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20EDPD%20-%20Maio%202017_3.pdf" type="application/pdf">Tabela de decisão EDPD - Maio 2017_3.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2017</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Maio 2017</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20EDP%20Distribui%C3%A7%C3%A3o%20-%20Maio%202017_2.pdf" type="application/pdf">Tabela de decisão EDP Distribuição - Maio 2017_2.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2016</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Agosto 2016</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20EDPD%20-%20agosto%202016_2.pdf" type="application/pdf">Tabela decisão EDPD - agosto 2016_2.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jul 2016</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Julho 2016</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20julho%202016_1.pdf" type="application/pdf">Tabela decisão - julho 2016_1.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2016</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão EDPD Abril 2016 4</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20-%20abril%202016_4.pdf" type="application/pdf">Tabela de decisão - abril 2016_4.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2016</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Fevereiro EE 2016</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Decis%C3%A3o%20EE%20fevereiro%202016_1.pdf" type="application/pdf">Decisão EE fevereiro 2016_1.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2016</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Fevereiro EDPD FEV 2016</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20EDPD_2016_FEV_TC_001.pdf" type="application/pdf">Tabela de decisão EDPD_2016_FEV_TC_001.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Dezembro 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20-%20dezembro.pdf" type="application/pdf">Tabela de decisão - dezembro.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Novembro 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20Decis%C3%A3o%20-%20Novembro%20de%202015.pdf" type="application/pdf">Tabela de Decisão - Novembro de 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Novembro 2015 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20-%20novembro.pdf" type="application/pdf">Tabela de decisão - novembro.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Novembro EDPD 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20Decis%C3%A3o%20-%20EDPD_2015_NOV_TC_001.pdf" type="application/pdf">Tabela de Decisão - EDPD_2015_NOV_TC_001.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Outubro 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20Decis%C3%A3o%20-%20Outubro%20de%202015.pdf" type="application/pdf">Tabela de Decisão - Outubro de 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Outubro 2015 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20outubro.pdf" type="application/pdf">Tabela de decisão outubro.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Outubro 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20Decis%C3%A3o%20-%20Outubro%20de%202015.pdf" type="application/pdf">Tabela de Decisão - Outubro de 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Setembro 2015 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20setembro.pdf" type="application/pdf">Tabela de decisão setembro.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Setembro 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20-%20Setembro%202015.pdf" type="application/pdf">Tabela de decisão - Setembro 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto 2015 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20-%20agosto%202015_1.pdf" type="application/pdf">Tabela Decisão - agosto 2015_1.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto 2 2015 </div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20agosto_2.pdf" type="application/pdf">Tabela de decisão agosto_2.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jul 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Julho 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20-%20julho%202015.pdf" type="application/pdf">Tabela Decisão - julho 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jul 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Julho 2015 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20-%20Julho%202015%20%282%29.pdf" type="application/pdf">Tabela Decisão - Julho 2015 (2).pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Junho 2015 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20junho%202015_.pdf" type="application/pdf">Tabela decisão - junho 2015_.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Junho 2015 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20junho%202015_.pdf" type="application/pdf">Tabela decisão - junho 2015_.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Maio 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20Decis%C3%A3o%20-%20Maio%202015.pdf" type="application/pdf">Tabela de Decisão - Maio 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Maio 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Maio 2 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20-%20maio%202015.pdf" type="application/pdf">Tabela Decisão - maio 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Abril 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20-%20abril%202015.pdf" type="application/pdf">Tabela de decisão - abril 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Abr 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Abril 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20-%20abril%202015.pdf" type="application/pdf">Tabela de decisão - abril 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Março 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20-%20Mar%C3%A7o%202015.pdf" type="application/pdf">Tabela Decisão - Março 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Mar 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Março 2015 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20-%20mar%C3%A7o%202015%20%281%5D.pdf" type="application/pdf">Tabela de decisão - março 2015 (1].pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Fevereiro 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20-%20Fevereiro%202015.pdf" type="application/pdf">Tabela Decisão - Fevereiro 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Fev 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Fevereiro 2015 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20-%20Fevereiro%202015%20%282%29.pdf" type="application/pdf">Tabela Decisão - Fevereiro 2015 (2).pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Janeiro 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20Decis%C3%A3o%20-%20Janeiro%202015.pdf" type="application/pdf">Tabela Decisão - Janeiro 2015.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2015</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Janeiro rel_93 EDPD 2015</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20de%20decis%C3%A3o%20-%20janeiro%202015_rel%2093.pdf" type="application/pdf">Tabela de decisão - janeiro 2015_rel 93.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Março 2014</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDPD%20mar%C3%A7o%202014.pdf" type="application/pdf">Tabela decisão - EDPD março 2014.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Dez 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Dezembro EDPD 2014</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDPD%20dezembro%202014.pdf" type="application/pdf">Tabela decisão - EDPD dezembro 2014.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Nov 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Novembro EDPD 2014</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDPD%20novembro%202014.pdf" type="application/pdf">Tabela decisão - EDPD novembro 2014.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Out 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Outubro EDPD 2014</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDPD%20outubro%202014.pdf" type="application/pdf">Tabela decisão - EDPD outubro 2014.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Set 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Setembro EDPD 2014</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDPD%20setembro%202014.pdf" type="application/pdf">Tabela decisão - EDPD setembro 2014.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto EDPD 2014 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDPD%20agosto%202014_2.pdf" type="application/pdf">Tabela decisão - EDPD agosto 2014_2.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Ago 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Agosto EDPD 2014</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-EDPD%20agosto%202014.pdf" type="application/pdf">Tabela decisão -EDPD agosto 2014.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jul 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Julho EDPD 2014 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDPD%20julho%202014_2.pdf" type="application/pdf">Tabela decisão - EDPD julho 2014_2.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jun 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela Decisão Junho EDPD 2014 2</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20decis%C3%A3o%20-%20EDPD%20junho%202014_2.pdf" type="application/pdf">Tabela decisão - EDPD junho 2014_2.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div><div class="views-row">
    


<div class="card">
      
    
<div>
      
<div class="card-body mt8">
      
            <div class="field field--name-field-date field--type-datetime field--label-hidden field__item">Jan 2014</div>
      
            <div class="field field--name-name field--type-string field--label-hidden field__item">Evento Excecional Tabela ERSE Janeiro 2014</div>
      
  </div>

<div class="icons icons-download card-footer processed">
      
            <div class="hidden field field--name-field-media-file field--type-file field--label-hidden field__item">
<span class="file file--mime-application-pdf file--application-pdf"> <a href="/sites/eredes/files/2019-02/Tabela%20ERSE-EDPD_2014_JAN-Parte1.pdf" type="application/pdf">Tabela ERSE-EDPD_2014_JAN-Parte1.pdf</a></span>
</div>
      
  <svg><use xlink:href="/themes/custom/eredes_theme/assets/svg/sprite.svg#download"></use></svg></div>

  </div>

</div>

  </div></div>

    </div>"""
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('span', {'class': 'file file--mime-application-pdf file--application-pdf'})
    for div in divs:
        link = div.find('a')['href']
        links.append(link)
    with open('links_eredes.txt', 'w') as file:
        for word in links:
            file.write(word + '\n')

plancholas()