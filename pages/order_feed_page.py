import allure

from locators.main_page_loc import MainPageLoc
from locators.personal_account_loc import PersonalAccountLoc
from pages.base_page import BasePage
from locators.order_feed_loc import OrderFeedLoc


class OrderFeedPage(BasePage):

    @allure.step('Клик на заказ')
    def click_on_order(self):
        self.element_is_visible(OrderFeedLoc.FEED_BUTTON)
        self.click_element_js(OrderFeedLoc.FEED_BUTTON)
        self.find_element_located_presence(OrderFeedLoc.ORDER_FEED_TITLE)
        order = self.find_elements_located(OrderFeedLoc.ORDER_LIST)[0]
        self.click_on_element(order)
        self.find_element_located_presence(OrderFeedLoc.ORDER_TITLE)
        return self.get_text(OrderFeedLoc.ORDER_TITLE)

    @allure.step('Находим созданный заказ в истории заказов пользователя и ленте заказов')
    def find_user_order(self, email, password):
        self.click_element_js(PersonalAccountLoc.LK_BUTTON)
        self.element_is_visible(PersonalAccountLoc.MAIL_INPUT)
        self.input_text(PersonalAccountLoc.MAIL_INPUT, email)
        self.input_text(PersonalAccountLoc.PASSWORD_INPUT, password)
        self.click_on_element(PersonalAccountLoc.LOGIN_SUBMIT_BUTTON)
        self.element_is_visible(MainPageLoc.FLUR_BUN)
        self.drag_and_drop(MainPageLoc.FLUR_BUN, MainPageLoc.BASKET)
        self.click_on_element(MainPageLoc.ORDER_BUTTON)
        self.click_with_retry(OrderFeedLoc.CLOSE_ORDER_BUTTON, OrderFeedLoc.OVERLAY)
        self.element_is_visible(PersonalAccountLoc.LK_BUTTON)
        self.click_on_element(PersonalAccountLoc.LK_BUTTON)
        self.element_is_visible(PersonalAccountLoc.ORDER_HISTORY_BUTTON)
        self.click_on_element(PersonalAccountLoc.ORDER_HISTORY_BUTTON)
        self.element_is_visible(OrderFeedLoc.ORDER_IN_LIST)
        order_in_user_list_order = self.get_text(OrderFeedLoc.ORDER_IN_LIST)
        self.element_is_visible(OrderFeedLoc.FEED_BUTTON)
        self.click_element_js(OrderFeedLoc.FEED_BUTTON)
        user_order_in_feed = self.get_text(OrderFeedLoc.ORDER_IN_LIST)
        return order_in_user_list_order, user_order_in_feed

    @allure.step('Создаем заказ и проверяем счетчик "Выполнено за всё время"')
    def check_counter_all_time(self, email, password):
        self.click_element_js(PersonalAccountLoc.LK_BUTTON)
        self.element_is_visible(PersonalAccountLoc.MAIL_INPUT)
        self.input_text(PersonalAccountLoc.MAIL_INPUT, email)
        self.input_text(PersonalAccountLoc.PASSWORD_INPUT, password)
        self.click_on_element(PersonalAccountLoc.LOGIN_SUBMIT_BUTTON)
        self.element_is_visible(OrderFeedLoc.FEED_BUTTON)
        self.click_on_element(OrderFeedLoc.FEED_BUTTON)
        self.element_is_visible(OrderFeedLoc.MADE_ALL_TIME)
        made_all_time_before = self.get_text(OrderFeedLoc.MADE_ALL_TIME)
        self.click_element_js(MainPageLoc.CONSTRUCTOR_BUTTON)
        self.element_is_visible(MainPageLoc.FLUR_BUN)
        self.drag_and_drop(MainPageLoc.FLUR_BUN, MainPageLoc.BASKET)
        self.click_on_element(MainPageLoc.ORDER_BUTTON)
        self.click_with_retry(OrderFeedLoc.CLOSE_ORDER_BUTTON, OrderFeedLoc.OVERLAY)
        self.element_is_visible(OrderFeedLoc.FEED_BUTTON)
        self.click_element_js(OrderFeedLoc.FEED_BUTTON)
        self.element_is_visible(OrderFeedLoc.MADE_ALL_TIME)
        made_all_time_after = self.get_text(OrderFeedLoc.MADE_ALL_TIME)
        return made_all_time_before, made_all_time_after

    @allure.step('Создаем заказ и проверяем счетчик "Выполнено за сегодня"')
    def check_counter_today(self, email, password):
        self.click_element_js(PersonalAccountLoc.LK_BUTTON)
        self.element_is_visible(PersonalAccountLoc.MAIL_INPUT)
        self.input_text(PersonalAccountLoc.MAIL_INPUT, email)
        self.input_text(PersonalAccountLoc.PASSWORD_INPUT, password)
        self.click_on_element(PersonalAccountLoc.LOGIN_SUBMIT_BUTTON)
        self.element_is_visible(OrderFeedLoc.FEED_BUTTON)
        self.click_on_element(OrderFeedLoc.FEED_BUTTON)
        self.element_is_visible(OrderFeedLoc.MADE_TODAY)
        made_today_before = self.get_text(OrderFeedLoc.MADE_TODAY)
        self.click_element_js(MainPageLoc.CONSTRUCTOR_BUTTON)
        self.element_is_visible(MainPageLoc.FLUR_BUN)
        self.drag_and_drop(MainPageLoc.FLUR_BUN, MainPageLoc.BASKET)
        self.click_on_element(MainPageLoc.ORDER_BUTTON)
        self.click_with_retry(OrderFeedLoc.CLOSE_ORDER_BUTTON, OrderFeedLoc.OVERLAY)
        self.element_is_visible(OrderFeedLoc.FEED_BUTTON)
        self.click_on_element(OrderFeedLoc.FEED_BUTTON)
        self.element_is_visible(OrderFeedLoc.MADE_TODAY)
        made_today_after = self.get_text(OrderFeedLoc.MADE_TODAY)
        return made_today_before, made_today_after

    @allure.step('Создаем заказ и проверяем отображение "В работе"')
    def check_in_work(self, email, password):
        self.click_element_js(PersonalAccountLoc.LK_BUTTON)
        self.element_is_visible(PersonalAccountLoc.MAIL_INPUT)
        self.input_text(PersonalAccountLoc.MAIL_INPUT, email)
        self.input_text(PersonalAccountLoc.PASSWORD_INPUT, password)
        self.click_on_element(PersonalAccountLoc.LOGIN_SUBMIT_BUTTON)
        self.element_is_visible(OrderFeedLoc.FEED_BUTTON)
        self.drag_and_drop(MainPageLoc.FLUR_BUN, MainPageLoc.BASKET)
        self.click_on_element(MainPageLoc.ORDER_BUTTON)
        order_id = self.get_text_visibility_of_all_element(OrderFeedLoc.CREATED_ORDER_ID)
        self.click_with_retry(OrderFeedLoc.CLOSE_ORDER_BUTTON, OrderFeedLoc.OVERLAY)
        self.element_is_visible(OrderFeedLoc.FEED_BUTTON)
        self.click_on_element(OrderFeedLoc.FEED_BUTTON)
        self.element_is_visible(OrderFeedLoc.ORDER_IN_WORK)
        order_in_work = self.get_text(OrderFeedLoc.ORDER_IN_WORK)
        return order_id, order_in_work



