import  pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("test_input", [
    "te",
    "tes",
    "testDesignappTesting",
    "testDesignappTetestDesignappTestingtests",
    "testDesignappTetestDesignappTestingtest",
    "123testing",
    "V_i!rg%in?ia*test",
    "T❄e❄st",
    " testing",
    "testing ",
    "TESTING",
    "тестування",
    "Т’е’с’тув’ання",
    "Т-е-с-тув-ання",
    "testing name field",
    "TeStInG",
    "Émilie",
    "ІванSmith"
])
def test_company_field_in_add_vacancy_window_valid_verifications_desktop(desktop_user_authorization_for_add_vacancy_form, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_company_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-company")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    " ",
    "t"
])
def test_company_field_by_entering_1_char_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, config_data: dict, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_company_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-company")).to_have_text(config_data['error_message_by_entering_less_then_min_quantity_chars_in_company_field'])


def test_company_field_by_entering_41_char_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, config_data: dict):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_company_field(config_data['enter_41_char_in_field'])
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-company")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_company_field'])


@pytest.mark.parametrize("test_input", [
    "te",
    "tes",
    "Averylongname thatexceeds leng",
    "Averylongname thatexceeds len",
    "Averylongnamess",
    "тестування",
    "1234567890testing",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?”=_",
    "TESTING",
    "T❄e❄st",
    "Émilie",
    "TeStInG",
    "Т’е’с’тув’ання",
    "Т-е-с-тув-ання",
    "ІванSmith"
])
def test_position_field_in_add_vacancy_window_valid_verifications_desktop(desktop_user_authorization_for_add_vacancy_form, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_position_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-vacancy")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    " ",
    "t"
])
def test_position_field_by_enter_1_char_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, config_data: dict, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_position_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-vacancy")).to_have_text(config_data['error_message_by_entering_less_then_min_quantity_chars_in_position_field'])


def test_position_field_by_enter_31_char_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, config_data: dict):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_position_field(config_data['enter_31_char_in_field'])
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-vacancy")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_position_field'])


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
    "https://cktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwmentofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwcvbfghdtrgfbnvhjgytubasd.com"
])
def test_job_link_field_in_add_vacancy_window_valid_verifications_desktop(desktop_user_authorization_for_add_vacancy_form, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_job_link_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-link")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    " ",
    "http://.com",
    "example.com",
    "http://example",
    "https://e_xample_example_example.com",
    "https://exa mple.com"
])
def test_job_link_field_in_add_vacancy_window_invalid_verifications_desktop(desktop_user_authorization_for_add_vacancy_form, test_input, config_data: dict):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_job_link_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-link")).to_have_text(config_data['link_error_message'])


@pytest.mark.parametrize("test_input", [
    "tes",
    "test",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_’",
    "1234567890",
    "https://demoqa.com/",
    "https://github.com/microsoft/playwright",
    "https://www.linkedin.com/in/alex-test"
])
def test_communication_channel_field_in_add_vacancy_window_valid_verifications_desktop(desktop_user_authorization_for_add_vacancy_form, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_communication_channel_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-communication")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    " ",
    "t",
    "tt"
])
def test_communication_channel_field_by_entering_less_then_3_char_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, config_data: dict, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_communication_channel_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-communication")).to_have_text(config_data['error_message_by_entering_less_then_min_quantity_chars_in_communication_channel_field'])


def test_communication_channel_field_by_entering_1001_char_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, config_data: dict):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_communication_channel_field(config_data['1001_char_in_note_field'])
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-communication")).to_have_text(config_data['error_message_by_entering_1001_char_in_field'])


@pytest.mark.parametrize("test_input", [
    "test",
    "1234567890",
    "tests",
    "TESTING",
    "тестування",
    "Т’е’с’тув’ання",
    "Т-е-с-тув-ання",
    "testing name field",
    "TeStInG",
    "Émilie",
    "V_i!rg%in?ia*test",
    "ІванSmith"
])
def test_location_field_in_add_vacancy_window_valid_verifications_desktop(desktop_user_authorization_for_add_vacancy_form, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_location_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-location")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    " ",
    "t",
    "tt",
    "ttt"
])
def test_location_field_by_entering_less_then_4_char_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, config_data: dict, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_location_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-location")).to_have_text(config_data['error_message_by_entering_less_then_min_quantity_chars_in_location_field'])


def test_location_field_by_entering_401_char_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, config_data: dict):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_location_field(config_data['enter_401_char_in_field'])
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-location")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_location_field'])


@pytest.mark.parametrize("test_input", [
    "testingapp",
    "testingappp",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_’",
    "1234567890",
    "https://demoqa.com/"
])
def test_note_field_in_add_vacancy_window_valid_verifications_desktop(desktop_user_authorization_for_add_vacancy_form, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_note_field(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-note")).not_to_be_visible()


def test_note_field_in_add_vacancy_window_by_entering_1001_char_desktop(desktop_user_authorization_for_add_vacancy_form, config_data: dict):
    desktop_user_authorization_for_add_vacancy_form.board.enter_value_in_note_field(config_data['1001_char_in_note_field'])
    expect(desktop_user_authorization_for_add_vacancy_form.locator("span#inputError-note")).to_have_text(config_data['notes_error_message'])


@pytest.mark.parametrize("test_input", [
    "remote",
    "office",
    "hybrid"
])
def test_checkbox_work_type_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.select_checkbox_work_type(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator(f"//input[@value='{test_input}']")).to_be_checked()


@pytest.mark.parametrize("test_input", [
    "offer",
    "hr",
    "reject",
    "tech",
    "test",
    "resume"
])
def test_checkboxes_in_status_in_add_vacancy_window_desktop(desktop_user_authorization_for_add_vacancy_form, test_input):
    desktop_user_authorization_for_add_vacancy_form.board.select_status_checkbox(test_input)
    expect(desktop_user_authorization_for_add_vacancy_form.locator(f"#{test_input}")).to_be_checked()
