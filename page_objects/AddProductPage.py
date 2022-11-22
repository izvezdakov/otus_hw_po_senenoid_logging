from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AddProductPage(BasePage):

    _INPUT_PRODUCT_NAME_FORM = (By.CSS_SELECTOR, '#input-name1')
    _INPUT_PRODUCT_TAG_FORM = (By.CSS_SELECTOR, '#input-meta-title1')
    _TAB_DATA = (By.CSS_SELECTOR, '[href$="#tab-data"]')
    _INPUT_MODEL_FORM = (By.CSS_SELECTOR, '#input-model')
    _BTN_SAVE = (By.CSS_SELECTOR, "[data-original-title='Save']")
    _ALERT_SUCCESS = (By.XPATH, "//*[@class='alert alert-success alert-dismissible']")

    @property
    def input_produt_name_form(self):
        return self.element(self._INPUT_PRODUCT_NAME_FORM)

    @property
    def input_produt_tag_form(self):
        return self.element(self._INPUT_PRODUCT_TAG_FORM)

    @property
    def tab_data(self):
        return self.element(self._TAB_DATA)

    @property
    def input_model_form(self):
        return self.element(self._INPUT_MODEL_FORM)

    @property
    def btn_save(self):
        return self.element(self._BTN_SAVE)

    @property
    def alert_success(self):
        return self.element(self._ALERT_SUCCESS)

