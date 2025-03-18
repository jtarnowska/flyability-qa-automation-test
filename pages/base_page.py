import time
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

    def hover_and_check_text(self, hover_locator, text_locator, expected_text):
        element_to_hover = self.find_element(hover_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()
        time.sleep(0.5)  # Needed for Firefox to process visibility of tooltip
        text_element = self.wait.until(EC.presence_of_element_located(text_locator))
        actual_text = text_element.text
        assert expected_text in actual_text, f"Expected '{expected_text}', but got '{actual_text}'"

    def hover_and_check_element_visibility(self, hover_locator, target_locator):
        element_to_hover = self.find_element(hover_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()
        time.sleep(0.5) # Needed for Firefox to process visibility of tooltip
        target_element = self.find_element(target_locator)
        assert target_element.is_displayed(), f"Element {target_locator} is not visible after hovering."

    def save_screenshot(self, test_name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"./screenshots/{test_name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)



