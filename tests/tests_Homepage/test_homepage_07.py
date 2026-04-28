import allure
from playwright.sync_api import expect


def test_homepage_link_login(page):

    with allure.step("Navigate to homepage"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify 'Login' link is visible"):
        expect(page.get_by_role("link", name="Login")).to_be_visible()

    with allure.step("Click 'Login' link"):
        page.get_by_role("link", name="Login").click()

    with allure.step("Verify login dialog/content is visible"):
        expect(page.get_by_text("Login Login Noch kein Account")).to_be_visible()
        expect(page.get_by_role("heading", name="Login")).to_be_visible()
        expect(page.get_by_role("textbox", name="Username")).to_be_visible()
        expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
        expect(page.get_by_role("button", name="Login")).to_be_visible()
        expect(page.get_by_text("Noch kein Account? Anmelden")).to_be_visible()