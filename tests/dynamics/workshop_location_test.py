"""
Workshop Location Creation Test (Dynamics 365)
Tests the complete flow: Login -> Select App -> Create Building Record

Flow:
1. Navigate to Dynamics login page
2. Enter email and click Next
3. Enter password and click Sign in
4. Check "Don't show this again" and click Yes
5. Wait for app selection page
6. Click HOPE Coach app
7. Handle debugger popup (click play)
8. Click Workshop Location sidebar
9. Click New button
10. Fill mandatory fields (Name)
11. Click Save & Close
12. Verify redirect to list view
"""

import sys
import os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

from config.config import BROWSER, TIMEOUTS, CHROME_OPTIONS
from utils.helpers import TestHelpers


# Test configuration
TEST_CONFIG = {
    'base_url': 'https://oh-dev.crm.dynamics.com/main.aspx',
    'credentials': {
        'email': 'hopecoacha@operationhope.org',
        'password': 'A%e&T$N#@hcc'
    },
    'app_url': 'https://oh-dev.crm.dynamics.com/main.aspx?appid=bbe8d0d8-7b2c-ef11-840a-000d3a125a79',
    'building': {
        'name': f'Test Building {int(time.time())}',  # Unique name with timestamp
        'estimated_capacity': '100',
        'cost': '5000',
        'description': 'Automated test building created by Selenium'
    },
    'expected_redirect': {
        'from': 'pagetype=entityrecord&etn=msevtmgt_building',
        'to': 'pagetype=entitylist&etn=msevtmgt_building'
    }
}


def workshop_location_test():
    """Main test function"""
    
    # Create Chrome options
    chrome_options = Options()
    for arg in CHROME_OPTIONS['args']:
        chrome_options.add_argument(arg)
    
    # Enable browser logging
    chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    # Create WebDriver instance
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        TestHelpers.log('🚀 Starting Workshop Location Creation Test (Dynamics 365)...')

        # Set timeouts
        driver.implicitly_wait(TIMEOUTS['implicit'])
        driver.set_page_load_timeout(TIMEOUTS['page_load'])
        driver.set_script_timeout(TIMEOUTS['script'])

        # Maximize window for better visibility
        driver.maximize_window()

        # ============================================================
        # STEP 1: Navigate to Dynamics login page
        # ============================================================
        TestHelpers.log('📍 Step 1: Navigating to Dynamics login page...')
        driver.get(TEST_CONFIG['base_url'])
        TestHelpers.wait_for_page_load(driver)
        time.sleep(2)
        TestHelpers.take_screenshot(driver, '01-login-page')

        # ============================================================
        # STEP 2: Enter email and click Next
        # ============================================================
        TestHelpers.log('📧 Step 2: Entering email...')
        
        email_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, 'loginfmt'))
        )
        email_input.clear()
        email_input.send_keys(TEST_CONFIG['credentials']['email'])
        TestHelpers.log(f"✅ Entered email: {TEST_CONFIG['credentials']['email']}")
        
        time.sleep(1)
        TestHelpers.take_screenshot(driver, '02-email-entered')
        
        # Click Next button
        next_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, 'idSIButton9'))
        )
        next_button.click()
        TestHelpers.log('✅ Clicked Next button')
        
        time.sleep(3)
        TestHelpers.take_screenshot(driver, '03-after-next')

        # ============================================================
        # STEP 3: Enter password and click Sign in
        # ============================================================
        TestHelpers.log('🔒 Step 3: Entering password...')
        
        password_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, 'passwd'))
        )
        password_input.clear()
        password_input.send_keys(TEST_CONFIG['credentials']['password'])
        TestHelpers.log('✅ Entered password')
        
        time.sleep(1)
        TestHelpers.take_screenshot(driver, '04-password-entered')
        
        # Click Sign in button
        signin_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, 'idSIButton9'))
        )
        signin_button.click()
        TestHelpers.log('✅ Clicked Sign in button')
        
        time.sleep(3)
        TestHelpers.take_screenshot(driver, '05-after-signin')

        # ============================================================
        # STEP 4: Check "Don't show this again" and click Yes
        # ============================================================
        TestHelpers.log('✅ Step 4: Handling "Stay signed in" prompt...')
        
        try:
            # Check the "Don't show this again" checkbox
            kmsi_checkbox = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'KmsiCheckboxField'))
            )
            if not kmsi_checkbox.is_selected():
                kmsi_checkbox.click()
                TestHelpers.log('✅ Checked "Don\'t show this again"')
            
            time.sleep(1)
            TestHelpers.take_screenshot(driver, '06-checkbox-checked')
            
            # Click Yes button
            yes_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.ID, 'idSIButton9'))
            )
            yes_button.click()
            TestHelpers.log('✅ Clicked Yes button')
            
        except (NoSuchElementException, TimeoutException):
            TestHelpers.log('⚠️  "Stay signed in" prompt not found, continuing...')
        
        time.sleep(10)  # Wait for heavy loading
        TestHelpers.take_screenshot(driver, '07-after-stay-signed-in')
        
        # Log current URL to debug
        current_url = driver.current_url
        TestHelpers.log(f'Current URL after sign-in: {current_url}')

        # ============================================================
        # STEP 5: Navigate to HOPE Coach app
        # ============================================================
        TestHelpers.log('📱 Step 5: Navigating to HOPE Coach app...')
        time.sleep(5)
        
        TestHelpers.take_screenshot(driver, '08-before-app-navigation')
        
        # Try to click the app tile, if not found, navigate directly
        try:
            TestHelpers.log('🔍 Looking for HOPE Coach app tile...')
            hope_coach_link = driver.find_element(By.ID, 'AppModuleTileSec_1_Item_1')
            hope_coach_link.click()
            TestHelpers.log('✅ Clicked HOPE Coach app tile')
        except NoSuchElementException:
            TestHelpers.log('⚠️  App tile not found, navigating directly to app URL...')
            driver.get(TEST_CONFIG['app_url'])
            TestHelpers.log('✅ Navigated directly to HOPE Coach app')
        
        time.sleep(15)  # Wait for app to load (heavy loading)
        TestHelpers.take_screenshot(driver, '09-hope-coach-loading')

        # ============================================================
        # STEP 6: Handle debugger popup (click play)
        # ============================================================
        TestHelpers.log('⏯️  Step 6: Handling debugger popup...')
        time.sleep(5)
        
        try:
            # Look for play button or skip button with multiple attempts
            play_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Play') or contains(text(), 'Skip') or contains(@aria-label, 'Play') or contains(@aria-label, 'Skip')]"))
            )
            play_button.click()
            TestHelpers.log('✅ Clicked Play/Skip button')
            time.sleep(2)
        except (NoSuchElementException, TimeoutException):
            TestHelpers.log('⚠️  Play button not found, continuing...')
        
        time.sleep(5)
        TestHelpers.take_screenshot(driver, '10-after-debugger')

        # ============================================================
        # STEP 7: Click Workshop Location sidebar
        # ============================================================
        TestHelpers.log('🏢 Step 7: Clicking Workshop Location sidebar...')
        
        # Wait for the sidebar to be loaded (increased timeout)
        workshop_location_sidebar = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Workshop Location')]"))
        )
        
        TestHelpers.log('✅ Found Workshop Location in sidebar')
        
        # Scroll to element and click
        TestHelpers.scroll_to_element(driver, workshop_location_sidebar)
        time.sleep(3)
        
        # Try clicking the parent div
        try:
            workshop_location_div = workshop_location_sidebar.find_element(By.XPATH, "./ancestor::div[@role='presentation'][1]")
            workshop_location_div.click()
            TestHelpers.log('✅ Clicked Workshop Location sidebar')
        except:
            # Fallback to clicking the span directly
            try:
                workshop_location_sidebar.click()
                TestHelpers.log('✅ Clicked Workshop Location sidebar (fallback)')
            except:
                # Try JavaScript click
                driver.execute_script('arguments[0].click();', workshop_location_sidebar)
                TestHelpers.log('✅ Clicked Workshop Location sidebar (JS)')
        
        time.sleep(10)  # Wait for Workshop Location view to load (increased from 5 to 10 seconds)
        TestHelpers.take_screenshot(driver, '11-workshop-location-view')

        # ============================================================
        # STEP 8: Click New button
        # ============================================================
        TestHelpers.log('➕ Step 8: Clicking New button...')
        
        # Wait for New button - using aria-label
        new_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='New' and contains(@data-id, 'NewRecord')]"))
        )
        
        new_button.click()
        TestHelpers.log('✅ Clicked New button')
        
        time.sleep(5)  # Wait for form to load
        TestHelpers.take_screenshot(driver, '12-new-building-form')

        # ============================================================
        # STEP 9: Fill mandatory fields
        # ============================================================
        TestHelpers.log('📝 Step 9: Filling building form...')
        
        # Fill Name (mandatory field marked with *)
        name_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Name' and @data-id='msevtmgt_name.fieldControl-text-box-text']"))
        )
        name_input.clear()
        name_input.send_keys(TEST_CONFIG['building']['name'])
        TestHelpers.log(f"✅ Entered Name: {TEST_CONFIG['building']['name']}")
        
        time.sleep(1)
        TestHelpers.take_screenshot(driver, '13-form-filled')

        # ============================================================
        # STEP 10: Click Save & Close
        # ============================================================
        TestHelpers.log('💾 Step 10: Clicking Save & Close...')
        
        # Wait for Save & Close button
        save_close_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Save & Close']"))
        )
        
        save_close_button.click()
        TestHelpers.log('✅ Clicked Save & Close button')
        
        time.sleep(15)  # Wait for save and redirect (increased from 5 to 15 seconds)
        TestHelpers.take_screenshot(driver, '14-after-save')

        # ============================================================
        # STEP 11: Verify redirect to list view
        # ============================================================
        TestHelpers.log('🔍 Step 11: Verifying redirect...')
        
        # Wait a bit more for redirect to complete
        time.sleep(5)
        
        current_url = driver.current_url
        TestHelpers.log(f"Current URL: {current_url}")
        
        # Check if we redirected from entity record to entity list
        if TEST_CONFIG['expected_redirect']['to'] in current_url:
            TestHelpers.log('✅ SUCCESS: Redirected to list view!')
            TestHelpers.log(f"✅ Building '{TEST_CONFIG['building']['name']}' created successfully!")
            TestHelpers.take_screenshot(driver, '15-success-list-view')
            test_passed = True
        elif TEST_CONFIG['expected_redirect']['from'] in current_url:
            TestHelpers.log('❌ FAIL: Still on entity record page, redirect did not occur')
            TestHelpers.take_screenshot(driver, '15-fail-still-on-form')
            test_passed = False
        else:
            TestHelpers.log(f"⚠️  WARNING: Unexpected URL: {current_url}")
            TestHelpers.take_screenshot(driver, '15-unexpected-url')
            test_passed = False

        # Wait to see final state
        time.sleep(3)

        if test_passed:
            TestHelpers.log('✅ Test completed successfully!')
            return True
        else:
            TestHelpers.log('❌ Test failed!')
            return False

    except Exception as error:
        print('\n❌ ERROR OCCURRED:')
        print(f'Error type: {type(error).__name__}')
        print(f'Error message: {str(error)}')
        
        TestHelpers.log_error(error)
        
        # Take screenshot on error
        try:
            TestHelpers.take_screenshot(driver, 'error-state')
        except Exception as screenshot_error:
            print(f'Failed to take error screenshot: {screenshot_error}')
        
        raise
    finally:
        # Keep browser open for 5 seconds to see final state
        TestHelpers.log('⏰ Waiting 5 seconds before closing browser...')
        time.sleep(5)
        
        # Close the browser
        TestHelpers.log('🔚 Closing browser...')
        driver.quit()


if __name__ == '__main__':
    try:
        result = workshop_location_test()
        if result:
            print('\n✅ Test passed!')
            print('📸 Check the screenshots folder for visual verification.')
            sys.exit(0)
        else:
            print('\n❌ Test failed!')
            print('📸 Check the screenshots folder for error details.')
            sys.exit(1)
    except Exception:
        print('\n❌ Test failed with exception!')
        print('📸 Check the screenshots folder for error details.')
        sys.exit(1)
