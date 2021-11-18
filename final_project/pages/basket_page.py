from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        current_url = self.browser.getCurrentUrl()
        assert "basket" in current_url, "'basket' is not presented in current URL"

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
                 "Basket is not empty"

    def should_be_message_about_emptiness(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
               "Message about emptiness is not presented"
