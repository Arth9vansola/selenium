from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.execute_script("window.scrollTo(0, 700)")  # Scroll down to make the table visible
time.sleep(2)
table = driver.find_element(By.ID, "countries")  # Locate the table by its ID
# print(table.text)
rows = table.find_elements(By.TAG_NAME, "tr")  # Get all rows in the table
# print(rows)
row_count = len(rows) 
# print(row_count)  # Print the number of rows
target_value = 'Sydney'
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")  # Get all cells in the row
    for cell in cells:
        if target_value in cell.text:
            print(f"Found '{target_value}' in the table.")
            found = True
            break
    if found:
        break   
    
if not found:
    print(f"'{target_value}' not found in the table.")    