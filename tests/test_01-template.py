from playwright.sync_api import expect


# to be used as template for tests
# the tests run in the background, so no chrome instance opens
# to have a chrome instance open:  terminal cmd : pytest --headed or pytest --headed --slowmo=500(for slower browser)
# proposed naming convention : test_testArea_testName_number  eg. test_logIn_logInPositiv_01


def test_login_flow(page):
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="About")).to_be_visible()
    expect(page.get_by_role("link", name="Shop")).to_be_visible()
    expect(page.get_by_role("link", name="Contact")).to_be_visible()
    expect(page.get_by_role("link", name="Login")).to_be_visible()
    expect(page.get_by_role("link", name="0")).to_be_visible()

    page.get_by_role("link", name="Login").click()

    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()