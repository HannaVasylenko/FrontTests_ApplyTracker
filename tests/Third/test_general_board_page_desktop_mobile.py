import pytest
from playwright.sync_api import expect


def test_logout_valid_desktop(desktop_user_authorization_for_logout, config_data: dict):
    desktop_user_authorization_for_logout.board.logout()
    expect(desktop_user_authorization_for_logout.locator("main h2")).to_have_text(config_data['title_login_page'])


def test_logout_valid_mobile(mobile_user_authorization_for_logout, config_data: dict):
    mobile_user_authorization_for_logout.board.logout_mobile()
    expect(mobile_user_authorization_for_logout.locator("main h2")).to_have_text(config_data['title_login_page'])


@pytest.mark.skip(reason="Optional verification, no modal window, message")
def test_send_message_in_contact_us_form_valid_desktop(desktop_user_authorization_contact_us_form, config_data: dict):
    desktop_user_authorization_contact_us_form.board.fill_in_fields_contact_us_form(config_data['name_cu'], config_data['text_cu'])
    #expect(desktop_user_authorization_contact_us_form.page.get_by_text(config_data['title_success_window_add_contact_message'])).to_be_visible()


@pytest.mark.skip(reason="Optional verification, no modal window, message")
def test_send_message_in_contact_us_form_valid_mobile(mobile_user_authorization_contact_us_form, config_data: dict):
    mobile_user_authorization_contact_us_form.board.fill_in_fields_contact_us_form(config_data['name_cu'], config_data['text_cu'])
    #expect(mobile_user_authorization_contact_us_form.page.get_by_text(config_data['title_success_window_add_contact_message'])).to_be_visible()
