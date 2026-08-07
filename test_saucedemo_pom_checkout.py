from selenium import webdriver
from selenium.webdriver.common.by import By

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

class inventoryPage:
    def __init__(self, driver):
        self.driver = driver 
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_backpack).click()
        
class cartPage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart_container = (By.ID, "shopping_cart_container")
        self.checkout = (By.ID, "checkout")

    def go_to_cart(self):
        self.driver.find_element(*self.shopping_cart_container).click()

    def proceed_to_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

class checkoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.First_Name = (By.ID, "first-name")
        self.Last_Name = (By.ID, "last-name")
        self.Zip_Code = (By.ID, "postal-code")
        self.Continue = (By.ID, "continue")

    def fill_form(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.First_Name).send_keys(first_name)
        self.driver.find_element(*self.Last_Name).send_keys(last_name)
        self.driver.find_element(*self.Zip_Code).send_keys(zip_code)
        self.driver.find_element(*self.Continue).click()

    def get_title(self):
        return self.driver.find_element(By.XPATH, '//span[@data-test = "title"]'). text

def test_saucedemo_pom_checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    login_Page = loginPage(driver)
    login_Page.login ("standard_user","secret_sauce")

    inventory_Page = inventoryPage(driver)
    inventory_Page.add_backpack_to_cart()

    cart_Page = cartPage(driver)
    cart_Page.go_to_cart()
    cart_Page.proceed_to_checkout()

    checkout_Page = checkoutPage(driver)
    checkout_Page.fill_form("Иван","Иванов","123456")

    assert checkout_Page.get_title() == "Checkout: Overview"
    

    
        
        
        

        
        