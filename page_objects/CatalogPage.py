from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CatalogPage(BasePage):

    _SORTBY = (By.XPATH, "//*[@class='input-group-addon']")
    _PRODUCT_CATEGORY = (By.CSS_SELECTOR, '#product-category')
    _COLUMN_LEFT = (By.CSS_SELECTOR, '#column-left')
    _CONTENT = (By.CSS_SELECTOR, '#content')
    _PASSWORD = (By.XPATH, "//*[@class='input-group']")

    @property
    def sortby(self):
        self.element(self._SORTBY)
        return self

    @property
    def product_category(self):
        self.element(self._PRODUCT_CATEGORY)
        return self

    @property
    def column_left(self):
        self.element(self._COLUMN_LEFT)
        return self

    @property
    def content(self):
        self.element(self._CONTENT)
        return self

    @property
    def password(self):
        self.element(self._PASSWORD)
        return self
