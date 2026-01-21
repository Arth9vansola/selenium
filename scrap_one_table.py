from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


class Scrapper:
    def __init__(self,driver,xpath,site,table_name):
        self.driver = driver
        self.xpath = xpath
        self.site = site
        self.table_name = table_name

    def scrapping_table(self):
        try:
            self.driver.get(self.site)
            self.driver.maximize_window()

            table = driver.find_element(By.XPATH, self.xpath)
            self.driver.execute_script('arguments[0].scrollIntoView(true);',table)
            time.sleep(2)

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

            df.to_excel(self.table_name, index=False, sheet_name="arth")

        except Exception as e:
            print("Error:", e)

        finally:
            self.driver.quit()

    def the_check(self,xpath):
        try:
            self.driver.get(self.site)

            check_box = driver.find_element(By.XPATH, xpath)
            check_box.click()
            time.sleep(5)
            

        except Exception as e:
            print("Error:", e)

        finally:
            self.driver.quit()        



        


if __name__ == "__main__":
    # options = Options()
    # options.add_argument("--headless=new")
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    table_xpath = "//table[contains(@id,'resultTable')]"
    # xpath = "//table[contains(@id,'tablepress-')]"
    table_name = "scraped_data_one_table.xlsx"
    site = "https://selectorshub.com/xpath-practice-page/"
    obj_scrapper = Scrapper(driver,table_xpath,site,table_name)
    obj_scrapper.scrapping_table()
    # xpath = "//td[text()='Garry White']/preceding-sibling::td//input"
    # xpath = "//tr[td[text()='Garry White']]//input[@type='checkbox']"
    # obj_scrapper.the_check(xpath)