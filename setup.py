from selenium import webdriver

# This will open a Chrome browser window
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)  # Print page title
driver.quit()  # Close the browser
