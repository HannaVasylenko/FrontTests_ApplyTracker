from datetime import datetime
from playwright.sync_api import expect


def test_search_field_by_note_name_mobile(mobile_user_authorization_for_note_page, config_data: dict):
    note = mobile_user_authorization_for_note_page.notes
    search_term = config_data['search_note_name_value']
    zero_results_locator = "//form/..//p[contains(text(), '0 search results')]"
    note.click_on_search_btn()
    note.type_in_search_field_on_notes_page(search_term)
    if mobile_user_authorization_for_note_page.locator(zero_results_locator).is_visible():
        print("Verification: '0 search results' is visible.")
    else:
        notes_names_values = note.collect_notes_search_result_values(config_data['search_note_name_value'])
        for search_value in notes_names_values:
            assert search_term in search_value, f"Expected '{search_term}' in search result, but got '{search_value}'"


def test_note_search_field_with_nonexistent_value_mobile(mobile_user_authorization_for_note_page, config_data: dict):
    note = mobile_user_authorization_for_note_page.notes
    nonexistent_search_term = config_data['search_vacancy_name_nonexistent_value']
    empty_search_text = config_data['empty_search_result']
    search_results_locator = "//div/p/span"
    empty_result_locator = "//main//following-sibling::div/p"
    note.click_on_search_btn()
    note.type_in_search_field_on_notes_page(nonexistent_search_term)
    mobile_user_authorization_for_note_page.locator(search_results_locator).wait_for(state='visible')
    expect(mobile_user_authorization_for_note_page.locator(empty_result_locator)).to_have_text(f"{empty_search_text}{nonexistent_search_term}")


def test_sort_notes_by_old_first_date_mobile(mobile_user_authorization_for_sorting_note, config_data: dict):
    notes_page = mobile_user_authorization_for_sorting_note.notes
    sort_option = config_data['old_first_sorting']
    notes_container_locator = "//main//div[contains(@class, 'w-full justify-center')]"
    note_dates_locator = "//div[contains(@class,'items-end')]/div[contains(@class, 'text-sm')]"

    notes_page.page.locator(notes_container_locator).wait_for(state='visible')
    initial_dates = notes_page.page.locator(note_dates_locator).all_text_contents()
    expected_sorted_dates = sorted(
        initial_dates,
        key=lambda date_str: datetime.strptime(date_str, '%d.%m.%Y')
    )
    notes_page.click_on_sort_btn_mobile()
    notes_page.select_sort_by_dropbox_value_on_notes_page(sort_option)
    notes_page.page.wait_for_selector(note_dates_locator, state='visible')
    sorted_dates = notes_page.page.locator(note_dates_locator).all_text_contents()
    assert sorted_dates == expected_sorted_dates, f"Expected sorted dates: {expected_sorted_dates}, but got: {sorted_dates}"


def test_sort_notes_by_alphabetically_date_mobile(mobile_user_authorization_for_sorting_note, config_data: dict):
    notes_page = mobile_user_authorization_for_sorting_note.notes
    notes_page.page.locator("//main//div[contains(@class, 'w-full justify-center')]").wait_for(state='visible')
    note_title_locator = "//main//div[contains(@class, 'grid')]//div[contains(@class, 'truncate ')]"
    note_title_elements = notes_page.page.locator(note_title_locator)
    titles_before_sort = note_title_elements.all_text_contents()

    def custom_sort_key(title):
        if not title:
            return '', '', '', ''
        first_char = title[0]
        if first_char.isalnum():
            if first_char.isdigit():
                return 1, title.lower()
            else:
                return 2, title.lower()
        elif first_char in '~`!@#$%^&*()_+[]{}<>/?\|*-= ':
            return 0, title
        else:
            return 0, title

    alphabetically_sorted_titles = sorted(titles_before_sort, key=custom_sort_key)
    notes_page.click_on_sort_btn_mobile()
    notes_page.select_sort_by_dropbox_value_on_notes_page(config_data['alphabetically_sorting'])
    notes_page.page.wait_for_selector(note_title_locator, state='visible')
    titles_after_sort = note_title_elements.all_text_contents()
    assert alphabetically_sorted_titles == titles_after_sort, \
        f"Expected sorted titles: {alphabetically_sorted_titles}, but got: {titles_after_sort}"


def test_add_note_mobile(mobile_user_authorization_for_add_note_test_window, config_data: dict):
    notes = mobile_user_authorization_for_add_note_test_window.notes
    toast_locator = "section.Toastify p"
    note_name = config_data['note_name']
    note_text = config_data['text_name']
    success_add_toast = config_data['success_add_note_toastify']
    success_delete_toast = config_data['success_delete_note_toastify']
    notes.add_note(note_name, note_text)
    expect(mobile_user_authorization_for_add_note_test_window.locator(toast_locator)).to_have_text(success_add_toast)
    mobile_user_authorization_for_add_note_test_window.locator(toast_locator).wait_for(state='hidden')
    notes.delete_note(note_name)
    expect(mobile_user_authorization_for_add_note_test_window.locator(toast_locator)).to_have_text(success_delete_toast)
