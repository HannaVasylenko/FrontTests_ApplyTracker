from playwright.sync_api import Page


class BoardPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_vacancy_company_field = self.page.get_by_placeholder("Enter company name")
        self.add_vacancy_position_field = self.page.get_by_placeholder("Enter position")
        self.add_vacancy_location_field = self.page.get_by_placeholder("Enter company location")
        self.add_vacancy_job_link_field = self.page.get_by_placeholder("Add job link")
        self.add_vacancy_communication_channel_field = self.page.get_by_placeholder("Enter communication channel")
        self.add_vacancy_note_field = self.page.get_by_placeholder("Place for your notes")
        self.add_vacancy_remote_checkbox = self.page.get_by_label("Remote")
        self.add_vacancy_hr_status = self.page.get_by_label("HR")
        self.logout_btn = self.page.locator("//aside//span[text()='Log out']")
        self.exit_btn = self.page.get_by_role("button", name="Log Out")
        self.list_work_type_values = self.page.locator("//section[@class='text-textBlack']//span[@class='text-sm']")
        self.list_search_result_values = self.page.locator("//section[@class='text-textBlack']//h3")
        self.list_search_result_company_name_values = self.page.locator("//section[@class='text-textBlack']//p")
        self.search_field = self.page.locator("#input-query")
        self.send_btn = self.page.get_by_role("button", name="Надіслати")
        self.en_language_btn = self.page.locator("//aside//span[text()='EN']")
        self.ua_language_btn = self.page.locator("//aside//span[text()='UA']")
        self.add_vacancy_btn = self.page.get_by_role("button", name="Add vacancy")
        self.save_vacancy_btn = self.page.locator("//aside/../following-sibling::div//span[text()='Add a new vacancy']/../following-sibling::div//button[text()='Save']")
        self.save_vacancy_in_editing_btn = self.page.locator("//aside/../following-sibling::div//span[text()='Edit the vacancy']/../following-sibling::div//button[text()='Save']")
        self.confirm_changes_button = self.page.locator("//h4/..//button[text()='Save']")
        self.confirm_changes_button_in_archive_window = self.page.locator("//h4/..//button[text()='To Archive']")
        self.delete_btn = self.page.get_by_role("button", name="Delete")
        self.confirm_delete_btn = self.page.locator("//h4/..//button[text()='Delete']")
        self.archive_btn = self.page.locator("//form//button[text()='Archive']")
        self.archive_tab = self.page.get_by_role("link", name="Feedback archive")
        self.contact_us_name_field = self.page.get_by_placeholder("Enter your name")
        self.contact_us_email_field = self.page.locator("#input-email")
        self.contact_us_request_text_field = self.page.get_by_placeholder("Enter your message")
        self.sort_btn = self.page.locator("button#sortButton")
        self.sort_btn_mobile = self.page.locator("//button[@aria-label='Sort_button']")
        self.by_work_type_sort_value = self.page.locator("//main//ul/li[text()='By work type']")
        self.sidebar_btn = self.page.locator("//header//button[@aria-label='Open sidebar button']")
        self.search_icon_btn = self.page.get_by_label("Search button")
        self.add_stage_btn = self.page.locator("//button[text()='Add stage']")
        self.save_changes_btn = self.page.get_by_role("button", name="Save")
        self.search_button = self.page.locator("//form//button[@type='submit']")
        self.by_status_dropbox = self.page.locator("//form//button[@type='submit']")
        self.cross_search_btn = self.page.locator("//button[@aria-label='Close button']")
        self.search_btn_mobile = self.page.locator("//button[@aria-label='Search button']")


    def close_search_field(self):
        self.cross_search_btn.click()

    def change_page_language_to_en(self):
        if "opacity-100" not in self.ua_language_btn.get_attribute("class"):
            self.en_language_btn.click()

    def change_page_language_to_en_in_mobile(self):
        self.click_on_sidebar_btn()
        if "opacity-100" not in self.ua_language_btn.get_attribute("class"):
            self.en_language_btn.click()
        self.page.locator(".size-11").click()

    def select_language(self, language: str):
        if language == 'UA':
            if "duration-1000" in self.en_language_btn.get_attribute("class"):
                self.ua_language_btn.click()
        elif language == 'EN':
            if "duration-1000" in self.ua_language_btn.get_attribute("class"):
                self.en_language_btn.click()
        else:
            raise ValueError("Invalid language selection. Use 'EN' or 'UA'.")

    def open_add_vacancy_form(self):
        self.add_vacancy_btn.click()

    def open_add_stage_dropdown(self):
        self.add_stage_btn.click()

    def click_on_sidebar_btn(self):
        self.sidebar_btn.click()

    def enter_value_in_company_field(self, test_input: str):
        self.add_vacancy_company_field.press("Control+A")
        self.add_vacancy_company_field.press("Delete")
        self.add_vacancy_company_field.fill(test_input)
        self.add_vacancy_position_field.click()

    def enter_value_in_position_field(self, test_input: str):
        self.add_vacancy_position_field.press("Control+A")
        self.add_vacancy_position_field.press("Delete")
        self.add_vacancy_position_field.fill(test_input)
        self.add_vacancy_job_link_field.click()

    def enter_value_in_job_link_field(self, test_input: str):
        self.add_vacancy_job_link_field.press("Control+A")
        self.add_vacancy_job_link_field.press("Delete")
        self.add_vacancy_job_link_field.fill(test_input)
        self.add_vacancy_communication_channel_field.click()

    def enter_value_in_communication_channel_field(self, test_input: str):
        self.add_vacancy_communication_channel_field.press("Control+A")
        self.add_vacancy_communication_channel_field.press("Delete")
        self.add_vacancy_communication_channel_field.fill(test_input)
        self.add_vacancy_location_field.click()

    def enter_value_in_location_field(self, test_input: str):
        self.add_vacancy_location_field.press("Control+A")
        self.add_vacancy_location_field.press("Delete")
        self.add_vacancy_location_field.fill(test_input)
        self.add_vacancy_communication_channel_field.click()

    def enter_value_in_note_field(self, test_input: str):
        self.add_vacancy_note_field.press("Control+A")
        self.add_vacancy_note_field.press("Delete")
        self.add_vacancy_note_field.fill(test_input)
        self.add_vacancy_location_field.click()

    def select_checkbox_work_type(self, work_type: str):
        self.page.locator(f"//input[@id='{work_type}']").check()

    def select_status_checkbox(self, status: str):
        self.page.locator(f"#{status}").check()

    def fill_in_create_vacancy_form(self, company_name: str, vacancy_name: str, link: str, communication_channel: str, location: str):
        self.add_vacancy_company_field.fill(company_name)
        self.add_vacancy_position_field.fill(vacancy_name)
        self.add_vacancy_job_link_field.fill(link)
        self.add_vacancy_communication_channel_field.fill(communication_channel)
        self.add_vacancy_location_field.fill(location)
        self.add_vacancy_remote_checkbox.check()
        self.save_vacancy_btn.click()
        self.confirm_changes_button.click()

    def logout(self):
        self.logout_btn.click()
        self.exit_btn.click()

    def logout_mobile(self):
        self.sidebar_btn.click()
        self.logout_btn.click()
        self.exit_btn.click()

    def enter_value_in_name_field_contact_us_form(self, test_input: str):
        self.contact_us_name_field.press("Control+A")
        self.contact_us_name_field.press("Delete")
        self.contact_us_name_field.fill(test_input)
        self.contact_us_request_text_field.click()

    def enter_value_in_email_field_contact_us_form(self, test_input: str):
        self.contact_us_email_field.press("Control+A")
        self.contact_us_email_field.press("Delete")
        self.contact_us_email_field.fill(test_input)
        self.contact_us_name_field.click()

    def enter_value_in_request_text_field_contact_us_form(self, test_input: str):
        self.contact_us_request_text_field.press("Control+A")
        self.contact_us_request_text_field.press("Delete")
        self.contact_us_request_text_field.fill(test_input)
        self.contact_us_name_field.click()

    def open_edit_vacancy_window(self, vacancy_name: str):
        self.page.get_by_role("button", name=f"{vacancy_name}").click()

    def click_on_sort_by_btn(self):
        self.sort_btn.click()

    def click_on_sort_by_btn_mobile(self):
        self.sort_btn_mobile.click()

    def select_sort_by_work_type(self):
        self.by_work_type_sort_value.click()

    def select_sort_by_dropbox_value(self, sort_by_value: str):
        self.page.locator(f"//ul[contains(@class, 'rounded-b-xl')]/li[text()='{sort_by_value}']").click()

    def select_sort_by_status_value(self, status_value: str):
        self.page.locator(f"//li[text()='By status']//li[text()='{status_value}']").click()

    def select_sort_by_work_type_value(self, work_type_value: str):
        self.page.locator(f"//main//ul/li[text()='By work type']//li[text()='{work_type_value}']").click()

    def collect_work_type_values(self):
        work_type_values = self.list_work_type_values.all_text_contents()
        return work_type_values

    def type_in_search_field(self, search_value: str):
        self.page.locator("//div[@class='flex-nowrap']").wait_for(state='hidden')
        self.search_field.press("Control+A")
        self.search_field.press("Delete")
        self.search_field.fill(search_value)
        self.page.locator("//main//div[@class='w-full']").wait_for(state='visible')
        self.search_field.press("Enter")

    def type_in_search_field_mobile_version(self, search_value: str):
        self.page.locator("//div[@class='flex-nowrap']").wait_for(state='hidden')
        self.search_field.press("Control+A")
        self.search_field.press("Delete")
        self.search_field.fill(search_value)
        self.search_field.press("Enter")

    def type_in_search_field_mobile(self, search_value: str):
        self.search_field.fill(search_value)
        self.search_field.press("Enter")

    def collect_search_result_values(self):
        search_result_values = self.list_search_result_values.all_text_contents()
        return search_result_values

    def collect_search_result_company_name_values(self):
        search_result_values = self.list_search_result_company_name_values.all_text_contents()
        return search_result_values

    def collect_search_result_location_values(self, location: str):
        search_result_values = self.page.locator(f"//section[@class='text-textBlack']//span[text()='{location}']").all_text_contents()
        return search_result_values

    def fill_in_fields_contact_us_form(self, name: str, request_text: str):
        self.contact_us_name_field.fill(name)
        self.contact_us_request_text_field.fill(request_text)
        #self.send_btn.click()

    def create_vacancy_for_moving_vacancy_cards(self, vacancy_name: str):
        self.add_vacancy_company_field.fill("company name")
        self.add_vacancy_position_field.fill(vacancy_name)
        self.add_vacancy_job_link_field.fill("https://demoqa.com/")
        self.add_vacancy_communication_channel_field.fill("https://demoqa.com/")
        self.add_vacancy_location_field.fill("location city")
        self.add_vacancy_remote_checkbox.check()
        self.save_vacancy_btn.click()
        self.confirm_changes_button.click()

    def click_on_vacancy(self, vacancy_name: str):
        self.page.get_by_role("button", name=f"{vacancy_name}").click()

    def select_vacancy_from_tab(self, vacancy_name: str, vacancy_tab: str):
        self.page.locator(f"//div[text()='{vacancy_tab}']/..//h3[text()='{vacancy_name}']").click()

    def click_on_add_vacancy_to_archive_btn(self):
        self.archive_btn.click()
        self.confirm_changes_button_in_archive_window.click()

    def select_vacancy_status(self, status_name: str):
        self.page.get_by_label(f"{status_name}").check()

    def select_add_stage_value(self, stage_value: str):
        self.page.locator("//button[text()='Select an additional stage']").click()
        self.page.locator(f"//aside/../following-sibling::div//span[text()='Add a new vacancy']/../following-sibling::div//button[text()='Select an additional stage']/..//li[text()='{stage_value}']").click()

    def edit_value_in_field_add_vacancy_form(self, field_name: str, value: str):
        self.page.locator(f"#input-{field_name}").press("Control+A")
        self.page.locator(f"#input-{field_name}").press("Delete")
        self.page.locator(f"#input-{field_name}").fill(value)
        self.page.locator("//label[text()='Status']").click()
        self.save_vacancy_in_editing_btn.click()
        self.confirm_changes_button.click()

    def edit_work_type_in_add_vacancy_form(self, work_type: str):
        self.select_checkbox_work_type(work_type)
        self.save_vacancy_in_editing_btn.click()
        self.confirm_changes_button.click()

    def confirm_save_changes_in_add_vacancy_form(self):
        self.save_changes_btn.click()
        self.confirm_changes_button.click()

    def select_dropdown_value_when_edit_vacancy_in_statuses(self, dropdown_placeholder: str, dropdown_value: str):
        self.page.locator(f"//aside/../following-sibling::div//span[text()='Edit the vacancy']/../following-sibling::div//button[text()='{dropdown_placeholder}']").click()
        self.page.locator(f"//aside/../following-sibling::div//span[text()='Edit the vacancy']/../following-sibling::div//button[text()='{dropdown_placeholder}']/..//li[text()='{dropdown_value}']").click()

    def add_vacancy_with_status_for_tests(self, vacancy_name, status):
        self.add_vacancy_company_field.fill("company name")
        self.add_vacancy_position_field.fill(vacancy_name)
        self.add_vacancy_job_link_field.fill("https://demoqa.com/")
        self.add_vacancy_communication_channel_field.fill("https://demoqa.com")
        self.add_vacancy_location_field.fill("location city")
        self.add_vacancy_remote_checkbox.check()
        self.select_vacancy_status(status)
        if status == "Rejection":
            self.page.locator("//aside/../following-sibling::div//span[text()='Add a new vacancy']/../following-sibling::div//button[text()='Select the reason for rejection']").click()
            self.page.locator("//aside/../following-sibling::div//span[text()='Add a new vacancy']/../following-sibling::div//button[text()='Select the reason for rejection']/..//li[text()='No answer']").click()
            self.save_vacancy_btn.click()
            self.confirm_changes_button.click()
        elif status == "Resume sent":
            self.page.locator("//aside/../following-sibling::div//span[text()='Add a new vacancy']/../following-sibling::div//button[text()='Select the sent CV']").click()
            self.page.locator("//aside/../following-sibling::div//span[text()='Add a new vacancy']/../following-sibling::div//button[text()='Select the sent CV']/..//li[text()='resume qa']").click()
            self.save_vacancy_btn.click()
            self.confirm_changes_button.click()
        else:
            self.save_vacancy_btn.click()
            self.confirm_changes_button.click()

    def delete_vacancy(self, vacancy_name: str, vacancy_tab: str):
        if vacancy_tab == "HR":
            locator_text = "HR interview"
        elif vacancy_tab == "Resume sent":
            locator_text = "Sent"
        else:
            locator_text = vacancy_tab
        vacancy_locator = self.page.locator(f"//div[text()='{locator_text}']/..//h3[text()='{vacancy_name}']")
        vacancy_locator.click()
        self.delete_btn.click()
        self.confirm_delete_btn.click()

    def open_contact_us_form(self):
        self.page.get_by_text("Contact Us").click()

    def open_archive_page(self):
        self.archive_tab.click()
        self.page.locator("//section/div[text()='Feedback archive']").wait_for(state='visible')

    def delete_vacancy_without_selecting(self):
        self.delete_btn.click()
        self.confirm_delete_btn.click()
