from selenium.webdriver.common.by import By

class PersonalAccountLoc:
    LK_BUTTON = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
    LK_TITLE = By.XPATH, "//h2[contains(text(),'Вход')]"
    MAIL_INPUT = By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input[@name='name']"
    PASSWORD_INPUT = By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input[@name='Пароль']"
    LOGIN_SUBMIT_BUTTON = By.XPATH, "//button[contains(text(),'Войти')]"
    ORDER_HISTORY_BUTTON = By.XPATH, "//a[contains(text(),'История заказов')]"
    USER_ORDER_LIST = By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]"
    EXIT_BUTTON = By.XPATH, "//button[contains(text(),'Выход')]"