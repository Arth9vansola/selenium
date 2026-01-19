from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# Switch to the top frame
driver.switch_to.frame("frame-top")

# Switch to the middle frame
driver.switch_to.frame("frame-middle")

content_middle = driver.find_element(By.ID, "content").text  # Locate the content inside the middle frame
print("Middle Frame Content:", content_middle)

# Switch back to the top frame
driver.switch_to.default_content()

# Switch to the bottom frame
driver.switch_to.frame("frame-bottom")

content_bottom = driver.find_element(By.TAG_NAME, "body").text  # Locate the content inside the bottom frame
print("Bottom Frame Content:", content_bottom)
