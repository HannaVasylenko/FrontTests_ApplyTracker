from datetime import datetime, timedelta
from playwright.sync_api import Page


class StatisticPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_event_btn = self.page.locator("//h3[text()='Soon']/..//button[text()='Add event']")
        self.month_arrow_next_btn = self.page.locator("//div[@class='w-full']/..//span[@class='text-xl']/../following-sibling::div//button[contains(@class, 'react-calendar__navigation__next-button')]")
        self.month_arrow_prev_btn = self.page.locator("//div[@class='w-full']/..//span[@class='text-xl']/../following-sibling::div//button[contains(@class, 'react-calendar__navigation__prev-button')]")
        self.name_field_in_add_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Add event']/../following-sibling::div//input[@id='input-soonEventName']")
        self.note_field_in_add_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Add event']/../following-sibling::div//textarea[@id='textarea-soonEventNotes']")
        self.hour_field_in_add_event_window = self.page.get_by_role("textbox", name="00").nth(2)
        self.minute_value = self.page.locator("//input[contains(@aria-activedescendant, '-option-2')]")
        self.minute_field_in_add_event_window = self.page.get_by_role("textbox", name="00").nth(3)
        self.previous_arrow_in_calendar_in_add_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Add event']/../following-sibling::div//button[contains(@class, 'react-calendar__navigation__prev-button')]")
        self.next_arrow_in_calendar_in_add_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Add event']/../following-sibling::div//button[contains(@class, 'react-calendar__navigation__next-button')]")
        self.save_btn_in_add_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Add event']/../following-sibling::div//button[@type='submit']")
        self.save_btn_in_edit_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Edit event']/../following-sibling::div//button[text()='Save']")
        self.name_field_in_edit_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Edit event']/../following-sibling::div//input[@id='input-soonEventName']")
        self.hour_field_in_edit_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Edit event']/../following-sibling::div//input[@id='input-hours']")
        self.minute_field_in_edit_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Edit event']/../following-sibling::div//input[@id='input-minutes']")
        self.delete_btn_in_edit_event_window = self.page.locator("//aside/../following-sibling::div//span[text()='Edit event']/../following-sibling::div//button[text()='Delete']")
        self.save_btn_in_confirm_window = self.page.locator("//aside/../following-sibling::div//h4/..//button[text()='Save']")
        self.delete_btn_in_confirm_window = self.page.locator("//aside/../following-sibling::div//h4/..//button[text()='Delete']")
        self.hour_in_edit_window = self.page.locator("//aside/../following-sibling::div//p[text()='Set time']/../div/div").first
        self.minute_in_edit_window = self.page.locator("//aside/../following-sibling::div//p[text()='Set time']/../div/div").last
        self.edit_event_title = self.page.locator("//aside/../following-sibling::div//span[text()='Edit event']")

    def select_calender_day_in_add_event_window(self):
        now = datetime.now() + timedelta(days=2)
        formatted_date = now.strftime("%e").strip()
        self.page.locator(f"//aside/../following-sibling::div//div[@class='react-calendar__month-view__days']//abbr[@aria-label='{now.strftime('%B')} {formatted_date}, {now.year}']").click()

    def type_in_name_field(self, value: str):
        self.name_field_in_add_event_window.press("Control+A")
        self.name_field_in_add_event_window.press("Delete")
        self.name_field_in_add_event_window.fill(value)
        self.note_field_in_add_event_window.click()

    def type_in_note_field(self, value: str):
        self.note_field_in_add_event_window.press("Control+A")
        self.note_field_in_add_event_window.press("Delete")
        self.note_field_in_add_event_window.fill(value)
        self.name_field_in_add_event_window.click()

    def add_event(self, name: str, hour: str, minute: str):
        self.name_field_in_add_event_window.fill(name)
        self.hour_field_in_add_event_window.click()
        self.click_on_time_dropbox_in_add_event_form(hour)
        self.minute_field_in_add_event_window.click()
        self.click_on_time_dropbox_in_add_event_form(minute)
        now = datetime.now() + timedelta(days=2)
        formatted_date = now.strftime("%e").strip()
        self.page.locator(f"//aside/../following-sibling::div//div[@class='react-calendar__month-view__days']//abbr[@aria-label='{now.strftime('%B')} {formatted_date}, {now.year}']").click()
        self.save_btn_in_add_event_window.click()
        self.save_btn_in_confirm_window.click()

    def delete_event(self, name: str):
        self.page.locator(f"//h3[text()='Soon']/..//li//p[text()='{name}']").click()
        self.edit_event_title.wait_for(state='visible')
        self.delete_btn_in_edit_event_window.click()
        self.delete_btn_in_confirm_window.click()

    def edit_name_in_edit_event_window(self, name: str, updated_name: str):
        self.page.locator(f"//h3[text()='Soon']/..//li//p[text()='{name}']").click()
        self.edit_event_title.wait_for(state='visible')
        self.name_field_in_edit_event_window.fill(updated_name)
        self.save_btn_in_edit_event_window.click()
        self.save_btn_in_confirm_window.click()

    def click_on_time_dropbox_in_add_event_form(self, time: str):
        self.page.get_by_role("option",name=f"{time}").click()

    def edit_time_in_edit_event_window(self, name: str, hour: str, minute: str):
        self.page.locator(f"//h3[text()='Soon']/..//li//p[text()='{name}']").click()
        self.edit_event_title.wait_for(state='visible')
        self.hour_in_edit_window.click()
        self.click_on_time_dropbox_in_add_event_form(hour)
        self.minute_in_edit_window.click()
        self.click_on_time_dropbox_in_add_event_form(minute)
        self.save_btn_in_edit_event_window.click()
        self.save_btn_in_confirm_window.click()

    def select_date_tab(self, date_tab: str):
        self.page.locator(f"//aside/..//button[text()='{date_tab}']").click()

    def click_on_event_btn(self):
        self.add_event_btn.click()

    def select_year_value(self):
        now = datetime.now()
        current_year = now.year
        self.page.locator(
            f"//aside/..//div[@class='react-calendar__decade-view']//button[text()='{current_year}']").click()
