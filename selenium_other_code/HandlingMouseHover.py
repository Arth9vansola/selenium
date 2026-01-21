from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")

actions = ActionChains(driver)
hover_element = driver.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
time.sleep(5)
actions.move_to_element(hover_element).perform()
driver.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()
time.sleep(5)
