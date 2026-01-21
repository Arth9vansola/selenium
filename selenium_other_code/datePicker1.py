import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # ✅ Fixed typo here

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/datepicker/#DropDown%20DatePicker")

time.sleep(3)

# Close the ad popup if it exists
try:
    driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()
except:
    pass  # In case the popup doesn't appear

# ✅ Switch to the correct iframe
iframe = driver.find_element(By.XPATH, "//iframe[contains(@class, 'demo-frame')]")
driver.switch_to.frame(iframe)

# Wait and interact with the datepicker
time.sleep(2)
date_input = driver.find_element(By.ID, "datepicker")
date_input.click()

# ✅ Calculate and input next day's date
current_date = datetime.now()
next_date = current_date + timedelta(days=-366)
formatted_date = next_date.strftime("%m/%d/%Y")

# ✅ Clear old value, input new one, and press TAB
date_input.clear()
date_input.send_keys(formatted_date)
date_input.send_keys(Keys.TAB)

time.sleep(5)
driver.quit()
