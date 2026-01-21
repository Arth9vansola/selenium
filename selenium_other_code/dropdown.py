from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")

element_to_be_selected = driver.find_element(By.ID, 'dropdown')
# 1. How to handle dropdowns using Selenium's Select class. and How to select options by visible text, value, and index.
# select = Select(element_to_be_selected)
# select.select_by_visible_text('Option 1')
# select.select_by_value('2')
# select.select_by_index(1)

# 2. Basic validation of dropdown option count.
# select = Select(element_to_be_selected)
# option_count = len(select.options)
# expected_option_count = 3
# if option_count == expected_option_count:
#     print("Option count test passed")
# else:
#     print("Option count test failed")    

# 3.How to iterate through dropdown options and perform actions based on conditions.
# select = Select(element_to_be_selected)
# target_value = 'Option 3'
# for option in select.options:
#     if option.text == target_value:
#         option.click()
#         print(f"{target_value} is selected")
#         break
#     else:
#         print(f"{option.text} is not selected")


time.sleep(5)
driver.quit()

