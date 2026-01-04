from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the driver
driver = webdriver.Chrome()

try:
    # Navigate to Google
    driver.get("https://www.google.com")
    
    # Verify page loaded
    print("Page Title:", driver.title)
    
    # Find the search box by name
    search_box = driver.find_element(By.NAME, "q")
    
    # Type search query
    search_box.send_keys("Selenium Python")
    
    # Press Enter
    search_box.send_keys(Keys.RETURN)

    
    # Wait a bit to see results
    time.sleep(7)
    
    # Verify search was successful
    assert "Selenium Python" in driver.page_source
    print("Test passed: Search successful!")

except Exception as e:
    print(f"there is an error {e}")    
    
finally:
    # Always close the driver
    driver.quit()
