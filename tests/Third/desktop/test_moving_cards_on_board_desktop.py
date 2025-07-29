import  pytest
from playwright.sync_api import expect


def test_add_vacancy_to_board_valid_desktop(desktop_user_authorization_for_moving_cards, config_data: dict):
    board = desktop_user_authorization_for_moving_cards.board
    toast_locator = "section.Toastify p"
    vacancy_name = config_data['vacancy_name']
    success_toast_text = config_data['success_add_vacancy_toastify_desktop']

    board.fill_in_create_vacancy_form(
        config_data['company_name'],
        vacancy_name,
        config_data['link'],
        config_data['move_vacancy_card_communication'],
        config_data['location']
    )
    expect(desktop_user_authorization_for_moving_cards.locator(toast_locator)).to_have_text(success_toast_text)
    vacancy_locator = f"//div[text()='Saved']/..//h3[text()='{vacancy_name}']"
    desktop_user_authorization_for_moving_cards.locator(f"{vacancy_locator}").wait_for(state='visible')
    board.delete_vacancy(vacancy_name, "Saved")
    expect(desktop_user_authorization_for_moving_cards.locator(vacancy_locator)).not_to_be_visible()


@pytest.mark.parametrize("initial_status, expected_status, requires_dropdown, dropdown_placeholder, dropdown_value", [
    ("Test task", "Test task", False, None, None),
    ("Technical interview", "Technical interview", False, None, None),
    ("Offer", "Offer", False, None, None),
    ("HR", "HR interview", False, None, None),
    ("Rejection", "Rejection", True, 'reject_dropdown_placeholder_in_statuses', 'no_answer_reject_reason'),
    ("Resume sent", "Sent", True, 'resume_dropdown_placeholder_in_statuses', 'default_resume_name'),
])
def test_change_vacancy_statuses_desktop(desktop_add_vacancy_without_status, config_data: dict, initial_status, expected_status, requires_dropdown, dropdown_placeholder, dropdown_value):
    vacancy_name = config_data['vacancy_name_for_changing_status']
    desktop_add_vacancy_without_status.board.click_on_vacancy(vacancy_name)
    desktop_add_vacancy_without_status.board.select_vacancy_status(initial_status)

    if requires_dropdown:
        desktop_add_vacancy_without_status.board.select_dropdown_value_when_edit_vacancy_in_statuses(
            config_data[dropdown_placeholder],
            config_data[dropdown_value]
        )
    desktop_add_vacancy_without_status.board.confirm_save_changes_in_add_vacancy_form()
    expect(desktop_add_vacancy_without_status.locator(f"//div[text()='{expected_status}']/..//h3[text()='{vacancy_name}']")).to_be_visible()


def test_add_vacancy_to_archive_desktop(desktop_add_vacancy_without_to_archive, config_data: dict):
    board = desktop_add_vacancy_without_to_archive.board
    vacancy_name = config_data['vacancy_name_for_add_to_archive']
    archive_locator = f"//div[text()='Feedback archive']/..//h3[text()='{vacancy_name}']"

    board.click_on_vacancy(vacancy_name)
    board.click_on_add_vacancy_to_archive_btn()
    expect(desktop_add_vacancy_without_to_archive.locator(archive_locator)).to_be_visible()


@pytest.mark.parametrize(
    "status, expected_board_text",
    [
        ("Test task", "Test task"),
        ("Technical interview", "Technical interview"),
        ("Offer", "Offer"),
        ("HR", "HR interview"),
        ("Rejection", "Rejection"),
        ("Resume sent", "Sent"),
    ],
)
def test_add_vacancy_with_status_on_board_desktop(
    desktop_user_authorization_for_adding_cards_to_statuses,
    config_data: dict,
    status: str,
    expected_board_text: str,
):
    board = desktop_user_authorization_for_adding_cards_to_statuses.board
    vacancy_name = config_data['vacancy_name_with_status']

    board.add_vacancy_with_status_for_tests(vacancy_name, status)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{expected_board_text}']/..//h3[text()='{vacancy_name}']")).to_be_visible()

    board.delete_vacancy(vacancy_name, expected_board_text)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{expected_board_text}']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()
    board.open_add_vacancy_form()


@pytest.mark.parametrize(
    "initial_status",
    [
        "Test task",
        "Technical interview",
        "Offer",
        "HR",
        "Rejection",
        "Resume sent",
    ],
)
def test_edit_company_location_position_in_vacancy_card_desktop(
    desktop_user_authorization_for_adding_cards_to_statuses,
    config_data: dict,
    initial_status: str,
):
    board = desktop_user_authorization_for_adding_cards_to_statuses.board
    original_vacancy_name = config_data['vacancy_name_for_edit']
    updated_value = config_data['updated_value']

    if initial_status == "HR":
        board_status_text = "HR interview"
    elif initial_status == "Resume sent":
        board_status_text = "Sent"
    else:
        board_status_text = initial_status

    board.add_vacancy_with_status_for_tests(original_vacancy_name, initial_status)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//h3[text()='{original_vacancy_name}']")).to_be_visible()
    board.select_vacancy_from_tab(original_vacancy_name, board_status_text)

    board.edit_value_in_field_add_vacancy_form("company", updated_value)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//p[text()='{updated_value}']")).to_be_visible()
    board.select_vacancy_from_tab(original_vacancy_name, board_status_text)

    board.edit_value_in_field_add_vacancy_form("location", updated_value)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//h3[text()='{original_vacancy_name}']/../following-sibling::div/span[text()='{updated_value}']")).to_be_visible()
    board.select_vacancy_from_tab(original_vacancy_name, board_status_text)

    board.edit_value_in_field_add_vacancy_form("vacancy", updated_value)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//h3[text()='{updated_value}']")).to_be_visible()

    board.delete_vacancy(updated_value, board_status_text)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//h3[text()='{updated_value}']")).not_to_be_visible()
    board.open_add_vacancy_form()


@pytest.mark.parametrize(
    "initial_status",
    [
        "Test task",
        "Technical interview",
        "Offer",
        "HR",
        "Rejection",
        "Resume sent",
    ],
)
def test_edit_work_type_in_vacancy_card_desktop(
    desktop_user_authorization_for_adding_cards_to_statuses,
    config_data: dict,
    initial_status: str,
):
    board = desktop_user_authorization_for_adding_cards_to_statuses.board
    vacancy_name = config_data['vacancy_name_for_edit']

    if initial_status == "HR":
        board_status_text = "HR interview"
    elif initial_status == "Resume sent":
        board_status_text = "Sent"
    else:
        board_status_text = initial_status

    board.add_vacancy_with_status_for_tests(vacancy_name, initial_status)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//h3[text()='{vacancy_name}']")).to_be_visible()

    board.select_vacancy_from_tab(config_data['vacancy_name_for_edit'], board_status_text)
    board.edit_work_type_in_add_vacancy_form("hybrid")
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//h3[text()='{vacancy_name}']/../following-sibling::div/span[text()='Hybrid']")).to_be_visible()

    board.select_vacancy_from_tab(config_data['vacancy_name_for_edit'], board_status_text)
    board.edit_work_type_in_add_vacancy_form("office")
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//h3[text()='{vacancy_name}']/../following-sibling::div/span[text()='Office']")).to_be_visible()

    board.select_vacancy_from_tab(config_data['vacancy_name_for_edit'], board_status_text)
    board.edit_work_type_in_add_vacancy_form("remote")
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//h3[text()='{vacancy_name}']/../following-sibling::div/span[text()='Remote']")).to_be_visible()

    board.delete_vacancy(vacancy_name, board_status_text)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.locator(f"//div[text()='{board_status_text}']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()
    board.open_add_vacancy_form()


@pytest.mark.parametrize("stage_name", [
    "Technical interview",
    "Test task",
    "HR"
])
def test_add_new_stage_desktop(desktop_user_authorization_for_adding_cards_to_statuses, config_data: dict, stage_name):
    board = desktop_user_authorization_for_adding_cards_to_statuses.board
    stage_label_locator = "//label[text()='Status']/..//div//div[@class='relative'][last()]//label"

    board.open_add_stage_dropdown()
    board.select_add_stage_value(stage_name)
    expect(desktop_user_authorization_for_adding_cards_to_statuses.page.locator(stage_label_locator)).to_have_text(stage_name)
