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
def test_email_field_in_sign_in_form_valid_verifications_mobile(sign_in_mobile_app, test_input):
    sign_in_mobile_app.registration.enter_value_in_email_field_registration_form(test_input)
    expect(sign_in_mobile_app.locator("span#inputError-email")).not_to_be_visible()


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
def test_email_field_in_sign_in_form_invalid_verifications_mobile(sign_in_mobile_app, test_input, config_data: dict):
    sign_in_mobile_app.registration.enter_value_in_email_field_registration_form(test_input)
    expect(sign_in_mobile_app.locator("span#inputError-email")).to_have_text(config_data['email_error_message'])


def test_email_field_in_sign_in_form_by_entering_255_char_negative_verification_mobile(sign_in_mobile_app, config_data: dict):
    sign_in_mobile_app.registration.enter_value_in_email_field_registration_form(config_data['255_char_in_email_field'])
    expect(sign_in_mobile_app.locator("span#inputError-email")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_email_field'])


@pytest.mark.parametrize("test_input", [
    "testing@gmail.ru",
    "testing@gmail.by"
])
def test_email_field_in_sign_in_form_by_entering_ru_by_in_domain_mobile(sign_in_mobile_app, test_input, config_data: dict):
    sign_in_mobile_app.registration.enter_value_in_email_field_registration_form(test_input)
    expect(sign_in_mobile_app.locator("span#inputError-email")).to_have_text(config_data['error_message_by_entering_ru_by_in_email_field'])


@pytest.mark.parametrize("test_input", [
    "Tes1ing@",
    "Tes1ing@a",
    "Tes1ing@design",
    "Tes1ing@desig",
    "1esT@ing",
    "esT@ing1",
    "@es1ingT",
    "T!e#g@a%p3p",
    "Tes1in!gapp",
    "Tes1in#gapp",
    "T$es1ingapp",
    "Tes%1ingapp",
    "Tes1i^ngapp",
    "Tes1ing&app",
    "t1234567890%A",
    "t!@#$%^&E1s",
    "@Test1ing@",
    "1Test%ing1"
])
def test_password_field_in_sign_in_form_valid_verifications_mobile(sign_in_mobile_app, test_input, config_data: dict):
    sign_in_mobile_app.registration.enter_value_in_password_field_register_form(test_input)
    expect(sign_in_mobile_app.locator("span#inputError-password")).not_to_be_visible()


@pytest.mark.parametrize("test_input", [
    "Tes 1ing@",
    "tes1in@g",
    "Testin@g",
    "Tes1ingapp",
    "TES1UNG@",
    "Tes1i💻ng@",
    "Tes1in g@app",
    "tE*st’in(ga1?p"
])
def test_password_field_in_sign_in_form_invalid_verifications_mobile(sign_in_mobile_app, test_input, config_data: dict):
    sign_in_mobile_app.registration.enter_value_in_password_field_register_form(test_input)
    expect(sign_in_mobile_app.locator("span#inputError-password")).to_have_text(config_data['password_error_message'])


@pytest.mark.parametrize("test_input", [
    " ",
    "t",
    "Te1ing@"
])
def test_password_field_in_sign_in_form_by_entering_less_then_8_char_mobile(sign_in_mobile_app, test_input, config_data: dict):
    sign_in_mobile_app.registration.enter_value_in_password_field_register_form(test_input)
    expect(sign_in_mobile_app.locator("span#inputError-password")).to_have_text(config_data['password_error_message_by_entering_1_char'])


def test_password_field_in_sign_in_form_by_entering_15_char_mobile(sign_in_mobile_app, config_data: dict):
    sign_in_mobile_app.registration.enter_value_in_password_field_register_form(config_data['15_char_in_password_field'])
    expect(sign_in_mobile_app.locator("span#inputError-password")).to_have_text(config_data['error_message_by_entering_more_then_15_char_in_password_field'])


def test_show_passwords_after_clicking_on_eye_icon_in_sign_in_form_mobile(sign_in_mobile_app, config_data: dict):
    registration = sign_in_mobile_app.registration
    password_fields = {
        "password": "input#input-password",
        "confirm_password": "input#input-confirmPassword"
    }

    for field, selector in password_fields.items():
        toggle_method = getattr(registration, f"show_{field}_after_click_on_eye_icon")

        toggle_method(config_data['valid_password'])
        expect(sign_in_mobile_app.locator(selector)).to_have_attribute("type", "text")

        toggle_method(config_data['valid_password'])
        expect(sign_in_mobile_app.locator(selector)).to_have_attribute("type", "password")
