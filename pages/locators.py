from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PWD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PWD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PWD = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    NOTIFICATION_ABOUT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div.alertinner > strong")
    NOTIFICATION_ABOUT_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div.alertinner > p > strong")




