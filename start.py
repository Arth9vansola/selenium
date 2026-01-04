from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/broken_images')
word = driver.find_element(By.CLASS_NAME,'example')
print(word.text)
time.sleep(2)
driver.quit()