from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_correct_adding(self):
        self.should_be_message_about_adding_to_basket()
        self.should_be_equal_price_for_basket_and_product()

    def should_be_equal_price_for_basket_and_product(self):
        price = (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)).text
        basket = (self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)).text
        assert price == basket, f"Product price ({price}) is not same with price in basket ({basket})"

    def should_be_message_about_adding_to_basket(self):
        product_name = (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)).text
        product_in_basket = (self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)).text
        assert product_name == product_in_basket, \
            f"Product name ({product_name}) is not same with name in basket ({product_in_basket})"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"
