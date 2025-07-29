import calendar
from datetime import datetime, timedelta
import  pytest


@pytest.mark.parametrize("date_tab", [
    "Year",
    "Month",
    "Day"
])
def test_select_date_tab_on_statistic_page_desktop(desktop_statistic_page, config_data: dict, date_tab):
    statistic = desktop_statistic_page.statistic
    button_locator = f"//aside/..//button[text()='{date_tab}']"
    statistic.select_date_tab(date_tab)
    button = desktop_statistic_page.page.locator(button_locator)
    assert "border-b-textBlack" in button.get_attribute("class")


def test_select_day_value_on_statistic_page_desktop(desktop_statistic_page, config_data: dict):
    statistic = desktop_statistic_page.statistic
    page = desktop_statistic_page.page
    statistic.select_date_tab("Day")
    now = datetime.now()

    day_minus_2 = now - timedelta(days=2)
    formatted_date_minus_2 = day_minus_2.strftime("%B %d, %Y").replace(" 0", " ")
    button_locator_minus_2_str = f"//aside/..//button//abbr[@aria-label='{formatted_date_minus_2}']/.."
    button_locator_minus_2 = page.locator(button_locator_minus_2_str)
    button_locator_minus_2.click()
    assert "react-calendar__tile--active" in button_locator_minus_2.get_attribute("class")

    day_plus_2 = now + timedelta(days=2)
    formatted_date_plus_2 = day_plus_2.strftime("%B %d, %Y").replace(" 0", " ")
    button_locator_plus_2_str = f"//aside/..//button//abbr[@aria-label='{formatted_date_plus_2}']/.."
    button_locator_plus_2 = page.locator(button_locator_plus_2_str)
    button_locator_plus_2.click()
    assert "react-calendar__tile--active" in button_locator_plus_2.get_attribute("class")


def test_select_month_value_on_statistic_page_desktop(desktop_statistic_page, config_data: dict):
    statistic = desktop_statistic_page.statistic
    page = desktop_statistic_page.page
    statistic.select_date_tab("Month")
    now = datetime.now()
    current_month = now.month

    previous_month_number = (current_month - 2 - 1) % 12 + 1
    previous_month_name = calendar.month_name[previous_month_number]
    previous_button_locator_str = f"//aside/../main//div[contains(@class,'row-start-2')]//abbr[text()='{previous_month_name}']/following-sibling::span/.."
    previous_button_locator = page.locator(previous_button_locator_str)
    previous_button_locator.click()
    assert "react-calendar__tile--hasActive" in previous_button_locator.get_attribute("class")

    next_month_number = (current_month + 2 - 1) % 12 + 1
    next_month_name = calendar.month_name[next_month_number]
    next_button_locator_str = f"//aside/../main//div[contains(@class,'row-start-2')]//abbr[text()='{next_month_name}']/following-sibling::span/.."
    next_button_locator = page.locator(next_button_locator_str)
    next_button_locator.click()
    assert "react-calendar__tile--hasActive" in next_button_locator.get_attribute("class")


def test_select_year_value_on_statistic_page_desktop(desktop_statistic_page, config_data: dict):
    statistic = desktop_statistic_page.statistic
    page = desktop_statistic_page.page
    now = datetime.now()
    current_year = now.year
    statistic.select_date_tab("Year")

    previous_year = current_year - 2
    previous_year_locator_str = f"//aside/..//button[text()='{previous_year}']"
    previous_year_button = page.locator(previous_year_locator_str)
    previous_year_button.click()
    assert "react-calendar__tile--hasActive" in previous_year_button.get_attribute("class")

    next_year = current_year + 2
    next_year_locator_str = f"//aside/..//button[text()='{next_year}']"
    next_year_button = page.locator(next_year_locator_str)
    next_year_button.click()
    assert "react-calendar__tile--hasActive" in next_year_button.get_attribute("class")
