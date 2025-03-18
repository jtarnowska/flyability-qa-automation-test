from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support import expected_conditions as EC
from utils.config import GOOGLE_MAPS_URL


class MapPage(BasePage):

    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//button[contains(., "Accept all")]')
    DIRECTIONS_BUTTON = (By.CSS_SELECTOR, '[aria-label="Directions"]')
    STARTING_POINT_INPUT = (By.CSS_SELECTOR, '[aria-label="Choose starting point, or click on the map..."]')
    DESTINATION_POINT_INPUT = (By.CSS_SELECTOR, '[aria-label="Choose destination, or click on the map..."]')
    DRIVING_BUTTON = (By.CSS_SELECTOR, '[aria-label="Driving"]')
    DRIVING_TOOLTIP = (By.XPATH, '//div[text()="Driving"]')
    DISTANCE_DISPLAY = (By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[2]/div')
    RESTAURANTS_BUTTON = (By.CSS_SELECTOR, '[aria-label="Restaurants"]')
    LAYERS_BUTTON = (By.CSS_SELECTOR, '[aria-label="Interactive map"]')
    MAP_ITEMS_TOOLTIP = (By.ID, "layer-switcher-quickm")

    def __init__(self, driver):
        super().__init__(driver)

    def open_map(self):
        self.open_url(GOOGLE_MAPS_URL)

    def accept_cookies(self):
        self.click_on(self.ACCEPT_COOKIES_BUTTON)

    def click_on_directions_button(self):
        self.click_on(self.DIRECTIONS_BUTTON)

    def enter_starting_point(self, town_name):
        self.input_text(self.STARTING_POINT_INPUT, town_name)

    def enter_destination_point(self, town_name):
        self.input_text(self.DESTINATION_POINT_INPUT, town_name)

    def press_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.RETURN).perform()

    def open_driving_panel(self):
        self.click_on(self.DRIVING_BUTTON)

    def get_distance_text(self):
        element = self.find_element(self.DISTANCE_DISPLAY)
        return element.text.strip()

    def scroll_to_restaurants_icon(self):
        element = self.find_element(self.RESTAURANTS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return EC.visibility_of_element_located(self.RESTAURANTS_BUTTON)(self.driver)

    def get_text_over_driving_icon(self):
        return self.hover_and_get_text(self.DRIVING_BUTTON, self.DRIVING_TOOLTIP)

    def get_tooltip_over_layers_button(self):
        return self.hover_to_get_tooltip(self.LAYERS_BUTTON, self.MAP_ITEMS_TOOLTIP)















