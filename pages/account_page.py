from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.conver_table_data import convert_table, create_transactions_file

from .base_app import BasePage


class AccountSeacrhLocators:
    LOCATOR_DEPOSIT_BUTTON = (By.CSS_SELECTOR, 'button[ng-class="btnClass2"]')
    LOCATOR_DEPOSIT = (By.CSS_SELECTOR, 'form[ng-submit="deposit()"]')

    LOCATOR_ENTER_VALUE = (By.CLASS_NAME, "form-control")

    LOCATOR_WITHDRAWN_BUTTON = (By.CSS_SELECTOR, 'button[ng-class="btnClass3"]')
    LOCATOR_WITHDRAWN = (By.CSS_SELECTOR, 'form[ng-submit="withdrawl()"]')
    LOCATOR_SUBMIT_WITHDRAWN = (By.CSS_SELECTOR, 'button[type="submit"]')

    LOCATOR_ACCOUNT_DATA = (By.CSS_SELECTOR, 'div[ng-hide="noAccount"]')

    LOCATOR_TRANSACTIONS_BUTTON = (By.CSS_SELECTOR, 'button[ng-class="btnClass1"]')
    LOCATOR_TRANSACTIONS_TABLE = (
        By.CSS_SELECTOR,
        'table[class="table table-bordered table-striped"] > tbody',
    )
    LOCATOR_TRANSACTION_RESULT = (By.CSS_SELECTOR, 'span[ng-show="message"]')


class AccountSearchHelper(BasePage):
    def click_on_deposit_button(self):
        return self.find_element(
            AccountSeacrhLocators.LOCATOR_DEPOSIT_BUTTON, time=2
        ).click()

    def enter_deposit_value(self, value: int):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AccountSeacrhLocators.LOCATOR_DEPOSIT)
        )
        return self.find_element(
            AccountSeacrhLocators.LOCATOR_ENTER_VALUE, time=2
        ).send_keys(value, Keys.ENTER)

    def click_on_withdrawn_button(self):
        return self.find_element(
            AccountSeacrhLocators.LOCATOR_WITHDRAWN_BUTTON, time=2
        ).click()

    def enter_withdrawn_value(self, value: int):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AccountSeacrhLocators.LOCATOR_WITHDRAWN)
        )
        return self.find_element(
            AccountSeacrhLocators.LOCATOR_ENTER_VALUE, time=2
        ).send_keys(value, Keys.ENTER)

    def check_account_data(self):
        account_data = self.find_elements(
            AccountSeacrhLocators.LOCATOR_ACCOUNT_DATA, time=2
        )
        account_data_string = [x.text for x in account_data if len(x.text) > 0][
            0
        ].replace(" ", "")
        account_data_dict = {}
        for element in account_data_string.split(","):
            el = element.split(":")
            account_data_dict[el[0]] = el[1]
        return account_data_dict

    def click_transactions_button(self):
        self.driver.refresh()
        return self.find_element(
            AccountSeacrhLocators.LOCATOR_TRANSACTIONS_BUTTON, time=5
        ).click()

    def check_transactions_table(self) -> str:
        transactions_table = self.find_element(
            AccountSeacrhLocators.LOCATOR_TRANSACTIONS_TABLE, time=2
        )
        table_dict_data = convert_table(transactions_table.text)
        return create_transactions_file(table_dict_data)
