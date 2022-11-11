from helpers import test_data
from helpers.help_functions import determine_current_currency
from page_objects.MainPage import MainPage


def test_switch_currency(driver):
    """
    # Переключение валют из верхнего меню опенкарта.
    """
    driver.get(driver.base_url + '')
    main_page = MainPage(driver)
    current_currency = determine_current_currency(main_page.btn_shopping_basket.text)
    test_data.currencies.discard(current_currency)
    new_currency = test_data.currencies.pop()
    main_page.click(main_page.btn_currencies)
    for btn in main_page.btn_dropdown_btns:
        if new_currency in btn.text:
            main_page.click(btn)
            break
    assert new_currency in main_page.btn_shopping_basket.text
