from playwright.sync_api import Page


class ResetPasswordPage:
    def __init__(self, page: Page):
        self.page = page
        self.reset_password_password_field = self.page.get_by_placeholder("Enter password")
        self.reset_password_confirm_password_field = self.page.get_by_placeholder("Confirm password")
        self.password_title = self.page.locator("//label[@for='input-password']")

    def reset_password_enter_value_in_confirm_password_field(self, password: str, confirm_password: str):
        self.reset_password_password_field.fill(password)
        self.reset_password_confirm_password_field.fill(confirm_password)
        self.password_title.click()

    def reset_password_enter_value_in_password_field(self, test_input: str):
        self.reset_password_password_field.press("Control+A")
        self.reset_password_password_field.press("Delete")
        self.reset_password_password_field.fill(test_input)
        self.reset_password_confirm_password_field.click()