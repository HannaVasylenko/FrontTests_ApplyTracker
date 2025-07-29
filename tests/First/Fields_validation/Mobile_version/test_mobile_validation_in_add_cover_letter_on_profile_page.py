import  pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("test_input", [
    "tt",
    "ttt",
    "But I must explain to you",
    "юзер",
    "1234567890",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_",
    "😎✌🎁",
    "TEST VARIANT",
    "TeSt TeSt",
    "user name"
])
def test_name_field_valid_in_cover_letter_in_profile_mobile(mobile_authorization_for_cover_letter_on_profile_page, config_data: dict, test_input):
    mobile_authorization_for_cover_letter_on_profile_page.profile.enter_value_in_name_field_in_cover_letter(test_input)
    expect(mobile_authorization_for_cover_letter_on_profile_page.locator(f"//span[@id='inputError-name']")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    "t",
    " "
])
def test_name_field_invalid_in_cover_letter_in_profile_mobile(mobile_authorization_for_cover_letter_on_profile_page, config_data: dict, test_input):
    mobile_authorization_for_cover_letter_on_profile_page.profile.enter_value_in_name_field_in_cover_letter(test_input)
    expect(mobile_authorization_for_cover_letter_on_profile_page.locator(f"//span[@id='inputError-name']")).to_have_text(config_data['error_message_by_entering_less_then_min_quantity_chars_in_name_field_profile'])


def test_name_field_by_entering_51_char_in_cover_letter_in_profile_desktop(mobile_authorization_for_cover_letter_on_profile_page, config_data: dict):
    mobile_authorization_for_cover_letter_on_profile_page.profile.enter_value_in_name_field_in_cover_letter(config_data['enter_51_char_in_field'])
    expect(mobile_authorization_for_cover_letter_on_profile_page.locator(f"//span[@id='inputError-name']")).to_have_text(config_data['error_message_by_entering_51_char'])
    
    
@pytest.mark.parametrize("test_input", [
    "tt",
    "ttt",
    "юзер",
    "1234567890",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_",
    "😎✌🎁",
    "TEST VARIANT",
    "TeSt TeSt",
    "user name"
])
def test_text_field_valid_in_cover_letter_in_profile_mobile(mobile_authorization_for_cover_letter_on_profile_page, config_data: dict, test_input):
    mobile_authorization_for_cover_letter_on_profile_page.profile.enter_value_in_text_field_in_cover_letter(test_input)
    expect(mobile_authorization_for_cover_letter_on_profile_page.locator(f"//span[@id='inputError-text']")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    "t",
    " "
])
def test_text_field_invalid_in_cover_letter_in_profile_mobile(mobile_authorization_for_cover_letter_on_profile_page, config_data: dict, test_input):
    mobile_authorization_for_cover_letter_on_profile_page.profile.enter_value_in_text_field_in_cover_letter(test_input)
    expect(mobile_authorization_for_cover_letter_on_profile_page.locator(f"//span[@id='inputError-text']")).to_have_text(config_data['error_message_by_entering_less_then_min_quantity_chars_in_name_field_profile'])
