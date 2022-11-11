from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductPage(BasePage):
    _ADDTOCART_BTN = (By.CSS_SELECTOR, '#button-cart')
    _DESCRIPTION = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/ul[2]/li[1]/a')
    _SHARE_BTN = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[3]/div/a[4]/a[1]')
    _ADD_TO_WISH_BTN = (By.XPATH, "//*[@class='fa fa-heart']")
    _THUMBNAILS = (By.XPATH, "//*[@class='thumbnails']")

    @property
    def btn_add_to_cart(self):
        self.element(self._ADDTOCART_BTN)
        return self

    @property
    def description(self):
        self.element(self._DESCRIPTION)
        return self

    @property
    def btn_share(self):
        self.element(self._SHARE_BTN)
        return self

    @property
    def btn_add_to_wish(self):
        self.element(self._ADD_TO_WISH_BTN)
        return self

    @property
    def thumbnails(self):
        self.element(self._THUMBNAILS)
        return self
