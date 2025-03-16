import pytest
from pages.map_page import MapPage


@pytest.mark.parametrize("browser", ["chrome"])
def test_enter_town_name(browser):
    map_page = MapPage(browser)
    map_page.open_url("https://www.google.com/maps")
    map_page.accept_cookies()
    map_page.enter_town_name("Lausanne")
    map_page.driver.quit()