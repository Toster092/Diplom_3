import allure

from locators.personal_account_loc import PersonalAccountLoc
from pages.base_page import BasePage
from locators.main_page_loc import MainPageLoc


class MainPage(BasePage):
    @allure.step('Клик на кнопку "Конструктор')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLoc.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на кнопку "Лента заказов')
    def click_on_feed_order_button(self):
        self.click_element_js(MainPageLoc.FEED_BUTTON)
        self.element_is_visible(MainPageLoc.ORDER_FEED_TITLE)

    @allure.step('Клик на кнопку "Ингридиент')
    def click_on_ingredient_button(self):
        self.click_element_js(MainPageLoc.FLUR_BUN)
        self.element_is_visible(MainPageLoc.BUN_TEXT)
        return self.get_text(MainPageLoc.BUN_TEXT)

    @allure.step('Клик на кнопку закрытия окна')
    def click_on_close_button(self):
        self.element_is_visible(MainPageLoc.FLUR_BUN)
        self.click_element_js(MainPageLoc.FLUR_BUN)
        self.element_is_visible(MainPageLoc.CLOSE_BUTTON)
        self.click_element_js(MainPageLoc.CLOSE_BUTTON)
        self.element_is_visible(MainPageLoc.LOGIN_BUTTON_LOCATOR)
        return self.get_text(MainPageLoc.LOGIN_BUTTON_LOCATOR)

    @allure.step('Добавляем ингридиент в заказ')
    def drag_and_drop_ingredient_to_basket(self):
        self.element_is_visible(MainPageLoc.FLUR_BUN)
        self.drag_and_drop(MainPageLoc.FLUR_BUN, MainPageLoc.BASKET)
        return self.get_text(MainPageLoc.BASKET_TEXT)

    @allure.step('Делаем заказ')
    def get_order_id(self, email, password):
        self.click_element_js(PersonalAccountLoc.LK_BUTTON)
        self.element_is_visible(PersonalAccountLoc.MAIL_INPUT)
        self.input_text(PersonalAccountLoc.MAIL_INPUT, email)
        self.input_text(PersonalAccountLoc.PASSWORD_INPUT, password)
        self.click_on_element(PersonalAccountLoc.LOGIN_SUBMIT_BUTTON)
        self.element_is_visible(MainPageLoc.FLUR_BUN)
        self.drag_and_drop(MainPageLoc.FLUR_BUN, MainPageLoc.BASKET)
        self.click_on_element(MainPageLoc.ORDER_BUTTON)
        self.element_is_visible(MainPageLoc.ORDER_ID_TEXT)
        return self.get_text(MainPageLoc.ORDER_ID_TEXT)