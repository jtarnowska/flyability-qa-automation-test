from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import GOOGLE_URL


class RegistrationPage(BasePage):

    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//button[contains(., "Accept all")]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[aria-label="Sign in"]')
    EMAIL_INPUT = (By.ID, 'identifierId')
    NEXT_BUTTON = (By.ID, 'identifierNext')
    COULD_NOT_FIND_ACCOUNT_TEXT = (By.XPATH, '//*[contains(text(), "Couldn’t find your Google Account")]')

    def __init__(self, driver):
        super().__init__(driver)

    def open_google(self):
        self.open_url(GOOGLE_URL)

    def accept_cookies(self):
        self.click_on(self.ACCEPT_COOKIES_BUTTON)

    def click_on_sign_in_button(self):
        self.click_on(self.SIGN_IN_BUTTON)

    def enter_email_address(self, email_address):
        self.input_text(self.EMAIL_INPUT, email_address)

    def click_on_next_button(self):
        self.click_on(self.NEXT_BUTTON)

    def get_wrong_email_text(self):
        element = self.find_element(self.COULD_NOT_FIND_ACCOUNT_TEXT)
        return element.text.strip()










