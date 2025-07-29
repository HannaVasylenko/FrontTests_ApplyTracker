from playwright.sync_api import expect


def test_change_language_of_app_on_board_page_mobile(mobile_user_authorization_for_sidebar, config_data: dict):
    board = mobile_user_authorization_for_sidebar.board
    page = mobile_user_authorization_for_sidebar.page

    board.click_on_sidebar_btn()
    board.select_language("UA")
    expect(page.get_by_role("link", name=config_data['ua_vacancy_tab_name'])).to_be_visible()

    board.select_language("EN")
    expect(page.get_by_role("link", name=config_data['en_vacancy_tab_name'])).to_be_visible()
