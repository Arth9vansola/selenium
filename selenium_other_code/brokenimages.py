import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/broken_images")

all_images = driver.find_elements(By.TAG_NAME, 'img')
broken_images = []

for image in all_images:
  src = image.get_attribute('src')
  print(src)
  if src:
    response = requests.get(src)
    if response.status_code !=200:
     broken_images.append(src)
     print(f"Broken image found: {src} with status code {response.status_code}")

if broken_images:
  print("list of broken images")
  for broken_image in broken_images:
    print(broken_image)
else:
  print("No broken images found")    



