from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_repeat():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys ("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID,"login-button")
    login_button.click()

    add_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_cart.click()

    cart = driver.find_element(By.ID, "shopping_cart_container")
    cart.click()

    item = driver.find_element(By.ID, "item_4_title_link")
    assert item.text == "Sauce Labs Backpack"

    driver.quit()