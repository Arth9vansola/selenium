# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
# import time

# class ScrapperTable:
#     """
#     A class for scraping tables from a webpage and performing actions like checking checkboxes or navigating paginated tables.
#     """

#     def __init__(self,driver,table_xpath='', table_name='',btn_xpath=''):
#         '''
#         Docstring for __init__
        
#         :param driver: assign driver to self.driver
#         :param table_xpath: assign table's xpath to self.table_xpath
#         :param site: assign site name to self.site
#         :param table_name: assign table name to self.table_name
#         :param btn_xpath: assign button xpath to self.btn_xpath
#         '''
#         self.driver = driver
#         self.table_xpath = table_xpath
#         self.site = 'https://selectorshub.com/xpath-practice-page/'
#         self.table_name = table_name
#         self.btn_xpath = btn_xpath

#     def scrapping_table(self):
#         """
#         table: it is locate to table element
#         headers: stores all header of table
#         main_rows: stores all of the rows data in form of list of lists
#         DataFrame: it is convert main_rows and headers into appropriate form 
#         to_excel: convert DataFrame into excel form

#         Scrapes table data from a webpage, handles pagination, and saves it to an Excel file.
#         """

#         try:
#             self.driver.get(self.site)
#             # self.driver.maximize_window()            

#             table = self.driver.find_element(By.XPATH, self.table_xpath)
#             self.driver.execute_script('arguments[0].scrollIntoView(true);',table)
#             time.sleep(2)            

#             headers = [
#                 th.get_attribute("textContent").strip()
#                 for th in table.find_elements(By.XPATH, ".//thead//tr//th")
#                 if th.get_attribute("textContent").strip()
#             ]

#             main_rows = []

#             while True:

#                 #  Get rows from current page
#                 rows = table.find_elements(By.XPATH, ".//tbody//tr")

#                 for row in rows:
#                     row_data = [
#                         td.get_attribute("textContent").strip()
#                         for td in row.find_elements(By.XPATH, ".//td")
#                         if td.get_attribute("textContent").strip()            
#                     ]
#                     main_rows.append(row_data)

#                 #  Try to click Next
#                 if self.btn_xpath:
#                     next_button = self.driver.find_element(By.XPATH, self.btn_xpath)

#                     # Stop if disabled
#                     if "disabled" in next_button.get_attribute("class"):
#                         break

#                     next_button.click()

#                     #  Wait for table refresh
#                     time.sleep(1)

#                 else:
#                     break

#             df = pd.DataFrame(main_rows, columns=headers)

#             print(headers)
#             print(main_rows)

#             df.to_excel(self.table_name, index=False, sheet_name="arth")

#         except Exception as e:
#             print("Error:", e)

#         finally:
#             self.driver.quit()   

#     def the_check(self):
#         """
#         check_box: element to locate checkbox
#         execute_script: scroll page till element become visible

#         Clicks a checkbox on a webpage based on the provided XPath.
#         """

#         try:
#             self.driver.get(self.site)
#             # self.driver.maximize_window()

#             check_box = self.driver.find_element(By.XPATH, self.table_xpath)
#             # self.driver.execute_script('arguments[0].scrollIntoView(true);',check_box)
#             self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",check_box)

#             time.sleep(1)      
#             # self.driver.execute_script("arguments[0].click();", check_box)
         
#             check_box.click()
#             time.sleep(5)
            

#         except Exception as e:
#             print("Error:", e)

#         finally:
#             self.driver.quit() 


# if __name__ == "__main__":
#     # options = Options()
#     # options.add_argument("--headless=new")
#     # driver = webdriver.Chrome(options=options)
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     table_name = "scraped_data_one_table.xlsx"

#     ''' 1. to scrap for single table'''

#     # table_xpath = "//table[contains(@id,'resultTable')]"
#     # obj_scrapperTable = ScrapperTable(driver,table_xpath,table_name)
#     # obj_scrapperTable.scrapping_table()


#     ''' 2. to scrap for multiple table '''

#     btn_xpath = "//button[contains(@class,'next')]"
#     table_xpath = "//table[contains(@id,'tablepress-')]"
#     obj_scrapperTable = ScrapperTable(driver,table_xpath,table_name,btn_xpath)
#     obj_scrapperTable.scrapping_table()

#     ''' 3. to check the box '''
#     # xpath = "//td[text()='Garry White']/preceding-sibling::td//input"
#     # xpath = "//tr[td[text()='Garry White']]//input[@type='checkbox']"
#     xpath = " //a[text()='Employee Name']/ancestor::tr//th[input[contains(@type,'checkbox')]]"
#     # obj_scrapperTable = ScrapperTable(driver,xpath)
#     # obj_scrapperTable.the_check()



#     # //td[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'garry white')]

# ===========================================================
# index_based.py # change the value in status column based on username like garry white

# import pandas as pd

# def change_excel_value(file_name, ref_column_name, ref_column_value, selected_column_name, selected_column_value):
#     # Read the Excel file into a DataFrame
#     df = pd.read_excel(file_name)

#     # Convert to lowercase for case-insensitive comparison and use .loc for safe row modification
#     df.loc[df[ref_column_name].str.lower() == ref_column_value.lower(), selected_column_name] = selected_column_value

#     # Save the modified DataFrame back to Excel (optional)
#     df.to_excel(file_name, index=False)

#     print(df)

# # Example function call
# file_name = 'scraped_data_one_table.xlsx'
# change_excel_value(file_name, 'Username', 'garry.white', 'Status', 'gameOn')


# ============================================
# modified code:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time


# class Scrapper:
#     """
#     A class to scrape tables and interact with checkboxes on a webpage.
#     """

#     def __init__(self, driver, site_url, table_xpath='', table_name='', btn_xpath=''):
#         '''
#         :param driver: The Selenium WebDriver instance.
#         :param site_url: URL of the site to scrape.
#         :param table_xpath: XPath for the table to scrape.
#         :param table_name: Name for the Excel file to store scraped data.
#         :param btn_xpath: XPath for the next button (used for pagination).
#         '''
#         self.driver = driver
#         self.site_url = site_url
#         self.table_xpath = table_xpath
#         self.table_name = table_name
#         self.btn_xpath = btn_xpath

#     def get_table_data(self):
#         """
#         Scrapes the table data from the webpage and returns the headers and rows.
#         """
#         try:
#             self.driver.get(self.site_url)
#             table = self.driver.find_element(By.XPATH, self.table_xpath)
#             self.driver.execute_script('arguments[0].scrollIntoView(true);', table)
#             time.sleep(2)

#             # Get table headers
#             headers = [th.get_attribute("textContent").strip() for th in table.find_elements(By.XPATH, ".//thead//tr//th") if th.get_attribute("textContent").strip()]

#             # Scrape rows and handle pagination
#             rows = []
#             while True:
#                 rows.extend(self.scrape_rows(table))
#                 if not self.click_next_button():
#                     break
#                 time.sleep(1)

#             return headers, rows

#         except Exception as e:
#             print("Error during scraping table data:", e)
#             return [], []

#     def scrape_rows(self, table):
#         """
#         Scrapes rows from the table and returns a list of row data.
#         """
#         rows = table.find_elements(By.XPATH, ".//tbody//tr")
#         row_data = []
#         for row in rows:
#             row_data.append([td.get_attribute("textContent").strip() for td in row.find_elements(By.XPATH, ".//td") if td.get_attribute("textContent").strip()])
#         return row_data

#     def click_next_button(self):
#         """
#         Clicks the next button for pagination, returns False if the button is disabled.
#         """
#         if self.btn_xpath:
#             try:
#                 next_button = self.driver.find_element(By.XPATH, self.btn_xpath)
#                 if "disabled" in next_button.get_attribute("class"):
#                     return False
#                 next_button.click()
#                 return True
#             except Exception:
#                 return False
#         return False

#     def save_to_excel(self, headers, rows):
#         """
#         Saves the scraped data into an Excel file.
#         """
#         df = pd.DataFrame(rows, columns=headers)
#         df.to_excel(self.table_name, index=False, sheet_name="ScrapedData")
#         print(f"Data saved to {self.table_name}")

#     def scrape_table_and_save(self):
#         """
#         Scrapes table data and saves it to an Excel file.
#         """
#         headers, rows = self.get_table_data()
#         if headers and rows:
#             self.save_to_excel(headers, rows)
#         else:
#             print("No data found to save.")

#     def interact_with_checkbox(self, checkbox_xpath):
#         """
#         Interacts with a checkbox on the webpage.
#         """
#         try:
#             self.driver.get(self.site_url)
#             checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)
#             self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", checkbox)
#             time.sleep(1)
#             checkbox.click()
#             time.sleep(5)
#             print("Checkbox clicked.")
#         except Exception as e:
#             print("Error while interacting with checkbox:", e)

#     def update_excel_value(self, file_name, ref_column_name, ref_column_value, selected_column_name, selected_column_value):
#         """
#         Updates an Excel file by changing a cell value based on a reference column's value.
#         """
#         df = pd.read_excel(file_name)

#         # Perform case-insensitive comparison and update the selected column's value
#         df.loc[df[ref_column_name].str.lower() == ref_column_value.lower(), selected_column_name] = selected_column_value
#         df.to_excel(file_name, index=False)
#         print(f"Excel updated: {file_name}")

#     def close_driver(self):
#         """
#         Closes the Selenium driver.
#         """
#         self.driver.quit()


# # Example usage:
# if __name__ == "__main__":
#     # Initialize WebDriver (Chrome)
#     driver = webdriver.Chrome()
#     driver.maximize_window()

#     # Define the URL and other parameters
#     site_url = 'https://selectorshub.com/xpath-practice-page/'
#     table_name = "scraped_data.xlsx"
#     table_xpath = "//table[contains(@id,'tablepress-')]"
#     btn_xpath = "//button[contains(@class,'next')]"

#     # Create an instance of Scrapper
#     scrapper = Scrapper(driver, site_url, table_xpath, table_name, btn_xpath)

#     # Scrape table data and save to Excel
#     scrapper.scrape_table_and_save()

#     # Interact with a checkbox (example XPath)
#     checkbox_xpath = "//a[text()='Employee Name']/ancestor::tr//th[input[contains(@type,'checkbox')]]"
#     scrapper.interact_with_checkbox(checkbox_xpath)

#     # Example of updating an Excel file
#     file_name = 'scraped_data.xlsx'
#     scrapper.update_excel_value(file_name, 'Username', 'garry.white', 'Status', 'gameOn')

#     # Close the driver after the task is complete
#     scrapper.close_driver()

