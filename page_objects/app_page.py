from  playwright.sync_api import Browser
from page_objects.board_page import BoardPage
from page_objects.notes_page import NotePage
from page_objects.profile_page import ProfilePage
from page_objects.reset_password_page import ResetPasswordPage
from page_objects.sign_in_page import RegistrationPage
from page_objects.statistic_page import StatisticPage


class App:
    def __init__(self, browser: Browser, base_url: str, **context_options):
        self.browser = browser
        self.context = self.browser.new_context(**context_options)
        self.page = self.context.new_page()
        self.base_url = base_url

        self.email_field = self.page.locator("#input-email")
        self.password_field = self.page.locator("#input-password")
        self.login_btn = self.page.locator("//form/button")
        self.forgot_password_email_field = self.page.locator("//h2[text()='Password recovery']/../..//input[@id='input-email']")
        self.forgot_password_title = self.page.get_by_role("heading", name="Password recovery")
        self.login_link = self.page.get_by_role("link", name="Login")
        self.forgot_password_link = self.page.get_by_text("Forgot password?")
        self.close_btn = self.page.locator(".rounded-md")
        self.continue_btn = self.page.locator("//button[text()='Continue']")

        self.registration = RegistrationPage(self.page)
        self.board = BoardPage(self.page)
        self.profile = ProfilePage(self.page)
        self.reset_password = ResetPasswordPage(self.page)
        self.statistic = StatisticPage(self.page)
        self.notes = NotePage(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def locator(self, selector):
        return self.page.locator(selector)

    def close(self):
        self.page.close()
        self.context.close()

    def enter_value_in_email_field(self, test_input: str):
        self.email_field.press("Control+A")
        self.email_field.press("Delete")
        self.email_field.fill(test_input)
        self.password_field.click()

    def enter_value_in_password_field(self, test_input: str):
        self.password_field.press("Control+A")
        self.password_field.press("Delete")
        self.password_field.fill(test_input)
        self.email_field.click()

    def fill_in_login_form(self, email: str, password: str):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.login_btn.click()

    def navigate_to_login_page(self):
        self.login_link.click()

    def navigate_to_forgot_password_form(self):
        self.forgot_password_link.click()

    def enter_value_in_forgot_password_email_field(self, test_input: str):
        self.forgot_password_email_field.press("Control+A")
        self.forgot_password_email_field.press("Delete")
        self.forgot_password_email_field.fill(test_input)
        self.forgot_password_title.click()

    def login(self, email: str, password: str):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.login_btn.click()

    def click_on_close_btn_forgot_password_form(self):
        self.close_btn.click()

    def close_success_login_window_by_clicking_on_close_btn(self):
        self.close_btn.click()

    def close_success_login_window_by_clicking_on_continue_btn(self):
        self.continue_btn.click()