from helpers import test_data
from page_objects.RegisterAccountPage import RegisterAccountPage


def test_register_new_account(driver):
    """
    # Регистрация нового пользователя в магазине опенкарта.
    """
    driver.get(driver.base_url + 'index.php?route=account/register')
    regoster_account_page = RegisterAccountPage(driver)
    regoster_account_page.input(element=regoster_account_page.input_firstname,
                                value=test_data.NEW_USER_FIRSTNAME)
    regoster_account_page.input(element=regoster_account_page.input_lastname,
                                value=test_data.NEW_USER_LASTNAME)
    regoster_account_page.input(element=regoster_account_page.input_email,
                                value=test_data.generate_uniq_email())
    regoster_account_page.input(element=regoster_account_page.input_telephone,
                                value=test_data.NEW_USER_TELEPHONE)
    regoster_account_page.input(element=regoster_account_page.input_password,
                                value=test_data.NEW_USER_PASSWORD)
    regoster_account_page.input(element=regoster_account_page.input_password_confirm,
                                value=test_data.NEW_USER_PASSWORD)
    regoster_account_page.click(regoster_account_page.checkbox_agree)
    regoster_account_page.click(regoster_account_page.btn_continue)
    assert 'Your Account Has Been Created!' in regoster_account_page.success_text.text
