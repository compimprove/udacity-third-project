# #!/usr/bin/env python
from telnetlib import TM
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# --uncomment when running in Azure DevOps.
options = ChromeOptions()
options.add_argument("--headless")
# options.add_argument('--window-size=1920,1080')
# userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
# options.add_argument('user-agent={userAgent}')

delay = 10
browser = webdriver.Chrome(options=options)
print('Starting the browser...')
# Start the browser and login with standard_user


def login(email, password):
    browser.find_element(by=By.CSS_SELECTOR,
                         value="a.login").click()
    print('Navigating to login.')
    try:
        email_input = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#email")))
        email_input.send_keys(email)
        print('set email: ', email)
        browser.find_element(by=By.CSS_SELECTOR,
                             value="#passwd").send_keys(password)
        print('set password: ', password)
        browser.find_element(by=By.CSS_SELECTOR,
                             value="#SubmitLogin").click()
        print('Login successfully with username:',
              email, 'password:', password)
    except TimeoutException:
        print("Loading took too much time!")


def go_to_home():
    print('goToHome')
    try:
        home = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#header_logo>a")))
        home.click()
    except TimeoutException:
        print("Loading took too much time!")


def add_product_to_cart():
    print('addProductToCart')
    WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#homefeatured li .button-container a.ajax_add_to_cart_button")))
    buttons = browser.find_elements(
        by=By.CSS_SELECTOR, value="#homefeatured li .button-container a.ajax_add_to_cart_button")
    for idx, button in enumerate(buttons):
        button.click()
        WebDriverWait(browser, delay).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#layer_cart")))
        WebDriverWait(browser, delay).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.continue.btn.btn-default.button.exclusive-medium"))).click()
        time.sleep(1)
        product_added = idx + 1
        print(f'add {product_added} to cart')
    quantity = browser.find_element(
        by=By.CSS_SELECTOR, value=".shopping_cart .ajax_cart_quantity")
    print(f'product add to cart:{quantity.text}')


# def wait_for_product_popup_appear():
#     while (browser.find_element(by=By.ID, value="layer_cart").value_of_css_property('display') == 'none'):
#         time.sleep(0.5)


def remove_product_from_cart():
    print('removeProductFromCart')
    browser.find_element(by=By.CSS_SELECTOR,
                         value="#header_logo>a").click()
# .clearfix .button-container a.button
# "#homefeatured li .button-container a.ajax_add_to_cart_button"


browser.get('http://automationpractice.com/')
# login('compimprove@gmail.com', '0987654321')
# go_to_home()
add_product_to_cart()
remove_product_from_cart()
