from selenium.webdriver.support.expected_conditions import element_to_be_selected

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class MapPage(BasePage):

    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[contains(., 'Accept all')]")
    DIRECTIONS_BUTTON = (By.CSS_SELECTOR, '[aria-label="Directions"]')
    STARTING_POINT_INPUT = (By.CSS_SELECTOR, '[aria-label="Choose starting point, or click on the map..."]')
    DESTINATION_POINT_INPUT = (By.CSS_SELECTOR, '[aria-label="Choose destination, or click on the map..."]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[aria-label="Search"]')

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









