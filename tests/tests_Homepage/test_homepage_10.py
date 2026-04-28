import allure
from playwright.sync_api import expect


def test_homepage_backToTop(page):

    with allure.step("Open homepage"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify back-to-top control is visible"):
        expect(page.get_by_text("˄")).to_be_visible()

    with allure.step("Click back-to-top control"):
        page.get_by_text("˄").click()

    with allure.step("Verify URL remains on index.php"):
        expect(page).to_have_url("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify main homepage elements are visible"):
        expect(page.get_by_text("0 Login Login Login Noch kein")).to_be_visible()
        expect(page.locator("#mpshoplink")).to_be_visible()
        expect(page.get_by_role("link", name="Auf zum Kaffee")).to_be_visible()

    with allure.step("Verify navigation links and cart counter are visible/enabled"):
        expect(page.get_by_role("link", name="Login")).to_be_enabled()
        expect(page.get_by_role("link", name="Home")).to_be_visible()
        expect(page.get_by_role("link", name="About")).to_be_visible()
        expect(page.get_by_role("link", name="Shop")).to_be_visible()
        expect(page.get_by_role("link", name="Contact")).to_be_visible()
        expect(page.get_by_role("link", name="0")).to_be_visible()