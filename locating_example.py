from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.apple.com")

# Find single element
button = driver.find_element(By.ID, "submit_btn")

# Find multiple elements
all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"Found {len(all_links)} links")

# Find nested element
login_form = driver.find_element(By.ID, "loginForm")
username_input = login_form.find_element(By.NAME, "username")

driver.quit()
