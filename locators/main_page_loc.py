from selenium.webdriver.common.by import By

class MainPageLoc:
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(),'Конструктор')]"
    FEED_BUTTON = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    ORDER_FEED_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    FLUR_BUN = By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]"
    BUN_TEXT = By.XPATH, "//p[contains(text(),'Жиры, г')]"
    CLOSE_BUTTON = By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button[@type='button']"
    BASKET = By.XPATH, "//span[contains(text(),'Перетяните булочку сюда (верх)')]"
    BASKET_TEXT = By.XPATH, "//p[@class='text text_type_digits-medium mr-3']"
    ORDER_ID_TEXT = By.XPATH, "//p[contains(text(),'идентификатор заказа')]"
    ORDER_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_type_primary') and text()='Оформить заказ']"
    LOGIN_BUTTON_LOCATOR = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"