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



class TestCheckout:

    def test_add_to_cart(self, driver, login):
        Folder_Path = r"J:\desktop\Desktop\Arslan_Sauce_Demo_Projec_Testing\Tests\04_Checkout_Tests"

        #Click on Add To Cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(5)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(5)

        #Click on Cart Icon
        driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()
        time.sleep(5)

        #Capture Screenshot
        product_cart = Folder_Path + "\\Products_Cart.png"
        driver.save_screenshot(product_cart)
        time.sleep(5)



    def test_continue_shopping(self, driver, login):

        Folder_Path = r"J:\desktop\Desktop\Arslan_Sauce_Demo_Projec_Testing\Tests\04_Checkout_Tests"

        # Click on Cart Icon
        driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()
        time.sleep(5)

        #Click on Continue Shopping
        driver.find_element(By.ID, "continue-shopping").click()
        time.sleep(5)

        # Add More Products
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(5)

        Continue_Shopping = Folder_Path + "\\Continue_Shopping.png"
        driver.save_screenshot(Continue_Shopping)
        time.sleep(5)

        #Click On Cart Icon
        driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()
        time.sleep(5)



    def test_checkout_valid(self, driver, login):

        Folder_Path = r"J:\desktop\Desktop\Arslan_Sauce_Demo_Projec_Testing\Tests\04_Checkout_Tests"

        # Add Products
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)

        # Click On Cart Icon
        driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()
        time.sleep(5)

        #Scroll To CheckOut Button and Click
        Checkout = driver.find_element(By.ID, "checkout")
        driver.execute_script("arguments[0].scrollIntoView(true);", Checkout)
        time.sleep(3)
        Checkout.click()

        Checkout_Valid = Folder_Path + "\\Checkout_Valid.png"
        driver.save_screenshot(Checkout_Valid)
        time.sleep(5)


    def test_checkout_empty_field(self, driver, login):

        Folder_Path = r"J:\desktop\Desktop\Arslan_Sauce_Demo_Projec_Testing\Tests\04_Checkout_Tests"

        # Click On Cart Icon
        driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()
        time.sleep(5)

        # Scroll To CheckOut Button and Click
        Checkout = driver.find_element(By.ID, "checkout")
        driver.execute_script("arguments[0].scrollIntoView(true);", Checkout)
        time.sleep(5)
        Checkout.click()

        #Click on Checkout
        driver.find_element(By.ID, "continue").click()
        time.sleep(5)

        Form_Invalid = Folder_Path + "\\Empty_Forms.png"
        driver.save_screenshot(Form_Invalid)
        time.sleep(5)


    def test_checkout_overview(self, driver, login):

        Folder_Path = r"J:\desktop\Desktop\Arslan_Sauce_Demo_Projec_Testing\Tests\04_Checkout_Tests"

        # Add Products
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)

        # Click On Cart Icon
        driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()
        time.sleep(5)

        # Scroll To CheckOut Button and Click
        Checkout = driver.find_element(By.ID, "checkout")
        driver.execute_script("arguments[0].scrollIntoView(true);", Checkout)
        time.sleep(5)
        Checkout.click()
        time.sleep(2)

        # Fill Form
        driver.find_element(By.ID, "first-name").send_keys("Arslan Sajid")
        driver.find_element(By.ID, "last-name").send_keys("Khan")
        driver.find_element(By.ID, "postal-code").send_keys("35200")
        time.sleep(5)

        # Click Continue
        driver.find_element(By.ID, "continue").click()
        time.sleep(5)

        Finish = driver.find_element(By.ID, "finish")
        driver.execute_script("arguments[0].scrollIntoView(true);", Finish)
        time.sleep(5)

        Cart_Overview = Folder_Path + "\\Cart_Overview.png"
        driver.save_screenshot(Cart_Overview)
        time.sleep(5)


    def test_checkout_final(self, driver, login):

        Folder_Path = r"J:\desktop\Desktop\Arslan_Sauce_Demo_Projec_Testing\Tests\04_Checkout_Tests"

        # Add Products
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)

        # Click On Cart Icon
        driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()
        time.sleep(5)

        # Scroll To CheckOut Button and Click
        Checkout = driver.find_element(By.ID, "checkout")
        driver.execute_script("arguments[0].scrollIntoView(true);", Checkout)
        time.sleep(5)
        Checkout.click()
        time.sleep(2)

        #Fill Form
        driver.find_element(By.ID, "first-name").send_keys("Arslan Sajid")
        driver.find_element(By.ID, "last-name").send_keys("Khan")
        driver.find_element(By.ID, "postal-code").send_keys("35200")
        time.sleep(5)

        #Click Continue
        driver.find_element(By.ID, "continue").click()
        time.sleep(5)

        #Click Finish
        Finish = driver.find_element(By.ID, "finish")
        driver.execute_script("arguments[0].scrollIntoView(true);", Finish)
        time.sleep(3)
        Finish.click()
        time.sleep(5)

        Checkout_Complete = Folder_Path + "\\Checkout_Complete.png"
        driver.save_screenshot(Checkout_Complete)
        time.sleep(5)

        #Click BAck To Main Page
        driver.find_element(By.ID, "back-to-products").click()
        time.sleep(5)

