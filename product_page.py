from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def add_to_basket(self):
        try:
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
            return True
        except NoSuchElementException:
            return False

