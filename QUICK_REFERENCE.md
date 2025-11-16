# Selenium Tests - Quick Reference Card

**Version**: 1.0 | **Date**: November 16, 2025

---

## 🚀 Quick Start Template

```python
"""
[Test Name] Test
Description and flow here
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

from config.config import TIMEOUTS, CHROME_OPTIONS
from utils.helpers import TestHelpers

TEST_CONFIG = {
    'base_url': 'https://example.com',
    'credentials': {'email': 'test@example.com', 'password': 'Pass123'}
}

def my_test():
    chrome_options = Options()
    for arg in CHROME_OPTIONS['args']:
        chrome_options.add_argument(arg)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        TestHelpers.log('🚀 Starting test...')
        driver.implicitly_wait(TIMEOUTS['implicit'])
        driver.set_page_load_timeout(TIMEOUTS['page_load'])
        driver.maximize_window()

        # Test steps here
        
        TestHelpers.log('✅ Test completed!')
    except Exception as error:
        TestHelpers.log_error(error)
        TestHelpers.take_screenshot(driver, 'error-state')
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    try:
        my_test()
        sys.exit(0)
    except Exception:
        sys.exit(1)
```

---

## ✅ DO's

### Setup
- ✅ Use `webdriver-manager` for ChromeDriver
- ✅ Use `CHROME_OPTIONS` from config
- ✅ Set all timeouts from config
- ✅ Maximize window
- ✅ Use try-except-finally

### Element Location
- ✅ Prefer ID selectors
- ✅ Use `TestHelpers.wait_for_element()`
- ✅ Use explicit waits (WebDriverWait)
- ✅ Handle optional elements with try-except

### Code Quality
- ✅ Use TEST_CONFIG for all data
- ✅ Log all major steps
- ✅ Take screenshots at key points
- ✅ Use descriptive variable names
- ✅ Add clear section headers

### Error Handling
- ✅ Use specific exceptions
- ✅ Log errors with TestHelpers.log_error()
- ✅ Take screenshot on failure
- ✅ Always cleanup in finally block

---

## ❌ DON'Ts

### Setup
- ❌ Hardcoded paths (`chromedriver.exe`)
- ❌ No error handling
- ❌ No cleanup (driver.quit())
- ❌ Global driver variables

### Waits
- ❌ Excessive `time.sleep()` (use explicit waits)
- ❌ No waits at all
- ❌ Long hardcoded sleeps (>2 seconds)

### Selectors
- ❌ Fragile XPath with indices
- ❌ Complex XPath expressions
- ❌ No wait before finding element

### Code Quality
- ❌ Hardcoded URLs, credentials, data
- ❌ No logging or screenshots
- ❌ Magic numbers
- ❌ Commented-out code blocks
- ❌ No docstrings

### Testing
- ❌ Manual intervention (CAPTCHA, input())
- ❌ Tests depending on each other
- ❌ Using real user accounts
- ❌ No assertions

---

## 🔧 Common Patterns

### Navigate and Wait
```python
driver.get(TEST_CONFIG['base_url'])
TestHelpers.wait_for_page_load(driver)
TestHelpers.take_screenshot(driver, '01-page-loaded')
```

### Find and Click
```python
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'submit'))
)
button.click()
```

### Fill Form Field
```python
email_input = driver.find_element(By.ID, 'email')
email_input.clear()
email_input.send_keys(TEST_CONFIG['credentials']['email'])
```

### Handle Optional Popup
```python
try:
    popup = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.popup-close'))
    )
    popup.click()
    TestHelpers.log('✅ Closed popup')
except (NoSuchElementException, TimeoutException):
    TestHelpers.log('⚠️  No popup found')
```

### Multiple Click Strategies
```python
# Method 1: jQuery trigger (best for jQuery sites)
try:
    driver.execute_script("jQuery('.button').trigger('click');")
except Exception:
    # Method 2: Regular click
    try:
        button.click()
    except Exception:
        # Method 3: JavaScript click
        driver.execute_script('arguments[0].click();', button)
```

### Verify Result
```python
# Wait for success message
try:
    success_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.success'))
    )
    TestHelpers.log(f'✅ SUCCESS: {success_msg.text}')
except TimeoutException:
    TestHelpers.log('❌ Success message not found')
    raise AssertionError('Expected success message')
```

---

## 🎯 Selector Priority

1. **ID** - `By.ID, 'submit-button'` ⭐ Best
2. **data-testid** - `By.CSS_SELECTOR, '[data-testid="submit"]'` ⭐ Great
3. **CSS class** - `By.CSS_SELECTOR, '.submit-btn'` ✅ Good
4. **CSS selector** - `By.CSS_SELECTOR, 'button[type="submit"]'` ✅ OK
5. **XPath** - `By.XPATH, "//button[@type='submit']"` ⚠️ Last resort

❌ **Never**: `/html/body/div[3]/form/button[2]`

---

## 📸 Screenshots

```python
# At each major step
TestHelpers.take_screenshot(driver, '01-homepage')
TestHelpers.take_screenshot(driver, '02-login-form')
TestHelpers.take_screenshot(driver, '03-dashboard')

# On error (in except block)
TestHelpers.take_screenshot(driver, 'error-state')
```

---

## 📝 Logging

```python
# Major steps
TestHelpers.log('📍 Step 1: Navigating to login page...')
TestHelpers.log('✅ Login successful!')
TestHelpers.log('❌ Login failed!')
TestHelpers.log('⚠️  Warning: Popup not found')

# Errors
TestHelpers.log_error(error)
```

---

## ⏱️ Timeouts

```python
# From config
driver.implicitly_wait(TIMEOUTS['implicit'])      # 10s
driver.set_page_load_timeout(TIMEOUTS['page_load'])  # 30s

# Explicit waits
WebDriverWait(driver, 10).until(...)  # Standard
WebDriverWait(driver, 20).until(...)  # Slow operation
WebDriverWait(driver, 5).until(...)   # Quick check
```

---

## 🧪 TestHelpers Methods

```python
# Wait for element
element = TestHelpers.wait_for_element(driver, (By.ID, 'button'))

# Wait and click
TestHelpers.wait_and_click(driver, (By.ID, 'submit'))

# Wait and type
TestHelpers.wait_and_send_keys(driver, (By.ID, 'email'), 'test@example.com')

# Screenshot
TestHelpers.take_screenshot(driver, 'step-name')

# Wait for page load
TestHelpers.wait_for_page_load(driver)

# Scroll to element
TestHelpers.scroll_to_element(driver, element)

# Logging
TestHelpers.log('Message')
TestHelpers.log_error(error)
```

---

## 🔍 Debugging Tips

```python
# Print current URL
print(f"Current URL: {driver.current_url}")

# Print page title
print(f"Page title: {driver.title}")

# Check element properties
print(f"Visible: {element.is_displayed()}")
print(f"Enabled: {element.is_enabled()}")
print(f"Text: {element.text}")

# Browser console logs
logs = driver.get_log('browser')
for entry in logs:
    print(f"{entry['level']}: {entry['message']}")

# Pause execution
input("Press Enter to continue...")
```

---

## 📋 Review Checklist

Before submitting PR, verify:

- [ ] Follows template structure
- [ ] Module docstring with flow
- [ ] TEST_CONFIG for all data
- [ ] Uses webdriver-manager
- [ ] Uses config file (TIMEOUTS, CHROME_OPTIONS)
- [ ] try-except-finally structure
- [ ] Logging at major steps
- [ ] Screenshots at key points
- [ ] Stable selectors (no fragile XPath)
- [ ] Explicit waits (minimal time.sleep)
- [ ] Error handling with screenshots
- [ ] No hardcoded values
- [ ] No commented-out code
- [ ] No manual intervention
- [ ] Proper cleanup (driver.quit())

---

## 🚨 Common Mistakes

### 1. Hardcoded ChromeDriver Path
```python
❌ service = Service(executable_path='chromedriver.exe')
✅ service = Service(ChromeDriverManager().install())
```

### 2. Excessive time.sleep()
```python
❌ time.sleep(10)
✅ WebDriverWait(driver, 10).until(EC.element_to_be_clickable(...))
```

### 3. No Error Handling
```python
❌ driver.find_element(By.ID, 'button').click()
✅ try:
    button = WebDriverWait(driver, 10).until(...)
    button.click()
except TimeoutException:
    TestHelpers.log_error(...)
```

### 4. Hardcoded Values
```python
❌ driver.get('https://example.com')
✅ driver.get(TEST_CONFIG['base_url'])
```

### 5. No Cleanup
```python
❌ driver = webdriver.Chrome()
   # test steps
   # No driver.quit()

✅ try:
    # test steps
finally:
    driver.quit()
```

---

## 📚 Resources

- **Full Guide**: `CODE_STYLE_GUIDE.md`
- **Documentation**: `DOCUMENTATION.md`
- **Example Tests**: `tests/client_portal/support_ticket_test.py`
- **Helpers**: `utils/helpers.py`
- **Config**: `config/config.py`

---

## 💡 Remember

1. **Clean code** is maintainable code
2. **Explicit waits** over time.sleep()
3. **Log everything** important
4. **Screenshot** at key points
5. **Handle errors** gracefully
6. **Use helpers** - don't reinvent
7. **Test independently** - no dependencies
8. **No manual intervention** - fully automated

---

**Questions?** See `CODE_STYLE_GUIDE.md` or ask the team!

