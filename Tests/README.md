🧪 SauceDemo Automation Testing Project

📌 Project Overview

This project is an automated testing framework for the SauceDemo website built using Selenium and Pytest.
It covers end-to-end testing of major functionalities including Login, Inventory, Cart, Menu, and Checkout.

The goal of this project is to simulate real user behavior and validate the application flow from login to order completion.

---

🚀 Technologies Used

- Python 🐍
- Selenium WebDriver 🌐
- Pytest ⚡

---

📂 Project Structure

saucedemo_project/
│
├── Tests/
│   ├── 01_Login_Tests/
│   │   ├── test_loginValid.py
│   │   ├── test_LoginInvalid.py
│   │   ├── test_LoginEmpty.py
│   │
│   ├── 02_Inventory_Tests/
│   │   ├── test_AddToCart.py
│   │   ├── test_CartCount.py
│   │   ├── test_ProductLoad.py
│   │   ├── test_RemoveCart.py
│   │   ├── Test_SortingMainPage.py
│   │   └── Test_ProductNames.py
│
│   ├── 03_Menu_Tests/
│   │   └── test_menu.py
│
│   ├── 04_Cart_Checkout_Tests/
│   │   └── test_cart_checkout.py
│
├── screenshots/
├── conftest.py

---

✅ Test Coverage (~19 Test Cases)

🔹 Login Module

- Valid login
- Invalid login
- Empty fields validation

🔹 Inventory Module

- Products loading validation
- Add to cart functionality
- Remove from cart
- Cart badge count validation
- Product sorting (A-Z, Z-A, Price)
- Product names verification

🔹 Menu Module

- Menu open/close
- About page redirection
- External navigation handling
- Logout functionality

🔹 Cart & Checkout Module

- Add items to cart
- Continue shopping functionality
- Checkout with valid data
- Checkout with empty fields
- Checkout overview validation
- Order completion (Finish button)

---

▶️ How to Run Tests

1. Install Py-charm IDE

2. Install Python in Your System

3. Create Project

4. Install Dependencies

5. pip install selenium pytest and related Libraries

6. Run All Tests

pytest -v

---

📸 Screenshots

Screenshots can be captured during test execution and stored in the "screenshots/" folder.

---

💡 Key Features

- End-to-end automation testing
- Organized folder structure
- Multiple test scenarios (~19 test cases)
- Pytest fixtures for setup and reuse
- Covers both positive and negative test cases

---

👨‍💻 Author

ARSLAN SAJID KHAN