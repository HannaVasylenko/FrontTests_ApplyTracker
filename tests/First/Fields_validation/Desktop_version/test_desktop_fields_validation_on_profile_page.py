import  pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("test_input", [
    "t",
    "tt",
    "юзер",
    "1234567890",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_",
    "😎✌🎁",
    "TEST VARIANT",
    "TeSt TeSt",
    "user name"
    " ",
    ""
])
def test_user_name_field_in_personal_info_form_desktop(desktop_user_authorization_for_profile_page, config_data: dict, test_input):
    desktop_user_authorization_for_profile_page.profile.fill_user_name_in_personal_info(test_input)
    expect(desktop_user_authorization_for_profile_page.locator("section.Toastify p")).to_contain_text("Name successfully updated")
    desktop_user_authorization_for_profile_page.locator("section.Toastify p").wait_for(state='hidden')


@pytest.mark.skip(reason="Duplicate")
@pytest.mark.parametrize("test_input", [
    " ",
    "😁✌😎",
    "abcde",
    "привітики"
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_"
])
def test_phone_number_field_in_personal_info_form_desktop(desktop_user_authorization_for_profile_page, config_data: dict, test_input):
    desktop_user_authorization_for_profile_page.profile.fill_phone_number_in_personal_info(test_input)
    expect(desktop_user_authorization_for_profile_page.locator("#inputError-phone")).to_have_text(config_data['phone_profile_error_message'])
    desktop_user_authorization_for_profile_page.locator("section.Toastify p").wait_for(state='hidden')


# "0999999999",
#     "099999999"
@pytest.mark.parametrize("test_input", [
    "123",
    "112345",
    "+380999999999",
    "0999999999",
    "099999999"
])
def test_phone_number_field_in_personal_info_form_valid_desktop(desktop_user_authorization_for_profile_page, config_data: dict, test_input):
    desktop_user_authorization_for_profile_page.profile.fill_phone_number_in_personal_info(test_input)
    expect(desktop_user_authorization_for_profile_page.locator("#inputError-phone")).not_to_be_visible()
    desktop_user_authorization_for_profile_page.locator("section.Toastify p").wait_for(state='hidden')


@pytest.mark.parametrize("test_input", [
    "1",
    "12",
    " ",
    "привітики",
    "😎✌🎁",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_"
])
def test_phone_number_field_in_personal_info_form_invalid_desktop(desktop_user_authorization_for_profile_page, config_data: dict, test_input):
    desktop_user_authorization_for_profile_page.profile.fill_phone_number_in_personal_info(test_input)
    expect(desktop_user_authorization_for_profile_page.locator("#inputError-phone")).to_have_text(config_data['error_message_phone_profile_page'])
    # desktop_user_authorization_for_profile_page.locator("section.Toastify p").wait_for(state='hidden')
