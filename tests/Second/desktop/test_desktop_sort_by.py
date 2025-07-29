import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("test_input", [
    "Hybrid",
    "Remote",
    "Office"
])
def test_sort_vacancy_by_work_type_desktop(select_sort_by_work_type_dropbox_desktop, config_data: dict, test_input):
    select_sort_by_work_type_dropbox_desktop.board.select_sort_by_work_type_value(test_input)
    select_sort_by_work_type_dropbox_desktop.locator(f"//button[@id='sortButton'][text()='{test_input}']").wait_for(state='visible')
    work_type_values = select_sort_by_work_type_dropbox_desktop.board.collect_work_type_values()
    for work_type_value in work_type_values:
        assert work_type_value == test_input, f"Expected work type value '{test_input}' but got {work_type_value}"
    select_sort_by_work_type_dropbox_desktop.board.click_on_sort_by_btn()


@pytest.mark.parametrize("test_input", [
    "Offer",
    "Rejection",
    "Technical interview",
    "Test task",
    "HR interview",
    "Sent",
    "Saved"
])
def test_sort_vacancy_by_status_desktop(select_sort_by_status_dropbox_desktop, config_data: dict, test_input):
    select_sort_by_status_dropbox_desktop.board.select_sort_by_status_value(test_input)
    status_locator = select_sort_by_status_dropbox_desktop.locator(f"//section//div[text()='{test_input}']")

    if status_locator.is_visible():
        expect(status_locator).to_be_visible()
    else:
        no_vacancies_locator = select_sort_by_status_dropbox_desktop.locator("//main//p[contains(@class, 'text-xl')]")
        expect(no_vacancies_locator).to_have_text(config_data['no_vacancies_message'])
    select_sort_by_status_dropbox_desktop.board.click_on_sort_by_btn()
