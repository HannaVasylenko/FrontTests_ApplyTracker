import  pytest
from playwright.sync_api import expect


# Field validation has been disabled and is not used on the project!


@pytest.mark.skip(reason="Field validation is not used")
@pytest.mark.parametrize("test_input", [
    "qwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopadrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwerrtyuijhfdnbvcuasdfg@gmail.com",
    "ab@gmail.co",
    " testing@gmail.com",
    "testing@gmail.com ",
    " testing@gmail.com ",
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
def test_email_field_valid_verifications_desktop(desktop_app, test_input):
    desktop_app.enter_value_in_email_field(test_input)
    expect(desktop_app.page.locator("span#inputError-email")).not_to_be_visible()


@pytest.mark.skip(reason="Field validation is not used")
@pytest.mark.parametrize("test_input", [
    "qwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopadrftgqwertyuiopaqwertyuiopasdfghjklqqawsedrftgqwertyuiopaqwerrtyuijhfdnbvcuasdfg@gmail.com",
    "ab@gmail.co",
    " testing@gmail.com",
    "testing@gmail.com ",
    " testing@gmail.com ",
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
def test_email_field_valid_verifications_mobile(mobile_app, test_input):
    mobile_app.enter_value_in_email_field(test_input)
    expect(mobile_app.page.locator("span#inputError-email")).not_to_be_visible()


@pytest.mark.skip(reason="Field validation is not used")
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
def test_email_field_invalid_verifications_desktop(desktop_app, test_input, config_data: dict):
    desktop_app.enter_value_in_email_field(test_input)
    expect(desktop_app.locator("span#inputError-email")).to_have_text(config_data['email_error_message'])


@pytest.mark.skip(reason="Field validation is not used")
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
def test_email_field_invalid_verifications_mobile(mobile_app, test_input, config_data: dict):
    mobile_app.enter_value_in_email_field(test_input)
    expect(mobile_app.locator("span#inputError-email")).to_have_text(config_data['email_error_message'])


# TODO need clarification
@pytest.mark.skip(reason="need clarification + mobile version")
def test_email_field_by_entering_space_desktop(desktop_app, config_data: dict):
    desktop_app.enter_value_in_email_field(" ")
    expect(desktop_app.locator("span#inputError-email")).to_have_text(config_data['email_error_message'])


@pytest.mark.skip(reason="Field validation is not used")
def test_email_field_by_entering_255_char_negative_verification_desktop(desktop_app, config_data: dict):
    desktop_app.enter_value_in_email_field(config_data['255_char_in_email_field'])
    expect(desktop_app.locator("span#inputError-email")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_email_field'])


@pytest.mark.skip(reason="Field validation is not used")
def test_email_field_by_entering_255_char_negative_verification_mobile(mobile_app, config_data: dict):
    mobile_app.enter_value_in_email_field(config_data['255_char_in_email_field'])
    expect(mobile_app.locator("span#inputError-email")).to_have_text(config_data['error_message_by_entering_more_then_max_quantity_chars_in_email_field'])


@pytest.mark.skip(reason="Field validation is not used")
@pytest.mark.parametrize("test_input", [
    "testing@gmail.ru",
    "testing@gmail.by"
])
def test_email_field__by_entering_ru_by_in_domain_desktop(desktop_app, test_input, config_data: dict):
    desktop_app.enter_value_in_email_field(test_input)
    expect(desktop_app.locator("span#inputError-email")).to_have_text(config_data['error_message_by_entering_ru_by_in_email_field'])


@pytest.mark.skip(reason="Field validation is not used")
@pytest.mark.parametrize("test_input", [
    "testing@gmail.ru",
    "testing@gmail.by"
])
def test_email_field__by_entering_ru_by_in_domain_mobile(mobile_app, test_input, config_data: dict):
    mobile_app.enter_value_in_email_field(test_input)
    expect(mobile_app.locator("span#inputError-email")).to_have_text(config_data['error_message_by_entering_ru_by_in_email_field'])


@pytest.mark.skip(reason="Field validation is not used")
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
def test_password_field_valid_verifications_desktop(desktop_app, test_input, config_data: dict):
    desktop_app.enter_value_in_password_field(test_input)
    expect(desktop_app.locator("span#inputError-password")).not_to_be_visible()


@pytest.mark.skip(reason="Field validation is not used")
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
def test_password_field_valid_verifications_mobile(mobile_app, test_input, config_data: dict):
    mobile_app.enter_value_in_password_field(test_input)
    expect(mobile_app.locator("span#inputError-password")).not_to_be_visible()


@pytest.mark.skip(reason="Field validation is not used")
@pytest.mark.parametrize("test_input", [
    "Tes 1ing@",
    "tes1in@g",
    "Testin@g",
    "Tes1ingapp",
    "TES1UNG@",
    "Tes1i💻ng@",
    "Tes1in g@app",
    "Tes1ing@designaqwer12345",
    "tE*st’in(ga1?p"
])
def test_password_field_invalid_verifications_desktop(desktop_app, test_input, config_data: dict):
    desktop_app.enter_value_in_password_field(test_input)
    expect(desktop_app.locator("span#inputError-password")).to_have_text(config_data['password_error_message'])


@pytest.mark.skip(reason="Field validation is not used")
@pytest.mark.parametrize("test_input", [
    "",
    " ",
    "t",
    "Te1ing@",
    "tt"
])
def test_password_field_by_entering_1_char_desktop(desktop_app, test_input, config_data: dict):
    desktop_app.enter_value_in_password_field(test_input)
    expect(desktop_app.locator("span#inputError-password")).to_have_text(config_data['password_error_message_by_entering_1_char'])


@pytest.mark.skip(reason="Field validation is not used")
@pytest.mark.parametrize("test_input", [
    "Tes 1ing@",
    "tes1in@g",
    "Testin@g",
    "Tes1ingapp",
    "TES1UNG@",
    "Tes1i💻ng@",
    "Tes1in g@app",
    "Tes1ing@designaqwer12345",
    "tE*st’in(ga1?p"
])
def test_password_field_invalid_verifications_mobile(mobile_app, test_input, config_data: dict):
    mobile_app.enter_value_in_password_field(test_input)
    expect(mobile_app.locator("span#inputError-password")).to_have_text(config_data['password_error_message'])


@pytest.mark.skip(reason="Field validation is not used")
@pytest.mark.parametrize("test_input", [
    "",
    " ",
    "t",
    "Te1ing@",
    "tt"
])
def test_password_field_by_entering_1_char_mobile(mobile_app, test_input, config_data: dict):
    mobile_app.enter_value_in_password_field(test_input)
    expect(mobile_app.locator("span#inputError-password")).to_have_text(config_data['password_error_message_by_entering_1_char'])


@pytest.mark.skip(reason="Field validation is not used")
def test_password_field_by_entering_15_char_desktop(desktop_app, config_data: dict):
    desktop_app.enter_value_in_password_field(config_data['15_char_in_password_field'])
    expect(desktop_app.locator("span#inputError-password")).to_have_text(config_data['error_message_by_entering_more_then_15_char_in_password_field'])


@pytest.mark.skip(reason="Field validation is not used")
def test_password_field_by_entering_15_char_mobile(mobile_app, config_data: dict):
    mobile_app.enter_value_in_password_field(config_data['15_char_in_password_field'])
    expect(mobile_app.locator("span#inputError-password")).to_have_text(config_data['error_message_by_entering_more_then_15_char_in_password_field'])
