import allure
from playwright.sync_api import expect
import re


def test_homepage_link_contact(page):

    with allure.step("Navigate to homepage"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify 'Contact' link is visible"):
        expect(page.get_by_role("link", name="Contact")).to_be_visible()

    with allure.step("Click 'Contact' link"):
        page.get_by_role("link", name="Contact").click()

    with allure.step("Verify URL ends with #footer"):
        expect(page).to_have_url(re.compile("#footer$"))

    with allure.step("Verify footer section is visible"):
        footer = page.locator("#footer")
        expect(footer).to_be_visible()