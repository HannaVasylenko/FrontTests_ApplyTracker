import calendar
from datetime import datetime, timedelta
import  pytest


@pytest.mark.parametrize("test_input", [
    "Year",
    "Month",
    "Day"
])
def test_select_date_tab_on_statistic_page_mobile(mobile_statistic_page, config_data: dict, test_input):
    mobile_statistic_page.statistic.select_date_tab(test_input)
    button_locator = mobile_statistic_page.page.locator(f"//aside/..//button[text()='{test_input}']")
    assert "border-b-textBlack" in button_locator.get_attribute("class")


def test_select_day_value_on_statistic_page_mobile(mobile_statistic_page, config_data: dict):
    mobile_statistic_page.statistic.select_date_tab("Day")
    now = datetime.now()

    day_minus_2 = now - timedelta(days=2)
    formatted_date_minus_2 = day_minus_2.strftime("%B ") + str(day_minus_2.day).strip() + day_minus_2.strftime(", %Y")
    button_locator = mobile_statistic_page.page.locator(f"//aside/..//button//abbr[@aria-label='{formatted_date_minus_2}']/..")
    button_locator.click()
    assert "react-calendar__tile--active" in button_locator.get_attribute("class")

    day_plus_2 = now + timedelta(days=2)
    formatted_date_plus_2 = day_plus_2.strftime("%B ") + str(day_plus_2.day).strip() + day_plus_2.strftime(", %Y")
    button_locator = mobile_statistic_page.page.locator(f"//aside/..//button//abbr[@aria-label='{formatted_date_plus_2}']/..")
    button_locator.click()
    assert "react-calendar__tile--active" in button_locator.get_attribute("class")


def test_select_month_value_on_statistic_page_mobile(mobile_statistic_page, config_data: dict):
    mobile_statistic_page.statistic.select_date_tab("Month")
    now = datetime.now()
    current_month = now.month

    number_previous = current_month - 2
    name_previous = calendar.month_name[number_previous]
    button_locator = mobile_statistic_page.page.locator(f"//aside/../main//div[contains(@class,'row-start-2')]//abbr[text()='{name_previous}']/following-sibling::span/..")
    button_locator.click()
    assert "react-calendar__tile--hasActive" in button_locator.get_attribute("class")

    number_next = current_month + 2
    name_next = calendar.month_name[number_next]
    button_locator = mobile_statistic_page.page.locator(f"//aside/../main//div[contains(@class,'row-start-2')]//abbr[text()='{name_next}']/following-sibling::span/..")
    button_locator.click()
    assert "react-calendar__tile--hasActive" in button_locator.get_attribute("class")


def test_select_year_value_on_statistic_page_mobile(mobile_statistic_page, config_data: dict):
    mobile_statistic_page.statistic.select_date_tab("Year")
    now = datetime.now()
    current_year = now.year

    button_locator = mobile_statistic_page.page.locator(f"//aside/..//button[text()='{current_year - 2}']")
    button_locator.click()
    assert "react-calendar__tile--hasActive" in button_locator.get_attribute("class")

    button_locator = mobile_statistic_page.page.locator(f"//aside/..//button[text()='{current_year + 2}']")
    button_locator.click()
    assert "react-calendar__tile--hasActive" in button_locator.get_attribute("class")
