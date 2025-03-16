from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
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
            options = ChromeOptions()
            options.add_argument("--lang=en-GB")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser.lower() == "firefox":
            options = FirefoxOptions()
            options.set_preference("intl.accept_languages", "en-GB")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser.lower() == "edge":
            options = EdgeOptions()
            options.add_argument("--lang=en-GB")
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
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



