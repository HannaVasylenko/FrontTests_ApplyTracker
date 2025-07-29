from playwright.sync_api import expect


def test_search_field_by_vacancy_name_desktop(desktop_user_authorization, config_data: dict):
    board = desktop_user_authorization.board
    search_term = config_data['search_vacancy_name_value']
    zero_results_locator = "//form/..//p[text()='0 search results']"
    no_vacancies_locator = "//p[text()='There are no vacancies in this section...']"
    search_results_locator = "//form/..//p"
    desktop_user_authorization.locator(".size-11").first.click()

    board.type_in_search_field(search_term)
    if desktop_user_authorization.locator(zero_results_locator).is_visible():
        expect(desktop_user_authorization.locator(no_vacancies_locator)).to_be_visible()
    else:
        desktop_user_authorization.locator(search_results_locator).wait_for(state='visible')
        vacancy_names_values = board.collect_search_result_values()
        for search_value in vacancy_names_values:
            search_term_lower = search_term.lower()
            search_value_lower = search_value.lower()
            assert search_term_lower in search_value_lower, f"Expected '{search_term_lower}' in search result, but got '{search_value_lower}'"


def test_search_field_by_company_name_desktop(desktop_user_authorization, config_data: dict):
    board = desktop_user_authorization.board
    search_term = config_data['company_name']
    zero_results_locator = "//form/..//p[text()='0 search results']"
    no_vacancies_locator = "//p[text()='There are no vacancies in this section...']"
    search_results_locator = "//form/..//p"
    desktop_user_authorization.locator(".size-11").first.click()

    board.type_in_search_field(search_term)
    if desktop_user_authorization.locator(zero_results_locator).is_visible():
        expect(desktop_user_authorization.locator(no_vacancies_locator)).to_be_visible()
    else:
        desktop_user_authorization.locator(search_results_locator).wait_for(state='visible')
        vacancy_names_values = board.collect_search_result_company_name_values()
        for search_value in vacancy_names_values:
            search_term_lower = search_term.lower()
            search_value_lower = search_value.lower()
            assert search_term_lower in search_value_lower, f"Expected '{search_term}' to be found in search result, but got '{search_value}'"


def test_search_field_by_location_desktop(desktop_user_authorization, config_data: dict):
    board = desktop_user_authorization.board
    search_term = config_data['location']
    zero_results_locator = "//form/..//p[text()='0 search results']"
    no_vacancies_locator = "//p[text()='There are no vacancies in this section...']"
    search_results_locator = "//form/..//p"
    desktop_user_authorization.locator(".size-11").first.click()

    board.type_in_search_field(search_term)
    if desktop_user_authorization.locator(zero_results_locator).is_visible():
        expect(desktop_user_authorization.locator(no_vacancies_locator)).to_be_visible()
    else:
        desktop_user_authorization.locator(search_results_locator).wait_for(state='visible')
        vacancy_names_values = board.collect_search_result_location_values(search_term)
        for search_value in vacancy_names_values:
            assert search_term in search_value, f"Expected '{search_term}' in search result, but got '{search_value}'"


def test_search_field_with_nonexistent_value_desktop(desktop_user_authorization, config_data: dict):
    board = desktop_user_authorization.board
    nonexistent_search_term = config_data['search_vacancy_name_nonexistent_value']
    empty_search_text = config_data['empty_search_result']
    no_vacancies_message = config_data['no_vacancies_message']
    search_results_locator = "//form/..//p"
    empty_result_locator = "//main//form/following-sibling::div/p"
    no_vacancies_locator = f"//p[text()='{no_vacancies_message}']"
    desktop_user_authorization.locator(".size-11").first.click()
    board.type_in_search_field(nonexistent_search_term)
    desktop_user_authorization.locator(search_results_locator).wait_for(state='visible')
    expect(desktop_user_authorization.locator(empty_result_locator)).to_have_text(f"{empty_search_text}{nonexistent_search_term}")
    expect(desktop_user_authorization.locator(no_vacancies_locator)).to_be_visible()
