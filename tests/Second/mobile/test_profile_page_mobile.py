import  pytest
from playwright.sync_api import expect


def test_add_resume_on_profile_page_mobile(mobile_user_authorization_for_profile_page, config_data: dict):
    profile = mobile_user_authorization_for_profile_page.profile
    resume_name = config_data['resume_name']
    resume_section = config_data['resume_section_in_profile']
    resume_xpath = f"//span[text()='Resumes']/../../following-sibling::div//input[@value='{resume_name}']"
    profile.add_resume_to_profile(resume_name, config_data['link'])
    expect(mobile_user_authorization_for_profile_page.locator(resume_xpath)).to_be_visible()
    profile.delete_document_in_profile(resume_section, resume_name)
    expect(mobile_user_authorization_for_profile_page.locator(resume_xpath)).not_to_be_visible()


def test_add_cover_letter_on_profile_page_mobile(mobile_user_authorization_for_profile_page, config_data: dict):
    profile = mobile_user_authorization_for_profile_page.profile
    cover_letter_name = config_data['cover_letter_name']
    cover_letter_section = config_data['cover_letter_section_in_profile']
    cover_letter_xpath = f"//span[text()='Cover letters']/../../following-sibling::div//input[@value='{cover_letter_name}']"
    profile.add_cover_letter_to_profile(cover_letter_name, config_data['link'])
    expect(mobile_user_authorization_for_profile_page.locator(cover_letter_xpath)).to_be_visible()
    profile.delete_document_in_profile(cover_letter_section, cover_letter_name)
    expect(mobile_user_authorization_for_profile_page.locator(cover_letter_xpath)).not_to_be_visible()


def test_add_project_link_on_profile_page_mobile(mobile_user_authorization_for_profile_page, config_data: dict):
    profile = mobile_user_authorization_for_profile_page.profile
    project_name = config_data['project_name']
    github_link = config_data['github_link']
    link = config_data['link']
    project_xpath = f"//span[text()='Projects']/../../following-sibling::div//input[contains(@value, '{project_name}')]"
    profile.add_project_to_profile(project_name, github_link, link)
    expect(mobile_user_authorization_for_profile_page.locator(project_xpath)).to_be_visible()
    profile.delete_project_in_profile(project_name)
    expect(mobile_user_authorization_for_profile_page.locator(project_xpath)).not_to_be_visible()


@pytest.mark.parametrize("link_name, link", [
    ("LinkedIn", "https://www.linkedin.com/in/username"),
    ("Telegram", "https://t.me/username"),
    ("Behance", "https://www.behance.net/yourusername/projectname"),
    ("Github", "https://github.com/microsoft/playwright-python.git")
])
def test_add_link_on_profile_page_mobile(mobile_user_authorization_for_profile_page, config_data: dict, link_name, link):
    profile = mobile_user_authorization_for_profile_page.profile
    locator = mobile_user_authorization_for_profile_page.locator(
        f"//span[text()='Personal information']/ancestor::section//label[text()='{link_name}']"
    )
    profile.add_link_to_profile(link_name, link)
    expect(locator).to_be_visible()
    profile.delete_custom_link_in_profile(link_name)
    expect(locator).not_to_be_visible()


@pytest.mark.skip(reason="Open when need to test")
def test_delete_account_mobile(mobile_user_authorization_for_delete_account, config_data: dict):
    mobile_user_authorization_for_delete_account.profile.delete_account()
    expect(mobile_user_authorization_for_delete_account.locator("main h2")).to_have_text(config_data['title_login_page'])
