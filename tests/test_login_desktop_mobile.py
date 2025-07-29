import pytest
from playwright.sync_api import expect


@pytest.mark.skip(reason="Field validation is not used")
def test_login_user_valid_desktop(desktop_app_for_login, config_data: dict):
    login_page = desktop_app_for_login
    valid_email = config_data['valid_email']
    valid_password = config_data['valid_password']
    add_vacancy_button_name = config_data['add_vacancy_btn']
    login_window_text = config_data['login_window_text']

    login_page.fill_in_login_form(valid_email, valid_password)
    login_page.page.get_by_role("button", name=add_vacancy_button_name).wait_for(state='visible')
    expect(login_page.page.get_by_text(login_window_text)).to_be_visible()
    login_page.close_success_login_window_by_clicking_on_close_btn()


@pytest.mark.skip(reason="Field validation is not used")
def test_login_user_valid_mobile(mobile_app_for_login, config_data: dict):
    login_page = mobile_app_for_login
    valid_email = config_data['valid_email']
    valid_password = config_data['valid_password']
    add_vacancy_button_name = config_data['add_vacancy_btn']
    login_window_text = config_data['login_window_text']

    login_page.fill_in_login_form(valid_email, valid_password)
    login_page.page.get_by_role("button", name=add_vacancy_button_name).wait_for(state='visible')
    expect(login_page.page.get_by_text(login_window_text)).to_be_visible()
    login_page.close_success_login_window_by_clicking_on_close_btn()