import allure
import pytest
from playwright.sync_api import expect
import uuid


@allure.feature("User Registration")
@allure.story("Registration - existing user")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Registration fails when username already exists")
def test_register_existent_user(page):

    with allure.step("Open application homepage (API check)"):
        response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
        assert response is not None
        assert response.status == 200

    USER = "NewUser"
    PASS = "12345678"
    allure.attach(USER, name="Test Username", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Open login dialog"):
        page.get_by_role("link", name="Login").click()

    with allure.step("Enter existing username in login field and tab out"):
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill(USER)
        page.get_by_role("textbox", name="Username").press("Tab")

    with allure.step("Verify 'user does not exist' message is NOT shown"):
        expect(page.get_by_text("Dieser User existiert nicht.")).not_to_be_visible()

    with allure.step("Go to registration form via 'Anmelden'"):
        page.get_by_role("link", name="Anmelden").click()

    with allure.step("Verify registration form fields are visible"):
        expect(page.locator(".reg").first).to_be_visible()
        expect(page.get_by_role("textbox", name="Passwort", exact=True)).to_be_visible()
        expect(page.get_by_role("textbox", name="Passwort wiederholen")).to_be_visible()
        expect(page.get_by_role("checkbox", name="Ja, ich habe die AGB gelesen")).to_be_visible()
        expect(page.get_by_role("textbox", name="Username")).to_be_visible()

    with allure.step("Focus username field"):
        page.get_by_role("textbox", name="Username").click()

    with allure.step("Accept AGB and type existing username (slow typing)"):
        page.get_by_role("checkbox", name="Ja, ich habe die AGB gelesen").check()
        page.get_by_role("textbox", name="Username").type(USER, delay=100)

    with allure.step("Focus password repeat field"):
        page.get_by_role("textbox", name="Passwort wiederholen").click()

    with allure.step("Verify 'user already exists' message is shown"):
        expect(page.get_by_text("Dieser Name ist schon")).to_be_visible()

    with allure.step("Fill passwords"):
        page.get_by_role("textbox", name="Passwort wiederholen").click()
        page.get_by_role("textbox", name="Passwort wiederholen").fill(PASS)

        page.get_by_role("textbox", name="Passwort", exact=True).click()
        page.get_by_role("textbox", name="Passwort", exact=True).fill(PASS)

        page.get_by_role("textbox", name="Passwort wiederholen").click()

    with allure.step("Submit registration"):
        page.get_by_role("button", name="Registrieren").click()

    with allure.step("Verify registration success message is NOT shown"):
        expect(page.get_by_text("Deine Registrierung war erfolgreich! OK")).not_to_be_visible()
        expect(page.get_by_role("heading", name="Deine Registrierung war")).not_to_be_visible()
        expect(page.get_by_role("button", name="OK")).not_to_be_visible()