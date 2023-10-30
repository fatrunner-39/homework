from selenium.webdriver.common.by import By

from .base_app import BasePage


class HomePageSeacrhLocators:
    LOCATOR_CUSTOMER_LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        'button[ng-click="customer()"]',
    )
    LOCATOR_CHOICE_HARRY_POTTER = (By.CSS_SELECTOR, 'option[value="2"]')
    LOCATOR_LOGIN_BUTTON = (By.CLASS_NAME, "btn-default")


class HomePageSearchHelper(BasePage):
    def click_on_customer_login_button(self):
        return self.find_element(
            HomePageSeacrhLocators.LOCATOR_CUSTOMER_LOGIN_BUTTON, time=2
        ).click()

    def choice_harry_potter(self):
        return self.find_element(
            HomePageSeacrhLocators.LOCATOR_CHOICE_HARRY_POTTER, time=2
        ).click()

    def login_button(self):
        return self.find_element(
            HomePageSeacrhLocators.LOCATOR_LOGIN_BUTTON, time=2
        ).click()
