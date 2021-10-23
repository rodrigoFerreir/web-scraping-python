import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

uri = "http://dietaseemagrecimento.com.br/nutricao/tabela-de-calorias/"

option = Options()
option.headless = True
driver = webdriver.Chrome('.\\chromedriver.exe')

driver.get(url=uri)
time.sleep(10)

element = driver.find_element_by_xpath('//*[@id="tblCalorias"]')

html_content = element.get_attribute("outerHTML")

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))[0].head(1000)
df = df_full[['Alimento', 'Porção', 'Calorias']]
df.columns = ['Alimento', 'Porção', 'Calorias']

top_ = {}
top_['Calorias'] = df.to_dict('records')

driver.quit()


js = json.dumps(top_)
fp = open('OrderByCalories.json', 'w')
fp.write(js)
fp.close()
