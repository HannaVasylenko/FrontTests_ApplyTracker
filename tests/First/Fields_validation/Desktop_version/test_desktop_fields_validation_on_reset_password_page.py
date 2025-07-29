import  pytest
from playwright.sync_api import expect


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
def test_reset_password_password_field_valid_verification_desktop(reset_password_desktop_app, config_data: dict, test_input):
    reset_password_desktop_app.reset_password.reset_password_enter_value_in_password_field(test_input)
    expect(reset_password_desktop_app.locator("span#inputError-password")).not_to_be_visible()


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
def test_reset_password_password_field_invalid_verification_desktop(reset_password_desktop_app, config_data: dict, test_input):
    reset_password_desktop_app.reset_password.reset_password_enter_value_in_password_field(test_input)
    expect(reset_password_desktop_app.locator("span#inputError-password")).to_have_text(config_data['password_error_message'])


@pytest.mark.parametrize("test_input", [
    " ",
    "t",
    "Te1ing@"
])
def test_reset_password_password_field_by_entering_less_then_8_char_desktop(reset_password_desktop_app, config_data: dict, test_input):
    reset_password_desktop_app.reset_password.reset_password_enter_value_in_password_field(test_input)
    expect(reset_password_desktop_app.locator("span#inputError-password")).to_have_text(config_data['password_error_message_by_entering_1_char'])


def test_reset_password_confirm_password_field_valid_verification_desktop(reset_password_desktop_app, config_data: dict):
    reset_password_desktop_app.reset_password.reset_password_enter_value_in_confirm_password_field(config_data['valid_password'], config_data['valid_password'])
    expect(reset_password_desktop_app.locator("span#inputError-confirmPassword")).not_to_be_visible()


def test_reset_password_confirm_password_field_invalid_verification_desktop(reset_password_desktop_app, config_data: dict):
    reset_password_desktop_app.reset_password.reset_password_enter_value_in_confirm_password_field(config_data['valid_password'], config_data['invalid_password'])
    expect(reset_password_desktop_app.locator("span#inputError-confirmPassword")).to_have_text(config_data['passwords_match_error_message'])
