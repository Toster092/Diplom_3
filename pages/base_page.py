from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
       self.driver = driver
    def go_to_site(self, URL):
       return self.driver.get(URL)
    def find_element_located(self, locator, time=15):
       return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))
    def find_elements_located(self, locator, time=15):
       return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator))
    def scroll_to_element_located(self, locator):
       element = self.find_element_located(locator)
       self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    def click_on_element(self, locator):
       return self.find_element_located(locator).click()

    def get_text(self, locator):
       return self.find_element_located(locator).text
    def get_element_attribute(self, locator):
       return self.find_element_located(locator).get_attribute('class')
    def input_text(self, locator, text):
       element = self.find_element_located(locator)
       element.send_keys(text)

    def drag_and_drop(self, locator_element_from, locator_element_to):
        from_element = self.find_element_located(locator_element_from)
        to_element = self.find_element_located(locator_element_to)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()

    def scroll_and_click(self, locator):
        element = self.find_element_located(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_with_retry(self, locator, overlay_locator, retries=3, wait_time=10):
        for attempt in range(retries):
            try:
                element = self.find_element_located(locator)
                element.click()
                return
            except ElementClickInterceptedException:
                if overlay_locator:
                    WebDriverWait(self.driver, wait_time).until(
                        expected_conditions.invisibility_of_element_located(overlay_locator)
                    )
                if attempt == retries - 1:
                    raise

    def get_text_visibility_of_all_element(self, locator):
        return self.find_element_located_presence(locator).text

    def find_element_located_presence(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located(locator))

    def click_virt_mouse(self, locator):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    def element_is_visible(self, locator: tuple[str, str], timeout: int = 15):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def click_element_js(self, locator: tuple[str, str], timeout: int = 15):
        element = self.find_element_located(locator, timeout)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
        else:
            return None

    def wait_element_to_be_clickable(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        except TimeoutException:
            return None

    def wait_for_element_to_disappear(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until_not(expected_conditions.presence_of_element_located(locator))

