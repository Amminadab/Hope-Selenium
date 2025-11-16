# Selenium Tests - Code Style Guide

**Version**: 1.0 | **Last Updated**: November 16, 2025

---

## Core Principles

1. **Senior Developer Quality** - Clean, maintainable, efficient code
2. **DRY** - Use existing helpers from `utils/helpers.py`
3. **Automation First** - NO manual intervention (CAPTCHA, user input)
4. **Configuration Over Hardcoding** - Use `config/config.py` for all settings
5. **Fail Fast, Fail Clear** - Log everything, screenshot on failures

---

## Mandatory Template

Every test file **MUST** follow this structure:

```python
"""
[Test Name] Test

Brief description and flow:
1. Step 1
2. Step 2
3. Step 3

Author: [Name] | Created: [Date]
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
    'credentials': {'email': 'test@example.com', 'password': 'Pass123'},
    'test_data': {}
}


def my_test():
    """Test function description"""
    
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

        # ============================================================
        # STEP 1: Description
        # ============================================================
        TestHelpers.log('📍 Step 1: Description...')
        driver.get(TEST_CONFIG['base_url'])
        TestHelpers.wait_for_page_load(driver)
        TestHelpers.take_screenshot(driver, '01-step-name')
        
        # More steps...
        
        TestHelpers.log('✅ Test completed!')

    except Exception as error:
        print(f'\n❌ ERROR: {type(error).__name__}: {str(error)}')
        TestHelpers.log_error(error)
        try:
            TestHelpers.take_screenshot(driver, 'error-state')
        except:
            pass
        raise
    finally:
        TestHelpers.log('🔚 Closing browser...')
        driver.quit()


if __name__ == '__main__':
    try:
        my_test()
        print('\n✅ Test passed!')
        sys.exit(0)
    except:
        print('\n❌ Test failed!')
        sys.exit(1)
```

---

## ✅ DO's

### Setup
- ✅ Use `webdriver-manager` (not hardcoded paths)
- ✅ Use `CHROME_OPTIONS` and `TIMEOUTS` from config
- ✅ Maximize window
- ✅ Use try-except-finally

### Element Location
- ✅ Prefer ID selectors: `By.ID, 'submit'`
- ✅ Use explicit waits: `WebDriverWait(driver, 10).until(...)`
- ✅ Use TestHelpers: `TestHelpers.wait_and_click(driver, (By.ID, 'button'))`

### Code Quality
- ✅ Store all data in TEST_CONFIG
- ✅ Log major steps: `TestHelpers.log('Step description...')`
- ✅ Take screenshots: `TestHelpers.take_screenshot(driver, 'step-name')`
- ✅ Descriptive variable names: `submit_button`, `email_input`
- ✅ Clear section headers with `# ========`

### Error Handling
- ✅ Use specific exceptions: `except (NoSuchElementException, TimeoutException):`
- ✅ Log errors: `TestHelpers.log_error(error)`
- ✅ Screenshot on failure
- ✅ Always cleanup in finally block

---

## ❌ DON'Ts

- ❌ Hardcoded paths: `chromedriver.exe`
- ❌ Hardcoded values: URLs, credentials, timeouts
- ❌ Excessive `time.sleep()` (use explicit waits)
- ❌ Fragile XPath: `/html/body/div[3]/form/button[2]`
- ❌ No error handling or cleanup
- ❌ No logging or screenshots
- ❌ Commented-out code blocks
- ❌ Manual intervention (CAPTCHA, `input()`)
- ❌ Tests depending on each other
- ❌ Generic variable names: `e`, `btn`, `element`

---

## Common Patterns

### Navigate and Wait
```python
driver.get(TEST_CONFIG['base_url'])
TestHelpers.wait_for_page_load(driver)
TestHelpers.take_screenshot(driver, '01-page')
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
# Method 1: jQuery (best for jQuery sites)
try:
    driver.execute_script("jQuery('.button').trigger('click');")
except:
    # Method 2: Regular click
    try:
        button.click()
    except:
        # Method 3: JavaScript click
        driver.execute_script('arguments[0].click();', button)
```

---

## Selector Priority

1. **ID** - `By.ID, 'submit-button'` ⭐ Best
2. **data-testid** - `By.CSS_SELECTOR, '[data-testid="submit"]'` ⭐ Great
3. **CSS class** - `By.CSS_SELECTOR, '.submit-btn'` ✅ Good
4. **CSS selector** - `By.CSS_SELECTOR, 'button[type="submit"]'` ✅ OK
5. **XPath** - `By.XPATH, "//button[@type='submit']"` ⚠️ Last resort

❌ **Never use**: `/html/body/div[3]/form/button[2]`

---

## Review Checklist

Before submitting PR:

- [ ] Follows template structure
- [ ] Module docstring with flow
- [ ] TEST_CONFIG for all data
- [ ] Uses `webdriver-manager`
- [ ] Uses config (TIMEOUTS, CHROME_OPTIONS)
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

## Common Mistakes

### 1. Hardcoded ChromeDriver
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

## Enforcement

**All code MUST comply before merge.**

Code reviews check:
1. Follows template
2. Uses helpers and config
3. No hardcoded values
4. Proper error handling
5. Adequate logging/screenshots
6. No manual intervention
7. Passes checklist

**Non-compliance = PR rejected**

---

## Resources

- **Full Documentation**: `DOCUMENTATION.md`
- **Quick Reference**: `QUICK_REFERENCE.md`
- **Example Tests**: `tests/client_portal/support_ticket_test.py`
- **Helpers**: `utils/helpers.py`
- **Config**: `config/config.py`

---

**Remember**: Clean code is maintainable code. Write code your future self will thank you for! ✅

