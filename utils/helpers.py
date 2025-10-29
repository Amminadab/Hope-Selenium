"""
Helper functions for Selenium tests
"""

import os
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestHelpers:
    """Helper class for common Selenium test operations"""

    @staticmethod
    def wait_for_element(driver, locator, timeout=10):
        """
        Wait for an element to be visible
        
        Args:
            driver: Selenium WebDriver instance
            locator: Tuple of (By, value) for element location
            timeout: Timeout in seconds
            
        Returns:
            WebElement: The found element
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            WebDriverWait(driver, timeout).until(
                EC.visibility_of(element)
            )
            return element
        except TimeoutException:
            print(f"Element not found: {locator}")
            raise

    @staticmethod
    def take_screenshot(driver, filename):
        """
        Take a screenshot
        
        Args:
            driver: Selenium WebDriver instance
            filename: Name for the screenshot file
            
        Returns:
            str: Path to the saved screenshot
        """
        screenshot_dir = os.path.join(os.path.dirname(__file__), '../screenshots')
        
        # Create screenshots directory if it doesn't exist
        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = int(time.time() * 1000)
        filepath = os.path.join(screenshot_dir, f"{filename}_{timestamp}.png")
        
        driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
        return filepath

    @staticmethod
    def wait_for_page_load(driver, timeout=30):
        """
        Wait for page to load completely
        
        Args:
            driver: Selenium WebDriver instance
            timeout: Timeout in seconds
        """
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    @staticmethod
    def scroll_to_element(driver, element):
        """
        Scroll to element
        
        Args:
            driver: Selenium WebDriver instance
            element: WebElement to scroll to
        """
        driver.execute_script('arguments[0].scrollIntoView(true);', element)
        time.sleep(0.5)  # Small delay after scroll

    @staticmethod
    def wait_and_click(driver, locator):
        """
        Wait and click element
        
        Args:
            driver: Selenium WebDriver instance
            locator: Tuple of (By, value) for element location
        """
        element = TestHelpers.wait_for_element(driver, locator)
        TestHelpers.scroll_to_element(driver, element)
        element.click()

    @staticmethod
    def wait_and_send_keys(driver, locator, text):
        """
        Wait and send keys to element
        
        Args:
            driver: Selenium WebDriver instance
            locator: Tuple of (By, value) for element location
            text: Text to send
        """
        element = TestHelpers.wait_for_element(driver, locator)
        TestHelpers.scroll_to_element(driver, element)
        element.clear()
        element.send_keys(text)

    @staticmethod
    def log(message):
        """
        Log test step
        
        Args:
            message: Log message
        """
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] {message}")

    @staticmethod
    def log_error(error):
        """
        Format error for logging
        
        Args:
            error: Exception object
        """
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] ERROR: {str(error)}")
        import traceback
        traceback.print_exc()
