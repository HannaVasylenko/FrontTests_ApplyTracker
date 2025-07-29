from playwright.sync_api import Page


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_email_field = self.page.locator("#input-email")
        self.sign_in_password_field = self.page.locator("#input-password")
        self.sign_in_confirm_password_field = self.page.locator("#input-confirmPassword")
        self.privacy_policy_checkbox = self.page.get_by_label("I agree with the privacy")
        self.sign_in_btn = self.page.locator("//form/button")
        self.sign_in_link = self.page.get_by_role("link", name="Register")
        self.confirm_password_eye_icon = self.page.locator("//input[@id='input-confirmPassword']/../button")
        self.password_eye_icon = self.page.locator("//input[@id='input-password']/../button")
        self.sign_in_checkbox = self.page.get_by_role("checkbox")

    def enter_value_in_confirm_password_field(self, email: str, password: str, confirm_password: str):
        self.sign_in_email_field.fill(email)
        self.sign_in_password_field.fill(password)
        self.sign_in_confirm_password_field.fill(confirm_password)
        self.sign_in_email_field.click()

    def enter_value_in_password_field_register_form(self, test_input: str):
        self.sign_in_password_field.press("Control+A")
        self.sign_in_password_field.press("Delete")
        self.sign_in_password_field.fill(test_input)
        self.sign_in_email_field.click()

    def enter_value_in_email_field_registration_form(self, test_input: str):
        self.sign_in_email_field.press("Control+A")
        self.sign_in_email_field.press("Delete")
        self.sign_in_email_field.fill(test_input)
        self.sign_in_password_field.click()

    def fill_in_register_form_valid(self, email: str, password: str):
        self.sign_in_email_field.fill(email)
        self.sign_in_password_field.fill(password)
        self.sign_in_confirm_password_field.fill(password)
        self.sign_in_checkbox.check()
        self.sign_in_btn.click()

    def fill_in_register_without_agreeing_to_privacy_policy(self, email: str, password: str):
        self.sign_in_email_field.fill(email)
        self.sign_in_password_field.fill(password)
        self.sign_in_confirm_password_field.fill(password)

    def show_password_after_click_on_eye_icon(self, password: str):
        self.sign_in_password_field.fill(password)
        self.password_eye_icon.click()

    def show_confirm_password_after_click_on_eye_icon(self, password: str):
        self.sign_in_confirm_password_field.fill(password)
        self.confirm_password_eye_icon.click()
