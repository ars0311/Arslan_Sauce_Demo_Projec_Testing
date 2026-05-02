from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import os


def test_RemoveCarts():
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

    # Click on Add To Cart Using For Loop
    Add_Carts = driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory ']")
    for cart in Add_Carts:
        cart.click()
        time.sleep(5)

    # Click on Remove Cart
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(5)


    # Add to Cart Page Screenshot
    Remove_Carts = Folder_Path + "\\RemoveCartsWorks.png"
    driver.save_screenshot(Remove_Carts)
    time.sleep(5)


    driver.quit()
