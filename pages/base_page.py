from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class BasePage:
    def __init__(self, browser = "chrome"):
        self.driver = self.initialize_driver(browser)
        self.wait = WebDriverWait(self.driver, 10)

    def initialize_driver(self, browser):
        if browser.lower() == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser.lower() == "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError("Unsupported browser! Choose from 'chrome', 'firefox' and 'edge'.")

        driver.maximize_window()
        return driver

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