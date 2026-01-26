from selenium import webdriver
from pages.table_page import TableMethods

class tableScrapTest(TableMethods):
  pass

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()



    ''' 1. to scrap for single table'''
    # table_name = "pages/scraped_data_one_table.xlsx"
    # table_xpath = "//table[contains(@id,'resultTable')]"
    # obj_scrapperTable = tableScrapTest(driver,table_xpath,table_name)
    # obj_scrapperTable.scrap_table()


    ''' 2. to scrap for multiple table '''

    # table_name = "pages/scraped_data_two_table.xlsx"
    # btn_xpath = "//button[contains(@class,'next')]"
    # table_xpath = "//table[contains(@id,'tablepress-')]"
    # obj_scrapperTable = tableScrapTest(driver,table_xpath,table_name,btn_xpath)
    # obj_scrapperTable.scrap_table()

    ''' 3. to check the box '''
    # xpath = "//td[text()='Jasmine Morgan']/preceding-sibling::td//input"
    # # xpath = "//tr[td[text()='Garry White']]//input[@type='checkbox']"
    # # xpath = " //a[text()='Employee Name']/ancestor::tr//th[input[contains(@type,'checkbox')]]"
    # obj_scrapperTable = tableScrapTest(driver,xpath)
    # obj_scrapperTable.check_the_box()

    ''' 4. change the value in the data of table '''
    file_name = 'pages/scraped_data_two_table.xlsx'
    obj_scraper = tableScrapTest()
    obj_scraper.change_excel_value(file_name, 'OS', 'windows', 'Country', 'Arth')
