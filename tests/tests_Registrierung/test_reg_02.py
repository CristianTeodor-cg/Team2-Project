import pytest
from playwright.sync_api import expect
import uuid



def test_register_existent_user(page):

    

    response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
    assert response is not None
    assert response.status == 200 

    USER = "NewUser"
    PASS = "12345678"

    page.get_by_role("link", name="Login").click()


    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(USER)
    page.get_by_role("textbox", name="Username").press("Tab")

    

    expect(page.get_by_text("Dieser User existiert nicht.")).not_to_be_visible()

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
    #page.get_by_role("textbox", name="Username").fill(USER)
    page.get_by_role("textbox", name="Username").type(USER, delay = 100)


    page.get_by_role("textbox", name="Passwort wiederholen").click()

    #User already exists text
    expect(page.get_by_text("Dieser Name ist schon")).to_be_visible()


    page.get_by_role("textbox", name="Passwort wiederholen").click()

    page.get_by_role("textbox", name="Passwort wiederholen").fill(PASS)

    page.get_by_role("textbox", name="Passwort", exact=True).click()

    page.get_by_role("textbox", name="Passwort", exact=True).fill(PASS)

    page.get_by_role("textbox", name="Passwort wiederholen").click()

    
    




    page.get_by_role("button", name="Registrieren").click()



   
    expect(page.get_by_text("Deine Registrierung war erfolgreich! OK")).not_to_be_visible()
    expect(page.get_by_role("heading", name="Deine Registrierung war")).not_to_be_visible()

    expect(page.get_by_role("button", name="OK")).not_to_be_visible()







