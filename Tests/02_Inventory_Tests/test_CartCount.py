from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import os


def test_CartCounts():
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

    # Click on Add To Cart on First Product
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(5)

    Cart_Count = Folder_Path + "\\CartCountOne.png"
    driver.save_screenshot(Cart_Count)
    time.sleep(5)

    # Click on Add To Cart on Second Product
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    time.sleep(5)

    Cart_Counts = Folder_Path + "\\CartCountTwo.png"
    driver.save_screenshot(Cart_Counts)
    time.sleep(5)

    # Click on Remove Cart First Product
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(5)

    Cart_Cnt = Folder_Path + "\\RemoveCartCountThree.png"
    driver.save_screenshot(Cart_Cnt)
    time.sleep(5)

    driver.quit()
