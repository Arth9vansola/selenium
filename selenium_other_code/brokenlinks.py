import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/")

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(len(all_links))

for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href) #it used for clicking this href link
    if response.status_code >= 400:
        print(f"{href} is a broken link and status code is {response.status_code}")
        break
  