# scroll page till element be visible
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://selectorshub.com/xpath-practice-page/")

table = driver.find_element(By.XPATH, "//table[contains(@id,'resultTable')]")
driver.execute_script('arguments[0].scrollIntoView(true);',table)
time.sleep(6)
driver.quit()