from playwright.sync_api import expect
from page_objects import AppPage


def test_login(page):

    #normally replace with environment variables for security purposes .. import os etc...
    _USER = "tester"
    _PASSWORD = "passwort1"
    app=AppPage.AppPage(page)
    
    
    #API test, checks that the page is available
    response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
    assert response is not None
    assert response.status == 200

    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    #Check log-in visibility
    expect(page.get_by_role("link", name="Login")).to_be_enabled()

    #Click log-in
    page.locator("#accountbar > a").click()

    #Check visibility of pop-up window, user, password and buttons
    expect(page.locator("#loginContainer")).to_be_visible()
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_role("link", name="Anmelden")).to_be_visible()

    #Log-in action
    # page.get_by_role("textbox", name="Username").click()
    # page.get_by_role("textbox", name="Username").fill("tester")
    # page.get_by_role("textbox", name="Passwort").click()
    # page.get_by_role("textbox", name="Passwort").fill("passwort1")
    # page.get_by_role("button", name="Login").click()

    app.login(_USER, _PASSWORD)
    

    #Verify log-in process 
    expect(page.get_by_role("link", name="Profil")).to_be_visible()
    expect(page.get_by_role("cell", name=_USER)).to_be_visible()









