import  pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("test_input", [
    "qwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopadrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwerrtyuijhfdnbvcuasdfg@gmail.com",
    "ab@gmail.co",
    " testing@gmail.com",
    "testing@gmail.com ",
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
def test_email_field_in_forgot_password_window_valid_verifications_mobile(navigate_to_forgot_password_form_mobile, test_input):
    navigate_to_forgot_password_form_mobile.enter_value_in_forgot_password_email_field(test_input)
    expect(navigate_to_forgot_password_form_mobile.locator("//button[text()='Recover']/..//span[@id='inputError-email']")).not_to_be_visible()


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
def test_forgot_password_email_field_invalid_verifications_mobile(navigate_to_forgot_password_form_mobile, test_input, config_data: dict):
    navigate_to_forgot_password_form_mobile.enter_value_in_forgot_password_email_field(test_input)
    expect(navigate_to_forgot_password_form_mobile.locator("//button[text()='Recover']/..//span[@id='inputError-email']")).to_have_text(config_data['email_error_message'])


def test_forgot_password_email_field_by_entering_255_char_negative_verification_mobile(navigate_to_forgot_password_form_mobile, config_data: dict):
    navigate_to_forgot_password_form_mobile.enter_value_in_forgot_password_email_field(config_data['255_char_in_email_field'])
    expect(navigate_to_forgot_password_form_mobile.locator("//button[text()='Recover']/..//span[@id='inputError-email']")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_email_field'])


@pytest.mark.parametrize("test_input", [
    "testing@gmail.ru",
    "testing@gmail.by"
])
def test_forgot_password_email_field_by_entering_ru_by_in_domain_mobile(navigate_to_forgot_password_form_mobile, test_input, config_data: dict):
    navigate_to_forgot_password_form_mobile.enter_value_in_forgot_password_email_field(test_input)
    expect(navigate_to_forgot_password_form_mobile.locator("//button[text()='Recover']/..//span[@id='inputError-email']")).to_have_text(config_data['error_message_by_entering_ru_by_in_email_field'])


def test_close_forgot_password_window_mobile(navigate_to_forgot_password_form_mobile, config_data: dict):
    navigate_to_forgot_password_form_mobile.click_on_close_btn_forgot_password_form()
    expect(navigate_to_forgot_password_form_mobile.locator("form h2")).not_to_be_visible()
