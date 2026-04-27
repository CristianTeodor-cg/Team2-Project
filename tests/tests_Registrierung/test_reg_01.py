import pytest
import allure
from playwright.sync_api import expect
import uuid


def create_user():
    return f"NewUser{uuid.uuid4().hex[:4]}"


@allure.feature("User Registration")
@allure.story("Successful user registration")
@allure.severity(allure.severity_level.CRITICAL)
def test_register(page):

    USER = create_user()
    PASS = "Passwort123"
   

    
    with allure.step("Open application homepage"):
        response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
        assert response is not None
        assert response.status == 200

    with allure.step("Navigate to login page"):
        page.get_by_role("link", name="Login").click()

    with allure.step("Check validation for non-existing user"):
        page.get_by_role("textbox", name="Username").type(USER)
        page.get_by_role("textbox", name="Username").press("Tab")
        expect(page.get_by_text("Dieser User existiert nicht.")).to_be_visible()

    with allure.step("Navigate to registration form"):
        page.get_by_role("link", name="Anmelden").click()

    with allure.step("Verify registration form fields"):
        expect(page.locator(".reg").first).to_be_visible()
        expect(page.get_by_role("textbox", name="Passwort", exact=True)).to_be_visible()
        expect(page.get_by_role("textbox", name="Passwort wiederholen")).to_be_visible()
        expect(page.get_by_role("checkbox", name="Ja, ich habe die AGB gelesen")).to_be_visible()
        expect(page.get_by_role("textbox", name="Username")).to_be_visible()

    with allure.step("Fill registration form"):
        page.get_by_role("checkbox", name="Ja, ich habe die AGB gelesen").check()

        page.get_by_role("textbox", name="Username").type(USER)
        page.locator("#register-username").fill(USER)

        page.locator("#register-pw").fill(PASS)
        page.get_by_role("textbox", name="Passwort wiederholen").type(PASS)

    with allure.step("Submit registration"):
        page.get_by_role("button", name="Registrieren").click()

    with allure.step("Verify successful registration"):
        expect(page.get_by_text("Deine Registrierung war erfolgreich! OK")).to_be_visible()
        expect(page.get_by_role("heading", name="Deine Registrierung war")).to_be_visible()
        expect(page.get_by_role("button", name="OK")).to_be_visible()

    # Optional: attach created user to report
    allure.attach(USER, name="Registered Username", attachment_type=allure.attachment_type.TEXT)