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
def test_name_field_valid_in_link_in_profile_mobile(mobile_authorization_for_link_on_profile_page, config_data: dict, test_input):
    mobile_authorization_for_link_on_profile_page.profile.enter_value_in_name_field_in_link(test_input)
    expect(mobile_authorization_for_link_on_profile_page.locator(f"//span[@id='inputError-name']")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    "t",
    " "
])
def test_name_field_invalid_in_link_in_profile_mobile(mobile_authorization_for_link_on_profile_page, config_data: dict, test_input):
    mobile_authorization_for_link_on_profile_page.profile.enter_value_in_name_field_in_link(test_input)
    expect(mobile_authorization_for_link_on_profile_page.locator(f"//span[@id='inputError-name']")).to_have_text(config_data['error_message_by_entering_less_then_min_quantity_chars_in_name_field_profile'])


def test_name_field_by_entering_51_char_in_link_in_profile_desktop(mobile_authorization_for_link_on_profile_page, config_data: dict):
    mobile_authorization_for_link_on_profile_page.profile.enter_value_in_name_field_in_link(config_data['enter_51_char_in_field'])
    expect(mobile_authorization_for_link_on_profile_page.locator(f"//span[@id='inputError-name']")).to_have_text(config_data['error_message_by_entering_51_char'])
    
    
@pytest.mark.parametrize("test_input", [
    "http://example.com",
    "https://example.com",
    "https://EXAMPLE.com",
    "https://Example.COM",
    "https://ex.com",
    "https://example.co",
    "https://exa1234567890mple.com",
    "https://sub.sub.example.com",
    "https://e-xample-example-example.com",
    "https://1example.com",
    "https://example1.com",
    "https://t.me/username",
    "https://www.behance.net/yourusername/projectname",
    "https://www.linkedin.com/in/alex-test",
    "https://github.com/microsoft/playwright-python.git"
])
def test_link_field_valid_in_link_in_profile_mobile(mobile_authorization_for_link_on_profile_page, config_data: dict, test_input):
    mobile_authorization_for_link_on_profile_page.profile.enter_value_in_link_field_in_link(test_input)
    expect(mobile_authorization_for_link_on_profile_page.locator(f"//span[@id='inputError-link']")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    " ",
    "https://exa mple.com",
    "example.com",
    "http://example",
    "https://e_xample_example_example.com",
    "http://.com"
])
def test_link_field_invalid_in_link_in_profile_mobile(mobile_authorization_for_link_on_profile_page, config_data: dict, test_input):
    mobile_authorization_for_link_on_profile_page.profile.enter_value_in_link_field_in_link(test_input)
    expect(mobile_authorization_for_link_on_profile_page.locator(f"//span[@id='inputError-link']")).to_have_text(config_data['error_message_by_entering_invalid_link_in_profile'])
