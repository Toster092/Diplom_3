import allure

from pages.order_feed_page import OrderFeedPage
class TestOrderFeedPage:
    @allure.title('Проверка открытия окна заказа с деталями')
    def test_open_order_from_feed(self, driver):
       order_feed_page = OrderFeedPage(driver)
       result = order_feed_page.click_on_order()
       assert result == 'Cостав'

    @allure.title('Проверка отображения заказов пользователя из истории заказов в ленте заказов')
    def test_user_order_in_feed(self, driver, user_data, delete_user):
        order_feed_page = OrderFeedPage(driver)
        order_in_user_list_order, user_order_in_feed = order_feed_page.find_user_order(user_data['email'],
                                                                                       user_data['password'])
        assert order_in_user_list_order == user_order_in_feed

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании заказа пользователем')
    def test_change_alltime_counter_after_order(self, driver, user_data, delete_user):
        order_feed_page = OrderFeedPage(driver)
        made_all_time_before, made_all_time_after = order_feed_page.check_counter_all_time(user_data['email'],
                                                                                       user_data['password'])
        assert made_all_time_before != made_all_time_after

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании заказа пользователем')
    def test_change_today_counter_after_order(self, driver, user_data, delete_user):
        order_feed_page = OrderFeedPage(driver)
        made_today_before, made_today_after = order_feed_page.check_counter_today(user_data['email'],
                                                                                           user_data['password'])
        assert made_today_before != made_today_after

    @allure.title('Проверка отображения номера заказа в разделе "В работе" при создании заказа пользователем')
    def test_order_appears_in_work(self, driver, user_data, delete_user):
        order_feed_page = OrderFeedPage(driver)
        order_id, order_in_work = order_feed_page.check_in_work(user_data['email'],
                                                                                           user_data['password'])
        assert order_id in order_in_work