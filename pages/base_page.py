import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import datetime


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def input_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click_on(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.click()

    def hover_and_get_text(self, hover_locator, text_locator):
        self.hover(hover_locator)
        return self.wait.until(EC.presence_of_element_located(text_locator)).text.strip()

    def hover_to_get_tooltip(self, hover_locator, target_locator):
        self.hover(hover_locator)
        target_exists = self.check_exists(target_locator)
        if target_exists:
            return True, self.find_element(target_locator)
        return False, None

    def check_exists(self, locator):
        try:
            self.find_element(locator)
        except TimeoutException or NoSuchElementException:
            return False
        return True

    def hover(self, hover_locator):
        element_to_hover = self.find_element(hover_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()
        time.sleep(0.5)  # Needed on Firefox, to ensure visibility of the target locator

    def save_screenshot(self, test_name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"./screenshots/{test_name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)



