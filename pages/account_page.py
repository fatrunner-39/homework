import csv
import uuid
from urllib.parse import urljoin

from selenium.webdriver import Keys

from helpers.conver_table_data import convert_table
from .base_app import BasePage
from selenium.webdriver.common.by import By


class AccountSeacrhLocators:
    LOCATOR_DEPOSIT_BUTTON = (By.CSS_SELECTOR, 'button[ng-class="btnClass2"]')
    LOCATOR_ENTER_VALUE = (By.CLASS_NAME, "form-control")

    LOCATOR_WITHDRAWL_BUTTON = (By.CSS_SELECTOR, 'button[ng-class="btnClass3"]')

    LOCATOR_ACCOUNT_DATA = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]')
    LOCATOR_TRANSACTIONS_BUTTON = (By.CSS_SELECTOR, 'button[ng-class="btnClass1"]')
    LOCATOR_TRANSACTIONS_TABLE = (By.CSS_SELECTOR, 'table[class="table table-bordered table-striped"] > tbody')


class AccountSearchHelper(BasePage):

    def click_on_deposit_button(self):
        return self.find_element(AccountSeacrhLocators.LOCATOR_DEPOSIT_BUTTON, time=2).click()

    def enter_value(self, value: int):
        return self.find_element(AccountSeacrhLocators.LOCATOR_ENTER_VALUE, time=2).send_keys(value, Keys.ENTER)

    def click_on_withdrawl_button(self):
        return self.find_element(AccountSeacrhLocators.LOCATOR_WITHDRAWL_BUTTON, time=2).click()

    def check_account_data(self):
        account_data = self.find_elements(AccountSeacrhLocators.LOCATOR_ACCOUNT_DATA, time=2)
        account_data_string = [x.text for x in account_data if len(x.text) > 0][0].replace(" ", "")
        account_data_dict = {}
        for element in account_data_string.split(","):
            el = element.split(":")
            account_data_dict[el[0]] = el[1]
        return account_data_dict

    def click_transactions_button(self):
        return self.find_element(AccountSeacrhLocators.LOCATOR_TRANSACTIONS_BUTTON, time=2).click()

    def check_transactions_table(self) -> str:
        transactions_table = self.find_element(AccountSeacrhLocators.LOCATOR_TRANSACTIONS_TABLE, time=2)
        table_dict_data = convert_table(transactions_table.text)

        name = f"transaction_{uuid.uuid4()}.csv"
        path = urljoin("transaction_files/", name)
        with open(path, 'w', newline='') as csvfile:
            fieldnames = table_dict_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(table_dict_data)
        return path

