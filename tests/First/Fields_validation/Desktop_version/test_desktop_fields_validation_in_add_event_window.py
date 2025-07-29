from datetime import datetime, timedelta
import  pytest
from playwright.sync_api import expect


def test_name_field_in_add_event_window_by_entering_space_desktop(desktop_add_event_window_on_statistic_page, config_data: dict):
    desktop_add_event_window_on_statistic_page.statistic.type_in_name_field(" ")
    expect(desktop_add_event_window_on_statistic_page.locator("span#inputError-soonEventName")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_name_field_event'])


@pytest.mark.parametrize("test_input", [
    "юзер",
    "1234567890",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_",
    "But I must explain to you",
    "😎✌🎁",
    "TEST VARIANT",
    "TeSt TeSt",
    "a",
    "ab",
    "user name"
])
def test_name_field_in_add_event_window_valid_desktop(desktop_add_event_window_on_statistic_page, config_data: dict, test_input):
    desktop_add_event_window_on_statistic_page.statistic.type_in_name_field(test_input)
    expect(desktop_add_event_window_on_statistic_page.locator("span#inputError-soonEventName")).not_to_be_visible()


def test_name_field_in_add_event_window_by_entering_51_char_desktop(desktop_add_event_window_on_statistic_page, config_data: dict):
    desktop_add_event_window_on_statistic_page.statistic.type_in_name_field(config_data['enter_51_char_in_field'])
    expect(desktop_add_event_window_on_statistic_page.locator("span#inputError-soonEventName")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_name_field_event'])


@pytest.mark.parametrize("test_input", [
    "юзер",
    "t",
    "tt",
    "1234567890",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_",
    "😎✌🎁",
    "TEST VARIANT",
    "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of hu",
    "TeSt TeSt",
    " ",
    "user name"
])
def test_note_field_in_add_event_window_valid_desktop(desktop_add_event_window_on_statistic_page, config_data: dict, test_input):
    desktop_add_event_window_on_statistic_page.statistic.type_in_note_field(test_input)
    expect(desktop_add_event_window_on_statistic_page.locator("span#inputError-soonEventNotes")).not_to_be_visible()


def test_note_field_in_add_event_window_by_entering_1001_char_desktop(desktop_add_event_window_on_statistic_page, config_data: dict):
    desktop_add_event_window_on_statistic_page.statistic.type_in_note_field(config_data['1001_char_in_note_field'])
    expect(desktop_add_event_window_on_statistic_page.locator("span#inputError-soonEventNotes")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_note_field_event'])


def test_select_day_in_calender_in_add_event_window_desktop(desktop_add_event_window_on_statistic_page, config_data: dict):
    desktop_add_event_window_on_statistic_page.statistic.select_calender_day_in_add_event_window()
    now = datetime.now() + timedelta(days=2)
    formatted_date = now.strftime("%e").strip()
    button_locator = desktop_add_event_window_on_statistic_page.page.locator(f"//aside/../following-sibling::div//div[@class='react-calendar__month-view__days']//abbr[@aria-label='{now.strftime('%B')} {formatted_date}, {now.year}']/..")
    assert "react-calendar__tile--active" in button_locator.get_attribute("class")


def test_add_event_with_expired_date_desktop(desktop_add_event_window_on_statistic_page, config_data: dict):
    now = datetime.now() - timedelta(days=1)
    formatted_date = now.strftime("%e").strip()
    expect(desktop_add_event_window_on_statistic_page.locator(f"//aside/../following-sibling::div//div[@class='react-calendar__month-view__days']//abbr[@aria-label='{now.strftime('%B')} {formatted_date}, {now.year}']/..")).to_be_disabled()
