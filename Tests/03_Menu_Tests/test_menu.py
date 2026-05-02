from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    time.sleep(5)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(5)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    return driver



class TestMenu:

    def test_about_redirect(self, driver, login):
        Folder_Path = r"J:\desktop\Desktop\Arslan_Sauce_Demo_Projec_Testing\Tests\03_Menu_Tests"
        current_window = driver.current_window_handle
        # Click Menu
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(5)

        menu_click = Folder_Path + "\\Menu_Click.png"
        driver.save_screenshot(menu_click)
        time.sleep(5)

        # Click About
        driver.find_element(By.ID, "about_sidebar_link").click()
        time.sleep(5)

        about_click = Folder_Path + "\\About_Click.png"
        driver.save_screenshot(about_click)
        time.sleep(5)

        driver.find_element(By.LINK_TEXT, "Sign up for free").click()
        time.sleep(5)

        External_click = Folder_Path + "\\External_Click.png"
        driver.save_screenshot(External_click)
        time.sleep(5)

        driver.switch_to.window(current_window)
        time.sleep(5)

        driver.find_element(By.LINK_TEXT, "Book a demo").click()
        time.sleep(5)

        driver.switch_to.window(current_window)
        driver.back()
        time.sleep(5)




    def test_logout(self, driver, login):
        Folder_Path = r"J:\desktop\Desktop\Arslan_Sauce_Demo_Projec_Testing\Tests\03_Menu_Tests"

        # Open menu
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(5)

        # Logout
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(5)

        Logout_click = Folder_Path + "\\Logout_Click.png"
        driver.save_screenshot(Logout_click)
        time.sleep(5)