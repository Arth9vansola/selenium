# Selenium Python: Complete Learning Guide
## From Basic to Advanced Concepts

---

## TABLE OF CONTENTS

1. [Introduction](#introduction)
2. [PART 1: BASIC CONCEPTS](#part-1-basic-concepts)
3. [PART 2: INTERMEDIATE CONCEPTS](#part-2-intermediate-concepts)
4. [PART 3: ADVANCED CONCEPTS](#part-3-advanced-concepts)
5. [Best Practices and Tips](#best-practices-and-tips)
6. [Complete Code Examples](#complete-code-examples)

---

## INTRODUCTION

### What is Selenium?

Selenium is a powerful automation tool for web browsers. The Python bindings provide a simple API to write functional/acceptance tests and automate web application testing. Selenium WebDriver interacts with web applications the same way users do—by clicking, typing, and navigating.

### Why Learn Selenium?

- **Web Testing Automation**: Automate repetitive testing tasks
- **Web Scraping**: Extract data from dynamic websites
- **RPA (Robotic Process Automation)**: Automate business processes
- **Cross-Browser Testing**: Test applications across multiple browsers
- **Performance Testing**: Simulate user interactions at scale

### Prerequisites

- Python 3.5 or higher
- Basic understanding of Python
- Familiarity with HTML/CSS (for locating elements)
- Basic understanding of web browsers

### Key Concepts Before Starting

- **WebDriver**: An interface that communicates with the browser
- **Browser Driver**: Executable that controls the browser (ChromeDriver, GeckoDriver, etc.)
- **Locators**: Methods to find elements on a web page
- **Waits**: Mechanisms to handle dynamic page loading
- **Actions**: User interactions like clicks, typing, drag-and-drop

---

# PART 1: BASIC CONCEPTS

## 1.1 Installation and Setup

### Step 1: Install Selenium Package

```bash
pip install selenium
```

### Step 2: Download Browser Driver

Selenium requires a driver for each browser:

| Browser | Driver | Download |
|---------|--------|----------|
| Chrome | ChromeDriver | https://chromedriver.chromium.org/ |
| Firefox | GeckoDriver | https://github.com/mozilla/geckodriver/releases |
| Edge | EdgeDriver | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| Safari | SafariDriver | Built-in |

**Modern Approach (Selenium 4.6.0+)**: Selenium Manager automatically downloads drivers!

```python
# No need to manually manage drivers with Selenium Manager
from selenium import webdriver

driver = webdriver.Chrome()  # Automatically downloads ChromeDriver if missing
```

### Step 3: Verify Installation

```python
from selenium import webdriver

# This will open a Chrome browser window
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)  # Print page title
driver.quit()  # Close the browser
```

## 1.2 Your First Selenium Script

### Simple Example: Search on Google

```python
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
    time.sleep(2)
    
    # Verify search was successful
    assert "Selenium Python" in driver.page_source
    print("Test passed: Search successful!")
    
finally:
    # Always close the driver
    driver.quit()
```

**Key Points:**
- Use `driver.get()` to navigate to a URL
- Use `find_element()` to locate elements
- Use `send_keys()` to type text
- Always use `driver.quit()` to close the browser

## 1.3 Understanding WebDriver Basics

### Creating Different WebDriver Instances

```python
from selenium import webdriver

# Chrome
driver = webdriver.Chrome()

# Firefox
driver = webdriver.Firefox()

# Edge
driver = webdriver.Edge()

# Safari (macOS only)
driver = webdriver.Safari()

# Internet Explorer
driver = webdriver.Ie()
```

### Basic Navigation Methods

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to URL
driver.get("https://www.example.com")

# Navigate forward (like browser forward button)
driver.forward()

# Navigate backward (like browser back button)
driver.back()

# Refresh the page
driver.refresh()

# Get current URL
print(driver.current_url)

# Get page title
print(driver.title)

# Get page source
print(driver.page_source)

driver.quit()
```

### Window Management

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Maximize window
driver.maximize_window()

# Set window size
driver.set_window_size(1024, 768)

# Get window size
size = driver.get_window_size()
print(f"Window size: {size['width']} x {size['height']}")

# Take screenshot
driver.save_screenshot("screenshot.png")

driver.quit()
```

## 1.4 Locating Elements

### Introduction to Locators

Locators are the most important skill in Selenium. They help you find elements on a page.

### 8 Locating Strategies

#### 1. **By ID**
```python
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "element_id")
```
Use when an element has a unique `id` attribute.

#### 2. **By NAME**
```python
element = driver.find_element(By.NAME, "element_name")
```
Use for form elements with a `name` attribute.

#### 3. **By CLASS NAME**
```python
element = driver.find_element(By.CLASS_NAME, "class_name")
```
Use to find elements by CSS class.

#### 4. **By TAG NAME**
```python
elements = driver.find_elements(By.TAG_NAME, "button")
```
Use to find elements by HTML tag.

#### 5. **By CSS SELECTOR**
```python
# Class selector
element = driver.find_element(By.CSS_SELECTOR, "p.class_name")

# ID selector
element = driver.find_element(By.CSS_SELECTOR, "input#id_name")

# Attribute selector
element = driver.find_element(By.CSS_SELECTOR, "input[type='text']")

# Descendant
element = driver.find_element(By.CSS_SELECTOR, "div.class button")
```

#### 6. **By XPATH**
```python
# Absolute path (fragile - avoid)
element = driver.find_element(By.XPATH, "/html/body/div[1]")

# Relative path (better)
element = driver.find_element(By.XPATH, "//button[@id='submit']")

# Text-based
element = driver.find_element(By.XPATH, "//button[text()='Click Me']")

# Attribute-based
element = driver.find_element(By.XPATH, "//input[@type='password']")

# Combined attributes
element = driver.find_element(By.XPATH, "//input[@name='username' and @type='text']")
```

#### 7. **By LINK TEXT**
```python
link = driver.find_element(By.LINK_TEXT, "Full Link Text")
```
Use for exact link text matching.

#### 8. **By PARTIAL LINK TEXT**
```python
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Partial Text")
```
Use for partial link text matching.

### Complete Locating Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Find single element
button = driver.find_element(By.ID, "submit_btn")

# Find multiple elements
all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"Found {len(all_links)} links")

# Find nested element
login_form = driver.find_element(By.ID, "loginForm")
username_input = login_form.find_element(By.NAME, "username")

driver.quit()
```

## 1.5 Interacting with Elements

### Basic Element Interactions

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Click an element
button = driver.find_element(By.ID, "submit")
button.click()

# Type text
text_field = driver.find_element(By.NAME, "username")
text_field.send_keys("myusername")

# Clear text field
text_field.clear()

# Submit a form
form = driver.find_element(By.TAG_NAME, "form")
form.submit()

# Get text from element
element_text = button.text
print(element_text)

# Get attribute value
href = driver.find_element(By.TAG_NAME, "a").get_attribute("href")

# Get CSS property
background_color = button.value_of_css_property("background-color")

# Check if element is displayed
is_visible = button.is_displayed()

# Check if element is enabled
is_enabled = button.is_enabled()

# Check if element is selected
is_selected = button.is_selected()

driver.quit()
```

### Working with Special Keys

```python
from selenium.webdriver.common.keys import Keys

# Send keys
text_field.send_keys("Hello World")

# Special keys
text_field.send_keys(Keys.RETURN)        # Enter
text_field.send_keys(Keys.TAB)           # Tab
text_field.send_keys(Keys.ESCAPE)        # Escape
text_field.send_keys(Keys.BACKSPACE)     # Backspace

# Modifier keys
text_field.send_keys(Keys.CONTROL, "a")  # Ctrl+A
text_field.send_keys(Keys.CONTROL, "c")  # Ctrl+C

# Arrow keys
text_field.send_keys(Keys.ARROW_DOWN)
text_field.send_keys(Keys.ARROW_UP)
text_field.send_keys(Keys.ARROW_LEFT)
text_field.send_keys(Keys.ARROW_RIGHT)
```

### Working with Dropdowns/Select Elements

```python
from selenium.webdriver.support.ui import Select

# Initialize Select object
select_element = driver.find_element(By.NAME, "dropdown")
select = Select(select_element)

# Select by visible text
select.select_by_visible_text("Option 1")

# Select by value
select.select_by_value("option1")

# Select by index (0-based)
select.select_by_index(0)

# Get all options
all_options = select.options
for option in all_options:
    print(option.text)

# Get selected option
selected_option = select.first_selected_option
print(selected_option.text)

# Deselect options (for multi-select)
select.deselect_all()
select.deselect_by_visible_text("Option 1")
```

---

# PART 2: INTERMEDIATE CONCEPTS

## 2.1 Waits: Handling Dynamic Content

One of the biggest challenges in Selenium is handling dynamic content. Elements may not be immediately available when you try to interact with them.

### Why Waits are Important

Modern web applications load content asynchronously using AJAX. Elements might not be present in the DOM when your script tries to find them.

**Bad Practice:**
```python
import time

driver.get("https://example.com")
time.sleep(5)  # Fixed wait - inefficient and unreliable
button = driver.find_element(By.ID, "myButton")
```

**Good Practice:**
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver.get("https://example.com")
# Wait up to 10 seconds for element to appear
wait = WebDriverWait(driver, 10)
button = wait.until(EC.presence_of_element_located((By.ID, "myButton")))
```

### Explicit Waits (Recommended)

Explicit waits are preferred. You define a condition to wait for.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Create a wait object
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

# Wait for element to be present in DOM
element = wait.until(EC.presence_of_element_located((By.ID, "myElement")))

# Wait for element to be visible
element = wait.until(EC.visibility_of_element_located((By.ID, "myElement")))

# Wait for element to be clickable
button = wait.until(EC.element_to_be_clickable((By.ID, "myButton")))
button.click()

# Wait for element text to change
wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "Success"))
```

### Common Expected Conditions

```python
from selenium.webdriver.support import expected_conditions as EC

# Element presence/visibility conditions
EC.presence_of_element_located((By.ID, "id"))          # Element in DOM
EC.visibility_of_element_located((By.ID, "id"))        # Element visible
EC.invisibility_of_element_located((By.ID, "id"))      # Element not visible
EC.presence_of_all_elements_located((By.CLASS_NAME, "class"))  # All elements

# Element interaction conditions
EC.element_to_be_clickable((By.ID, "id"))              # Element clickable
EC.element_to_be_selected((By.ID, "id"))               # Element selected
EC.element_located_to_be_selected((By.ID, "id"))       # Located element selected

# Text conditions
EC.text_to_be_present_in_element((By.ID, "id"), "text")        # Text in element
EC.text_to_be_present_in_element_value((By.ID, "id"), "text")  # Text in value

# Other conditions
EC.title_is("Page Title")                               # Exact title
EC.title_contains("Partial Title")                      # Partial title match
EC.alert_is_present()                                   # Alert dialog present
EC.frame_to_be_available_and_switch_to_it((By.ID, "id"))  # Switch to frame
```

### Implicit Waits

Implicit waits tell WebDriver to wait a specified time when finding elements.

```python
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Wait up to 10 seconds for any element

driver.get("https://example.com")
# Will wait up to 10 seconds for element to appear
element = driver.find_element(By.ID, "myElement")
```

**Note:** Explicit waits are generally preferred over implicit waits for better control.

### Custom Wait Conditions

```python
class element_has_css_class(object):
    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class
    
    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.css_class in element.get_attribute("class"):
            return element
        else:
            return False

# Usage
wait = WebDriverWait(driver, 10)
element = wait.until(element_has_css_class((By.ID, "myElement"), "active"))
```

## 2.2 Page Objects Design Pattern

The Page Object Model is a design pattern that improves test code organization and maintainability.

### Benefits of Page Object Pattern

- **Maintainability**: Change selectors in one place
- **Reusability**: Use same page objects across multiple tests
- **Readability**: Tests read like business language
- **Scalability**: Easy to extend for new pages

### Basic Page Object Structure

**locators.py** - Define all locators
```python
from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

class DashboardPageLocators:
    WELCOME_TEXT = (By.ID, "welcome")
    LOGOUT_BUTTON = (By.ID, "logout")
```

**page.py** - Define page objects
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, DashboardPageLocators

class BasePage:
    """Base class for all pages"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

class LoginPage(BasePage):
    """Login page object"""
    
    def enter_username(self, username):
        element = self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.USERNAME_INPUT)
        )
        element.clear()
        element.send_keys(username)
    
    def enter_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        )
        element.clear()
        element.send_keys(password)
    
    def click_login(self):
        button = self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        button.click()
    
    def login(self, username, password):
        """Complete login flow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self):
        element = self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE)
        )
        return element.text

class DashboardPage(BasePage):
    """Dashboard page object"""
    
    def is_welcome_displayed(self):
        element = self.wait.until(
            EC.visibility_of_element_located(DashboardPageLocators.WELCOME_TEXT)
        )
        return element.is_displayed()
    
    def logout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(DashboardPageLocators.LOGOUT_BUTTON)
        )
        button.click()
```

**test_login.py** - Use page objects in tests
```python
import unittest
from selenium import webdriver
from page import LoginPage, DashboardPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/login")
        self.login_page = LoginPage(self.driver)
    
    def test_successful_login(self):
        self.login_page.login("validuser", "validpass")
        
        dashboard = DashboardPage(self.driver)
        self.assertTrue(dashboard.is_welcome_displayed())
    
    def test_invalid_login(self):
        self.login_page.login("invaliduser", "wrongpass")
        
        error_message = self.login_page.get_error_message()
        self.assertIn("Invalid credentials", error_message)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

## 2.3 Form Handling and Input

### Text Input Fields

```python
from selenium.webdriver.common.by import By

# Clear and enter text
text_field = driver.find_element(By.ID, "username")
text_field.clear()
text_field.send_keys("john_doe")

# Get current value
current_value = text_field.get_attribute("value")
print(current_value)
```

### Checkboxes

```python
checkbox = driver.find_element(By.ID, "agree")

# Check if already checked
if not checkbox.is_selected():
    checkbox.click()

# Check and uncheck
checkbox.click()  # Toggle
```

### Radio Buttons

```python
radio_buttons = driver.find_elements(By.NAME, "gender")

# Select a specific radio button
for radio in radio_buttons:
    if radio.get_attribute("value") == "male":
        radio.click()
        break
```

### Dropdowns/Select

```python
from selenium.webdriver.support.ui import Select

dropdown = driver.find_element(By.NAME, "country")
select = Select(dropdown)

# Select options
select.select_by_visible_text("United States")
select.select_by_value("US")
select.select_by_index(0)

# Get selected value
selected_option = select.first_selected_option
print(selected_option.text)
```

### Multi-Select Dropdowns

```python
select = Select(driver.find_element(By.ID, "multiselect"))

# Select multiple options
select.select_by_visible_text("Option 1")
select.select_by_visible_text("Option 2")

# Get all selected options
selected_options = select.all_selected_options
for option in selected_options:
    print(option.text)

# Deselect options
select.deselect_by_visible_text("Option 1")
select.deselect_all()
```

### File Upload

```python
# For file input fields
file_input = driver.find_element(By.ID, "file_upload")
file_input.send_keys("/path/to/file.txt")

# Or absolute path
import os
file_path = os.path.abspath("file.txt")
file_input.send_keys(file_path)
```

### Complete Form Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com/form")
wait = WebDriverWait(driver, 10)

# Wait for form to load
form = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

# Fill text fields
driver.find_element(By.NAME, "firstname").send_keys("John")
driver.find_element(By.NAME, "lastname").send_keys("Doe")
driver.find_element(By.NAME, "email").send_keys("john@example.com")

# Select radio button
male_radio = driver.find_element(By.CSS_SELECTOR, "input[value='male']")
male_radio.click()

# Check checkbox
agree_checkbox = driver.find_element(By.ID, "agree")
agree_checkbox.click()

# Select dropdown
country_select = Select(driver.find_element(By.NAME, "country"))
country_select.select_by_visible_text("United States")

# Upload file
file_input = driver.find_element(By.ID, "document")
file_input.send_keys("/path/to/document.pdf")

# Submit form
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

driver.quit()
```

## 2.4 Test Framework Integration

### Using unittest

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleSearchTest(unittest.TestCase):
    
    def setUp(self):
        """Run before each test"""
        self.driver = webdriver.Chrome()
    
    def test_google_search(self):
        """Test Google search functionality"""
        driver = self.driver
        driver.get("https://www.google.com")
        
        # Assert page loaded
        self.assertIn("Google", driver.title)
        
        # Perform search
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium WebDriver")
        search_box.submit()
        
        # Assert results appear
        self.assertIn("Selenium", driver.page_source)
    
    def test_page_title(self):
        """Test page title"""
        self.driver.get("https://www.python.org")
        self.assertIn("Python", self.driver.title)
    
    def tearDown(self):
        """Run after each test"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

### Using pytest

```bash
pip install pytest pytest-selenium
```

```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    """Fixture to provide WebDriver instance"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(driver):
    """Test Google search"""
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium")
    search_box.submit()
    
    assert "Selenium" in driver.page_source

def test_python_org_title(driver):
    """Test Python.org title"""
    driver.get("https://www.python.org")
    assert "Python" in driver.title
```

---

# PART 3: ADVANCED CONCEPTS

## 3.1 Action Chains: Complex User Interactions

Action Chains allow you to perform complex interactions like mouse movements, drag-and-drop, right-clicks, etc.

### Basic Action Chain Methods

```python
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
actions = ActionChains(driver)

# Mouse movements
element = driver.find_element(By.ID, "element")
actions.move_to_element(element).perform()

# Hover over element
menu = driver.find_element(By.ID, "menu")
actions.move_to_element(menu).perform()

# Click
actions.click(element).perform()

# Double-click
actions.double_click(element).perform()

# Right-click (context click)
actions.context_click(element).perform()

# Click and hold
actions.click_and_hold(element).perform()

# Release
actions.release(element).perform()

# Right-click and click
actions.context_click(element).click(menu_item).perform()
```

### Drag and Drop

```python
from selenium.webdriver.common.action_chains import ActionChains

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

# Method 1: Drag to element
ActionChains(driver).drag_and_drop(source, target).perform()

# Method 2: Drag by offset
ActionChains(driver).drag_and_drop_by_offset(source, 100, 50).perform()
```

### Keyboard Interactions

```python
actions = ActionChains(driver)

# Key down and up
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Multiple key combinations
actions.key_down(Keys.SHIFT)
actions.send_keys("a", "b", "c")
actions.key_up(Keys.SHIFT)
actions.perform()

# Send keys to specific element
element = driver.find_element(By.ID, "input")
actions.send_keys_to_element(element, "text").perform()
```

### Advanced Action Chains Example

```python
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://example.com")

# Method 1: Chain method calls
menu = driver.find_element(By.ID, "menu")
submenu = driver.find_element(By.ID, "submenu")

ActionChains(driver)\
    .move_to_element(menu)\
    .move_to_element(submenu)\
    .click(submenu)\
    .perform()

# Method 2: Queue actions then perform
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click()
actions.send_keys("search_text")
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
actions.perform()

# Method 3: Pause between actions
actions = ActionChains(driver, duration=250)
actions.move_to_element(menu).pause(1).click(submenu).perform()
```

## 3.2 Handling JavaScript Alerts and Popups

### Alert Types and Handling

```python
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Simple alert (OK button only)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

# Confirmation dialog (OK/Cancel)
alert.dismiss()  # Click Cancel

# Prompt dialog (with text input)
alert.send_keys("input text")
alert.accept()
```

### Wait for Alert and Handle

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

wait = WebDriverWait(driver, 10)

# Wait for alert to appear
alert = wait.until(EC.alert_is_present())

# Get alert text
alert_text = alert.text
print(alert_text)

# Accept alert
alert.accept()

# Or dismiss
alert.dismiss()
```

### Complete Alert Handling Example

```python
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com/alerts")
wait = WebDriverWait(driver, 10)

# Handle simple alert
driver.find_element(By.ID, "simple_alert").click()
alert = wait.until(EC.alert_is_present())
print(f"Alert text: {alert.text}")
alert.accept()

# Handle confirmation
driver.find_element(By.ID, "confirm_button").click()
alert = wait.until(EC.alert_is_present())
if "Are you sure?" in alert.text:
    alert.dismiss()  # Click Cancel

# Handle prompt
driver.find_element(By.ID, "prompt_button").click()
alert = wait.until(EC.alert_is_present())
alert.send_keys("John Doe")
alert.accept()
```

## 3.3 Switching Between Windows and Frames

### Working with Windows

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Get current window handle
current_window = driver.current_window_handle
print(current_window)

# Get all window handles
all_windows = driver.window_handles

# Switch to a new window
driver.switch_to.window(all_windows[1])

# Switch back to original
driver.switch_to.window(current_window)

# Close current window
driver.close()

# Switch to another window after closing
if driver.current_window_handle != current_window:
    driver.switch_to.window(current_window)
```

### Working with Frames and iFrames

```python
# Switch to frame by name
driver.switch_to.frame("frame_name")

# Switch to frame by ID
driver.switch_to.frame("frame_id")

# Switch to frame by index
driver.switch_to.frame(0)  # First frame

# Switch to frame by WebElement
frame_element = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(frame_element)

# Switch to nested frame (using dot notation)
driver.switch_to.frame("frame1.frame2.frame3")

# Switch back to parent frame
driver.switch_to.parent_frame()

# Switch to main content (out of all frames)
driver.switch_to.default_content()
```

### Complete Window and Frame Example

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")
wait = WebDriverWait(driver, 10)

# Handle new window
original_window = driver.current_window_handle

# Click button that opens new window
driver.find_element(By.ID, "open_new_window").click()

# Wait for new window
wait.until(EC.number_of_windows_to_be(2))

# Switch to new window
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Work in new window
print(driver.title)
driver.close()

# Switch back to original
driver.switch_to.window(original_window)

# Handle iframe
iframe = wait.until(
    EC.presence_of_element_located((By.TAG_NAME, "iframe"))
)
driver.switch_to.frame(iframe)

# Find element inside iframe
element = driver.find_element(By.ID, "iframe_element")
element.click()

# Back to main content
driver.switch_to.default_content()
```

## 3.4 JavaScript Execution

### Executing JavaScript

```python
# Simple script execution
result = driver.execute_script("return document.title;")
print(result)

# Accessing elements
element = driver.find_element(By.ID, "myElement")
driver.execute_script("arguments[0].style.border='2px solid red';", element)

# Multiple arguments
driver.execute_script(
    "return arguments[0].textContent + ' ' + arguments[1].getAttribute('id');",
    element1,
    element2
)

# Scroll to element
element = driver.find_element(By.ID, "myElement")
driver.execute_script("arguments[0].scrollIntoView();", element)

# Scroll to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Get window properties
window_size = driver.execute_script(
    "return {width: window.innerWidth, height: window.innerHeight};"
)

# Highlight element
driver.execute_script(
    """
    arguments[0].setAttribute('style', 'border: 2px solid red;');
    """,
    element
)

# Get all links
links = driver.execute_script(
    "return Array.from(document.querySelectorAll('a')).map(a => a.href);"
)

# Wait for jQuery AJAX requests to complete
driver.execute_script("return jQuery.active == 0;")
```

### Async JavaScript Execution

```python
# Execute async script
result = driver.execute_async_script("""
    var callback = arguments[arguments.length - 1];
    setTimeout(function() {
        callback('async result');
    }, 1000);
""")
print(result)

# With element arguments
driver.execute_async_script("""
    var element = arguments[0];
    var callback = arguments[arguments.length - 1];
    
    setTimeout(function() {
        element.click();
        callback('clicked');
    }, 2000);
""", element)
```

### Advanced JavaScript Examples

```python
# Check if page uses jQuery
has_jquery = driver.execute_script("return typeof jQuery !== 'undefined';")

# Wait for Angular to finish loading
driver.execute_script("""
    return window.getAllAngularTestabilities().findIndex(testability => {
        return !testability.isStable();
    }) === -1;
""")

# Get all console errors
errors = driver.execute_script("""
    return window.__errors || [];
""")

# Inject custom logging
driver.execute_script("""
    window.__logs = [];
    console.log = function(msg) {
        window.__logs.push(msg);
    };
""")
```

## 3.5 Advanced Element Selection and Navigation

### Shadow DOM Access

```python
# Access shadow DOM
shadow_root = driver.execute_script(
    "return arguments[0].shadowRoot;",
    shadow_host_element
)

# Find element in shadow DOM
element_in_shadow = driver.execute_script(
    """
    const shadowHost = arguments[0];
    const shadowRoot = shadowHost.shadowRoot;
    return shadowRoot.querySelector('button');
    """,
    shadow_host_element
)
```

### Relative Locators (Modern Approach)

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.relative_locator import locate_with

# Find element near another element
email_input = locate_with(By.TAG_NAME, "input").below(
    driver.find_element(By.ID, "username")
)

# Find element with multiple conditions
button = locate_with(By.TAG_NAME, "button").above(
    footer
).to_left_of(
    signup_button
)
```

## 3.6 Headless Browser Execution

### Chrome Headless Mode

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")
driver.save_screenshot("screenshot.png")
driver.quit()
```

### Firefox Headless Mode

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get("https://example.com")
driver.quit()
```

### Advanced Browser Options

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# Headless mode
options.add_argument("--headless")

# Window size
options.add_argument("--window-size=1920,1080")

# Disable images for faster loading
options.add_argument("--blink-settings=imagesEnabled=false")

# Disable JavaScript
options.add_argument("--disable-javascript")

# Incognito mode
options.add_argument("--incognito")

# Start maximized
options.add_argument("--start-maximized")

# User agent
options.add_argument("user-agent=Mozilla/5.0...")

# Disable notifications
options.add_experimental_option(
    "prefs",
    {"profile.default_content_setting_values.notifications": 2}
)

# Disable plugins
options.add_argument("--disable-plugins")

driver = webdriver.Chrome(options=options)
```

## 3.7 Exception Handling

### Common Exceptions

```python
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    NoSuchFrameException,
    NoAlertPresentException,
    InvalidSelectorException,
    JavascriptException
)

# NoSuchElementException - Element not found
try:
    element = driver.find_element(By.ID, "nonexistent")
except NoSuchElementException:
    print("Element not found")

# TimeoutException - Wait exceeded
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id")))
except TimeoutException:
    print("Element took too long to appear")

# StaleElementReferenceException - Element no longer in DOM
try:
    element = driver.find_element(By.ID, "id")
    driver.refresh()  # Page refreshed
    element.click()  # Element reference is now stale
except StaleElementReferenceException:
    print("Element is no longer attached to DOM")
    # Refind the element
    element = driver.find_element(By.ID, "id")
    element.click()

# ElementNotInteractableException - Element not clickable
try:
    element = driver.find_element(By.ID, "hidden_element")
    element.click()
except ElementNotInteractableException:
    print("Element is not interactable")

# NoAlertPresentException - No alert found
try:
    alert = driver.switch_to.alert
except NoAlertPresentException:
    print("No alert dialog present")

# InvalidSelectorException - Bad selector syntax
try:
    element = driver.find_element(By.XPATH, "//invalid//xpath//")
except InvalidSelectorException:
    print("Invalid selector syntax")
```

### Comprehensive Exception Handling

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    wait = WebDriverWait(driver, 10)
    
    try:
        # Try to find element with wait
        element = wait.until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        element.click()
    
    except TimeoutException:
        print("Element took too long to appear")
        # Fallback action
    
    except StaleElementReferenceException:
        print("Element became stale, refinding...")
        element = driver.find_element(By.ID, "submit")
        element.click()
    
    except ElementNotInteractableException:
        print("Element not interactable, scrolling into view...")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

except NoSuchElementException:
    print("Critical element not found")
    
except NoAlertPresentException:
    print("Alert handling failed")
    
except JavascriptException as e:
    print(f"JavaScript error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
    driver.save_screenshot("error_screenshot.png")

finally:
    driver.quit()
```

---

# BEST PRACTICES AND TIPS

## 1. Code Organization

```python
# Good structure
project/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   └── test_dashboard.py
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py
│   └── logger.py
└── conftest.py  # pytest configuration
```

## 2. Driver Management

```python
# Good: Ensure driver cleanup
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Or use context manager
from contextlib import contextmanager

@contextmanager
def get_driver():
    driver = webdriver.Chrome()
    try:
        yield driver
    finally:
        driver.quit()

# Usage
with get_driver() as driver:
    driver.get("https://example.com")
```

## 3. Timeout Best Practices

```python
# Use reasonable timeouts
WAIT_TIME = 10

# For fast modern apps
WAIT_TIME_FAST = 5

# For slow/legacy apps
WAIT_TIME_SLOW = 30

wait = WebDriverWait(driver, WAIT_TIME)

# Specific waits for specific scenarios
element = wait.until(EC.presence_of_element_located((By.ID, "id")))  # Load
element = wait.until(EC.visibility_of_element_located((By.ID, "id")))  # Display
element = wait.until(EC.element_to_be_clickable((By.ID, "id")))  # Interact
```

## 4. Robust Selectors

```python
# Avoid fragile selectors
# Bad
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/button[3]")

# Good
driver.find_element(By.ID, "submit_button")
driver.find_element(By.NAME, "email")
driver.find_element(By.CSS_SELECTOR, ".btn-primary")

# Flexible XPath
driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
driver.find_element(By.XPATH, "//input[@id='email' and @type='text']")
```

## 5. Error Recovery

```python
# Retry mechanism
def retry_action(func, max_retries=3, delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except (StaleElementReferenceException, 
                ElementNotInteractableException) as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(delay)

# Usage
def click_element():
    driver.find_element(By.ID, "button").click()

retry_action(click_element)
```

## 6. Logging and Debugging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def search_element(locator):
    logger.info(f"Searching for element: {locator}")
    try:
        element = driver.find_element(*locator)
        logger.info("Element found successfully")
        return element
    except NoSuchElementException:
        logger.error(f"Element not found: {locator}")
        driver.save_screenshot(f"error_{locator[1]}.png")
        raise
```

## 7. Performance Tips

```python
# 1. Use headless mode for faster execution
options.add_argument("--headless")

# 2. Disable images if not needed
options.add_argument("--blink-settings=imagesEnabled=false")

# 3. Use explicit waits instead of sleep
# Don't do: time.sleep(5)
# Do: wait.until(EC.presence_of_element_located(...))

# 4. Reuse driver instance across tests
# Bad: Create new driver for each test
# Good: Use fixtures to share driver

# 5. Parallel execution
# Use pytest-xdist: pytest -n auto
```

---

# COMPLETE CODE EXAMPLES

## Example 1: Complete Login Test with Page Objects

```python
# locators.py
from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login_button")
    ERROR_MSG = (By.CLASS_NAME, "error-message")

class DashboardLocators:
    WELCOME_MSG = (By.ID, "welcome")
    LOGOUT_BTN = (By.ID, "logout_button")

# pages.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, DashboardLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

class LoginPage(BasePage):
    def login(self, username, password):
        self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.USERNAME)
        ).send_keys(username)
        
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        
        self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BTN)
        ).click()
        
        return DashboardPage(self.driver)
    
    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.ERROR_MSG)
        ).text

class DashboardPage(BasePage):
    def is_logged_in(self):
        return self.wait.until(
            EC.visibility_of_element_located(DashboardLocators.WELCOME_MSG)
        ).is_displayed()

# test_login.py
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/login")
    
    def test_successful_login(self):
        from pages import LoginPage
        
        login_page = LoginPage(self.driver)
        dashboard = login_page.login("user@example.com", "password123")
        
        self.assertTrue(dashboard.is_logged_in())
    
    def test_invalid_credentials(self):
        from pages import LoginPage
        
        login_page = LoginPage(self.driver)
        login_page.login("invalid@example.com", "wrongpass")
        
        error = login_page.get_error_message()
        self.assertIn("Invalid", error)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

## Example 2: E-Commerce Shopping Flow

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class EcommerceTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def test_shopping_flow(self):
        # Navigate to store
        self.driver.get("https://example-store.com")
        
        # Browse products
        self.browse_products()
        
        # Add to cart
        self.add_to_cart()
        
        # Checkout
        self.checkout()
        
        # Complete purchase
        self.complete_purchase()
    
    def browse_products(self):
        # Filter by price
        price_select = Select(
            self.driver.find_element(By.ID, "price_filter")
        )
        price_select.select_by_value("under_50")
        
        # Wait for products to load
        products = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product"))
        )
        print(f"Found {len(products)} products")
    
    def add_to_cart(self):
        # Select product
        product = self.driver.find_element(By.CSS_SELECTOR, ".product:first-child")
        ActionChains(self.driver).move_to_element(product).perform()
        
        # Click add to cart
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart"))
        )
        add_btn.click()
        
        # Confirm add to cart message
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "success-msg"))
        )
    
    def checkout(self):
        # Go to cart
        cart_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "cart_button"))
        )
        cart_btn.click()
        
        # Proceed to checkout
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout_button"))
        )
        checkout_btn.click()
    
    def complete_purchase(self):
        # Fill shipping address
        self.driver.find_element(By.NAME, "address").send_keys("123 Main St")
        self.driver.find_element(By.NAME, "city").send_keys("New York")
        self.driver.find_element(By.NAME, "zipcode").send_keys("10001")
        
        # Select shipping method
        shipping_select = Select(
            self.driver.find_element(By.NAME, "shipping")
        )
        shipping_select.select_by_visible_text("Express Shipping")
        
        # Payment
        self.driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
        
        # Complete order
        order_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "place_order"))
        )
        order_btn.click()
        
        # Verify order confirmation
        confirmation = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "confirmation"))
        )
        return confirmation.text
    
    def close(self):
        self.driver.quit()

# Usage
if __name__ == "__main__":
    test = EcommerceTest()
    try:
        confirmation = test.test_shopping_flow()
        print(f"Order confirmed: {confirmation}")
    finally:
        test.close()
```

## Example 3: Advanced Form Handling with Validation

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormHandler:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def fill_text_field(self, locator, value):
        """Fill text field with validation"""
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(value)
        
        # Verify value was entered
        assert element.get_attribute("value") == value
    
    def select_from_dropdown(self, locator, value):
        """Select from dropdown"""
        from selenium.webdriver.support.ui import Select
        
        dropdown = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        Select(dropdown).select_by_visible_text(value)
    
    def check_checkbox(self, locator, should_check=True):
        """Check or uncheck checkbox"""
        checkbox = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        
        is_checked = checkbox.is_selected()
        
        if should_check and not is_checked:
            checkbox.click()
        elif not should_check and is_checked:
            checkbox.click()
    
    def upload_file(self, locator, file_path):
        """Upload file"""
        file_input = self.driver.find_element(*locator)
        file_input.send_keys(file_path)
    
    def submit_form(self, submit_locator):
        """Submit form and wait for result"""
        submit_btn = self.wait.until(
            EC.element_to_be_clickable(submit_locator)
        )
        submit_btn.click()
        
        # Wait for form to be processed
        self.wait.until(
            EC.invisibility_of_element_located(submit_locator)
        )
    
    def get_validation_error(self, error_locator):
        """Get validation error message"""
        error = self.wait.until(
            EC.visibility_of_element_located(error_locator)
        )
        return error.text

# Usage
if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com/form")
        
        form = FormHandler(driver)
        
        # Fill form
        form.fill_text_field((By.NAME, "firstname"), "John")
        form.fill_text_field((By.NAME, "lastname"), "Doe")
        form.fill_text_field((By.NAME, "email"), "john@example.com")
        
        form.select_from_dropdown((By.NAME, "country"), "United States")
        form.check_checkbox((By.ID, "newsletter"), should_check=True)
        
        form.upload_file((By.ID, "document"), "/path/to/file.pdf")
        
        form.submit_form((By.ID, "submit"))
        
        print("Form submitted successfully")
    
    except Exception as e:
        print(f"Error: {e}")
        error_msg = form.get_validation_error((By.CLASS_NAME, "error"))
        print(f"Validation error: {error_msg}")
    
    finally:
        driver.quit()
```

---

## QUICK REFERENCE GUIDE

### Import Statements (Copy & Paste)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    ElementNotInteractableException,
)
```

### Common Methods Quick Reference

| Task | Code |
|------|------|
| Navigate | `driver.get("url")` |
| Find element | `driver.find_element(By.ID, "id")` |
| Find elements | `driver.find_elements(By.TAG_NAME, "button")` |
| Click | `element.click()` |
| Type text | `element.send_keys("text")` |
| Clear field | `element.clear()` |
| Submit form | `form.submit()` |
| Get text | `element.text` |
| Get attribute | `element.get_attribute("attr")` |
| Wait for element | `wait.until(EC.presence_of_element_located(...))` |
| Take screenshot | `driver.save_screenshot("file.png")` |
| Execute JS | `driver.execute_script("code")` |
| Handle alert | `alert = driver.switch_to.alert; alert.accept()` |
| Switch frame | `driver.switch_to.frame("name")` |
| Scroll | `driver.execute_script("window.scrollTo(0, 100);")` |
| Close browser | `driver.quit()` |

---

## CONCLUSION

### What You've Learned

**Basic Level:**
- Installation and setup
- Browser navigation
- Element location (8 methods)
- Basic interactions
- Simple tests

**Intermediate Level:**
- Explicit and implicit waits
- Page Object Model
- Form handling
- Test frameworks
- Complex element interactions

**Advanced Level:**
- Action Chains
- JavaScript execution
- Alert and window handling
- Frame switching
- Exception handling
- Headless execution

### Next Steps

1. **Practice**: Build projects using what you've learned
2. **Explore**: Check official Selenium documentation
3. **Specialize**: Choose your focus (testing, scraping, RPA)
4. **Optimize**: Learn performance and best practices
5. **Master**: Contribute to Selenium community

### Resources

- Official Docs: https://selenium.dev/documentation/
- Python Bindings: https://selenium-python.readthedocs.io/
- Tutorials: Udemy, Coursera (for AI/ML integration)
- Community: Stack Overflow, Reddit r/selenium

### Final Tips

- Always use explicit waits
- Follow Page Object pattern for maintainability
- Handle exceptions gracefully
- Keep selectors simple and flexible
- Organize code logically
- Use headless mode for CI/CD
- Log errors for debugging
- Write modular, reusable code

---

**Happy Selenium Learning! 🚀**

*Last Updated: January 2026*
*Selenium Version: 4.x+*
