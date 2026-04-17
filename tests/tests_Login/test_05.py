from playwright.sync_api import expect



def test_login_non_existent_user(page):

  

    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    #Check log-in visibility
    expect(page.get_by_role("link", name="Login")).to_be_visible()

    #Click log-in
    page.get_by_role("link", name="Login").click()

    #Check visibility of pop-up window, user, password and buttons
    expect(page.locator("#loginContainer")).to_be_visible()
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_role("link", name="Anmelden")).to_be_visible()

    #Log-in action
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("asd")
    page.get_by_role("textbox", name="Passwort").click()
    
    #Verify log-in process 
    expect(page.get_by_text("Dieser User existiert nicht.")).to_be_visible()









