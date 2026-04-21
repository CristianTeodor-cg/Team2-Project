import pytest
from playwright.sync_api import expect

## Wichtig ! Nutz bitte das Format unten für smoke tests! @pytest.mark.smoke ..

@pytest.mark.smoke
def test_homepage(page):

    response = page.goto("http://10.40.226.200/BC_Team_2/index.php")
    assert response is not None
    assert response.status == 200 

    expect(page.get_by_role("link", name="Login")).to_be_enabled()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="About")).to_be_visible()
    expect(page.get_by_role("link", name="Shop")).to_be_visible()
    expect(page.get_by_role("link", name="Contact")).to_be_visible()
    expect(page.get_by_role("link", name="0")).to_be_visible()
    expect(page.get_by_role("link", name="Auf zum Kaffee")).to_be_visible()
