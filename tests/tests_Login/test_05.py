import allure
from playwright.sync_api import expect


@allure.feature("Authentication")
@allure.story("Login - negative")
@allure.title("Login shows 'user does not exist' for non-existent username")
def test_login_non_existent_user(page):

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

    with allure.step("Enter non-existent username"):
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill("asd")

    with allure.step("Focus password field"):
        page.get_by_role("textbox", name="Passwort").click()

    with allure.step("Verify 'user does not exist' message is shown"):
        expect(page.get_by_text("Dieser User existiert nicht.")).to_be_visible()