import allure

from data import Constants
from pages.base_page import BasePage
from locators.password_recovery_loc import PasswordRecoveryLoc


class PasswordRecoveryPage(BasePage):
    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_recovery_button(self):
        self.click_element_js(PasswordRecoveryLoc.LK_BUTTON)
        self.element_is_visible(PasswordRecoveryLoc.RECOVERY_PASS_BUTTON)
        self.click_on_element(PasswordRecoveryLoc.RECOVERY_PASS_BUTTON)
        self.element_is_visible(PasswordRecoveryLoc.RECOVERY_TITLE)
        return self.get_text(PasswordRecoveryLoc.RECOVERY_TITLE)

    @allure.step('Вводим email')
    def input_email(self):
        self.click_element_js(PasswordRecoveryLoc.LK_BUTTON)
        self.element_is_visible(PasswordRecoveryLoc.RECOVERY_PASS_BUTTON)
        self.click_on_element(PasswordRecoveryLoc.RECOVERY_PASS_BUTTON)
        self.element_is_visible(PasswordRecoveryLoc.RECOVERY_INPUT)
        self.input_text(PasswordRecoveryLoc.RECOVERY_INPUT, Constants.MAIL)
        self.element_is_visible(PasswordRecoveryLoc.RECOVERY_PASS_BUTTON)
        self.click_on_element(PasswordRecoveryLoc.RECOVERY_BUTTON)
        self.element_is_visible(PasswordRecoveryLoc.SAVE_BUTTON)
        return self.get_text(PasswordRecoveryLoc.SAVE_BUTTON)

    @allure.step('Клик по кнопке "показать/скрыть пароль"')
    def click_on_eye_button(self):
        self.click_element_js(PasswordRecoveryLoc.LK_BUTTON)
        self.element_is_visible(PasswordRecoveryLoc.RECOVERY_PASS_BUTTON)
        self.click_on_element(PasswordRecoveryLoc.RECOVERY_PASS_BUTTON)
        self.element_is_visible(PasswordRecoveryLoc.RECOVERY_INPUT)
        self.input_text(PasswordRecoveryLoc.RECOVERY_INPUT, Constants.MAIL)
        self.element_is_visible(PasswordRecoveryLoc.RECOVERY_PASS_BUTTON)
        self.click_on_element(PasswordRecoveryLoc.RECOVERY_BUTTON)
        self.element_is_visible(PasswordRecoveryLoc.EYE_BUTTON)
        self.click_on_element(PasswordRecoveryLoc.EYE_BUTTON)
        return self.get_element_attribute(PasswordRecoveryLoc.PASSWORD_INPUT_ACTIVE)