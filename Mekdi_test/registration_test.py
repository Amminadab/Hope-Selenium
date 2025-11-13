from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mailslurp_client import ApiClient, Configuration, InboxControllerApi, WaitForControllerApi
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, os, datetime
import re
import time

service=Service(executable_path='chromedriver.exe')
driver=webdriver.Chrome(service=service)

driver.get("https://oh-clientportals-uat.powerappsportals.com/")
driver.maximize_window()

try:
    continue_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "b2c-popup-continue"))
    )
    continue_btn.click()
except:
    pass

client_dropeDown=driver.find_element(By.CLASS_NAME, 'home-page-chevron')
client_dropeDown.click()
time.sleep(2)

element = driver.find_element(By.CLASS_NAME, "register-btn-client")
element.click()
time.sleep(10)

config = Configuration()
config.api_key["x-api-key"] = "4e46f5230a2a3f2e59ee3a609b09f84d417617fa756471edfd4589efcf0a98f5"

with ApiClient(config) as api_client:
    inbox_api = InboxControllerApi(api_client)
    wait_api = WaitForControllerApi(api_client)
#
#     try:
#         inbox = inbox_api.create_inbox()
#     except mailslurp_client.exceptions.ApiException as e:
#         if e.status == 426:
#             inboxes = inbox_api.get_all_inboxes(page=0, size=1)
#             if inboxes.content:
#                 inbox = inboxes.content[0]
#             else:
#                 inboxes = inbox_api.get_all_inboxes()
#                 for old in inboxes.content:
#                     inbox_api.delete_inbox(old.id)
#                 inbox = inbox_api.create_inbox()
#         else:
#             raise e


    inbox = inbox_api.create_inbox()
    test_email = inbox.email_address
    inbox_id = inbox.id
    print("Test email created:", test_email)

    driver.find_element(By.ID, "email").send_keys(test_email)
    driver.find_element(By.CLASS_NAME, "sendCode").click()
    time.sleep(5)

    email = wait_api.wait_for_latest_email(inbox_id=inbox_id, timeout=30000)
    body = email.body

    match = re.search(r'\b(\d{4,6})\b', body)
    if match:
        otp = match.group(1)
        print("Extracted OTP:", otp)
    else:
        otp = ""
    time.sleep(5)
    if otp:
        verification_input = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "VerificationCode"))
        )
        verification_input.clear()
        verification_input.send_keys(otp)
        time.sleep(2)
        driver.find_element(By.ID, "emailVerificationControl_but_verify_code").click()
        time.sleep(5)
        driver.find_element(By.ID, "continue").click()
        # time.sleep(5)
        # driver.find_element(By.ID, "newPassword").send_keys("Password@123")
        wait = WebDriverWait(driver, 15)

        new_password_input = wait.until(
            EC.presence_of_element_located((By.ID, "newPassword"))
        )
        new_password_input.send_keys("Password@123")

        time.sleep(2)
        driver.find_element(By.ID, "reenterPassword").send_keys("Password@123")
        time.sleep(2)
        driver.find_element(By.ID, "givenName").send_keys("Emma")
        time.sleep(2)
        driver.find_element(By.ID, "surname").send_keys("Noah")
        time.sleep(2)
        driver.find_element(By.ID, "ext_terms_and_conditions_true").click()
        time.sleep(15)

        os.makedirs("screenshots", exist_ok=True)
        captcha_el = driver.find_element(By.ID, "captchaControlChallengeCode-img")
        ts = datetime.datetime.now().strftime("%H%M%S")
        filename = f"screenshots/{ts}_captcha.png"
        captcha_el.screenshot(filename)

        captcha_text = input("Enter CAPTCHA text: ").strip()
        driver.find_element(By.ID, "captchaControlChallengeCode").send_keys(captcha_text)
        time.sleep(5)
        driver.find_element(By.ID, "continue").click()

        time.sleep(30)


