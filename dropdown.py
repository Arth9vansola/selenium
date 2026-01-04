from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


# Example 1: Select car from registration form :
# driver = webdriver.Chrome()
# driver.get("https://www.automationtesting.co.uk/dropdown.html")
# driver.maximize_window()

# drop = driver.find_element(By.XPATH, "//select[@id='cars']")
# select = Select(drop)
# time.sleep(2)
# select.select_by_visible_text('BMW')
# time.sleep(5)

# Example 2: Select option using value :
# driver = webdriver.Chrome()
# driver.get("https://www.automationtesting.co.uk/dropdown.html")
# driver.maximize_window()

# drop = driver.find_element(By.XPATH, "//select[@id='cars']")
# select = Select(drop)
# time.sleep(2)
# select.select_by_value("bmw")
# time.sleep(5)

# Example 3: Print all dropdown values (Verification) :
# driver = webdriver.Chrome()
# driver.get("https://www.automationtesting.co.uk/dropdown.html")
# driver.maximize_window()

# drop = driver.find_element(By.XPATH, "//select[@id='cars']")
# select = Select(drop)
# time.sleep(2)
# for option in select.options:
#   print(option.text)

# Example 4: Verify default selected option :
# driver = webdriver.Chrome()
# driver.get("https://www.automationtesting.co.uk/dropdown.html")
# driver.maximize_window()

# drop = driver.find_element(By.XPATH, "//select[@id='cars']")
# select = Select(drop)
# time.sleep(2)
# default_option = select.first_selected_option
# print(default_option.text)

# Example 5: Select last option dynamically  :
# driver = webdriver.Chrome()
# driver.get("https://www.automationtesting.co.uk/dropdown.html")
# driver.maximize_window()

# drop = driver.find_element(By.XPATH, "//select[@id='cars']")
# select = Select(drop)
# time.sleep(2)
# last = select.options
# select.select_by_index(len(last)-1)
# time.sleep(2)

# Example 6: Multi-select dropdown (Skills form) :
# driver = webdriver.Chrome()
# driver.get("http://tutorialspoint.com/selenium/practice/select-menu.php")
# driver.maximize_window()

# drop = driver.find_element(By.XPATH, "//input[@id='demo-multiple-select-input']")
# select = Select(drop)
# time.sleep(2)
# select.select_by_visible_text("Bookd")
# time.sleep(2)
# select.select_by_visible_text("Movies, Music & Games")
# time.sleep(2)
# select.select_by_visible_text("Electronics & Computers")
# time.sleep(5)

# Example 7: Clear all selected options :
# driver = webdriver.Chrome()
# driver.get("http://tutorialspoint.com/selenium/practice/select-menu.php")
# driver.maximize_window()

# drop = driver.find_element(By.XPATH, "//input[@id='demo-multiple-select-input']")
# select = Select(drop)
# time.sleep(2)
# select.select_by_visible_text("Bookd")
# time.sleep(2)
# select.select_by_visible_text("Movies, Music & Games")
# time.sleep(2)
# select.select_by_visible_text("Electronics & Computers")
# time.sleep(2)
# select.deselect_all()
# time.sleep(5)

# Example 8: Check if dropdown supports multiple selection :
# driver = webdriver.Chrome()
# driver.get("https://www.automationtesting.co.uk/dropdown.html")
# driver.maximize_window()

# drop = driver.find_element(By.XPATH, "//select[@id='cars']")
# select = Select(drop)

# if select.is_multiple:
#   print("it supports multiple select")
# else:
#   print("it is not support multiple support")  
