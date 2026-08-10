from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Класс LoginPage
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()


# 2. Класс InventoryPage
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_backpack).click()


# 3. Класс CartPage
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.ID, "shopping_cart_container")
        self.checkout_button = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def checkout(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.checkout_button).click()
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()


# 4. Тест
def test_saucedemo_pom():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()

    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    cart_page.checkout("Иван", "Иванов", "123456")

    # Проверяем, что мы на странице подтверждения
    assert "Checkout: Overview" in driver.page_source

    print("Тест пройден!")
    driver.quit()