import allure
from playwright.sync_api import expect


@allure.feature("Authentication")
@allure.story("Logout")
@allure.title("Logout removes profile visibility")
def test_logout(page):
    # normally replace with environment variables for security purposes .. import os etc...
    _USER = "tester"
    _PASSWORD = "passwort1"

    with allure.step("API check: index page available (HTTP 200)"):
        response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
        assert response is not None
        assert response.status == 200

    with allure.step("Open index page"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify Login link is visible"):
        expect(page.get_by_role("link", name="Login")).to_be_visible()

    with allure.step("Open login dialog"):
        page.get_by_role("link", name="Login").click()

    with allure.step("Verify login dialog fields and actions are visible"):
        expect(page.locator("#loginContainer")).to_be_visible()
        expect(page.get_by_role("textbox", name="Username")).to_be_visible()
        expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
        expect(page.get_by_role("button", name="Login")).to_be_visible()
        expect(page.get_by_role("link", name="Anmelden")).to_be_visible()

    with allure.step(f"Login as '{_USER}'"):
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill(_USER)
        page.get_by_role("textbox", name="Passwort").click()
        page.get_by_role("textbox", name="Passwort").fill(_PASSWORD)
        page.get_by_role("button", name="Login").click()

    with allure.step("Verify login succeeded (Profile + username visible)"):
        expect(page.get_by_role("link", name="Profil")).to_be_visible()
        expect(page.get_by_role("cell", name=_USER)).to_be_visible()

    with allure.step("Logout"):
        page.get_by_role("link", name="Logout").click()

    with allure.step("Verify logout succeeded (Profile + username not visible)"):
        expect(page.get_by_role("link", name="Profil")).not_to_be_visible()
        expect(page.get_by_role("cell", name=_USER)).not_to_be_visible()