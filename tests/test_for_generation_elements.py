import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("test_input", [
    "DevOps engineer",
    "Database analyst",
    "SEO manager",
    "Game developer",
    "Test automation engineer",
    "Frontend developer",
    "Backend developer",
    "Project manager",
    "Tester",
    "Fullstack developer"
])
def test_add_vacancies_cards_to_board_desktop(desktop_user_authorization_for_generate_cards, config_data: dict, test_input):
    desktop_user_authorization_for_generate_cards.board.fill_in_create_vacancy_form(config_data['company_name'], test_input, config_data['link'], config_data['move_vacancy_card_communication'], config_data['location'])
    expect(desktop_user_authorization_for_generate_cards.locator("section.Toastify p")).to_have_text(config_data['success_add_vacancy_toastify_desktop'])

    expect(desktop_user_authorization_for_generate_cards.locator("section.Toastify p")).to_have_text(config_data['success_add_vacancy_toastify_desktop'])
    desktop_user_authorization_for_generate_cards.locator("section.Toastify p").wait_for(state='hidden')
    desktop_user_authorization_for_generate_cards.board.open_add_vacancy_form()


@pytest.mark.parametrize("test_input", [
    "Name",
    "Yo char d ut perspiciatis u30e",
    "Do char perspiciatis unde omnis iste natus erro50t"
])
def test_add_notes_with_titles_desktop(desktop_user_authorization_for_generate_notes, config_data: dict, test_input):
    notes = desktop_user_authorization_for_generate_notes.notes
    toast_locator = "section.Toastify p"
    note_name = test_input
    note_text = config_data['text_name']
    success_add_toast = config_data['success_add_note_toastify']
    notes.add_note(note_name, note_text)
    expect(desktop_user_authorization_for_generate_notes.locator(toast_locator)).to_have_text(success_add_toast)
    desktop_user_authorization_for_generate_notes.locator(toast_locator).wait_for(state='hidden')
    desktop_user_authorization_for_generate_notes.page.get_by_role("button", name="Add a note").click()
    desktop_user_authorization_for_generate_notes.page.locator("//span[text()='New note']").wait_for(state='visible')


@pytest.mark.parametrize("test_input", [
    "Name",
    "To char d ut perspiciatis 30de",
    "Qo char perspiciatis unde omnis iste natus erro50t"
])
def test_add_event_valid_desktop(desktop_add_event_window_on_statistic_page, config_data: dict, test_input):
    toast_locator = "section.Toastify p"
    event_name = test_input
    success_add_toast = config_data['success_add_event_toastify']
    desktop_add_event_window_on_statistic_page.statistic.add_event(event_name, "10", "05")
    expect(desktop_add_event_window_on_statistic_page.locator(toast_locator)).to_have_text(success_add_toast)
    desktop_add_event_window_on_statistic_page.locator(toast_locator).wait_for(state='hidden')
    desktop_add_event_window_on_statistic_page.page.get_by_role("button", name="Add event").click()
    desktop_add_event_window_on_statistic_page.page.locator("//aside/../following-sibling::div//span[text()='Add event']").wait_for(state='visible')
