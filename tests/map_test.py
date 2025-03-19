import re
import pytest
from pages.map_page import MapPage

@pytest.fixture(scope="class")
def map_page(driver):
    map_page = MapPage(driver)
    map_page.open_map()
    map_page.accept_cookies()
    return map_page

class TestMapPage:
    def test_distance_display(self, request, map_page):
        map_page.open_map()
        map_page.click_on_directions_button()
        map_page.enter_starting_point("Lausanne")
        map_page.enter_destination_point("Genève")
        map_page.press_enter()

        driving_text = map_page.get_text_over_driving_icon()
        assert "Driving" in driving_text, f"Expected 'Driving' but got '{driving_text}'"

        map_page.open_driving_panel()

        distance_display = map_page.get_distance_text()
        pattern = r"^\d{1,3}(,\d{3})*(\.\d+)?\s*(km|miles)$"
        assert re.match(pattern, distance_display), f"Distance format is incorrect: {distance_display}"

        restaurant_icon = map_page.scroll_to_restaurants_icon()
        assert restaurant_icon, "Scrolling to the restaurants button failed"

        map_page.save_screenshot(request.node.originalname)

    def test_hover_layers(self, request, map_page):
        map_page.open_map()

        tooltip_exists, tooltip  = map_page.get_tooltip_over_layers_button()
        assert tooltip_exists, "Tooltip over layers button is not visible after hovering"

        map_page.save_screenshot(request.node.originalname)