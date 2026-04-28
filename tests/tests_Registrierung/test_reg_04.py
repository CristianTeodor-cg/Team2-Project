import pytest
import allure
from playwright.sync_api import expect
import uuid


def create_user():
    # 8 chars is usually safe; adjust if your site requires longer
    return f"NewUser{uuid.uuid4().hex[:4]}"


@allure.feature("User Registration")
@allure.story("Registration - password policy")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Registration fails when password is too short")
def test_register(page):
    with allure.step("Open application homepage (API check)"):
        response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
        assert response is not None
        assert response.status == 200

    USER = create_user()
    PASS1 = "12"
    PASS2 = "12"
    allure.attach(USER, name="Test Username", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Open login dialog"):
        page.get_by_role("link", name="Login").click()

    with allure.step("Validate non-existing user message in login field"):
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill(USER)
        page.get_by_role("textbox", name="Username").press("Tab")
        expect(page.get_by_text("Dieser User existiert nicht.")).to_be_visible()

    with allure.step("Navigate to registration form (Anmelden)"):
        page.get_by_role("link", name="Anmelden").click()

    with allure.step("Verify registration form fields are visible"):
        expect(page.locator(".reg").first).to_be_visible()
        expect(page.get_by_role("textbox", name="Passwort", exact=True)).to_be_visible()
        expect(page.get_by_role("textbox", name="Passwort wiederholen")).to_be_visible()
        expect(page.get_by_role("checkbox", name="Ja, ich habe die AGB gelesen")).to_be_visible()
        expect(page.get_by_role("textbox", name="Username")).to_be_visible()

    with allure.step("Fill registration form with too-short password"):
        page.get_by_role("textbox", name="Username").click()

        page.get_by_role("checkbox", name="Ja, ich habe die AGB gelesen").check()
        page.get_by_role("textbox", name="Username").fill(USER)

        page.get_by_role("textbox", name="Passwort wiederholen").click()
        page.get_by_role("textbox", name="Passwort wiederholen").fill(PASS1)

        page.get_by_role("textbox", name="Passwort", exact=True).click()
        page.get_by_role("textbox", name="Passwort", exact=True).fill(PASS2)

        page.get_by_role("textbox", name="Passwort wiederholen").click()
        page.get_by_role("textbox", name="Passwort", exact=True).click()

    with allure.step("Submit registration"):
        page.get_by_role("button", name="Registrieren").click()

    with allure.step("Verify password policy error is shown"):
        expect(page.get_by_text("-20 Zeichen: a-z, A-Z, 0-9, @$!%*?")).to_be_visible()

    with allure.step("Verify success message is NOT shown"):
        expect(page.get_by_text("Deine Registrierung war erfolgreich! OK")).not_to_be_visible()
        expect(page.get_by_role("heading", name="Deine Registrierung war")).not_to_be_visible()
        expect(page.get_by_role("button", name="OK")).not_to_be_visible()