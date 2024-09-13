import allure
from data import Constants

from pages.main_page import MainPage
class TestMainPage:
    @allure.title('Проверка перехода по кнопке "Конструктор"')
    def test_go_to_constructor_page(self, driver):
       main_page = MainPage(driver)
       main_page.click_on_constructor_button()
       assert driver.current_url == Constants.URL

    @allure.title('Проверка перехода в ленту заказов')
    def test_go_to_feed_orders_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_feed_order_button()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/feed'

    @allure.title('Проверка открытия всплывающего окна с деталями ингридиента')
    def test_go_to_ingridient_window(self, driver):
        main_page = MainPage(driver)
        result = main_page.click_on_ingredient_button()
        assert result == 'Жиры, г'

    @allure.title('Проверка закрытия всплывающего окна с деталями ингридиента')
    def test_close_ingridient_window(self, driver):
        main_page = MainPage(driver)
        result = main_page.click_on_close_button()
        assert result == 'Войти в аккаунт'

    @allure.title('Проверка увеличине счетчика ингридиента при добавлении его в заказ')
    def test_add_ingridient_to_basket(self, driver):
        main_page = MainPage(driver)
        result = main_page.drag_and_drop_ingredient_to_basket()
        assert result == '1976'

    @allure.title('Проверка создания заказа авторизованным пользователем')
    def test_create_order_auth_user(self, driver, user_data, delete_user):
        main_page = MainPage(driver)
        result = main_page.get_order_id(user_data['email'], user_data['password'])
        assert result == 'идентификатор заказа'


