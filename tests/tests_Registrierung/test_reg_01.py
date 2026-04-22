import pytest
from playwright.sync_api import expect
import uuid


def create_user():
    # 8 chars is usually safe; adjust if your site requires longer
    return f"NewUser{uuid.uuid4().hex[:4]}"

def test_register(page):

    

    response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
    assert response is not None
    assert response.status == 200 

    USER = create_user()
    PASS = "Passwort123"

    page.get_by_role("link", name="Login").click()

    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(USER)
    page.get_by_role("textbox", name="Username").press("Tab")
    expect(page.get_by_text("Dieser User existiert nicht.")).to_be_visible()

    #Click on 'Anmelden'
    page.get_by_role("link", name="Anmelden").click()

    #Verify visibility of elements 
    expect(page.locator(".reg").first).to_be_visible()
    expect(page.get_by_role("textbox", name="Passwort", exact=True)).to_be_visible()
    expect(page.get_by_role("textbox", name="Passwort wiederholen")).to_be_visible()
    expect(page.get_by_role("checkbox", name="Ja, ich habe die AGB gelesen")).to_be_visible()
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()


    page.get_by_role("textbox", name="Username").click()

    #Verify error message
    #page.get_by_role("textbox", name="Username").fill("New")
    #expect(page.get_by_text("Bitte mindestens 4 Zeichen")).to_be_visible()

    page.get_by_role("checkbox", name="Ja, ich habe die AGB gelesen").check() 
    page.get_by_role("textbox", name="Username").fill(USER)

    page.get_by_role("textbox", name="Passwort wiederholen").click()

    page.get_by_role("textbox", name="Passwort wiederholen").fill(PASS)

    page.get_by_role("textbox", name="Passwort", exact=True).click()

    page.get_by_role("textbox", name="Passwort", exact=True).fill(PASS)

    page.get_by_role("textbox", name="Passwort wiederholen").click()

    
    

    page.get_by_role("textbox", name="Passwort", exact=True).click()



    page.get_by_role("button", name="Registrieren").click()



   
    expect(page.get_by_text("Deine Registrierung war erfolgreich! OK")).to_be_visible()
    expect(page.get_by_role("heading", name="Deine Registrierung war")).to_be_visible()

    expect(page.get_by_role("button", name="OK")).to_be_visible()







