import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f'logs/{self.driver.test_name}.log')
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        file_handler.setLevel(self.driver.log_level)
        self.logger.addHandler(file_handler)

    def click(self, element):
        self.logger.info(f'Clicking element: {element}')
        with allure.step(f'click on element {element}'):
            ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def input(self, element, value):
        self.logger.info(f'Input {value} in {element}')
        with allure.step(f'input {value} in {element}'):
            self.click(element)
            element.clear()
            element.send_keys(value)

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_element(*child_locator)

    def element(self, locator: tuple):
        self.logger.debug(f'Find element by locator {locator}')
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.critical(f'Element is not present: {locator}')
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            allure.attach(body=self.driver.get_screenshot_as_png,
                          attachment_type=allure.attachment_type.PNG,
                          name='screenshot_image')
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def verify_product_item(self, product_name):
        return self.element((By.LINK_TEXT, product_name))