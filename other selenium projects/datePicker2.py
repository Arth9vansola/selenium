import time
from datetime import datetime, timedelta
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")

driver.find_element(By.ID, "datepicker2").click()
time.sleep(5)
current_date = datetime.now()
next_date = current_date + timedelta(days=1)
print(next_date)
next_day = str(next_date.day)
print(next_day)
current_month = datetime.now().month
current_year = current_date.year
print(current_month)
print(current_year)
next_month = (current_month % 12) + 1
next_month_year = f"{next_month}/{current_year}" # for selecting month

month_dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
select = Select(month_dropdown)
select.select_by_value(str(next_month_year))
year_dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the year']")
select = Select(year_dropdown)
select.select_by_visible_text("2025")
driver.find_element(By.LINK_TEXT, f"{next_day}").click()
time.sleep(5)

