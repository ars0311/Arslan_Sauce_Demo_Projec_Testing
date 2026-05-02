from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import os


def test_Login():
    Folder_Path = r"/Tests/Login1_Tests"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    time.sleep(5)

    #Enter Invalid username and Password With Elements for Test Invalid Credentials
    driver.find_element(By.ID, "user-name").send_keys("Arslan")
    driver.find_element(By.ID, "password").send_keys("Arslan")
    time.sleep(5)

    #Click on Login Button
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(5)

    # Capture Screenshot of Login Page Error After Invalid Credentials
    After_Login = Folder_Path + "\\AfterLoginInvalidError.png"
    driver.save_screenshot(After_Login)

    time.sleep(5)
    driver.quit()
