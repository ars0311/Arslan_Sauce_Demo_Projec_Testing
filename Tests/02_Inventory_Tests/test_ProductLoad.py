from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import os


def test_PageLoading():
    Folder_Path = r"/Tests/01_Inventory_Tests"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    time.sleep(5)

    #Enter username and Password With Elements
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(5)

    #Capture Screenshot of Full Login Before Login
    full_page_Path = Folder_Path + "\\LoginPage.png"
    driver.save_screenshot(full_page_Path)
    time.sleep(3)

    #Click on Login Button
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(5)

    # Capture Screenshot of Product Page Load Successfully
    After_Login = Folder_Path + "\\ProductsPage.png"
    driver.save_screenshot(After_Login)
    time.sleep(5)

    #Move to Bottom Product with using JavaScript Scroll
    Product = driver.find_element(By.PARTIAL_LINK_TEXT, "Test.allTheThings()")
    driver.execute_script("arguments[0].scrollIntoView(true);", Product)
    time.sleep(5)

    # Capture Screenshot of Product Page Load from Bottom Successfully
    Full_Product_Page = Folder_Path + "\\ProductsPageScroll.png"
    driver.save_screenshot(Full_Product_Page)
    time.sleep(5)

    driver.quit()
