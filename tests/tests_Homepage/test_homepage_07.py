from playwright.sync_api import expect



def test_homepage_link_login(page):


    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    #Check if 'Home' link is visible
    expect(page.get_by_role("link", name="Login")).to_be_visible()

    #Click 'Home' link
    page.get_by_role("link", name="Login").click()


    expect(page.get_by_text("Login Login Noch kein Account")).to_be_visible()
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_text("Noch kein Account? Anmelden")).to_be_visible()






