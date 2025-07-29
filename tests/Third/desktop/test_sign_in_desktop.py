import pytest
from playwright.sync_api import expect


def test_confirm_password_field_in_sign_in_form_invalid_verification_desktop(sign_in_desktop_app, config_data: dict):
    sign_in_desktop_app.registration.enter_value_in_confirm_password_field(config_data['valid_email'], config_data['valid_password'], config_data['invalid_password'])
    expect(sign_in_desktop_app.locator("span#inputError-confirmPassword")).to_have_text(config_data['passwords_match_error_message'])


@pytest.mark.skip(reason="Open when need to test")
def test_valid_sign_in_user_desktop(sign_in_desktop_app_with_chrome_browser, config_data: dict):
    sign_in_desktop_app_with_chrome_browser.registration.fill_in_register_form_valid(config_data['registration_email'], config_data['registration_password'])
    expect(sign_in_desktop_app_with_chrome_browser.page.get_by_text(config_data['title_sign_in_window'])).to_be_visible()


@pytest.mark.skip(reason="Open when need to test")
def test_already_registered_user_in_sign_in_form_desktop(sign_in_desktop_app, config_data: dict):
    sign_in_desktop_app.registration.fill_in_register_form_valid(config_data['valid_email'], config_data['valid_password'])
    expect(sign_in_desktop_app.page.get_by_text(config_data['title_already_registered_user_error_message'])).to_be_visible()


def test_register_user_without_agreeing_to_privacy_policy_in_sign_in_form_desktop(sign_in_desktop_app, config_data: dict):
    sign_in_desktop_app.registration.fill_in_register_without_agreeing_to_privacy_policy(config_data['valid_email'], config_data['valid_password'])
    expect(sign_in_desktop_app.locator("//button[@type='submit'][contains(@class, 'pointer-events-none')]")).to_be_visible()
