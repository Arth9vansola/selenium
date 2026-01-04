from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/')
time.sleep(5)
driver.maximize_window()

# search_box = driver.find_element(By.XPATH, "//input[@id='tnb-google-search-input']")
# search_box.send_keys('python')
# hrefs = driver.find_elements(By.TAG_NAME, 'a')
# for href in hrefs:
#   print(href.get_attribute('href'))
# time.sleep(2)
# search_box.send_keys(Keys.RETURN)

bg_color = driver.find_element(By.XPATH, "//div[@id='tnb-login-btn']")
# print(bg_color.value_of_css_property('background-color'))
print(bg_color.is_displayed())
print(bg_color.is_enabled)
print(bg_color.is_selected)
time.sleep(5)
# search_box.clear()
# time.sleep(2)
driver.quit()
