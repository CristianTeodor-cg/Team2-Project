import allure
from playwright.sync_api import expect


@allure.feature("Authentication")
@allure.story("Login - negative")
@allure.title("Login fails with correct username and wrong password")
def test_login_wrong_P(page):

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

    with allure.step("Attempt login with valid username and invalid password"):
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill("tester")
        page.get_by_role("textbox", name="Passwort").click()
        page.get_by_role("textbox", name="Passwort").fill("asd")
        page.get_by_role("button", name="Login").click()

    with allure.step("Verify error message is shown"):
        expect(page.get_by_text("Benutzername oder Passwort")).to_be_visible()