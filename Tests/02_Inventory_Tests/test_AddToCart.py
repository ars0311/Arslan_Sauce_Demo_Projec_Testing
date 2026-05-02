from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import os


def test_AddToCart():
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

    #Click on Add To Cart Using For Loop
    Add_Carts = driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory ']")
    for cart in Add_Carts:
        cart.click()
        time.sleep(5)

    # Add to Cart Page Screenshot
    Add_To_Cart = Folder_Path + "\\AddToCartWork.png"
    driver.save_screenshot(Add_To_Cart)
    time.sleep(5)

    # Move to Bottom Product with using JavaScript Scroll
    Product = driver.find_element(By.PARTIAL_LINK_TEXT, "Test.allTheThings()")
    driver.execute_script("arguments[0].scrollIntoView(true);", Product)
    time.sleep(3)

    # Move to Top From Bottom Product with using JavaScript Scroll
    Products = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
    driver.execute_script("arguments[0].scrollIntoView(true);", Products)
    time.sleep(3)

    driver.quit()
