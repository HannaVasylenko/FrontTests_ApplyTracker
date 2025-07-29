from playwright.sync_api import expect


def test_add_event_valid_desktop(desktop_add_event_on_statistic_page, config_data: dict):
    statistic = desktop_add_event_on_statistic_page.statistic
    event_name = config_data['event_name']
    event_locator = f"//h3[text()='Soon']/..//li//p[text()='{event_name}']"

    statistic.add_event(event_name, "10", "05")
    expect(desktop_add_event_on_statistic_page.locator(event_locator)).to_be_visible()
    statistic.delete_event(event_name)
    expect(desktop_add_event_on_statistic_page.locator(event_locator)).not_to_be_visible()


def test_edit_event_time_and_date_desktop(desktop_add_and_delete_event, config_data: dict):
    statistic = desktop_add_and_delete_event.statistic
    original_event_name = config_data['event_name']
    updated_event_name = config_data['updated_event_name']
    event_time_locator = f"//h3[text()='Soon']/..//li//p[text()='{original_event_name}']/following-sibling::p[text()='13:15']"
    updated_event_locator = f"//h3[text()='Soon']/..//li//p[text()='{updated_event_name}']"

    statistic.edit_time_in_edit_event_window(original_event_name, "13", "15")
    expect(desktop_add_and_delete_event.locator(event_time_locator)).to_be_visible()
    statistic.edit_name_in_edit_event_window(original_event_name, updated_event_name)
    expect(desktop_add_and_delete_event.locator(updated_event_locator)).to_be_visible()


def test_add_event_valid_mobile(mobile_add_event, config_data: dict):
    statistic = mobile_add_event.statistic
    event_name = config_data['event_name']
    event_locator = f"//h3[text()='Soon']/..//li//p[text()='{event_name}']"

    statistic.add_event(event_name, "10", "05")
    expect(mobile_add_event.locator(event_locator)).to_be_visible()
    statistic.delete_event(event_name)
    expect(mobile_add_event.locator(event_locator)).not_to_be_visible()


def test_edit_event_time_and_date_mobile(mobile_add_and_delete_event, config_data: dict):
    statistic = mobile_add_and_delete_event.statistic
    original_event_name = config_data['event_name']
    updated_event_name = config_data['updated_event_name']
    event_time_locator = f"//h3[text()='Soon']/..//li//p[text()='{original_event_name}']/following-sibling::p[text()='13:15']"
    updated_event_locator = f"//h3[text()='Soon']/..//li//p[text()='{updated_event_name}']"

    statistic.edit_time_in_edit_event_window(original_event_name, "13", "15")
    expect(mobile_add_and_delete_event.locator(event_time_locator)).to_be_visible()
    statistic.edit_name_in_edit_event_window(original_event_name, updated_event_name)
    expect(mobile_add_and_delete_event.locator(updated_event_locator)).to_be_visible()
