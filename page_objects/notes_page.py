from playwright.sync_api import Page


class NotePage:
    def __init__(self, page: Page):
        self.page = page
        self.name_field_in_add_note_form = self.page.get_by_placeholder("Name file")
        self.text_field_in_add_note_form = self.page.get_by_placeholder("Text")
        self.search_field = self.page.locator("#input-query") # //header//button[@aria-label='Search button']
        self.list_search_result_values = self.page.locator("//main//div[contains(@class, 'grid')]/div")
        self.list_notes_dates = self.page.locator("//div[contains(@class,'items-end')]/div[contains(@class, 'text-sm')]")
        self.sort_btn = self.page.locator("button#sortButton")
        self.create_note_btn = self.page.locator("//aside/../following-sibling::div//span[text()='New note']/../following-sibling::div//button[@type='button']")
        self.save_note_btn = self.page.locator("//h4[text()='Save changes?']/..//button[text()='Save']")
        self.delete_note_btn = self.page.locator("//h4[text()='Delete note?']/..//button[text()='Delete']")
        self.sort_note_btn_mobile = self.page.locator("//button[@aria-label='Sort_button']")
        self.note_search_icon_btn = self.page.get_by_label("Search button")

    def click_on_search_btn(self):
        self.note_search_icon_btn.click()

    def click_on_sort_btn_mobile(self):
        self.sort_note_btn_mobile.click()

    def click_on_sort_by_btn_on_notes_page(self):
        self.page.locator("//div[@class='flex-nowrap']").wait_for(state='hidden')
        self.sort_btn.click()

    def select_sort_by_dropbox_value_on_notes_page(self, sort_by_value: str):
        self.page.locator(f"//ul[contains(@class, 'rounded-b-xl')]/li[text()='{sort_by_value}']").click()

    def enter_value_in_name_field_in_add_note_window(self, name: str):
        self.name_field_in_add_note_form.press("Control+A")
        self.name_field_in_add_note_form.press("Delete")
        self.name_field_in_add_note_form.fill(name)
        self.text_field_in_add_note_form.click()

    def enter_value_in_text_field_in_add_note_window(self, text: str):
        self.text_field_in_add_note_form.press("Control+A")
        self.text_field_in_add_note_form.press("Delete")
        self.text_field_in_add_note_form.fill(text)
        self.name_field_in_add_note_form.click()

    def type_in_search_field_on_notes_page(self, search_value: str):
        self.page.locator("//div[@class='flex-nowrap']").wait_for(state='hidden')
        self.search_field.press("Control+A")
        self.search_field.press("Delete")
        self.search_field.fill(search_value)
        self.search_field.press("Enter")

    def collect_notes_search_result_values(self, name: str):
        search_result_values = self.page.locator(f"//main//div[contains(@class, 'grid')]//div[text()='{name}']").all_text_contents()
        return search_result_values

    def add_note(self, name: str, text: str):
        self.name_field_in_add_note_form.fill(name)
        self.text_field_in_add_note_form.fill(text)
        self.create_note_btn.click()
        self.save_note_btn.click()

    def delete_note(self, note_title: str):
        self.page.locator(f"//main//div[text()='{note_title}']/..//button[@aria-label='Delete_note_button']").click()
        self.delete_note_btn.click()
