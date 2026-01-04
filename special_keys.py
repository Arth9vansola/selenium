from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 : login using enter:
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()

# username = driver.find_element(By.XPATH, "//input[@id='user-name']")
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# login = driver.find_element(By.XPATH, "//input[@id='login-button']")

# username.send_keys("standard_user")
# time.sleep(2)
# password.send_keys("secret_sauce")
# time.sleep(2)
# login.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.quit()

# Example 2: Use TAB to move to next field :
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()

# username = driver.find_element(By.XPATH, "//input[@id='user-name']")
# login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# username.send_keys('standard_user')
# username.send_keys(Keys.TAB) # this will send cursor from username to password field
# time.sleep(2)

# password = driver.switch_to.active_element # now this activate current password field to fill password in it
# password.send_keys('secret_sauce')
# time.sleep(2)
# login.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.quit()

# Example 3: Clear text using Ctrl+A + Backspace :
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()

# username = driver.find_element(By.XPATH, "//input[@id='user-name']")
# time.sleep(2)
# username.send_keys('standard_user')
# time.sleep(2)
# username.send_keys(Keys.CONTROL, "a")
# time.sleep(2)
# username.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# username.send_keys('hello world')
# time.sleep(5)
# driver.quit()

# Example 4: Copy & Paste using keyboard keys :
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()

# username = driver.find_element(By.XPATH, "//input[@id='user-name']")
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# time.sleep(2)
# username.send_keys('standard_user')
# time.sleep(2)
# username.send_keys(Keys.CONTROL, "a")
# time.sleep(2)
# username.send_keys(Keys.CONTROL, "c")
# time.sleep(2)
# username.send_keys(Keys.END)
# time.sleep(2)
# password.send_keys(Keys.CONTROL, "v")
# time.sleep(5)
# driver.quit()

# Example 5: Use Arrow keys (Dropdown / List) :
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/dropdown")
# driver.maximize_window()

# drop = driver.find_element(By.XPATH, "//select[@id='dropdown']")

# drop.send_keys(Keys.ARROW_DOWN)
# time.sleep(2)
# # drop.send_keys(Keys.ARROW_DOWN)
# # time.sleep(2)
# drop.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.quit()

# Example 6: Scroll page using keyboard :
# driver = webdriver.Chrome()
# driver.get("https://automationexercise.com/")
# driver.maximize_window()

# time.sleep(2)
# body = driver.find_element(By.TAG_NAME, "body")

# body.send_keys(Keys.PAGE_DOWN)
# body.send_keys(Keys.PAGE_DOWN)
# body.send_keys(Keys.PAGE_DOWN)
# time.sleep(5)
# driver.quit()

# Example 7: Multi-line input (Chat / Textarea) :
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username = driver.find_element(By.XPATH, "//input[@id='user-name']")
username.send_keys('hello')
time.sleep(2)
username.send_keys(Keys.SHIFT, Keys.RETURN)
time.sleep(2)
username.send_keys('world')
time.sleep(2)
driver.quit()



