import allure

from pages.password_recovery_page import PasswordRecoveryPage
class TestPasswordRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_go_to_password_recovery_page(self, driver):
       password_recovery_page = PasswordRecoveryPage(driver)
       result = password_recovery_page.click_on_recovery_button()
       assert result == 'Восстановление пароля'

    @allure.title('Проверка перехода по кнопке "Восстановить пароль" с введенными данными email')
    def test_input_email(self, driver):
       password_recovery_page = PasswordRecoveryPage(driver)
       result = password_recovery_page.input_email()
       assert result == 'Сохранить'

    @allure.title('Проверка перехода поля "Пароль" в актиный статус при нажатии кнопки "показать/скрыть пароль"')
    def test_password_field_active(self, driver):
       password_recovery_page = PasswordRecoveryPage(driver)
       result = password_recovery_page.click_on_eye_button()
       assert result == 'input pr-6 pl-6 input_type_text input_size_default input_status_active'


