from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.apple.com")

# Maximize window
driver.maximize_window()

# Set window size
driver.set_window_size(1024, 768)

# Get window size
size = driver.get_window_size()
print(f"Window size: {size['width']} x {size['height']}")

# Take screenshot
driver.save_screenshot("window_management.png")

driver.quit()
