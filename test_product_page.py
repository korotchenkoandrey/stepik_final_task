import pytest
import time

# from .main_page import MainPage
from .main_page import MainPage
from .base_page import BasePage
from .locators import ProductPageLocators
from .login_page import LoginPage
from .product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
