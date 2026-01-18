from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome() 
driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds means it will wait for elements to appear for up to 10 seconds or max to max 10 seconds it will wait for that element
driver.maximize_window()



driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()

driver.quit()    