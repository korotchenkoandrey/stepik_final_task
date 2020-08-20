from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Invalid login url"
        assert "login" in self.browser.current_url, "Invalid login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        register_element = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        password_element = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        register_confirm_element = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_FIELD)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        register_element.send_keys(email)
        password_element.send_keys(password)
        register_confirm_element.send_keys(password)
        submit_button.click()


