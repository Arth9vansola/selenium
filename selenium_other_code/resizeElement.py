from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome() 
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Resizable.html")

resizable_element = driver.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
actual_box_element = driver.find_element(By.XPATH, "//div[@id='resizable']")
actions = ActionChains(driver)
print(actual_box_element.size) 
actions.click_and_hold(resizable_element).move_by_offset(150,150).release().perform()
time.sleep(5)
print(actual_box_element.size)
driver.quit()