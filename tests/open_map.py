import pytest
from pages.map_page import MapPage

@pytest.mark.parametrize("browser", ["chrome"])
def test_enter_town_name(browser):
    map_page = MapPage(browser)
    map_page.open_url("https://www.google.com/maps")
    map_page.accept_cookies()
    map_page.click_on_directions_button()
    map_page.enter_starting_point("Lausanne")
    map_page.enter_destination_point("Genève")
    map_page.press_enter()
    map_page.driver.quit()