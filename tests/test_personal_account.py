import allure
from data import Constants

from pages.personal_account_page import PersonalAccountPage
class TestPersonalAccountPage:

    @allure.title('Проверка перехода в личный кабинет')
    def test_go_to_lk_page_success(self, driver):
       personal_account_page = PersonalAccountPage(driver)
       result = personal_account_page.click_on_lk_button()
       assert result == 'Вход'

    @allure.title('Проверка перехода в историю заказов пользователя')
    def test_go_to_order_history_success(self, driver, user_data, delete_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_on_order_history(user_data['email'], user_data['password'])
        assert driver.current_url == f'{Constants.URL}account/order-history'

    @allure.title('Проверка успешного выхода из аккаунта')
    def test_exit_success(self, driver, user_data, delete_user):
        personal_account_page = PersonalAccountPage(driver)
        result = personal_account_page.click_on_exit(user_data['email'], user_data['password'])
        assert result == 'Вход'
