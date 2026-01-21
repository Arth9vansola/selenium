from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

username = "admin"
password = "admin"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth") #https://username:password@domain/path it's format for basic authentication
time.sleep(5)