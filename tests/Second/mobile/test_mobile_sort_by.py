import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("test_input", [
    "Hybrid",
    "Remote",
    "Office"
])
def test_sort_vacancy_by_work_type_mobile(mobile_user_authorization_for_sort_by_work_type, config_data: dict, test_input):
    mobile_user_authorization_for_sort_by_work_type.board.select_sort_by_work_type_value(test_input)
    work_type_values = mobile_user_authorization_for_sort_by_work_type.board.collect_work_type_values()
    for work_type_value in work_type_values:
        assert work_type_value == test_input, f"Expected work type value '{test_input}' but got {work_type_value}"
    mobile_user_authorization_for_sort_by_work_type.board.click_on_sort_by_btn_mobile()


@pytest.mark.parametrize("test_input", [
    "Offer",
    "Rejection",
    "Technical interview",
    "Test task",
    "HR interview",
    "Sent",
    "Saved"
])
def test_sort_vacancy_by_status_mobile(mobile_user_authorization_for_status_type, config_data: dict, test_input):
    mobile_user_authorization_for_status_type.board.select_sort_by_status_value(test_input)
    status_locator = mobile_user_authorization_for_status_type.locator(f"//section//div[text()='{test_input}']")

    if status_locator.is_visible():
        expect(status_locator).to_be_visible()
    else:
        no_vacancies_locator = mobile_user_authorization_for_status_type.locator("//main//p[contains(@class, 'text-xl')]")
        expect(no_vacancies_locator).to_have_text(config_data['no_vacancies_message'])
    mobile_user_authorization_for_status_type.board.click_on_sort_by_btn_mobile()
