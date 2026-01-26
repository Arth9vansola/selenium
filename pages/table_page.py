# from selenium import webdriver
from selenium.webdriver.common.by import By
# from utils.driver_setup import Driver
import pandas as pd
import time

class TableLocators:
  def __init__(self,driver=None,table_xpath=None,table_name=None,btn_xpath=None):
      self.driver = driver
      self.table_xpath = table_xpath
      self.site_url = 'https://selectorshub.com/xpath-practice-page/'
      self.table_name = table_name
      self.btn_xpath = btn_xpath    

class TableMethods(TableLocators):
  def __init__(self, driver=None, table_xpath=None, table_name=None, btn_xpath=None):
     super().__init__(driver, table_xpath, table_name, btn_xpath)

  def get_site(self):
     self.driver.get(self.site_url)

  def get_table(self):
    table = self.driver.find_element(By.XPATH, self.table_xpath)  
    return table       

  def scroll_to_element(self, element):
      self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)  


  def scraped_header(self,table):
    headers = [
        th.get_attribute("textContent").strip()
        for th in table.find_elements(By.XPATH, ".//thead//tr//th")
        if th.get_attribute("textContent").strip()
    ]     

    return headers
  
  def scraped_rows(self,table):
    main_rows = []

    while True:

        #  Get rows from current page
        rows = table.find_elements(By.XPATH, ".//tbody//tr")

        for row in rows:
            row_data = [
                td.get_attribute("textContent").strip()
                for td in row.find_elements(By.XPATH, ".//td")
                if td.get_attribute("textContent").strip()            
            ]
            main_rows.append(row_data)

    
        if self.btn_xpath:    
          #  Try to click Next
          next_button = self.driver.find_element(By.XPATH, self.btn_xpath)

          # Stop if disabled
          if "disabled" in next_button.get_attribute("class"):
            break

          next_button.click()

          #  Wait for table refresh
          time.sleep(1)
        else:
          break   

    return main_rows          
  
  # def handle_pagination(self):
  #       if self.btn_xpath:
  #           try:
  #               next_button = self.driver.find_element(By.XPATH, self.btn_xpath)
  #               if "disabled" in next_button.get_attribute("class"):
  #                   return False
  #               next_button.click()
  #               return True
  #           except Exception:
  #               return False
  #       return False   

  def save_to_excel(self,header,rows):
    df = pd.DataFrame(rows, columns=header)

    print(header)
    print(rows)

    df.to_excel(self.table_name, index=False, sheet_name="arth")     
          

  def scrap_table(self):
    try:  
        self.get_site()
        table = self.get_table()
        self.scroll_to_element(table)
        time.sleep(2)
        header = self.scraped_header(table)
        rows = self.scraped_rows(table)
        self.save_to_excel(header,rows)

    except Exception as e:
        print("Error:", e)

    finally:
        self.driver.quit()   


  def check_the_box(self):
    try:  
      self.get_site()

      check_box = self.driver.find_element(By.XPATH, self.table_xpath)
      self.scroll_to_element(check_box)

      time.sleep(1)      
      check_box.click()
      time.sleep(5)

    except Exception as e:
        print("Error:", e)

    finally:
        self.driver.quit() 

  def change_excel_value(self,file_name, ref_column_name, ref_column_value, selected_column_name, selected_column_value):
    try:  
      # Read the Excel file into a DataFrame
      df = pd.read_excel(file_name)

      # Convert to lowercase for case-insensitive comparison and use .loc for safe row modification
      df.loc[df[ref_column_name].str.lower() == ref_column_value.lower(), selected_column_name] = selected_column_value

      # Save the modified DataFrame back to Excel (optional)
      df.to_excel(file_name, index=False, sheet_name="arth")

      print(df)

    except Exception as e:
        print("Error:", e)
    
    

# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     table_name = "scraped_data_one_table.xlsx"

#     ''' 1. to scrap for single table'''

#     table_xpath = "//table[contains(@id,'resultTable')]"
#     obj_scrapperTable = TableMethods(driver,table_xpath,table_name)
#     obj_scrapperTable.scrap_table()


#     ''' 2. to scrap for multiple table '''

#     btn_xpath = "//button[contains(@class,'next')]"
#     table_xpath = "//table[contains(@id,'tablepress-')]"
#     obj_scrapperTable = TableMethods(driver,table_xpath,table_name,btn_xpath)
#     obj_scrapperTable.scrap_table()

#     ''' 3. to check the box '''
#     # xpath = "//td[text()='Garry White']/preceding-sibling::td//input"
#     # xpath = "//tr[td[text()='Garry White']]//input[@type='checkbox']"
#     xpath = " //a[text()='Employee Name']/ancestor::tr//th[input[contains(@type,'checkbox')]]"
#     obj_scrapperTable = TableMethods(driver,xpath)
#     obj_scrapperTable.check_the_box()

#     ''' 4. change the value in the data of table '''
#     file_name = 'scraped_data_two_table.xlsx'
#     obj_scraper = TableMethods()
#     obj_scraper.change_excel_value(file_name, 'OS', 'windows', 'Country', 'Arth')
