import allure

from pages.homepage import HomePageSearchHelper
from pages.account_page import AccountSearchHelper


@allure.feature('Dog Api')
def test_homework(browser, fibonacci: int):
    main_page = HomePageSearchHelper(browser)
    account_page = AccountSearchHelper(browser)

    # enter to account
    main_page.go_to_site()
    main_page.click_on_customer_login_button()
    main_page.choice_harry_potter()
    main_page.login_button()

    # actions by account
    # enter deposit
    account_page.click_on_deposit_button()
    account_page.enter_value(fibonacci)

    # enter withdrawl
    account_page.click_on_withdrawl_button()
    account_page.sleep(1)
    account_page.enter_value(fibonacci)
    account_page.sleep(1)

    # check balance
    acc_data = account_page.check_account_data()
    assert acc_data.get("Balance") == "0"

    # create csv file for transactions
    account_page.click_transactions_button()
    file_path = account_page.check_transactions_table()
    allure.attach.file(file_path, attachment_type=allure.attachment_type.CSV)
