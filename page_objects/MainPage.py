from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    _MENU = (By.CSS_SELECTOR, '#menu')
    _LOGO = (By.CSS_SELECTOR, '#logo')
    _SLIDESHOW = (By.CSS_SELECTOR, '#slideshow0')
    _SEARCH = (By.CSS_SELECTOR, '#search')
    _CART = (By.CSS_SELECTOR, '#cart')
    _BTN_SHOPPING_BASKET = (By.CSS_SELECTOR, '#cart-total')
    _BTN_CURRENCIES = (By.XPATH, "//*[@class='btn btn-link dropdown-toggle']")
    _DROPDOWN_CURRENCIES_BTNS = (By.XPATH, "//*[@class='currency-select btn btn-link btn-block']")

    @property
    def btn_dropdown_btns(self):
        return self.elements(self._DROPDOWN_CURRENCIES_BTNS)


    @property
    def btn_currencies(self):
        return self.element(self._BTN_CURRENCIES)

    @property
    def menu(self):
        self.element(self._MENU)
        return self

    @property
    def logo(self):
        self.element(self._LOGO)
        return self

    @property
    def slideshow(self):
        self.element(self._SLIDESHOW)
        return self

    @property
    def search(self):
        self.element(self._SEARCH)
        return self

    @property
    def cart(self):
        self.element(self._CART)
        return self

    @property
    def btn_shopping_basket(self):
        return self.element(self._BTN_SHOPPING_BASKET)
