from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    _MENU_CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    _MENU_CATALOG_PRODUCTS = (By.CSS_SELECTOR, "li:nth-child(2)")
    _BTN_ADD_NEW_PRODUCT = (By.CSS_SELECTOR, "[data-original-title='Add New']")
    _PRODUCT_TABLE = (By.XPATH, "//*[@class='table table-bordered table-hover']")
    _BTN_DELETE = (By.CSS_SELECTOR, "[data-original-title='Delete']")
    _ALERT_SUCCESS_DELETED = (By.XPATH, "//*[@class='alert alert-success alert-dismissible']")

    @property
    def menu_catalog(self):
        return self.element(self._MENU_CATALOG)

    @property
    def menu_catalog__products(self):
        return self.element_in_element(parent_locator=self._MENU_CATALOG, child_locator=self._MENU_CATALOG_PRODUCTS)

    @property
    def btn_add_new_product(self):
        return self.element(self._BTN_ADD_NEW_PRODUCT)

    @property
    def btn_delete(self):
        return self.element(self._BTN_DELETE)

    @property
    def product_table(self):
        return self.element(self._PRODUCT_TABLE)

    @property
    def alert_success_deleted(self):
        return self.element(self._ALERT_SUCCESS_DELETED)