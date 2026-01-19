from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

csv_file_path = "testdataexcel.csv"
test_data = []
with open(csv_file_path, mode ='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)

for data in test_data:
    driver = webdriver.Firefox() # Here i used firefox browser instead of chrome because chrome give me password saving popup
    driver.maximize_window()
    username = data['username']
    password = data['password']

    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    driver.quit()
       