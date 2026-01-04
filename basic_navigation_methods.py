from selenium import webdriver
import time

driver = webdriver.Chrome()

# Navigate to URL
driver.get("https://www.example.com")
time.sleep(2)

# Navigate forward (like browser forward button)
driver.forward()
time.sleep(2)

# Navigate backward (like browser back button)
driver.back()
time.sleep(2)

# Refresh the page
driver.refresh()
time.sleep(2)

# Get current URL
print(driver.current_url)
time.sleep(5)

# Get page title
print(driver.title)
time.sleep(5)

# Get page source
print(driver.page_source)
time.sleep(5)

driver.quit()
