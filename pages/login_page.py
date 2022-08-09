from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        assert login_url == f"http://selenium1py.pythonanywhere.com/en-gb/accounts/login/",\
            f"Login URL is wrong." \
            f"\n'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/' should be." \
            f"\n{login_url} is set"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "E-mail field in the login form is missing"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PWD), "The password field in the login form is missing"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "E-mail field in the register form is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PWD), "The password field in the register form is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PWD), "The field to confirm password in the register form is missing"

    def register_new_user(self, email, pwd):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        pwd_input = self.browser.find_element(*LoginPageLocators.REGISTER_PWD)
        pwd_input.send_keys(pwd)
        confirm_pwd_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PWD)
        confirm_pwd_input.send_keys(pwd)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()


