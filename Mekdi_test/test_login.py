import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_continue(driver):
    driver.get("https://oh-clientportal-dev.powerappsportals.com/?preview=yes")
    driver.find_element(By.CLASS_NAME, "b2c-popup-continue").click()
    time.sleep(2)

def test_login_best_case(driver):
    driver.get("https://oh-clientportal-dev.powerappsportals.com/?preview=yes")
    driver.find_element(By.CLASS_NAME, "b2c-popup-continue").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='iy7u2']/a[1]/div").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "b2c-popup-continue").click()
    time.sleep(2)
    driver.find_element(By.ID, "signInName").send_keys("mekides332@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("Password@123")
    time.sleep(2)
    driver.find_element(By.ID, "next").click()
    time.sleep(5)
    message = driver.find_element(By.XPATH, "//*[@id='screen-welcome']/div/div/div/div/div[1]/h1/span[1]").text
    assert 'Welcome to' in message

def test_login_invalid_email(driver):
    driver.get("https://oh-clientportal-dev.powerappsportals.com/?preview=yes")
    driver.find_element(By.CLASS_NAME, "b2c-popup-continue").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='iy7u2']/a[1]/div").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "b2c-popup-continue").click()
    time.sleep(2)
    driver.find_element(By.ID, "signInName").send_keys("mekides333@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("Password@123")
    time.sleep(2)
    driver.find_element(By.ID, "next").click()
    time.sleep(5)
    message = driver.find_element(By.XPATH, "//*[@id='localAccountForm']/div[2]/p").text
    assert "We can't seem to find your account." in message

def test_login_invalid_password(driver):
    driver.get("https://oh-clientportal-dev.powerappsportals.com/?preview=yes")
    driver.find_element(By.CLASS_NAME, "b2c-popup-continue").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='iy7u2']/a[1]/div").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "b2c-popup-continue").click()
    time.sleep(2)
    driver.find_element(By.ID, "signInName").send_keys("mekides332@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password@123")
    time.sleep(2)
    driver.find_element(By.ID, "next").click()
    time.sleep(5)
    message = driver.find_element(By.XPATH, "//*[@id='localAccountForm']/div[2]/p").text
    assert "Your password is incorrect." in message

def test_login_empty_field(driver):
    driver.get("https://oh-clientportal-dev.powerappsportals.com/?preview=yes")
    driver.find_element(By.CLASS_NAME, "b2c-popup-continue").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='iy7u2']/a[1]/div").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "b2c-popup-continue").click()
    time.sleep(2)
    driver.find_element(By.ID, "next").click()
    time.sleep(3)
    message = driver.find_element(By.XPATH, "//*[@id='localAccountForm']/div[3]/div[1]/div/p").text
    assert "Please enter your Email Address" in message
    message1 = driver.find_element(By.XPATH, "//*[@id='localAccountForm']/div[3]/div[2]/div[2]/p").text
    assert "Please enter your password" in message1
    time.sleep(2)