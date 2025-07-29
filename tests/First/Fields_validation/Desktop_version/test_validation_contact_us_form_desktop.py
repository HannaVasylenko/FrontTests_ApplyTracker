import  pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("test_input", [
    "te",
    "tes",
    "testDesignappTe",
    "testDesignappTetestDesignappTe",
    "TESTING",
    "тестування",
    "Т’е’с’тув’ання",
    "Т-е-с-тув-ання",
    "testing name field",
    "TeStInG",
    "ІванSmith"
])
def test_name_field_in_contact_us_form_valid_verifications_desktop(desktop_user_authorization_for_contact_us_form, test_input):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_name_field_contact_us_form(test_input)
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-name")).not_to_be_visible()


# Do format?
@pytest.mark.parametrize("test_input", [
    "123testing",
    "testing456",
    "tes789ting",
    "V_i!rg%in?ia*test",
    "T❄e❄st",
    "J. K. Rowling",
    "R%C3%A9n%C3%A9e",
    "`testing",
    "testing'",
    "-testing",
    "testing-",
    "Пръерплрт",
    "Орамыьтор",
    "апмЭтиор",
    "потлоЁьтбоа",
    "Тиитрэтьтор",
    "Иимпаётир",
    "вапвЫвапіра",
    "іавпвмЪисавап"
])
def test_name_field_in_contact_us_form_invalid_verifications_desktop(desktop_user_authorization_for_contact_us_form, test_input, config_data: dict):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_name_field_contact_us_form(test_input)
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-name")).to_have_text(config_data['name_error_message'])


@pytest.mark.parametrize("test_input", [
    "t"
])
def test_name_field_in_contact_us_form_by_entering_1_char_desktop(desktop_user_authorization_for_contact_us_form, config_data: dict, test_input):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_name_field_contact_us_form(test_input)
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-name")).to_have_text(config_data['error_message_by_entering_less_then_min_quantity_chars_in_name_field'])


def test_name_field_in_contact_us_form_by_entering_31_char_desktop(desktop_user_authorization_for_contact_us_form, config_data: dict):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_name_field_contact_us_form(config_data['enter_31_char_in_field'])
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-name")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_name_field'])


@pytest.mark.parametrize("test_input", [
    "qwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopadrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwerrtyuijhfdnbvcuasdfg@gmail.com",
    "ab@gmail.co",
    "a!#%*+=’a@gmail.com",
    "abc@gmail.co",
    "test@gmail.co",
    "testing890@gmail.com",
    "123testing@gmail.com",
    "1234567890@gmail.com",
    "testing@g123l.com",
    "t_e_stin_gexp@gmail.com",
    "t.e.stin.gexp@gmail.com",
    "t-e-stin-gexp@gmail.com",
    "test@sub.domain.example.com",
    "test@gmail.com.com",
    "TESTING@gmail.com",
    "teSTIng@gmail.com"
])
def test_email_field_in_contact_us_form_valid_verifications_desktop(desktop_user_authorization_for_contact_us_form, test_input):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_email_field_contact_us_form(test_input)
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-email")).not_to_be_visible()


# spaces format?
@pytest.mark.parametrize("test_input", [
    "a@gmail.co",
    "test ing@gmail.com",
    "testing@gm ail.com",
    "привіт@gmail.com",
    "testing@gmail.coм",
    "testing@gmail.co1",
    "test ing@gmail.com",
    "testing@gm ail.com",
    "testing@gmail.co m",
    "testing@",
    "test@gmail.c",
    "test@gmail.",
    "@gmail.com",
    "testgmail.com",
    "testing@gmail.co@m",
    "tes@ting@gmail.com",
    "test..ing@gmail.com",
    ".testing@gmail.com",
    "testing.@gmail.com",
    "test💻ing@gmail.com",
    "testing@gmail.co..m",
    "testing@[123.123.123.123]",
    "testing@gmail.com."
])
def test_email_field_in_contact_us_form_invalid_verifications_desktop(desktop_user_authorization_for_contact_us_form, test_input, config_data: dict):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_email_field_contact_us_form(test_input)
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-email")).to_have_text(config_data['email_error_message'])


def test_email_field_in_contact_us_form_by_entering_255_char_desktop(desktop_user_authorization_for_contact_us_form, config_data: dict):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_email_field_contact_us_form(config_data['255_char_in_email_field'])
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-email")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_email_field'])


@pytest.mark.parametrize("test_input", [
    "testing@gmail.ru",
    "testing@gmail.by"
])
def test_email_field__by_entering_ru_by_in_domain_in_contact_us_form_desktop(desktop_user_authorization_for_contact_us_form, test_input, config_data: dict):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_email_field_contact_us_form(test_input)
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-email")).to_have_text(config_data['error_message_by_entering_ru_by_in_email_field'])


@pytest.mark.parametrize("test_input", [
    "testingapp",
    "testingappp",
    "!().,:;<>[]{}~₴@#$%^&*+/|\?””’’=-_’",
    "1234567890"
])
def test_request_text_field_in_contact_us_form_valid_verifications_desktop(desktop_user_authorization_for_contact_us_form, test_input):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_request_text_field_contact_us_form(test_input)
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-requestText")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    "a",
    "aa",
    "aaaaa",
    "aaaaaaaaa"
])
def test_request_text_field_in_contact_us_form_by_entering_more_less_then_min_count_char_desktop(desktop_user_authorization_for_contact_us_form, config_data: dict, test_input):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_request_text_field_contact_us_form(test_input)
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-requestText")).to_have_text(config_data['request_text_error_message_by_entering_less_then_min_count_char'])


def test_request_text_field_in_contact_us_form_by_entering_4001_char_desktop(desktop_user_authorization_for_contact_us_form, config_data: dict):
    desktop_user_authorization_for_contact_us_form.board.enter_value_in_request_text_field_contact_us_form(config_data['enter_4001_char_in_field'])
    expect(desktop_user_authorization_for_contact_us_form.locator("span#inputError-requestText")).to_have_text(config_data['error_message_message_text_more_max_char_contact_us'])
