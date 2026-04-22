import pytest
from playwright.sync_api import expect


def test_login(page):

    response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
    assert response is not None
    assert response.status == 200

    #Check log-in visibility
    expect(page.get_by_role("link", name="Login")).to_be_enabled()

    #Navigate to log-in dialog page
    page.get_by_role("link", name="Login").click()

    #Check visiblitiy of fields
    expect(page.locator("#loginContainer")).to_be_visible()
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_role("link", name="Anmelden")).to_be_visible()

