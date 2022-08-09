from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "'Add to basket' button is not presented"

    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_be_notification_about_added_product(self):
        product_name = self.get_product_name()
        notification = self.browser.find_element(*ProductPageLocators.NOTIFICATION_ABOUT_NAME)
        notification_text = notification.text
        assert product_name == notification_text, "Product name is missing in the notification"

    def should_be_notification_about_price(self):
        product_price = self.get_product_price()
        notification = self.browser.find_element(*ProductPageLocators.NOTIFICATION_ABOUT_PRICE)
        notification_text = notification.text
        assert product_price == notification_text, "Product price is missing in the notification"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "SUCCESS message is presented but should not be"

    def success_message_should_disappear_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "SUCCESS message does not disappear after the timeout is over"


