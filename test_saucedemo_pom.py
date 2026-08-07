from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Класс logoPage
class loginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()
# 2. Кдасс  inventoryPage
class inventoryPage:
    def __init__(self, driver):
        self.driver = driver 
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")

    def add_backpack_to_cart(self): 
        self.driver.find_element(*self.add_backpack).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_name = (By.XPATH, "//div[@data-test='inventory-item-name']")

    def get_item_name(self):
        return self.driver.find_element(*self.item_name).text

          
# 3. Тест 
def test_login_and_add_item():
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")

        login_page = loginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        inventory = inventoryPage(driver)
        inventory.add_backpack_to_cart()

        badge = driver.find_element(By.XPATH, '//span[@data-test="shopping-cart-badge"]')
        assert badge.text == "1"

        print("Тест пройден!")
        driver.quit()


        
        