from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import os


def test_ProductName():
    Folder_Path = r"/Tests/01_Inventory_Tests"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    time.sleep(5)

    #Enter username and Password With Elements
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(5)


    #Click on Login Button
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(5)

    # Move to Bottom Product with using JavaScript Scroll
    Product = driver.find_element(By.PARTIAL_LINK_TEXT, "Test.allTheThings()")
    driver.execute_script("arguments[0].scrollIntoView(true);", Product)
    time.sleep(2)

    # Print Product List using for Loop
    products = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name ']")
    print("Product List")
    for product in products:
        print(product.text)

    driver.quit()
