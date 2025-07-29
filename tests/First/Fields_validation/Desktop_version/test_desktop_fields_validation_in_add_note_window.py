import  pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("test_input", [
    "tt",
    "юзер",
    "1234567890",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_",
    "😎✌🎁",
    "TEST VARIANT",
    "TeSt TeSt",
    "user name"
])
def test_name_field_valid_in_add_note_window_desktop(desktop_user_authorization_for_add_note_window, config_data: dict, test_input):
    desktop_user_authorization_for_add_note_window.notes.enter_value_in_name_field_in_add_note_window(test_input)
    expect(desktop_user_authorization_for_add_note_window.locator(f"//span[@id='inputError-name']")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    " ",
    "t"
])
def test_name_field_valid_in_add_note_window_desktop(desktop_user_authorization_for_add_note_window, config_data: dict, test_input):
    desktop_user_authorization_for_add_note_window.notes.enter_value_in_name_field_in_add_note_window(test_input)
    expect(desktop_user_authorization_for_add_note_window.locator(f"//span[@id='inputError-noteName']")).to_have_text(config_data['error_message_min_char_notes'])


def test_name_field_by_entering_101char_in_add_note_window_desktop(desktop_user_authorization_for_add_note_window, config_data: dict):
    desktop_user_authorization_for_add_note_window.notes.enter_value_in_name_field_in_add_note_window(config_data['more_then_max_char_in_name_field_in_add_event'])
    expect(desktop_user_authorization_for_add_note_window.locator(f"//span[@id='inputError-noteName']")).to_have_text(config_data[''])


@pytest.mark.parametrize("test_input", [
    "tt",
    "юзер",
    "1234567890",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_",
    "😎✌🎁",
    "TEST VARIANT",
    "TeSt TeSt",
    "user name"
])
def test_text_field_valid_in_add_note_window_desktop(desktop_user_authorization_for_add_note_window, config_data: dict, test_input):
    desktop_user_authorization_for_add_note_window.notes.enter_value_in_text_field_in_add_note_window(test_input)
    expect(desktop_user_authorization_for_add_note_window.locator(f"//span[@id='inputError-text']")).not_to_be_visible()


def test_text_field_by_entering_4001_char_in_add_note_window_desktop(desktop_user_authorization_for_add_note_window, config_data: dict):
    desktop_user_authorization_for_add_note_window.notes.enter_value_in_text_field_in_add_note_window(config_data['enter_4001_char_in_field'])
    expect(desktop_user_authorization_for_add_note_window.locator(f"//span[@id='inputError-text']")).to_have_text(config_data['error_message_by_entering_more_then_4000_char'])
