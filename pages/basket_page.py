from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        basket_url = self.browser.current_url
        assert basket_url == f"http://selenium1py.pythonanywhere.com/en-gb/basket/",\
            f"Login URL is wrong." \
            f"\n'http://selenium1py.pythonanywhere.com/en-gb/basket/' should be." \
            f"\n{basket_url} is set"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_message_about_empty_basket(self):
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        message_text = message.text.strip()
        assert 'empty' in message_text, "Message about empty basket is wrong"
