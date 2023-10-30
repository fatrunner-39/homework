from .base_app import BasePage
from selenium.webdriver.common.by import By


class HomePageSeacrhLocators:
    LOCATOR_CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, 'div.borderM.box.padT20 > div:nth-child(1) > button')
    LOCATOR_CHOICE_HARRY_POTTER = (By.CSS_SELECTOR, '#userSelect > option:nth-child(3)')
    LOCATOR_LOGIN_BUTTON = (By.CLASS_NAME, "btn-default")


class HomePageSearchHelper(BasePage):

    def click_on_customer_login_button(self):
        return self.find_element(HomePageSeacrhLocators.LOCATOR_CUSTOMER_LOGIN_BUTTON, time=2).click()

    def choice_harry_potter(self):
        return self.find_element(HomePageSeacrhLocators.LOCATOR_CHOICE_HARRY_POTTER, time=2).click()

    def login_button(self):
        return self.find_element(HomePageSeacrhLocators.LOCATOR_LOGIN_BUTTON, time=2).click()

    # def enter_word(self, word):
    #     search_field = self.find_element(SeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
    #     search_field.click()
    #     search_field.send_keys(word)
    #     return search_field
    #
    # def click_on_the_search_button(self):
    #     return self.find_element(SeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()
    #
    # def check_navigation_bar(self):
    #     all_list = self.find_elements(SeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     return nav_bar_menu
