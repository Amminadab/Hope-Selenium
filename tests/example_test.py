"""
Example Selenium Test
This is a template showing how to structure a test
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from config.config import BROWSER, TIMEOUTS, CHROME_OPTIONS
from utils.helpers import TestHelpers


def example_test():
    """Example test function"""
    
    # Create Chrome options
    chrome_options = Options()
    for arg in CHROME_OPTIONS['args']:
        chrome_options.add_argument(arg)

    # Create WebDriver instance
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        TestHelpers.log('Starting example test...')

        # Set timeouts
        driver.implicitly_wait(TIMEOUTS['implicit'])
        driver.set_page_load_timeout(TIMEOUTS['page_load'])
        driver.set_script_timeout(TIMEOUTS['script'])

        # Navigate to a URL
        TestHelpers.log('Navigating to Google...')
        driver.get('https://www.google.com')

        # Wait for page to load
        TestHelpers.wait_for_page_load(driver)

        # Take a screenshot
        TestHelpers.take_screenshot(driver, 'google-homepage')

        # Find search box and search for something
        TestHelpers.log('Finding search box...')
        search_box = TestHelpers.wait_for_element(
            driver,
            (By.NAME, 'q')
        )

        TestHelpers.log('Entering search text...')
        search_box.send_keys('Operation Hope')
        search_box.submit()

        # Wait for results page
        TestHelpers.wait_for_page_load(driver)
        
        TestHelpers.log('Waiting for search results...')
        WebDriverWait(driver, 10).until(
            EC.title_contains('Operation Hope')
        )

        # Take another screenshot
        TestHelpers.take_screenshot(driver, 'search-results')

        TestHelpers.log('Test completed successfully! ✓')

    except Exception as error:
        TestHelpers.log_error(error)
        # Take screenshot on error
        try:
            TestHelpers.take_screenshot(driver, 'error')
        except Exception as screenshot_error:
            print(f'Failed to take error screenshot: {screenshot_error}')
        raise
    finally:
        # Always close the browser
        TestHelpers.log('Closing browser...')
        driver.quit()


if __name__ == '__main__':
    try:
        example_test()
        print('\n✅ All tests passed!')
        sys.exit(0)
    except Exception:
        print('\n❌ Test failed!')
        sys.exit(1)
