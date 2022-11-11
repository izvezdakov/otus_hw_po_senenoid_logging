from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import test_data
from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminPage import AdminPage


def test_delete_product(driver):
    """
    # Удаление товара из списка в разделе администартора.
    """
    driver.get(driver.base_url + 'admin')
    admin_login_page = AdminLoginPage(driver)
    admin_login_page.input(element=admin_login_page.form_input_username,
                           value=test_data.USER)
    admin_login_page.input(element=admin_login_page.form_input_password,
                           value=test_data.PASSWORD)
    admin_login_page.click(element=admin_login_page.btn_login)

    admin_page = AdminPage(driver)
    admin_page.click(element=admin_page.menu_catalog)
    admin_page.click(element=admin_page.menu_catalog__products)

    checkboxes = admin_page.product_table.find_elements(By.CSS_SELECTOR, 'input[type=checkbox]')
    assert not checkboxes[1].is_selected()
    checkboxes[1].click()
    assert checkboxes[1].is_selected()
    admin_page.click(admin_page.btn_delete)
    alert = WebDriverWait(driver, 2).until(expected_conditions.alert_is_present())
    alert.accept()
    assert admin_page.alert_success_deleted
