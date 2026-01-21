from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

class ScrapperTable:
    def __init__(self,driver,table_xpath,site,table_name,btn_xpath=''):
        self.driver = driver
        self.table_xpath = table_xpath
        self.site = site
        self.table_name = table_name
        self.btn_xpath = btn_xpath

    def scrapping_table(self):
        try:
            self.driver.get(self.site)
            self.driver.maximize_window()            

            table = self.driver.find_element(By.XPATH, self.table_xpath)
            self.driver.execute_script('arguments[0].scrollIntoView(true);',table)
            time.sleep(2)            

            headers = [
                th.get_attribute("textContent").strip()
                for th in table.find_elements(By.XPATH, ".//thead//tr//th")
                if th.get_attribute("textContent").strip()
            ]

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

                #  Try to click Next
                if self.btn_xpath:
                    next_button = self.driver.find_element(By.XPATH, self.btn_xpath)

                    # Stop if disabled
                    if "disabled" in next_button.get_attribute("class"):
                        break

                    next_button.click()

                    #  Wait for table refresh
                    time.sleep(1)

                else:
                    break

            df = pd.DataFrame(main_rows, columns=headers)

            print(headers)
            print(main_rows)

            df.to_excel(self.table_name, index=False, sheet_name="arth")

        except Exception as e:
            print("Error:", e)

        finally:
            self.driver.quit()    


if __name__ == "__main__":
    # options = Options()
    # options.add_argument("--headless=new")
    # driver = webdriver.Chrome(options=options)
    # table_xpath = "//table[contains(@id,'tablepress-')]"
    driver = webdriver.Chrome()
    table_xpath = "//table[contains(@id,'resultTable')]"
    site = "https://selectorshub.com/xpath-practice-page/"
    table_name = "scraped_data_all.xlsx"
    # btn_xpath = "//button[contains(@class,'next')]"
    obj_scrapperTable = ScrapperTable(driver,table_xpath,site,table_name)
    obj_scrapperTable.scrapping_table()
    # xpath = "//td[text()='Garry White']/preceding-sibling::td//input"
    # xpath = "//tr[td[text()='Garry White']]//input[@type='checkbox']"
    # obj_scrapper.the_check(xpath)