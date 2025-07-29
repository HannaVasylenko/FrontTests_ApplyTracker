import json
import logging
import os.path
import re
from datetime import datetime
import  pytest
from page_objects.app_page import App
from settings import *
from pytest import  fixture
from playwright.sync_api import sync_playwright, expect

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("report.txt", mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


def pytest_runtest_logreport(report):
    if report.when == "call":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        test_status = "PASSED" if report.passed else "FAILED" if report.failed else "SKIPPED"

        with open("report.txt", "a", encoding="utf-8") as f:
            f.write(f"Time: {current_time}\n")
            f.write(f"Test name: {report.nodeid}\nStatus: {test_status}\n")
            f.write("\n")


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


# @fixture(scope='session', params=['firefox', 'chrome', 'msedge', 'webkit'], ids=['firefox', 'chrome', 'msedge', 'webkit'])
# def get_browser(get_playwright, request):
#     browser = request.param
#     os.environ['PWBROWSER'] = browser
#     headless= request.config.getini('headless').lower == 'false'
#
#     if browser == 'firefox':
#         yield get_playwright.firefox.launch(headless=headless)
#     elif browser == 'chrome':
#         yield get_playwright.chromium.launch(headless=headless, channel="chrome")
#     elif browser == 'msedge':
#         yield get_playwright.chromium.launch(headless=headless, channel="msedge")
#     elif browser == 'webkit':
#         yield get_playwright.webkit.launch(headless=headless)
#     else:
#         pytest.fail("Unsupported browser specified")
#     del os.environ['PWBROWSER']


@pytest.fixture(scope='session')
def get_browser(get_playwright, request):
    browser = 'chrome'
    os.environ['PWBROWSER'] = browser

    yield get_playwright.chromium.launch(headless=False, channel="chrome")
    del os.environ['PWBROWSER']


@fixture(scope='session')
def get_browser_chrome(get_playwright, request):
    os.environ['PWBROWSER'] = 'chrome'
    browser = get_playwright.chromium.launch(headless=False, channel="chrome")
    yield browser
    browser.close()
    del os.environ['PWBROWSER']


@fixture(scope='session')
def desktop_app_only_chrome_browser(get_browser_chrome, request):
    base_url = request.config.getini('base_url')
    viewport_size ={'width': 1536, 'height': 864}
    app = App(get_browser_chrome, base_url=base_url, viewport=viewport_size, **BROWSER_OPTIONS)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def desktop_user_authorization_with_chrome_browser(desktop_app_only_chrome_browser, request):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app_only_chrome_browser
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    yield app


@fixture(scope='session')
def desktop_user_authorization_for_vacancy_form_with_chrome_browser(desktop_user_authorization_with_chrome_browser, config_data: dict):
    app = desktop_user_authorization_with_chrome_browser
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add vacancy").click()
    app.page.get_by_text("Add a new vacancy").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def sign_in_desktop_app_with_chrome_browser(desktop_app_only_chrome_browser, config_data: dict):
    app = desktop_app_only_chrome_browser
    app.goto('/sign-up')
    yield app

    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.profile.delete_account()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_app(get_browser, request, config_data: dict):
    base_url = request.config.getini('base_url')
    viewport_size ={'width': 1536, 'height': 864}
    context_options = {
        'locale': 'en-US',
        'viewport': viewport_size,
        'base_url': base_url
    }
    if os.environ.get('PWBROWSER') == 'webkit':
        pytest.skip("Skipping WebKit browser for desktop")
    app = App(get_browser, **context_options)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def desktop_app_for_login(get_browser, request, config_data: dict):
    base_url = request.config.getini('base_url')
    viewport_size ={'width': 1536, 'height': 864}
    if os.environ.get('PWBROWSER') == 'webkit':
        pytest.skip("Skipping WebKit browser for desktop")
    app = App(get_browser, base_url=base_url, viewport=viewport_size, **BROWSER_OPTIONS)
    app.goto('/')
    yield app

    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])
    app.close()


# @fixture(scope='session', params=['iPhone 15', 'Pixel 7'])
# def mobile_app(get_playwright, get_browser, request, config_data: dict):
#     browser = os.environ.get('PWBROWSER')
#
#     if browser in ['firefox', 'msedge']:
#         pytest.skip(f"Mobile version is not supported for {browser}.")
#     if browser == 'webkit' and request.param == 'Pixel 7':
#         pytest.skip(f"Skipping WebKit browser for {request.param} device.")
#
#     base_url = request.config.getini('base_url')
#     device = request.param
#
#     device_config = get_playwright.devices.get(device, {})
#     if not device_config:
#         pytest.fail(f"Device configuration not found for {device}.")
#
#     if browser == 'webkit':
#         device_config['device_scale_factor'] = 1
#         device_config['is_mobile'] = True
#         device_config['has_touch'] = True
#
#     if device == 'iPhone 15':
#         device_config['viewport'] = {'width': 393, 'height': 852}
#     elif device == 'Pixel 7':
#         device_config['viewport'] = {'width': 412, 'height': 915}
#
#     app = App(get_browser, base_url=base_url, **device_config)
#     app.goto('/')
#     app.page.wait_for_load_state('networkidle')
#     expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])
#     yield app
#     app.close()


@fixture(scope='session', params=['iPhone 15'])
def mobile_app(get_playwright, get_browser, request, config_data: dict):
    browser = os.environ.get('PWBROWSER')

    if browser in ['firefox', 'msedge']:
        pytest.skip(f"Mobile version is not supported for {browser}.")

    base_url = request.config.getini('base_url')
    device = request.param

    device_config = get_playwright.devices.get(device, {}).copy()
    if not device_config:
        pytest.fail(f"Device configuration not found for {device}.")

    device_config['locale'] = 'en-US'

    if browser == 'webkit':
        device_config['device_scale_factor'] = device_config.get('device_scale_factor', 1)
        device_config['is_mobile'] = True
        device_config['has_touch'] = True

    if device == 'iPhone 15':
        device_config['viewport'] = {'width': 393, 'height': 852}

    app = App(get_browser, base_url=base_url, **device_config)
    app.goto('/')
    app.page.wait_for_load_state('networkidle')
    yield app
    app.close()


@fixture(scope='session', params=['iPhone 15', 'Pixel 7'])
def mobile_app_for_login(get_playwright, get_browser, request, config_data: dict):
    browser = os.environ.get('PWBROWSER')

    if browser in ['firefox', 'msedge']:
        pytest.skip(f"Mobile version is not supported for {browser}.")
    if browser == 'webkit' and request.param == 'Pixel 7':
        pytest.skip(f"Skipping WebKit browser for {request.param} device.")

    base_url = request.config.getini('base_url')
    device = request.param

    device_config = get_playwright.devices.get(device, {})
    if not device_config:
        pytest.fail(f"Device configuration not found for {device}.")

    if browser == 'webkit':
        device_config['device_scale_factor'] = 1
        device_config['is_mobile'] = True
        device_config['has_touch'] = True

    if device == 'iPhone 15':
        device_config['viewport'] = {'width': 393, 'height': 852}
    elif device == 'Pixel 7':
        device_config['viewport'] = {'width': 412, 'height': 915}

    app = App(get_browser, base_url=base_url, **device_config)
    app.goto('/')
    app.page.wait_for_load_state('networkidle')
    yield app

    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])
    app.close()


@fixture(scope='session')
def sign_in_desktop_app(desktop_app, config_data: dict):
    app = desktop_app
    app.goto('/sign-up')
    yield app


@fixture(scope='session')
def sign_in_mobile_app(mobile_app, config_data: dict):
    app = mobile_app
    app.goto('/sign-up')
    yield app


@fixture(scope='session')
def reset_password_desktop_app(desktop_app, config_data: dict):
    app = desktop_app
    app.goto('/reset-password')
    yield app


@fixture(scope='session')
def reset_password_mobile_app(mobile_app, config_data: dict):
    app = mobile_app
    app.goto('/reset-password')
    yield app


@fixture(scope='session')
def desktop_app_auth(desktop_app, request):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    yield app


@fixture(scope='session')
def mobile_app_auth(mobile_app, request):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    yield app


@fixture(scope='session')
def desktop_user_authorization(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    # app.page.locator(".size-11").first.click()
    yield app

    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_logout(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    # app.page.locator(".size-11").first.click()
    yield app


@fixture(scope='session')
def mobile_user_authorization(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    yield app

    app.board.close_search_field()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_user_authorization_for_logout(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    yield app


@fixture(scope='session')
def mobile_user_authorization_for_sidebar(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    yield app

    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_note_page(desktop_user_authorization, config_data: dict):
    app = desktop_user_authorization
    app.page.get_by_role("link", name="Notes").click()
    app.page.get_by_text("Add a note").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    yield app


@fixture(scope='session')
def mobile_user_authorization_for_sorting_note(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Notes").click()
    app.page.get_by_text("Add a note").wait_for(state='visible')
    yield app

    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_user_authorization_for_note_page(mobile_user_authorization, config_data: dict):
    app = mobile_user_authorization
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Notes").click()
    app.page.get_by_text("Add a note").wait_for(state='visible')
    # app.page.locator(".size-11").first.click()
    yield app


@fixture(scope='session')
def desktop_user_authorization_for_add_note_window(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Notes").click()
    app.page.get_by_text("Add a note").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add a note").click()
    app.page.locator("//span[text()='New note']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_user_authorization_for_add_note_window(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Notes").click()
    app.page.get_by_text("Add a note").wait_for(state='visible')
    app.page.get_by_role("button", name="Add a note").click()
    app.page.locator("//span[text()='New note']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_add_note_test_window(desktop_user_authorization_for_note_page, config_data: dict):
    app = desktop_user_authorization_for_note_page
    app.page.get_by_role("button", name="Add a note").click()
    app.page.locator("//span[text()='New note']").wait_for(state='visible')
    yield app


@fixture(scope='session')
def desktop_user_authorization_for_generate_notes(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Notes").click()
    app.page.get_by_text("Add a note").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add a note").click()
    app.page.locator("//span[text()='New note']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_user_authorization_for_add_note_test_window(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Notes").click()
    app.page.get_by_text("Add a note").wait_for(state='visible')
    app.page.get_by_role("button", name="Add a note").click()
    app.page.locator("//span[text()='New note']").wait_for(state='visible')
    yield app

    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_profile_page(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    yield app

    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_delete_account(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    yield app


@fixture(scope='session')
def mobile_user_authorization_for_delete_account(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    # app.page.locator(".size-11").first.click()
    yield app


@fixture(scope='session')
def mobile_user_authorization_for_profile_page(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    # app.page.locator(".size-11").first.click()
    yield app

    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_authorization_for_resume_on_profile_page(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add Resume +").click()
    app.page.locator("//span[text()='Add resume']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_authorization_for_resume_on_profile_page(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.get_by_role("button", name="Add Resume +").click()
    app.page.locator("//span[text()='Add resume']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_authorization_for_cover_letter_on_profile_page(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add cover letter +").click()
    app.page.locator("//span[text()='Add cover letter']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_authorization_for_cover_letter_on_profile_page(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.get_by_role("button", name="Add cover letter +").click()
    app.page.locator("//span[text()='Add cover letter']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_authorization_for_project_link_on_profile_page(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add project link +").click()
    app.page.locator("//span[text()='Add project']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_authorization_for_project_link_on_profile_page(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.get_by_role("button", name="Add project link +").click()
    app.page.locator("//span[text()='Add project']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_authorization_for_link_on_profile_page(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add link +").click()
    app.page.locator("//span[text()='Add link']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_authorization_for_link_on_profile_page(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.click_on_sidebar_btn()
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Account").click()
    app.page.get_by_text("Personal information").wait_for(state='visible')
    app.page.get_by_role("button", name="Add link +").click()
    app.page.locator("//span[text()='Add link']").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.page.locator("//h4/..//button[text()='Close']").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_contact_us_form(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_text("Contact Us").click()
    app.page.get_by_text("Name").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_contact_us_form(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_text("Contact Us").click()
    app.page.get_by_text("Name").wait_for(state='visible')
    yield app

    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_user_authorization_for_contact_us_form(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_text("Contact Us").click()
    app.page.get_by_text("Name").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_user_authorization_contact_us_form(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.get_by_text("Contact Us").click()
    app.page.get_by_text("Name").wait_for(state='visible')
    yield app

    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_add_vacancy_form(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add vacancy").click()
    app.page.get_by_text("Add a new vacancy").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_moving_cards(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add vacancy").click()
    app.page.get_by_text("Add a new vacancy").wait_for(state='visible')
    yield app

    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_generate_cards(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add vacancy").click()
    app.page.get_by_text("Add a new vacancy").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_user_authorization_for_adding_cards_to_statuses(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add vacancy").click()
    app.page.get_by_text("Add a new vacancy").wait_for(state='visible')
    yield app

    app.locator(".z-0 > .z-0").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_user_authorization_for_vacancy_form(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.page.get_by_role("button", name="Add vacancy").click()
    yield app

    app.locator(".z-0 > .z-0").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_user_authorization_for_vacancy_form_for_moving_cards(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.page.get_by_role("button", name="Add vacancy").click()
    yield app

    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_user_authorization_for_add_vacancy_form(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.page.get_by_role("button", name="Add vacancy").click()
    yield app

    app.locator(".z-0 > .z-0").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def navigate_to_forgot_password_page_desktop(desktop_app):
    app = desktop_app
    app.navigate_to_forgot_password_form()
    app.locator("form h2").wait_for(state='visible')
    yield app


@fixture(scope='session')
def navigate_to_forgot_password_form_mobile(mobile_app):
    app = mobile_app
    app.navigate_to_forgot_password_form()
    app.locator("form h2").wait_for(state='visible')
    yield app


@fixture(scope='session')
def select_sort_by_status_dropbox_desktop(desktop_user_authorization, config_data: dict):
    app = desktop_user_authorization
    app.locator(".size-11").first.click()
    app.page.locator("//div[@class='flex-nowrap']").wait_for(state='hidden')
    app.board.click_on_sort_by_btn()
    app.board.select_sort_by_dropbox_value(config_data['sort_by_status'])
    yield app


@fixture(scope='session')
def mobile_user_authorization_for_status_type(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sort_by_btn_mobile()
    app.board.select_sort_by_dropbox_value(config_data['sort_by_status'])
    yield app

    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def select_sort_by_work_type_dropbox_desktop(desktop_user_authorization, config_data: dict):
    app = desktop_user_authorization
    app.locator(".size-11").first.click()
    app.board.click_on_sort_by_btn()
    app.board.select_sort_by_dropbox_value(config_data['sort_by_value'])
    yield app


@fixture(scope='session')
def mobile_user_authorization_for_sort_by_work_type(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sort_by_btn_mobile()
    app.board.select_sort_by_dropbox_value(config_data['sort_by_value'])
    yield app

    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_statistic_page(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Statistics").click()
    app.page.locator("//div[@class='react-calendar__navigation']").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    yield app

    app.page.get_by_role("link", name="Vacancies").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])

@fixture(scope='session')
def mobile_statistic_page(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.locator("//span[text()='Statistics']").click()
    app.page.locator("//div[@class='react-calendar__navigation']").wait_for(state='visible')
    yield app

    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Vacancies").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_add_event_window_on_statistic_page(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Statistics").click()
    #app.page.locator("//span[text()='Statistics']").click()
    app.page.locator("//div[@class='react-calendar__navigation']").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add event").click()
    app.page.locator("//aside/../following-sibling::div//span[text()='Add event']").wait_for(state='visible')
    yield app

    app.locator("div:nth-child(2) > div > .scrollbar-transparent > div:nth-child(2) > .z-0").click()
    app.page.get_by_role("button", name="Close").nth(1).click()
    app.page.get_by_role("link", name="Vacancies").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_add_event_for_edit_event(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Statistics").click()
    app.page.locator("//div[@class='react-calendar__navigation']").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add event").click()
    app.page.locator("//aside/../following-sibling::div//span[text()='Add event']").wait_for(state='visible')
    yield app

    app.page.get_by_role("link", name="Vacancies").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def desktop_add_event_on_statistic_page(desktop_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.locator("#input-query").wait_for(state='visible')
    app.board.change_page_language_to_en()
    app.page.get_by_role("link", name="Statistics").click()
    #app.page.locator("//span[text()='Statistics']").click()
    app.page.locator("//div[@class='react-calendar__navigation']").wait_for(state='visible')
    app.page.locator(".size-11").first.click()
    app.page.get_by_role("button", name="Add event").click()
    app.page.locator("//aside/../following-sibling::div//span[text()='Add event']").wait_for(state='visible')
    yield app

    app.page.get_by_role("link", name="Vacancies").click()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_add_event_window_on_statistic_page(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.locator("//span[text()='Statistics']").click()
    app.page.locator("//div[@class='react-calendar__navigation']").wait_for(state='visible')
    #app.page.locator("//h3[text()='Total Vacancies']").wait_for(state='visible')
    app.page.get_by_role("button", name="Add event").click()
    app.page.locator("//aside/../following-sibling::div//span[text()='Add event']").wait_for(state='visible')
    yield app

    app.locator("div:nth-child(2) > div > .scrollbar-transparent > div:nth-child(2) > .z-0").click()
    app.page.get_by_role("button", name="Close").nth(1).click()
    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Vacancies").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_add_event_for_edit_event(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.locator("//span[text()='Statistics']").click()
    app.page.locator("//div[@class='react-calendar__navigation']").wait_for(state='visible')
    #app.page.locator("//h3[text()='Total Vacancies']").wait_for(state='visible')
    app.page.get_by_role("button", name="Add event").click()
    app.page.locator("//aside/../following-sibling::div//span[text()='Add event']").wait_for(state='visible')
    yield app

    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Vacancies").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


@fixture(scope='session')
def mobile_add_event(mobile_app, request, config_data: dict):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.goto('/log-in')
    app.login(**config)
    app.page.locator("//div[contains(@class, 'scrollbar-transparent')]//button[@type='button']").click()
    app.page.get_by_label("Search button").wait_for(state='visible')
    app.board.change_page_language_to_en_in_mobile()
    app.board.click_on_sidebar_btn()
    app.page.locator("//span[text()='Statistics']").click()
    app.page.locator("//div[@class='react-calendar__navigation']").wait_for(state='visible')
    #app.page.locator("//h3[text()='Total Vacancies']").wait_for(state='visible')
    app.page.get_by_role("button", name="Add event").click()
    app.page.locator("//aside/../following-sibling::div//span[text()='Add event']").wait_for(state='visible')
    yield app

    app.board.click_on_sidebar_btn()
    app.page.get_by_role("link", name="Vacancies").click()
    app.board.click_on_sidebar_btn()
    app.locator("div").filter(has_text=re.compile(r"^Log out$")).get_by_role("img").click()
    app.board.exit_btn.click()
    app.page.locator("main h2").wait_for(state='visible')
    expect(app.locator("main h2")).to_have_text(config_data['title_login_page'])


def pytest_addoption(parser):
    parser.addoption('--secure', action='store', default='secure.json')
    parser.addini('base_url', help='base url of website under test', default='https://')
    parser.addini('headless', help='run browser in headless mode', default='False')


@pytest.fixture(scope="session")
def config_data() -> dict:
    config_path = os.path.join(os.path.dirname(__file__), "tests/user_config.json")
    with open(config_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_config(project_path: str, file: str) -> dict:
    config_file = os.path.join(project_path, file)
    with open(config_file) as cfg:
        return json.loads(cfg.read())


@fixture(scope='session')
def desktop_add_and_delete_event(desktop_add_event_for_edit_event, config_data: dict):
    app = desktop_add_event_for_edit_event
    event_name = config_data['event_name']
    updated_event_name = config_data['updated_event_name']
    app.statistic.add_event(event_name, "10", "05")
    expect(app.locator(f"//h3[text()='Soon']/..//li//p[text()='{config_data['event_name']}']")).to_be_visible()

    yield app

    app.statistic.delete_event(updated_event_name)
    expect(app.locator(f"//h3[text()='Soon']/..//li//p[text()='{updated_event_name}']")).not_to_be_visible()


@fixture(scope='session')
def mobile_add_and_delete_event(mobile_add_event_for_edit_event, config_data: dict):
    app = mobile_add_event_for_edit_event
    event_name = config_data['event_name']
    updated_event_name = config_data['updated_event_name']
    app.statistic.add_event(event_name, "10", "05")
    expect(app.locator(f"//h3[text()='Soon']/..//li//p[text()='{config_data['event_name']}']")).to_be_visible()

    yield app

    app.statistic.delete_event(updated_event_name)
    expect(app.locator(f"//h3[text()='Soon']/..//li//p[text()='{updated_event_name}']")).not_to_be_visible()


@fixture(scope='session')
def desktop_add_vacancy_without_status(desktop_user_authorization_for_moving_cards, config_data: dict):
    app = desktop_user_authorization_for_moving_cards
    vacancy_name = config_data['vacancy_name_for_changing_status']
    app.board.create_vacancy_for_moving_vacancy_cards(vacancy_name)
    expect(app.locator(f"//div[text()='Saved']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()

    yield app

    app.board.delete_vacancy(vacancy_name,"Sent")
    expect(app.locator(f"//div[text()='Offer']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()


@fixture(scope='session')
def mobile_add_vacancy_without_status(mobile_user_authorization_for_vacancy_form_for_moving_cards, config_data: dict):
    app = mobile_user_authorization_for_vacancy_form_for_moving_cards
    vacancy_name = config_data['vacancy_name_for_changing_status']
    app.board.create_vacancy_for_moving_vacancy_cards(vacancy_name)
    expect(app.locator(f"//div[text()='Saved']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()

    yield app

    app.board.delete_vacancy(vacancy_name,"Sent")
    expect(app.locator(f"//div[text()='Offer']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()


@fixture(scope='session')
def desktop_add_vacancy_without_to_archive(desktop_user_authorization_for_moving_cards, config_data: dict):
    app = desktop_user_authorization_for_moving_cards
    vacancy_name = config_data['vacancy_name_for_add_to_archive']
    app.board.create_vacancy_for_moving_vacancy_cards(vacancy_name)
    expect(app.locator(f"//div[text()='Saved']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()

    yield app

    app.board.delete_vacancy(vacancy_name,"Feedback archive")
    expect(app.locator(f"//div[text()='Feedback archive']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()


@fixture(scope='session')
def mobile_add_vacancy_without_status_to_archive(mobile_user_authorization_for_vacancy_form_for_moving_cards, config_data: dict):
    app = mobile_user_authorization_for_vacancy_form_for_moving_cards
    vacancy_name = config_data['vacancy_name_for_add_to_archive']
    app.board.create_vacancy_for_moving_vacancy_cards(vacancy_name)
    expect(app.locator(f"//div[text()='Saved']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()

    yield app

    app.board.delete_vacancy(vacancy_name,"Feedback archive")
    expect(app.locator(f"//div[text()='Feedback archive']/..//h3[text()='{vacancy_name}']")).not_to_be_visible()
