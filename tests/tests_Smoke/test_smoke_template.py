import pytest

## Wichtig ! Nutz bitte das Format unten für smoke tests! @pytest.mark.smoke ..

@pytest.mark.smoke
def test_login_smoke(page):
    ...
# expect(page.get_by_role("link", name="Home")).to_be_visible()
# expect(page.get_by_role("link", name="About")).to_be_visible()
# expect(page.get_by_role("link", name="Shop")).to_be_visible()
# expect(page.get_by_role("link", name="Contact")).to_be_visible()
# expect(page.get_by_role("link", name="Login")).to_be_visible()
# expect(page.get_by_role("link", name="0")).to_be_visible()
# expect(page.get_by_role("link", name="Auf zum Kaffee")).to_be_visible()