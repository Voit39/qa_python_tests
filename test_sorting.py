import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
    
    def sort_products(self, sort_type):
        dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        dropdown.click()
        sort_options = self.driver.find_elements(By.XPATH, "//option")
        for option in sort_options:
            if option.get_attribute("value") == sort_type:
                option.click()
                break
        time.sleep(1)
    
    def get_all_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = []
        for element in price_elements:
            price_text = element.text.replace("$", "")
            prices.append(float(price_text))
        return prices

def test_sorting():
    # Создаем настройки для Firefox
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")  # Включаем невидимый режим
    
    # Запускаем Firefox в фоне
    driver = webdriver.Firefox(options=firefox_options)
    
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.sort_products("lohi")
    
    prices = inventory_page.get_all_prices()
    
    assert prices == sorted(prices), "Цены не отсортированы по возрастанию!"
    
    driver.quit()