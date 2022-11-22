from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegisterAccountPage(BasePage):
    
    _INPUT_FIRSTNAME = (By.CSS_SELECTOR, '#input-firstname')
    _INPUT_LASTNAME = (By.CSS_SELECTOR, '#input-lastname')
    _INPUT_EMAIL = (By.CSS_SELECTOR, '#input-email')
    _INPUT_TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
    _INPUT_PASSWORD = (By.CSS_SELECTOR, '#input-password')
    _INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
    _CHECKBOX_AGREE = (By.CSS_SELECTOR, 'input[type=checkbox]')
    _BTN_CONTINUE = (By.XPATH, "//*[@class='btn btn-primary']")
    _SUCCESS_MESSAGE = (By.XPATH, "//*[@class='col-sm-9']")


    @property
    def input_firstname(self):
        return self.element(self._INPUT_FIRSTNAME)

    @property
    def input_lastname(self):
        return self.element(self._INPUT_LASTNAME)

    @property
    def input_email(self):
        return self.element(self._INPUT_EMAIL)

    @property
    def input_telephone(self):
        return self.element(self._INPUT_TELEPHONE)

    @property
    def input_password(self):
        return self.element(self._INPUT_PASSWORD)

    @property
    def input_password_confirm(self):
        return self.element(self._INPUT_PASSWORD_CONFIRM)

    @property
    def checkbox_agree(self):
        return self.element(self._CHECKBOX_AGREE)

    @property
    def btn_continue(self):
        return self.element(self._BTN_CONTINUE)

    @property
    def success_text(self):
        return self.element(self._SUCCESS_MESSAGE)
