import pytest
from pages.registration_page import RegistrationPage

class TestRegistrationPage:
    @pytest.mark.smoke
    def test_wrong_email(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open_google()
        registration_page.accept_cookies()
        registration_page.click_on_sign_in_button()
        registration_page.enter_email_address('joanna@gmail.com')
        registration_page.click_on_next_button()

        wrong_email_text = registration_page.get_wrong_email_text()
        assert 'Couldn’t find your Google Account' in wrong_email_text, f"Expected but got '{wrong_email_text}'"

