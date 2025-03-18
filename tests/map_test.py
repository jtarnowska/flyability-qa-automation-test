from pages.map_page import MapPage

def test_distance_display(driver):
    map_page = MapPage(driver)
    map_page.open_map()
    map_page.accept_cookies()
    map_page.click_on_directions_button()
    map_page.enter_starting_point("Lausanne")
    map_page.enter_destination_point("Genève")
    map_page.press_enter()
    map_page.assert_text_over_driving_icon("Driving")
    map_page.click_on_driving_button()
    map_page.assert_distance_display()
    map_page.assert_scrolling()
    map_page.save_screenshot_for_specific_test("test_distance_display")

def test_hover_layers(driver):
    map_page = MapPage(driver)
    map_page.open_map()
    map_page.accept_cookies()
    map_page.assert_tooltip_over_layers_button()
    map_page.save_screenshot_for_specific_test("test_hover_layers")