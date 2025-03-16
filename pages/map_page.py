from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MapPage(BasePage):

    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[contains(., 'Accept all')]")
    TOWN_SEARCH_FROM = (By.ID, "searchboxinput")

    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies(self):
        self.click_on(self.ACCEPT_COOKIES_BUTTON)

    def enter_town_name(self, townname):
        self.input_text(self.TOWN_SEARCH_FROM, "Lausanne")



