from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
        REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
        LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    