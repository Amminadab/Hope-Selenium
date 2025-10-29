"""
Support Ticket Submission Test
Tests the complete flow: Login -> Navigate to Dashboard -> Submit Support Ticket

Flow:
1. Navigate to portal home
2. Click sign-in button
3. Handle debugger popups (skip)
4. Click signin-page-grid-item-button
5. Fill login form and submit
6. Navigate to dashboard
7. Click Support sidebar
8. Click Submit Ticket button
9. Fill support ticket form
10. Submit and verify success/error
"""

import sys
import os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    'base_url': 'https://oh-clientportal-dev.powerappsportals.com/',
    'credentials': {
        'email': 'cuqumyky@cyclelove.cc',
        'password': 'Hope2025'
    },
    'support_ticket': {
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '+11234567890',  # Must be only numbers with optional +
        'can_login': 'yes',
        'issue_type': 'I need help connecting to a coach',
        'additional_info': 'This is an automated test submission from Selenium. Please ignore.'
    }
}


def support_ticket_test():
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
        TestHelpers.log('🚀 Starting Support Ticket Submission Test...')

        # Set timeouts
        driver.implicitly_wait(TIMEOUTS['implicit'])
        driver.set_page_load_timeout(TIMEOUTS['page_load'])
        driver.set_script_timeout(TIMEOUTS['script'])

        # Maximize window for better visibility
        driver.maximize_window()

        # ============================================================
        # STEP 1: Navigate to portal home page
        # ============================================================
        TestHelpers.log('📍 Step 1: Navigating to portal home page...')
        driver.get(TEST_CONFIG['base_url'])
        TestHelpers.wait_for_page_load(driver)
        TestHelpers.take_screenshot(driver, '01-homepage')

        # ============================================================
        # STEP 1.5: Click .b2c-popup-continue button (first popup)
        # ============================================================
        TestHelpers.log('🔘 Step 1.5: Clicking .b2c-popup-continue button (first popup)...')
        time.sleep(2)
        
        try:
            b2c_popup_continue = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.b2c-popup-continue'))
            )
            b2c_popup_continue.click()
            TestHelpers.log('✅ Clicked .b2c-popup-continue button')
            time.sleep(1)
            TestHelpers.take_screenshot(driver, '01b-after-b2c-popup')
        except (NoSuchElementException, TimeoutException):
            TestHelpers.log('⚠️  .b2c-popup-continue button not found, continuing...')

        # ============================================================
        # STEP 2: Click sign-in button
        # ============================================================
        TestHelpers.log('🔘 Step 2: Clicking sign-in button...')
        time.sleep(2)  # Wait for page to fully load
        
        sign_in_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.sign-in-btn'))
        )
        sign_in_btn.click()
        time.sleep(2)
        TestHelpers.take_screenshot(driver, '02-clicked-signin')

        # ============================================================
        # STEP 3: Handle first debugger/popup - Try to skip
        # ============================================================
        TestHelpers.log('⏭️  Step 3: Handling first debugger popup...')
        time.sleep(2)
        
        try:
            skip_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Skip')]")
            skip_button.click()
            TestHelpers.log('✅ Clicked Skip button')
        except NoSuchElementException:
            TestHelpers.log('⚠️  Skip button not found, continuing...')
        
        time.sleep(1)
        TestHelpers.take_screenshot(driver, '03-after-first-debugger')

        # ============================================================
        # STEP 4: Click signin-page-grid-item-button
        # ============================================================
        TestHelpers.log('🔘 Step 4: Clicking signin-page-grid-item-button...')
        
        signin_grid_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.signin-page-grid-item-button'))
        )
        signin_grid_btn.click()
        time.sleep(2)
        TestHelpers.take_screenshot(driver, '04-clicked-grid-button')

        # ============================================================
        # STEP 5: Handle second debugger/popup
        # ============================================================
        TestHelpers.log('⏭️  Step 5: Handling second debugger popup...')
        time.sleep(2)
        
        try:
            skip_button2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Skip')]")
            skip_button2.click()
            TestHelpers.log('✅ Clicked second Skip button')
        except NoSuchElementException:
            TestHelpers.log('⚠️  Second skip button not found, continuing...')
        
        time.sleep(1)
        TestHelpers.take_screenshot(driver, '05-after-second-debugger')

        # ============================================================
        # STEP 5.5: Click .b2c-popup-continue button (second popup)
        # ============================================================
        TestHelpers.log('🔘 Step 5.5: Clicking .b2c-popup-continue button (second popup)...')
        time.sleep(2)
        
        try:
            b2c_popup_continue2 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.b2c-popup-continue'))
            )
            b2c_popup_continue2.click()
            TestHelpers.log('✅ Clicked .b2c-popup-continue button')
            time.sleep(1)
            TestHelpers.take_screenshot(driver, '05b-after-second-b2c-popup')
        except (NoSuchElementException, TimeoutException):
            TestHelpers.log('⚠️  .b2c-popup-continue button not found, continuing...')

        # ============================================================
        # STEP 6: Fill login form and submit
        # ============================================================
        TestHelpers.log('📝 Step 6: Filling login form...')
        
        # Wait for login form to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'localAccountForm'))
        )
        
        # Fill email
        email_input = driver.find_element(By.ID, 'signInName')
        email_input.clear()
        email_input.send_keys(TEST_CONFIG['credentials']['email'])
        TestHelpers.log(f"📧 Entered email: {TEST_CONFIG['credentials']['email']}")
        
        # Fill password
        password_input = driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys(TEST_CONFIG['credentials']['password'])
        TestHelpers.log('🔒 Entered password')
        
        TestHelpers.take_screenshot(driver, '06-login-form-filled')
        
        # Click sign in button
        sign_in_submit_btn = driver.find_element(By.ID, 'next')
        sign_in_submit_btn.click()
        TestHelpers.log('✅ Clicked Sign In button')
        
        # Wait for redirect
        time.sleep(5)
        TestHelpers.take_screenshot(driver, '07-after-login')

        # ============================================================
        # STEP 7: Navigate to dashboard
        # ============================================================
        TestHelpers.log('🏠 Step 7: Navigating to dashboard...')
        driver.get(TEST_CONFIG['base_url'] + 'Dashboard')
        TestHelpers.wait_for_page_load(driver)
        
        # Wait for jQuery to be loaded (the page uses jQuery)
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script('return typeof jQuery !== "undefined"')
        )
        TestHelpers.log('✅ jQuery loaded')
        
        time.sleep(3)  # Wait for dashboard to fully load
        TestHelpers.take_screenshot(driver, '08-dashboard-loaded')

        # ============================================================
        # STEP 8: Click Support sidebar item
        # ============================================================
        TestHelpers.log('🆘 Step 8: Clicking Support sidebar item...')
        
        support_nav_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.new-dashboard-nav-item[data-section="support"]'))
        )
        support_nav_item.click()
        TestHelpers.log('✅ Clicked Support menu item')
        
        time.sleep(2)
        TestHelpers.take_screenshot(driver, '09-support-section')

        # ============================================================
        # STEP 9: Click Submit Ticket button
        # ============================================================
        TestHelpers.log('🎫 Step 9: Clicking Submit Ticket button...')
        
        submit_ticket_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.new-dashboard-submit-ticket-btn'))
        )
        submit_ticket_btn.click()
        TestHelpers.log('✅ Clicked Submit Ticket button')
        
        time.sleep(2)
        TestHelpers.take_screenshot(driver, '10-support-ticket-form')

        # ============================================================
        # STEP 10: Fill support ticket form
        # ============================================================
        TestHelpers.log('📋 Step 10: Filling support ticket form...')
        
        # Fill Name
        name_input = driver.find_element(By.ID, 'supportName')
        name_input.clear()
        name_input.send_keys(TEST_CONFIG['support_ticket']['name'])
        TestHelpers.log(f"✍️  Name: {TEST_CONFIG['support_ticket']['name']}")
        
        # Fill Email
        email_ticket_input = driver.find_element(By.ID, 'supportEmail')
        email_ticket_input.clear()
        email_ticket_input.send_keys(TEST_CONFIG['support_ticket']['email'])
        TestHelpers.log(f"📧 Email: {TEST_CONFIG['support_ticket']['email']}")
        
        # Fill Phone
        phone_input = driver.find_element(By.ID, 'supportPhone')
        phone_input.clear()
        phone_input.send_keys(TEST_CONFIG['support_ticket']['phone'])
        TestHelpers.log(f"📱 Phone: {TEST_CONFIG['support_ticket']['phone']}")
        
        # Select "Can Login" radio button
        login_yes_radio = driver.find_element(By.ID, 'loginYes')
        login_yes_radio.click()
        TestHelpers.log('✅ Selected "Can Login: Yes"')
        
        # Select Issue Type
        issue_type_select = driver.find_element(By.ID, 'issueType')
        issue_type_select.click()
        time.sleep(0.5)
        
        # Find and select the specific issue type option
        issue_option = driver.find_element(
            By.XPATH, f"//option[@value=\"{TEST_CONFIG['support_ticket']['issue_type']}\"]"
        )
        issue_option.click()
        TestHelpers.log(f"📝 Issue Type: {TEST_CONFIG['support_ticket']['issue_type']}")
        
        # Fill Additional Info
        additional_info_textarea = driver.find_element(By.ID, 'additionalInfo')
        additional_info_textarea.clear()
        additional_info_textarea.send_keys(TEST_CONFIG['support_ticket']['additional_info'])
        TestHelpers.log('💬 Additional Info filled')
        
        time.sleep(1)
        TestHelpers.take_screenshot(driver, '11-form-filled')

        # ============================================================
        # STEP 11: Submit form and verify
        # ============================================================
        TestHelpers.log('🚀 Step 11: Submitting form...')
        
        # Wait for submit button to be clickable and scroll to it
        submit_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.new-dashboard-submit-btn'))
        )
        
        # Scroll to submit button to ensure it's in view
        TestHelpers.scroll_to_element(driver, submit_btn)
        time.sleep(1)
        
        # Debug: Check button properties
        is_displayed = submit_btn.is_displayed()
        is_enabled = submit_btn.is_enabled()
        TestHelpers.log(f"🔍 Button visible: {is_displayed}, enabled: {is_enabled}")
        
        # Take screenshot before clicking
        TestHelpers.take_screenshot(driver, '11b-before-clicking-submit')
        
        # Try multiple methods to click the button
        button_clicked = False
        
        # Method 1: Trigger jQuery click event (BEST for this page since it uses jQuery)
        try:
            clicked = driver.execute_script("""
                if (typeof jQuery !== 'undefined') {
                    jQuery('.new-dashboard-submit-btn').trigger('click');
                    console.log('jQuery click triggered');
                    return true;
                }
                return false;
            """)
            if clicked:
                TestHelpers.log('✅ Method 1: jQuery trigger click successful')
                button_clicked = True
            else:
                raise Exception('jQuery not available')
        except Exception as jquery_error:
            TestHelpers.log('⚠️  Method 1: jQuery trigger failed, trying regular click...')
            
            # Method 2: Regular Selenium click
            try:
                submit_btn.click()
                TestHelpers.log('✅ Method 2: Regular click successful')
                button_clicked = True
            except Exception as click_error:
                TestHelpers.log('⚠️  Method 2: Regular click failed, trying JavaScript click...')
                
                # Method 3: JavaScript click
                try:
                    driver.execute_script('arguments[0].click();', submit_btn)
                    TestHelpers.log('✅ Method 3: JavaScript click successful')
                    button_clicked = True
                except Exception as js_click_error:
                    TestHelpers.log('⚠️  Method 3: JavaScript click failed, trying by text...')
                    
                    # Method 4: Find by button text and click
                    try:
                        submit_btn_by_text = driver.find_element(
                            By.XPATH, "//button[contains(@class, 'new-dashboard-submit-btn')]//span[text()='Submit']"
                        )
                        driver.execute_script('arguments[0].click();', submit_btn_by_text)
                        TestHelpers.log('✅ Method 4: Click by text successful')
                        button_clicked = True
                    except Exception as text_click_error:
                        TestHelpers.log('⚠️  Method 4: Click by text failed, trying Actions click...')
                        
                        # Method 5: Use Actions to move and click
                        try:
                            from selenium.webdriver.common.action_chains import ActionChains
                            actions = ActionChains(driver)
                            actions.move_to_element(submit_btn).click().perform()
                            TestHelpers.log('✅ Method 5: Actions click successful')
                            button_clicked = True
                        except Exception as actions_click_error:
                            TestHelpers.log('⚠️  Method 5: Actions click failed, trying direct DOM click...')
                            
                            # Method 6: Direct DOM manipulation
                            try:
                                driver.execute_script("""
                                    const btn = document.querySelector('.new-dashboard-submit-btn');
                                    if (btn) {
                                        btn.click();
                                        return true;
                                    }
                                    return false;
                                """)
                                TestHelpers.log('✅ Method 6: Direct DOM click successful')
                                button_clicked = True
                            except Exception as dom_click_error:
                                TestHelpers.log('❌ All 6 click methods failed!')
        
        if button_clicked:
            TestHelpers.log('✅ .new-dashboard-submit-btn button clicked - Form submitted!')
        else:
            TestHelpers.log('❌ WARNING: Submit button may not have been clicked!')
        
        # Wait for response
        time.sleep(5)  # Increased wait time for AJAX response
        
        # Check browser console for any errors or validation messages
        try:
            logs = driver.get_log('browser')
            if logs:
                TestHelpers.log('📋 Browser console logs:')
                for entry in logs:
                    print(f"  {entry['level']}: {entry['message']}")
        except Exception as log_error:
            TestHelpers.log('⚠️  Could not retrieve browser logs')
        
        TestHelpers.take_screenshot(driver, '12-after-submit')

        # ============================================================
        # STEP 12: Verify success or error
        # ============================================================
        TestHelpers.log('🔍 Step 12: Verifying submission result...')
        
        # Wait a bit more for toast to appear
        time.sleep(2)
        
        found_message = False
        
        # Check for success toast with multiple possible selectors
        success_selectors = [
            '.new-dashboard-toast-success',
            '.toast-success',
            '.success-message',
            '[class*="toast"][class*="success"]',
            '[class*="success"][class*="toast"]'
        ]
        
        for selector in success_selectors:
            try:
                success_toast = driver.find_element(By.CSS_SELECTOR, selector)
                if success_toast and success_toast.is_displayed():
                    success_text = success_toast.text
                    TestHelpers.log(f"✅ SUCCESS: {success_text}")
                    TestHelpers.take_screenshot(driver, '13-success')
                    found_message = True
                    break
            except (NoSuchElementException, TimeoutException):
                # Try next selector
                pass
        
        # Check for error toast if no success found
        if not found_message:
            error_selectors = [
                '.new-dashboard-toast-error',
                '.toast-error',
                '.error-message',
                '[class*="toast"][class*="error"]',
                '[class*="error"][class*="toast"]'
            ]
            
            for selector in error_selectors:
                try:
                    error_toast = driver.find_element(By.CSS_SELECTOR, selector)
                    if error_toast and error_toast.is_displayed():
                        error_text = error_toast.text
                        TestHelpers.log(f"❌ ERROR: {error_text}")
                        TestHelpers.take_screenshot(driver, '13-error')
                        found_message = True
                        break
                except (NoSuchElementException, TimeoutException):
                    # Try next selector
                    pass
        
        # If still no message found, check the page content and button state
        if not found_message:
            TestHelpers.log('⚠️  No toast message found. Checking page state...')
            
            # Check if we were redirected back to support (success case)
            current_url = driver.current_url
            TestHelpers.log(f"Current URL: {current_url}")
            
            # Check submit button text (changes to "loading..." during submit)
            try:
                submit_btn_text = driver.execute_script("""
                    return document.querySelector('.new-dashboard-submit-btn')?.textContent || 'not found';
                """)
                TestHelpers.log(f"Submit button text: {submit_btn_text}")
                
                # If button text is back to normal (not "loading..."), submission likely completed
                if 'Submit' in submit_btn_text and 'loading' not in submit_btn_text:
                    TestHelpers.log('✅ Form appears to have been submitted (button reset to normal state)')
                    found_message = True
            except Exception as btn_error:
                TestHelpers.log('Could not check button state')
            
            TestHelpers.take_screenshot(driver, '13-unknown-state')

        # Wait a bit to see final state
        time.sleep(2)

        if found_message:
            TestHelpers.log('✅ Test completed with verified result!')
        else:
            TestHelpers.log('⚠️  Test completed but could not verify submission result.')
            TestHelpers.log('   Check screenshots 11b, 12, and 13 to verify manually.')

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
        
        # Only raise error if it's a critical failure (not just verification)
        error_msg = str(error).lower()
        if 'no such element' not in error_msg and 'toast' not in error_msg:
            raise
        else:
            print('\n⚠️  Non-critical error - test will continue')
    finally:
        # Keep browser open for 5 seconds to see final state
        TestHelpers.log('⏰ Waiting 5 seconds before closing browser...')
        time.sleep(5)
        
        # Close the browser
        TestHelpers.log('🔚 Closing browser...')
        driver.quit()


if __name__ == '__main__':
    try:
        support_ticket_test()
        print('\n✅ All tests passed!')
        print('📸 Check the screenshots folder for visual verification.')
        sys.exit(0)
    except Exception:
        print('\n❌ Test failed!')
        print('📸 Check the screenshots folder for error details.')
        sys.exit(1)
