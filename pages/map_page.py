from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support import expected_conditions as EC

class MapPage(BasePage):

    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//button[contains(., "Accept all")]')
    DIRECTIONS_BUTTON = (By.CSS_SELECTOR, '[aria-label="Directions"]')
    STARTING_POINT_INPUT = (By.CSS_SELECTOR, '[aria-label="Choose starting point, or click on the map..."]')
    DESTINATION_POINT_INPUT = (By.CSS_SELECTOR, '[aria-label="Choose destination, or click on the map..."]')
    DRIVING_BUTTON = (By.CSS_SELECTOR, '[aria-label="Driving"]')
    DISTANCE_DISPLAY = (By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[2]/div')
    RESTAURANTS_BUTTON = (By.CSS_SELECTOR, '[aria-label="Restaurants"]')
    WALKING_BUTTON = (By.CSS_SELECTOR, '[aria-label="Walking"]')
    WALKING_TOOLTIP = (By.XPATH, '//div[text()="Walking"]')

    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies(self):
        self.click_on(self.ACCEPT_COOKIES_BUTTON)

    def click_on_directions_button(self):
        self.click_on(self.DIRECTIONS_BUTTON)

    def enter_starting_point(self, townname):
        self.input_text(self.STARTING_POINT_INPUT, townname)

    def enter_destination_point(self, townname):
        self.input_text(self.DESTINATION_POINT_INPUT, townname)

    def press_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.RETURN).perform()

    def click_on_driving_button(self):
        self.click_on(self.DRIVING_BUTTON)

    def assert_distance_display(self):
        element = self.find_element(self.DISTANCE_DISPLAY)
        distance_display = element.text.strip()

        pattern = r"^\d+(\.\d+)?\s*km$"

        assert re.match(pattern, distance_display), f"Distance format is incorrect: {distance_display}"

    def assert_scrolling(self):
        element = self.find_element(self.RESTAURANTS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        assert EC.visibility_of_element_located(self.RESTAURANTS_BUTTON)(self.driver), "Scrolling failed!"

    def assert_text_over_walking_icon(self, expected_text):
        self.hover_and_check_text(self.WALKING_BUTTON, self.WALKING_TOOLTIP, expected_text)












