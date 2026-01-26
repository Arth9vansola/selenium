# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# import time

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Frames.html")

# # iframe = driver.find_element(By.ID, "mce_0_ifr")  # Locate the iframe by its ID
# driver.switch_to.frame("singleframe")  # Switch to the iframe

# text_area = driver.find_element(By.XPATH, "//input[@type='text']")  # Locate the text area inside the iframe
# text_area.clear()  # Clear any existing text
# text_area.send_keys("Hello, World!")  # Enter new text
# time.sleep(2)

# driver.switch_to.default_content()  # Switch back to the main content(html)
# selenium_link = driver.find_element(By.XPATH, "//a[@class='analystic' and text()='Iframe with in an Iframe']").click()



from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")

iframes = driver.find_elements(By.TAG_NAME, "iframe")
print(len(iframes))

