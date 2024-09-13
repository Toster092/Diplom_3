from selenium.webdriver.common.by import By

class PasswordRecoveryLoc:
    LK_BUTTON = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
    RECOVERY_PASS_BUTTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]"
    RECOVERY_TITLE = By.XPATH, "//h2[contains(text(),'Восстановление пароля')]"
    RECOVERY_INPUT = By.XPATH, "//input[@type='text']"
    RECOVERY_BUTTON = By.XPATH, "//button[contains(text(), 'Восстановить')]"
    SAVE_BUTTON = By.XPATH, "//button[contains(text(), 'Сохранить')]"
    EYE_BUTTON = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]"
    PASSWORD_INPUT = By.XPATH, "//input[@type='password']"
    PASSWORD_INPUT_ACTIVE = By.XPATH, "//div[contains(@class, 'input_status_active')]"
