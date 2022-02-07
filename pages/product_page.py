from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def add_to_cart_and_calculate(self): 
        self.add_to_cart()
        self.solve_quiz_and_get_code()

    def add_to_cart(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        btn.click()

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), 'Add to cart button is not present'

    