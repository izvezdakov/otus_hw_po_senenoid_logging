from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterPage(BasePage):
    
    _FIRSTNAME = (By.CSS_SELECTOR, '#input-firstname')
    _LASTNAME = (By.CSS_SELECTOR, '#input-lastname')
    _EMAIL = (By.CSS_SELECTOR, '#input-email')
    _TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
    _PASSWORD = (By.CSS_SELECTOR, '#input-password')

    @property
    def input_firstname(self):
        self.element(self._FIRSTNAME)
        return self

    @property
    def input_lastname(self):
        self.element(self._LASTNAME)
        return self

    @property
    def input_email(self):
        self.element(self._EMAIL)
        return self

    @property
    def input_telephone(self):
        self.element(self._TELEPHONE)
        return self

    @property
    def input_password(self):
        self.element(self._PASSWORD)
        return self
