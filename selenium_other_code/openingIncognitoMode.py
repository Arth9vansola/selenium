from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(5)
driver.quit()