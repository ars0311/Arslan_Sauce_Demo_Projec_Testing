from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest
import os


def test_Sorting():
    Folder_Path = r"/Tests/01_Inventory_Tests"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    time.sleep(5)

    # Enter username and Password With Elements
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(5)

    # Click on Login Button
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(5)

    #Select Element of Class of Dropdown Using Select Method
    Dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))

    Dropdown.select_by_index(0)
    time.sleep(5)

    Dropdown.select_by_index(1)
    time.sleep(5)

    dropDown_one = Folder_Path + "\\Dropdown_one.png"
    driver.save_screenshot(dropDown_one)
    time.sleep(5)

    #Select Element of Dropdown Class Using XPATH Due To Stale error Using Select Method
    DropsDown = Select(driver.find_element(By.XPATH, "//select[@class = 'product_sort_container']"))
    DropsDown.select_by_visible_text("Price (low to high)")
    time.sleep(5)

    dropDown_Two = Folder_Path + "\\Dropdown_Two.png"
    driver.save_screenshot(dropDown_Two)
    time.sleep(5)

    DropDowns = Select(driver.find_element(By.XPATH, "//select[@class = 'product_sort_container']"))
    DropDowns.select_by_visible_text("Price (high to low)")
    time.sleep(5)

    DropDown_Three = Folder_Path + "\\Dropdown_Three.png"
    driver.save_screenshot(DropDown_Three)
    time.sleep(5)

    driver.quit()