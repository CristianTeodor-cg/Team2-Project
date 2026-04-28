import allure
from playwright.sync_api import expect
from page_objects import AppPage


@allure.feature("Authentication")
@allure.story("Login")
@allure.title("Login works and profile is visible")
def test_login(page):
    # normally replace with environment variables for security purposes .. import os etc...
    _USER = "tester"
    _PASSWORD = "passwort1"
    app = AppPage.AppPage(page)

    with allure.step("API check: index page available (HTTP 200)"):
        response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
        assert response is not None
        assert response.status == 200

    with allure.step("Open index page"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify Login link is enabled"):
        expect(page.get_by_role("link", name="Login")).to_be_enabled()

    with allure.step("Open login dialog"):
        page.locator("#accountbar > a").click()

    with allure.step("Verify login dialog fields and actions are visible"):
        expect(page.locator("#loginContainer")).to_be_visible()
        expect(page.get_by_role("textbox", name="Username")).to_be_visible()
        expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
        expect(page.get_by_role("button", name="Login")).to_be_visible()
        expect(page.get_by_role("link", name="Anmelden")).to_be_visible()

    with allure.step(f"Login as '{_USER}'"):
        app.login(_USER, _PASSWORD)

    with allure.step("Verify login succeeded (Profile + username visible)"):
        expect(page.get_by_role("link", name="Profil")).to_be_visible()
        expect(page.get_by_role("cell", name=_USER)).to_be_visible()