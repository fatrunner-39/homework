import allure

from pages.account_page import AccountSearchHelper
from pages.homepage import HomePageSearchHelper


@allure.feature("Homework")
def test_homework(browser, fibonacci: int):
    main_page = HomePageSearchHelper(browser)
    account_page = AccountSearchHelper(browser)

    # enter to account
    with allure.step("Login to account"):
        main_page.go_to_site()
        main_page.click_on_customer_login_button()
        main_page.choice_harry_potter()
        main_page.login_button()

    # actions by account
    with allure.step("Actions by account"):
        # enter deposit
        account_page.click_on_deposit_button()
        account_page.enter_deposit_value(fibonacci)

        # enter withdrawn
        account_page.click_on_withdrawn_button()
        account_page.enter_withdrawn_value(fibonacci)

    # check balance
    acc_data = account_page.check_account_data()
    with allure.step("Check balance equally 0"):
        assert acc_data.get("Balance") == "0"

    # create csv file for transactions
    account_page.click_transactions_button()
    file_path = account_page.check_transactions_table()
    with allure.step("Attach file to allure report"):
        allure.attach.file(file_path, attachment_type=allure.attachment_type.CSV)
