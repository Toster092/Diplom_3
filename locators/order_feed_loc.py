from selenium.webdriver.common.by import By

class OrderFeedLoc:
    ORDER_LIST = By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li"
    FEED_BUTTON = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    ORDER_FEED_TITLE = By.XPATH, "//div[@id='root']//h1[@class='text text_type_main-large mt-10 mb-5']"
    ORDER_TITLE = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"
    USER_ORDER_LIST = By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li"
    CLOSE_ORDER_BUTTON = By.XPATH, "//button[contains(@class, 'close')]"
    OVERLAY = By.XPATH, "//section[@class='Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']"
    ORDER_IN_LIST = By.XPATH, "//li[1]//div[contains(@class, 'OrderHistory_textBox')]"
    ORDER_N = By.XPATH, "//ul[contains(@class,'OrderHistory_profileList')]//li[1]//p"
    MADE_ALL_TIME = By.XPATH, "//div[contains(@class, 'undefined mb-15')]/p[contains(@class, 'OrderFeed_number__')]"
    MADE_TODAY = By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']/div[3]/p[contains(@class, 'OrderFeed_number__')]"
    ORDER_IN_WORK = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]/li[contains(@class, 'text_type_digits-default')]"
    CREATED_ORDER_ID = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"