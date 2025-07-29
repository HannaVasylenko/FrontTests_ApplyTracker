from playwright.sync_api import expect


def test_change_language_of_app_on_board_page_desktop(desktop_user_authorization, config_data: dict):
    board = desktop_user_authorization.board
    footer_locator = "//footer//h2"

    board.select_language("UA")
    expect(desktop_user_authorization.locator(footer_locator)).to_have_text(config_data['footer_board_ua'])

    board.select_language("EN")
    expect(desktop_user_authorization.locator(footer_locator)).to_have_text(config_data['footer_board_en'])
