import allure

from pages.base_page import BasePage
from locators.personal_account_loc import PersonalAccountLoc

class PersonalAccountPage(BasePage):
    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_lk_button(self):
        self.click_element_js(PersonalAccountLoc.LK_BUTTON)
        self.element_is_visible(PersonalAccountLoc.LK_TITLE)
        return self.get_text(PersonalAccountLoc.LK_TITLE)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_order_history(self, email, password):
        self.click_element_js(PersonalAccountLoc.LK_BUTTON)
        self.element_is_visible(PersonalAccountLoc.MAIL_INPUT)
        self.input_text(PersonalAccountLoc.MAIL_INPUT, email)
        self.input_text(PersonalAccountLoc.PASSWORD_INPUT, password)
        self.click_on_element(PersonalAccountLoc.LOGIN_SUBMIT_BUTTON)
        self.element_is_visible(PersonalAccountLoc.LK_BUTTON)
        self.click_on_element(PersonalAccountLoc.LK_BUTTON)
        self.element_is_visible(PersonalAccountLoc.ORDER_HISTORY_BUTTON)
        self.click_element_js(PersonalAccountLoc.ORDER_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def click_on_exit(self, email, password):
        self.click_on_element(PersonalAccountLoc.LK_BUTTON)
        self.input_text(PersonalAccountLoc.MAIL_INPUT, email)
        self.input_text(PersonalAccountLoc.PASSWORD_INPUT, password)
        self.click_on_element(PersonalAccountLoc.LOGIN_SUBMIT_BUTTON)
        self.click_on_element(PersonalAccountLoc.LK_BUTTON)
        self.click_on_element(PersonalAccountLoc.EXIT_BUTTON)
        self.find_element_located(PersonalAccountLoc.PASSWORD_INPUT)
        return self.get_text(PersonalAccountLoc.LK_TITLE)


