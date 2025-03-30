import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.config import BROWSER_LANGUAGE


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure using hook"""
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")  # Get driver from fixture
        if driver:
            # Save the screenshot
            screenshots_dir = "../screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_name = f"{item.nodeid.replace('::', '_').replace('.', '_')}.png"
            screenshot_name_normalized = "failed_" + get_last_path_segment(screenshot_name)
            screenshot_path = os.path.join(screenshots_dir, screenshot_name_normalized)

            driver.save_screenshot(screenshot_path)
            print(f"\n[INFO] Screenshot saved: {screenshot_path}")

def get_last_path_segment(path):
    """Returns the last segment of a given path"""
    return path.split('/')[-1]

def pytest_addoption(parser):
    """Custom Pytest command line options"""
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def driver(request):
    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument(f"--lang={BROWSER_LANGUAGE}")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", BROWSER_LANGUAGE)
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument(f"--lang={BROWSER_LANGUAGE}")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        print("No browser is selected")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

