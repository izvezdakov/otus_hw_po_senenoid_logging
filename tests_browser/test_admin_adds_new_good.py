from helpers import test_data
from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminPage import AdminPage
from page_objects.AddProductPage import AddProductPage


def test_add_new_product(driver):
    """
    # Добавление нового товара в разделе администратора.
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
    admin_page.click(element=admin_page.btn_add_new_product)

    add_product_page = AddProductPage(driver)
    add_product_page.click(element=add_product_page.input_produt_name_form)
    add_product_page.input(element=add_product_page.input_produt_name_form,
                           value=test_data.generate_product_name())
    add_product_page.input(element=add_product_page.input_produt_tag_form,
                           value=test_data.generate_product_tag())
    add_product_page.click(element=add_product_page.tab_data)
    add_product_page.input(element=add_product_page.input_model_form,
                           value=test_data.generate_product_model())
    add_product_page.click(element=add_product_page.btn_save)
    assert add_product_page.alert_success

