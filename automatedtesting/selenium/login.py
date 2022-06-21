# #!/usr/bin/env python
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
    browser.get('http://automationpractice.com/')
    browser.find_element(by=By.CSS_SELECTOR,
                         value="a.login").click()
    print('Navigating to login.')
    try:
        emailInput = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#email")))
        emailInput.send_keys(email)
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


def goToHome():
    print('goToHome')
    try:
        home = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#header_logo>a")))
        home.click()
    except TimeoutException:
        print("Loading took too much time!")


def addProductToCart():
    print('addProductToCart')
    browser.find_element(by=By.CSS_SELECTOR,
                         value="#header_logo>a").click()


def removeProductFromCart():
    print('removeProductFromCart')
    browser.find_element(by=By.CSS_SELECTOR,
                         value="#header_logo>a").click()
# .clearfix .button-container a.button
# "#homefeatured li .button-container a.ajax_add_to_cart_button"


login('compimprove@gmail.com', '0987654321')
goToHome()
addProductToCart()
removeProductFromCart()
