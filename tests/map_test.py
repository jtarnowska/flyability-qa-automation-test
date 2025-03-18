import re

from pages.map_page import MapPage

def test_distance_display(driver):
    map_page = MapPage(driver)
    map_page.open_map()
    map_page.accept_cookies()
    map_page.click_on_directions_button()
    map_page.enter_starting_point("Lausanne")
    map_page.enter_destination_point("Genève")
    map_page.press_enter()

    driving_text = map_page.get_text_over_driving_icon()
    assert "Driving" in driving_text, f"Expected 'Driving' but got '{driving_text}'"

    map_page.click_on_driving_button()

    distance_display = map_page.get_distance_display_text()
    pattern = r"^\d+(\.\d+)?\s*km$"
    assert re.match(pattern, distance_display), f"Distance format is incorrect: {distance_display}"

    is_scrolling_successful = map_page.scroll_to_restaurants_icon()
    assert is_scrolling_successful, "Scrolling to the restaurants button failed"

    map_page.save_screenshot_for_specific_test("test_distance_display")

def test_hover_layers(driver):
    map_page = MapPage(driver)
    map_page.open_map()
    map_page.accept_cookies()

    is_tooltip_visible = map_page.get_tooltip_over_layers_button()
    assert is_tooltip_visible, "Tooltip over layers button is not visible after hovering"

    map_page.save_screenshot_for_specific_test("test_hover_layers")