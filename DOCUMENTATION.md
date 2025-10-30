# Operation HOPE Selenium Tests (Python) - Comprehensive Documentation

## Table of Contents

- [Operation HOPE Selenium Tests (Python) - Comprehensive Documentation](#operation-hope-selenium-tests-python---comprehensive-documentation)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
    - [Purpose](#purpose)
    - [Key Features](#key-features)
    - [Tested Portals](#tested-portals)
  - [Architecture](#architecture)
    - [Test Architecture](#test-architecture)
    - [Technology Stack](#technology-stack)
  - [Project Structure](#project-structure)

---

## Project Overview

This project contains **Selenium WebDriver** automated tests for the Operation HOPE portals (Client Portal and VMS Portal). The tests are written in Python and use Selenium 4.x with Chrome WebDriver.

### Purpose

- **End-to-End Testing**: Validate complete user workflows
- **Regression Testing**: Ensure new changes don't break existing functionality
- **Integration Testing**: Test portal interactions with backend services
- **UI Testing**: Verify user interface elements and behaviors

### Key Features

- **Automated Browser Testing**: Chrome browser automation
- **Screenshot Capture**: Automatic screenshots at each test step
- **Configurable Environments**: Support for dev, QA, UAT, and production
- **Helper Utilities**: Reusable functions for common operations
- **Error Handling**: Comprehensive error logging and debugging
- **Multiple Click Strategies**: Fallback mechanisms for reliable element interaction

### Tested Portals

- **Client Portal**: `https://oh-clientportal-dev.powerappsportals.com/`
- **VMS Portal**: Volunteer Management System
- **Authentication**: Azure AD B2C integration

---

## Architecture

### Test Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Test Runner                               │
│              (pytest or direct execution)                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  Test Files                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ example_test │  │ support_     │  │ future_tests │      │
│  │              │  │ ticket_test  │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Helper Utilities & Config                       │
│  ┌──────────────┐  ┌──────────────┐                         │
│  │ TestHelpers  │  │ Config       │                         │
│  │ - wait       │  │ - timeouts   │                         │
│  │ - screenshot │  │ - URLs       │                         │
│  │ - logging    │  │ - options    │                         │
│  └──────────────┘  └──────────────┘                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Selenium WebDriver                              │
│  ┌──────────────┐  ┌──────────────┐                         │
│  │ ChromeDriver │  │ WebDriver    │                         │
│  │ Manager      │  │ API          │                         │
│  └──────────────┘  └──────────────┘                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Chrome Browser                                  │
│  - Automated browser instance                                │
│  - Executes test actions                                     │
│  - Captures screenshots                                      │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

- **Python**: 3.8+
- **Selenium**: 4.27.1 (WebDriver automation)
- **webdriver-manager**: 4.0.2 (Automatic ChromeDriver management)
- **pytest**: 8.3.3 (Test framework)
- **Chrome Browser**: Latest stable version

---

## Project Structure

```
selenium-tests-py/
├── tests/                      # Test files
│   ├── __init__.py            # Package initializer
│   ├── example_test.py        # Example/template test
│   └── support_ticket_test.py # Support ticket submission test
├── config/                     # Configuration files
│   ├── __init__.py            # Package initializer
│   └── config.py              # Test configuration (timeouts, URLs, options)
├── utils/                      # Helper utilities
│   ├── __init__.py            # Package initializer
│   └── helpers.py             # TestHelpers class with common functions
├── screenshots/                # Test screenshots (auto-generated)
│   └── *.png                  # Timestamped screenshots
├── venv/                       # Virtual environment (not in git)
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Python dependencies
├── setup.sh                   # Setup script for Unix/Mac
├── README.md                  # Quick start guide
└── DOCUMENTATION.md           # This comprehensive documentation
```

### File Descriptions

#### **tests/**

- **example_test.py**: Template test showing basic Selenium usage
- **support_ticket_test.py**: Complete E2E test for support ticket submission
- \***\*init**.py\*\*: Makes tests directory a Python package

#### **config/**

- **config.py**: Centralized configuration for:
  - Browser settings
  - Timeouts (implicit, page load, script)
  - Environment URLs (local, dev, QA, prod)
  - Screenshot settings
  - Chrome options

#### **utils/**

- **helpers.py**: TestHelpers class with reusable functions:
  - Element waiting and interaction
  - Screenshot capture
  - Page load detection
  - Scrolling utilities
  - Logging functions

#### **screenshots/**

- Auto-generated directory for test screenshots
- Timestamped PNG files for each test step
- Useful for debugging and visual verification

---

## Setup & Installation

### Prerequisites

1. **Python 3.8 or higher**

   ```bash
   python3 --version
   ```

2. **Chrome Browser**

   - Download from: https://www.google.com/chrome/
   - ChromeDriver is automatically managed by webdriver-manager

3. **Git** (for cloning repository)
   ```bash
   git --version
   ```

### Installation Steps

#### Option 1: Using setup.sh (Mac/Linux)

```bash
# Navigate to project directory
cd selenium-tests-py

# Make setup script executable
chmod +x setup.sh

# Run setup script
./setup.sh
```

The script will:

- Check Python 3 installation
- Create virtual environment
- Activate virtual environment
- Install all dependencies

#### Option 2: Manual Setup

```bash
# Navigate to project directory
cd selenium-tests-py

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### Verify Installation

```bash
# Check Selenium installation
python -c "import selenium; print(selenium.__version__)"

# Check pytest installation
pytest --version

# List installed packages
pip list
```

---

## Running Tests

### Activate Virtual Environment

Before running tests, activate the virtual environment:

```bash
# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Run Individual Tests

#### Example Test (Google Search)

```bash
python tests/example_test.py
```

#### Support Ticket Test

```bash
python tests/support_ticket_test.py
```

### Run All Tests with pytest

```bash
# Run all tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/support_ticket_test.py

# Run with detailed output
python -m pytest tests/ -v -s
```

### Run Tests in Headless Mode

Edit `config/config.py` and uncomment the headless option:

```python
CHROME_OPTIONS = {
    'args': [
        '--headless',  # Uncomment this line
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--window-size=1920,1080',
        '--disable-gpu'
    ]
}
```

### View Test Results

- **Console Output**: Real-time test progress and logs
- **Screenshots**: Check `screenshots/` folder for visual verification
- **Exit Codes**:
  - `0` = Success
  - `1` = Failure

---

## Writing Tests

### Test Structure

Every test should follow this structure:

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config.config import BROWSER, TIMEOUTS, CHROME_OPTIONS
from utils.helpers import TestHelpers


def my_test():
    """Test function description"""

    # Setup Chrome options
    chrome_options = Options()
    for arg in CHROME_OPTIONS['args']:
        chrome_options.add_argument(arg)

    # Create WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Set timeouts
        driver.implicitly_wait(TIMEOUTS['implicit'])
        driver.set_page_load_timeout(TIMEOUTS['page_load'])
        driver.set_script_timeout(TIMEOUTS['script'])

        # Test steps
        TestHelpers.log('Starting test...')
        driver.get('https://example.com')
        TestHelpers.wait_for_page_load(driver)
        TestHelpers.take_screenshot(driver, 'step-1')

        # More test steps...

        TestHelpers.log('Test completed!')

    except Exception as error:
        TestHelpers.log_error(error)
        TestHelpers.take_screenshot(driver, 'error')
        raise
    finally:
        driver.quit()


if __name__ == '__main__':
    try:
        my_test()
        print('\n✅ Test passed!')
        sys.exit(0)
    except Exception:
        print('\n❌ Test failed!')
        sys.exit(1)
```

### Common Test Patterns

#### 1. Navigate to Page

```python
driver.get('https://example.com')
TestHelpers.wait_for_page_load(driver)
TestHelpers.take_screenshot(driver, 'page-loaded')
```

#### 2. Find and Click Element

```python
# Using TestHelpers
TestHelpers.wait_and_click(driver, (By.CSS_SELECTOR, '.button-class'))

# Manual approach
element = TestHelpers.wait_for_element(driver, (By.ID, 'button-id'))
element.click()
```

#### 3. Fill Form Fields

```python
# Using TestHelpers
TestHelpers.wait_and_send_keys(driver, (By.ID, 'email'), 'test@example.com')

# Manual approach
email_input = driver.find_element(By.ID, 'email')
email_input.clear()
email_input.send_keys('test@example.com')
```

#### 4. Wait for Element

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for element to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.button'))
)
```

#### 5. Handle Popups/Modals

```python
try:
    popup_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.popup-close'))
    )
    popup_button.click()
except TimeoutException:
    TestHelpers.log('No popup found, continuing...')
```

#### 6. Multiple Click Strategies

```python
# Try multiple methods to click stubborn elements
button_clicked = False

# Method 1: jQuery trigger (best for jQuery-based sites)
try:
    driver.execute_script("jQuery('.button').trigger('click');")
    button_clicked = True
except:
    pass

# Method 2: Regular click
if not button_clicked:
    try:
        button.click()
        button_clicked = True
    except:
        pass

# Method 3: JavaScript click
if not button_clicked:
    try:
        driver.execute_script('arguments[0].click();', button)
        button_clicked = True
    except:
        pass
```

---

## Configuration

### config/config.py

#### Browser Configuration

```python
BROWSER = 'chrome'  # Currently only Chrome is supported
```

#### Timeouts

```python
TIMEOUTS = {
    'implicit': 10,      # Wait for elements to appear (seconds)
    'page_load': 30,     # Wait for page to load (seconds)
    'script': 30         # Wait for scripts to execute (seconds)
}
```

#### Environment URLs

```python
URLS = {
    'local': 'http://localhost:3000',
    'dev': 'https://dev.operationhope.com',
    'qa': 'https://qa.operationhope.com',
    'prod': 'https://www.operationhope.com'
}
```

#### Screenshot Settings

```python
SCREENSHOTS = {
    'enabled': True,
    'path': './screenshots',
    'on_failure': True
}
```

#### Chrome Options

```python
CHROME_OPTIONS = {
    'args': [
        # '--headless',              # Run without GUI
        '--no-sandbox',              # Bypass OS security model
        '--disable-dev-shm-usage',   # Overcome limited resource problems
        '--window-size=1920,1080',   # Set window size
        '--disable-gpu'              # Disable GPU acceleration
    ]
}
```

### Test-Specific Configuration

Each test can have its own configuration:

```python
TEST_CONFIG = {
    'base_url': 'https://oh-clientportal-dev.powerappsportals.com/',
    'credentials': {
        'email': 'test@example.com',
        'password': 'SecurePassword123'
    },
    'test_data': {
        'name': 'Test User',
        'phone': '+11234567890'
    }
}
```

---

## Helper Functions

### TestHelpers Class

Located in `utils/helpers.py`, provides reusable functions:

#### wait_for_element(driver, locator, timeout=10)

Wait for element to be visible.

```python
element = TestHelpers.wait_for_element(
    driver,
    (By.CSS_SELECTOR, '.button')
)
```

#### take_screenshot(driver, filename)

Capture screenshot with timestamp.

```python
TestHelpers.take_screenshot(driver, 'login-page')
# Saves as: screenshots/login-page_1234567890.png
```

#### wait_for_page_load(driver, timeout=30)

Wait for page to fully load.

```python
driver.get('https://example.com')
TestHelpers.wait_for_page_load(driver)
```

#### scroll_to_element(driver, element)

Scroll element into view.

```python
button = driver.find_element(By.ID, 'submit')
TestHelpers.scroll_to_element(driver, button)
```

#### wait_and_click(driver, locator)

Wait for element and click it.

```python
TestHelpers.wait_and_click(driver, (By.ID, 'submit-button'))
```

#### wait_and_send_keys(driver, locator, text)

Wait for element and enter text.

```python
TestHelpers.wait_and_send_keys(
    driver,
    (By.ID, 'email'),
    'test@example.com'
)
```

#### log(message)

Log test step with timestamp.

```python
TestHelpers.log('Starting login process...')
# Output: [2025-10-29T12:34:56] Starting login process...
```

#### log_error(error)

Log error with stack trace.

```python
try:
    # test code
except Exception as error:
    TestHelpers.log_error(error)
```

---

## Test Examples

### Example 1: Simple Navigation Test

```python
def navigation_test():
    """Test basic navigation"""
    driver = setup_driver()

    try:
        TestHelpers.log('Testing navigation...')

        # Navigate to home page
        driver.get('https://example.com')
        TestHelpers.wait_for_page_load(driver)
        TestHelpers.take_screenshot(driver, 'home')

        # Click About link
        about_link = driver.find_element(By.LINK_TEXT, 'About')
        about_link.click()
        TestHelpers.wait_for_page_load(driver)
        TestHelpers.take_screenshot(driver, 'about')

        # Verify URL
        assert 'about' in driver.current_url
        TestHelpers.log('Navigation test passed!')

    finally:
        driver.quit()
```

### Example 2: Form Submission Test

```python
def form_submission_test():
    """Test form submission"""
    driver = setup_driver()

    try:
        TestHelpers.log('Testing form submission...')

        # Navigate to form
        driver.get('https://example.com/contact')
        TestHelpers.wait_for_page_load(driver)

        # Fill form
        TestHelpers.wait_and_send_keys(driver, (By.ID, 'name'), 'John Doe')
        TestHelpers.wait_and_send_keys(driver, (By.ID, 'email'), 'john@example.com')
        TestHelpers.wait_and_send_keys(driver, (By.ID, 'message'), 'Test message')

        TestHelpers.take_screenshot(driver, 'form-filled')

        # Submit form
        TestHelpers.wait_and_click(driver, (By.ID, 'submit'))

        # Wait for success message
        success_msg = TestHelpers.wait_for_element(
            driver,
            (By.CSS_SELECTOR, '.success-message')
        )

        assert success_msg.is_displayed()
        TestHelpers.take_screenshot(driver, 'success')
        TestHelpers.log('Form submission test passed!')

    finally:
        driver.quit()
```

### Example 3: Login Test

```python
def login_test():
    """Test user login"""
    driver = setup_driver()

    try:
        TestHelpers.log('Testing login...')

        # Navigate to login page
        driver.get('https://example.com/login')
        TestHelpers.wait_for_page_load(driver)

        # Enter credentials
        TestHelpers.wait_and_send_keys(
            driver,
            (By.ID, 'email'),
            'test@example.com'
        )
        TestHelpers.wait_and_send_keys(
            driver,
            (By.ID, 'password'),
            'password123'
        )

        TestHelpers.take_screenshot(driver, 'credentials-entered')

        # Click login button
        TestHelpers.wait_and_click(driver, (By.ID, 'login-button'))

        # Wait for dashboard
        TestHelpers.wait_for_element(driver, (By.CSS_SELECTOR, '.dashboard'))
        TestHelpers.take_screenshot(driver, 'logged-in')

        # Verify login
        assert 'dashboard' in driver.current_url
        TestHelpers.log('Login test passed!')

    finally:
        driver.quit()
```

---

## Best Practices

### Test Design

1. **Keep Tests Independent**

   - Each test should run independently
   - Don't rely on other tests' state
   - Clean up after each test

2. **Use Descriptive Names**

   ```python
   # Good
   def test_user_can_submit_support_ticket():
       pass

   # Bad
   def test1():
       pass
   ```

3. **Add Comments and Logging**

   ```python
   # Step 1: Navigate to login page
   TestHelpers.log('Navigating to login page...')
   driver.get(LOGIN_URL)
   ```

4. **Take Screenshots at Key Steps**

   ```python
   TestHelpers.take_screenshot(driver, 'before-submit')
   submit_button.click()
   TestHelpers.take_screenshot(driver, 'after-submit')
   ```

5. **Use Explicit Waits**

   ```python
   # Good - explicit wait
   element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.ID, 'button'))
   )

   # Avoid - implicit wait only
   element = driver.find_element(By.ID, 'button')
   ```

### Element Location

1. **Prefer Stable Selectors**

   ```python
   # Best - ID (most stable)
   driver.find_element(By.ID, 'submit-button')

   # Good - CSS class (if stable)
   driver.find_element(By.CSS_SELECTOR, '.submit-btn')

   # Okay - XPath (if necessary)
   driver.find_element(By.XPATH, "//button[@type='submit']")

   # Avoid - complex XPath
   driver.find_element(By.XPATH, "/html/body/div[3]/form/button[2]")
   ```

2. **Use Data Attributes**
   ```python
   # HTML: <button data-testid="submit-btn">Submit</button>
   driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-btn"]')
   ```

### Error Handling

1. **Always Use try-finally**

   ```python
   driver = webdriver.Chrome()
   try:
       # Test code
   finally:
       driver.quit()  # Always cleanup
   ```

2. **Handle Expected Exceptions**

   ```python
   try:
       popup = driver.find_element(By.CSS_SELECTOR, '.popup')
       popup.click()
   except NoSuchElementException:
       TestHelpers.log('No popup found, continuing...')
   ```

3. **Take Screenshots on Failure**
   ```python
   except Exception as error:
       TestHelpers.log_error(error)
       TestHelpers.take_screenshot(driver, 'error-state')
       raise
   ```

### Performance

1. **Minimize Waits**

   - Use appropriate timeout values
   - Don't use `time.sleep()` unless necessary
   - Prefer explicit waits over implicit waits

2. **Reuse Driver When Possible**

   - For related tests, consider reusing driver
   - Balance between speed and test independence

3. **Run Tests in Parallel**
   ```bash
   pytest tests/ -n 4  # Run 4 tests in parallel
   ```

### Maintenance

1. **Use Configuration Files**

   - Store URLs, credentials, and settings in config
   - Don't hardcode values in tests

2. **Create Helper Functions**

   - Extract common operations into helpers
   - Reduce code duplication

3. **Keep Tests Updated**
   - Update selectors when UI changes
   - Review and refactor tests regularly

---

## Troubleshooting

### Common Issues

#### 1. ChromeDriver Version Mismatch

**Problem**: ChromeDriver version doesn't match Chrome browser

**Solution**: webdriver-manager handles this automatically, but if issues persist:

```bash
# Update webdriver-manager
pip install --upgrade webdriver-manager

# Clear cache
rm -rf ~/.wdm
```

#### 2. Element Not Found

**Problem**: `NoSuchElementException` or `TimeoutException`

**Solutions**:

- Increase timeout: `WebDriverWait(driver, 20)`
- Check selector: Use browser DevTools to verify
- Wait for page load: `TestHelpers.wait_for_page_load(driver)`
- Check if element is in iframe: `driver.switch_to.frame(iframe)`

```python
# Debug element location
try:
    element = driver.find_element(By.ID, 'button')
except NoSuchElementException:
    # Print page source to debug
    print(driver.page_source)
    # Take screenshot
    TestHelpers.take_screenshot(driver, 'element-not-found')
```

#### 3. Element Not Clickable

**Problem**: `ElementClickInterceptedException`

**Solutions**:

- Scroll to element: `TestHelpers.scroll_to_element(driver, element)`
- Wait for element to be clickable:
  ```python
  element = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.ID, 'button'))
  )
  ```
- Use JavaScript click:
  ```python
  driver.execute_script('arguments[0].click();', element)
  ```

#### 4. Stale Element Reference

**Problem**: `StaleElementReferenceException`

**Solution**: Re-find the element

```python
# Bad
button = driver.find_element(By.ID, 'button')
driver.refresh()
button.click()  # Stale!

# Good
button = driver.find_element(By.ID, 'button')
driver.refresh()
button = driver.find_element(By.ID, 'button')  # Re-find
button.click()
```

#### 5. Popup/Modal Handling

**Problem**: Can't interact with elements behind popup

**Solution**: Close popup first

```python
try:
    close_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.popup-close'))
    )
    close_button.click()
    time.sleep(1)
except TimeoutException:
    pass  # No popup
```

#### 6. Slow Tests

**Problem**: Tests take too long to run

**Solutions**:

- Reduce unnecessary waits
- Use headless mode
- Run tests in parallel
- Optimize selectors

#### 7. Tests Pass Locally but Fail in CI

**Problem**: Environment differences

**Solutions**:

- Use headless mode in CI
- Increase timeouts for slower CI environments
- Check for environment-specific issues
- Ensure consistent Chrome version

### Debugging Tips

#### 1. Enable Verbose Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### 2. Print Page Source

```python
print(driver.page_source)
```

#### 3. Check Current URL

```python
TestHelpers.log(f"Current URL: {driver.current_url}")
```

#### 4. List All Elements

```python
elements = driver.find_elements(By.CSS_SELECTOR, '.button')
TestHelpers.log(f"Found {len(elements)} buttons")
```

#### 5. Check Element Properties

```python
element = driver.find_element(By.ID, 'button')
TestHelpers.log(f"Visible: {element.is_displayed()}")
TestHelpers.log(f"Enabled: {element.is_enabled()}")
TestHelpers.log(f"Text: {element.text}")
```

#### 6. Browser Console Logs

```python
logs = driver.get_log('browser')
for entry in logs:
    print(f"{entry['level']}: {entry['message']}")
```

#### 7. Pause Execution

```python
import pdb; pdb.set_trace()  # Python debugger
# Or
input("Press Enter to continue...")  # Manual pause
```

---

## Advanced Topics

### Page Object Model (POM)

For larger test suites, consider using Page Object Model:

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, 'email')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login')

    def login(self, email, password):
        TestHelpers.wait_and_send_keys(self.driver, self.email_input, email)
        TestHelpers.wait_and_send_keys(self.driver, self.password_input, password)
        TestHelpers.wait_and_click(self.driver, self.login_button)

# tests/login_test.py
def test_login():
    driver = setup_driver()
    try:
        login_page = LoginPage(driver)
        login_page.login('test@example.com', 'password')
        # Verify login...
    finally:
        driver.quit()
```

### Data-Driven Testing

Use pytest parametrize for data-driven tests:

```python
import pytest

@pytest.mark.parametrize("email,password,expected", [
    ("valid@example.com", "correct", "success"),
    ("invalid@example.com", "wrong", "error"),
    ("", "", "error"),
])
def test_login_scenarios(email, password, expected):
    # Test with different data sets
    pass
```

### Parallel Execution

Install pytest-xdist:

```bash
pip install pytest-xdist
```

Run tests in parallel:

```bash
pytest tests/ -n 4  # 4 parallel workers
```

### CI/CD Integration

#### GitHub Actions Example

```yaml
name: Selenium Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.9"
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest tests/ -v
```

---

## Test Coverage

### Current Tests

1. **example_test.py**

   - Basic navigation test
   - Google search example
   - Template for new tests

2. **support_ticket_test.py**
   - Complete E2E workflow
   - Login flow with Azure AD B2C
   - Dashboard navigation
   - Support ticket form submission
   - Multiple click strategies
   - Comprehensive error handling

### Planned Tests

- User registration flow
- Profile management
- Program enrollment
- Coach selection
- Session booking
- VMS volunteer onboarding
- Service request management
- Hour logging

---

## Resources

### Documentation

- [Selenium Python Docs](https://selenium-python.readthedocs.io/)
- [WebDriver API](https://www.selenium.dev/documentation/webdriver/)
- [pytest Documentation](https://docs.pytest.org/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

### Tutorials

- [Selenium with Python Tutorial](https://www.selenium.dev/documentation/webdriver/getting_started/)
- [pytest Tutorial](https://docs.pytest.org/en/stable/getting-started.html)
- [Page Object Model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

### Tools

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Inspect elements
- [Selenium IDE](https://www.selenium.dev/selenium-ide/) - Record and playback
- [XPath Helper](https://chrome.google.com/webstore/detail/xpath-helper/) - Chrome extension

---

## Appendix

### Selenium Locator Strategies

| Strategy          | Example                                | Use Case                          |
| ----------------- | -------------------------------------- | --------------------------------- |
| ID                | `By.ID, 'submit'`                      | Most reliable, use when available |
| CSS Selector      | `By.CSS_SELECTOR, '.button'`           | Flexible, good performance        |
| XPath             | `By.XPATH, '//button[@type="submit"]'` | Complex queries                   |
| Name              | `By.NAME, 'email'`                     | Form fields                       |
| Link Text         | `By.LINK_TEXT, 'Click Here'`           | Exact link text                   |
| Partial Link Text | `By.PARTIAL_LINK_TEXT, 'Click'`        | Partial link text                 |
| Tag Name          | `By.TAG_NAME, 'button'`                | Find by HTML tag                  |
| Class Name        | `By.CLASS_NAME, 'btn'`                 | Single class name                 |

### Common WebDriver Methods

```python
# Navigation
driver.get(url)
driver.back()
driver.forward()
driver.refresh()

# Element interaction
element.click()
element.send_keys(text)
element.clear()
element.submit()

# Element properties
element.text
element.get_attribute('href')
element.is_displayed()
element.is_enabled()
element.is_selected()

# Browser properties
driver.title
driver.current_url
driver.page_source

# Windows and frames
driver.switch_to.window(window_handle)
driver.switch_to.frame(frame_reference)
driver.switch_to.default_content()

# Alerts
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()
alert.send_keys(text)

# Screenshots
driver.save_screenshot('screenshot.png')
element.screenshot('element.png')

# JavaScript execution
driver.execute_script('return document.title')
driver.execute_script('arguments[0].click();', element)
```

### Exit Codes

- `0` - All tests passed
- `1` - One or more tests failed
- `2` - Test execution error
- `3` - Internal error

---

**Document Version**: 1.0  
**Last Updated**: October 29, 2025  
**Maintained By**: Operation HOPE QA Team

For questions or issues, please contact the development team or create an issue in the repository.
