from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_full():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    add_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_cart.click()

    badge = driver.find_element(By.XPATH, '//span[@data-test="shopping-cart-badge"]')
    assert badge.text == "1"

    cart = driver.find_element(By.ID, "shopping_cart_container")
    cart.click()

    item = driver.find_element(By.ID, "item_4_title_link")
    assert item.text == "Sauce Labs Backpack"

    delete = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    delete.click()

    badges = driver.find_elements(By.XPATH, '//span[@data-test="shopping-cart-badge"]')
    assert len(badges) == 0

    burger_button = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_button.click()

    wait = WebDriverWait(driver, 5)
    logout = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
    logout.click()

    print("Тест пройден!")
    driver.quit()