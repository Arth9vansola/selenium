from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# 1 Handling JavaScript Alert only without any cancel and all
# js_alert_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
# js_alert_button.click()
# time.sleep(2)

# # print and accept alert
# alert = driver.switch_to.alert
# alert_text = alert.text
# print("Alert Text:", alert_text)
# time.sleep(2)
# alert.accept()
# time.sleep(2)

# 2 Handling JavaScript Confirm Alert with OK and Cancel
# js_alert_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
# js_alert_button.click()
# time.sleep(2)

# # print and accept alert
# alert = driver.switch_to.alert
# alert_text = alert.text
# print("Alert Text:", alert_text)
# time.sleep(2)
# alert.dismiss()
# time.sleep(2)

# 3 Handling JavaScript Confirm Alert with OK and Cancel with prompt
js_alert_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
js_alert_button.click()
time.sleep(2)

# print and accept alert
alert = driver.switch_to.alert
alert_text = alert.text
print("Alert Text:", alert_text)
time.sleep(2)
alert.send_keys("Selenium Test")
time.sleep(2)
alert.accept()
time.sleep(2)

