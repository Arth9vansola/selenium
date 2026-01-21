# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import pandas as pd

# driver = webdriver.Chrome()

# try:
#     driver.get('https://selectorshub.com/xpath-practice-page/')

#     scraped_data = []

#     header_column_length = len(driver.find_elements(By.XPATH, '//table[@id="resultTable"]//thead//tr//th'))
#     scraped_header = []
#     for i in range(1,header_column_length+1):
       
#         header_data = driver.find_element(By.XPATH, f'//table[@id="resultTable"]//thead//tr//th[{i}]').text
#         if header_data != '' : scraped_header.append(header_data)

#     data_row_length = len(driver.find_elements(By.XPATH, '//table[@id="resultTable"]//tbody//tr'))

#     for i in range(1, data_row_length + 1):
#         rows = []
#         for j in range(1, header_column_length + 1):
#             data = driver.find_element(By.XPATH, f'//table[@id="resultTable"]//tbody//tr[{i}]//td[{j}]').text
#             if data != '' : rows.append(data)
#         scraped_data.append(rows)

#     data = pd.DataFrame(scraped_data,columns=scraped_header)
#     print(scraped_header)
#     print(scraped_data)
#     data.to_excel("scraped_data.xlsx",index=False,sheet_name="arth")

#     # for i in range(2,)
#     # user_table = driver.find_element(By.XPATH, '//table[@id="resultTable"]')

#     # print(user_table.text)

# except Exception as e:
#     print(e)
 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://selectorshub.com/xpath-practice-page/")

    table = wait.until(
        EC.presence_of_element_located((By.XPATH, "//table[contains(@id,'resultTable')]"))
    )

    headers = [
        th.get_attribute("textContent").strip()
        for th in table.find_elements(By.XPATH, ".//thead//tr//th")
        if th.get_attribute("textContent").strip()
    ]

    data = []
    rows = table.find_elements(By.XPATH, ".//tbody//tr")

    for row in rows:
        row_data = [
            td.get_attribute("textContent").strip()
            for td in row.find_elements(By.XPATH, ".//td")
            if td.get_attribute("textContent").strip()
        ]
        data.append(row_data)

    df = pd.DataFrame(data, columns=headers)

    print(headers)
    print(data)

    df.to_excel("scraped_data.xlsx", index=False, sheet_name="arth")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
