from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")

driver.switch_to.new_window('tab') # Open a new tab in current window

driver.get("https://playwright.dev/")

number_of_tabs = len(driver.window_handles)  # it will give number of tabs opened
print(f"Number of tabs opened: {number_of_tabs}")

tabs = driver.window_handles  # it will give the unique id of each tab opened
print(f"Unique id of each tab opened: {tabs}")

current_tab = driver.current_window_handle  # it will give the unique id of current tab
print(f"Unique id of current tab: {current_tab}")


driver.find_element(By.XPATH , "//a[normalize-space()='Docs']").click()
time.sleep(2)

firstTab = driver.window_handles[0]
if current_tab != firstTab:
  driver.switch_to.window(firstTab) # switching to first tab

time.sleep(5)
driver.find_element(By.CSS_SELECTOR, 'body > header:nth-child(1) > nav:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1) > span:nth-child(1)').click()

time.sleep(10)
driver.quit()