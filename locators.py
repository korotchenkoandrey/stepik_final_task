from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_EMAIL_ENTRY_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_ENTRY_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTER_EMAIL_ENTRY_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_ENTRY_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_ENTRY_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini>span>a')
    EMPTY_BASKET = (By.ID, "content_inner")
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')