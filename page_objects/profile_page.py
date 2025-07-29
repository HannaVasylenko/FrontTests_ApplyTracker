from playwright.sync_api import Page


class ProfilePage:
    def __init__(self, page: Page):
        self.page = page
        self.profile_user_name_field = self.page.locator("#input-username")
        self.profile_email_field = self.page.locator("#input-email")
        self.profile_phone_number_field = self.page.locator("#input-phone")
        self.profile_tab = self.page.get_by_role("link", name="Account")
        self.save_btn_in_save_link_window = self.page.locator("//form//button[text()='Save']")
        self.confirm_add_element = self.page.locator("//h4[text()='Save changes?']/..//button[text()='Save']")
        self.delete_account_btn = self.page.locator("//section//button[text()='Remove account']")
        self.confirm_delete_account_btn = self.page.locator("//button[text()='Ок']")
        self.confirm_delete_account_second_window_btn = self.page.locator("//button[text()='Delete']")
        self.name_field_in_add_link_form = self.page.get_by_placeholder("Enter the name of the link")
        self.link_field_in_add_link_form = self.page.get_by_placeholder("Insert a link to a social")
        self.name_field_in_add_project_link_form = self.page.get_by_placeholder("Enter the name of the project")
        self.technologies_field_in_add_project_link_form = self.page.get_by_placeholder("Specify the technologies used")
        self.link_field_in_add_project_link_form = self.page.get_by_placeholder("Link to the project")
        self.description_field_in_add_project_link_form = self.page.get_by_placeholder("You can describe the project")
        self.name_field_in_add_cover_letter_form = self.page.get_by_placeholder("Enter a name for the letter")
        self.text_field_in_add_cover_letter_form = self.page.locator("//textarea[@id='textarea-text']")
        self.name_field_in_add_resume_form = self.page.get_by_placeholder("Enter the name of the resume")
        self.link_field_in_add_resume_form = self.page.get_by_placeholder("Insert a link to your resume")
        self.ok_button_in_delete_account_window = self.page.locator("//h2[text()='Are you sure you want to delete your account?']/../button[text()='Yes']")
        self.confirm_button_in_delete_account_window = self.page.locator("//h2[text()='This action cannot be undone. Are you sure?']/../button[text()='Delete']")

    def delete_account(self):
        self.delete_account_btn.click()
        self.ok_button_in_delete_account_window.click()
        self.confirm_button_in_delete_account_window.click()

    def fill_user_name_in_personal_info(self, value: str):
        self.profile_user_name_field.press("Control+A")
        self.profile_user_name_field.press("Delete")
        self.profile_user_name_field.fill(value)
        self.page.locator("//span[text()='Personal information']").click()

    def fill_phone_number_in_personal_info(self, value: str):
        self.profile_phone_number_field.press("Control+A")
        self.profile_phone_number_field.press("Delete")
        self.profile_phone_number_field.fill(value)
        self.profile_user_name_field.click()

    def enter_value_in_name_field_in_link(self, name: str):
        self.name_field_in_add_link_form.press("Control+A")
        self.name_field_in_add_link_form.press("Delete")
        self.name_field_in_add_link_form.fill(name)
        self.link_field_in_add_link_form.click()

    def enter_value_in_link_field_in_link(self, name: str):
        self.link_field_in_add_link_form.press("Control+A")
        self.link_field_in_add_link_form.press("Delete")
        self.link_field_in_add_link_form.fill(name)
        self.name_field_in_add_link_form.click()

    def enter_value_in_name_field_in_project_link(self, name: str):
        self.name_field_in_add_project_link_form.press("Control+A")
        self.name_field_in_add_project_link_form.press("Delete")
        self.name_field_in_add_project_link_form.fill(name)
        self.technologies_field_in_add_project_link_form.click()

    def enter_value_in_technologies_field_in_project_link(self, name: str):
        self.technologies_field_in_add_project_link_form.press("Control+A")
        self.technologies_field_in_add_project_link_form.press("Delete")
        self.technologies_field_in_add_project_link_form.fill(name)
        self.name_field_in_add_project_link_form.click()

    def enter_value_in_link_field_in_project_link(self, link: str):
        self.link_field_in_add_project_link_form.press("Control+A")
        self.link_field_in_add_project_link_form.press("Delete")
        self.link_field_in_add_project_link_form.fill(link)
        self.technologies_field_in_add_project_link_form.click()

    def enter_value_in_description_field_in_project_link(self, name: str):
        self.description_field_in_add_project_link_form.press("Control+A")
        self.description_field_in_add_project_link_form.press("Delete")
        self.description_field_in_add_project_link_form.fill(name)
        self.link_field_in_add_project_link_form.click()

    def enter_value_in_name_field_in_cover_letter(self, name: str):
        self.name_field_in_add_cover_letter_form.press("Control+A")
        self.name_field_in_add_cover_letter_form.press("Delete")
        self.name_field_in_add_cover_letter_form.fill(name)
        self.text_field_in_add_cover_letter_form.click()

    def enter_value_in_text_field_in_cover_letter(self, text: str):
        self.text_field_in_add_cover_letter_form.press("Control+A")
        self.text_field_in_add_cover_letter_form.press("Delete")
        self.text_field_in_add_cover_letter_form.fill(text)
        self.name_field_in_add_cover_letter_form.click()

    def enter_value_in_name_field_in_resume(self, name: str):
        self.name_field_in_add_resume_form.press("Control+A")
        self.name_field_in_add_resume_form.press("Delete")
        self.name_field_in_add_resume_form.fill(name)
        self.link_field_in_add_resume_form.click()

    def enter_value_in_link_field_in_resume(self, link: str):
        self.link_field_in_add_resume_form.press("Control+A")
        self.link_field_in_add_resume_form.press("Delete")
        self.link_field_in_add_resume_form.fill(link)
        self.name_field_in_add_resume_form.click()

    def add_resume_to_profile(self, name: str, link: str):
        self.page.get_by_role("button", name="Add Resume +").click()
        self.name_field_in_add_resume_form.fill(name)
        self.link_field_in_add_resume_form.fill(link)
        self.save_btn_in_save_link_window.click()
        self.confirm_add_element.click()

    def add_cover_letter_to_profile(self, name: str, link: str):
        self.page.get_by_role("button", name="Add cover letter +").click()
        self.name_field_in_add_cover_letter_form.fill(name)
        self.text_field_in_add_cover_letter_form.fill(link)
        self.save_btn_in_save_link_window.click()
        self.confirm_add_element.click()

    def add_project_to_profile(self, name: str, github_link: str, link: str):
        self.page.get_by_role("button", name="Add Project Link +").click()
        self.name_field_in_add_project_link_form.fill(name)
        self.technologies_field_in_add_project_link_form.fill(github_link)
        self.link_field_in_add_project_link_form.fill(link)
        self.description_field_in_add_project_link_form.fill(name)
        self.save_btn_in_save_link_window.click()
        self.confirm_add_element.click()

    def add_link_to_profile(self, name: str, link: str):
        self.page.get_by_role("button", name="Add link +").click()
        self.name_field_in_add_link_form.fill(name)
        self.link_field_in_add_link_form.fill(link)
        self.save_btn_in_save_link_window.click()
        self.confirm_add_element.click()

    def delete_document_in_profile(self, section: str, name: str):
        self.page.locator(f"//span[text()='{section}']/ancestor::main//input[@value='{name}']/..//button[@aria-label='remove field']").click()
        self.page.get_by_role("button", name="Delete").click()

    def delete_project_in_profile(self, name: str):
        self.page.locator(f"//span[text()='Projects']/ancestor::main//input[contains(@value, '{name}')]/..//button[@aria-label='remove field']").click()
        self.page.get_by_role("button", name="Delete").click()

    def delete_custom_link_in_profile(self, name: str):
        self.page.locator(f"//span[text()='Personal information']/ancestor::main//input[@placeholder='{name}']/..//button[@aria-label='remove field']").click()
        self.page.locator("//h2[text()='Are you sure you want to delete?']/..//button[text()='Delete']").click()

    def click_on_copy_btn(self, field_name: str):
        self.page.locator(f"//input[@id='input-{field_name}']/..//button[@aria-label='copy text']").click()

    def navigate_to_profile_tab(self):
        self.profile_tab.click()

    def add_default_link_in_profile(self, link_name: str, link_value):
        self.page.locator(f"//ul//label[text()='{link_name}']").fill(link_value)
        self.page.get_by_text("Personal information").click()
        self.page.get_by_text("Personal information").press("F5")
