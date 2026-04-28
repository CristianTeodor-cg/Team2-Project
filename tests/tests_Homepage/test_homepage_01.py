import allure
from playwright.sync_api import expect


@allure.feature("Homepage")
@allure.story("CTA navigation to Shop")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Homepage CTA 'Auf zum Kaffee' navigates to Shop and core elements are visible")
def test_homepage_cta_btn(page):

    with allure.step("Open homepage"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Click CTA 'Auf zum Kaffee'"):
        cta = page.get_by_role("link", name="Auf zum Kaffee")
        expect(cta).to_be_visible()
        expect(cta).to_be_enabled()
        cta.scroll_into_view_if_needed()
        cta.click(force=True)

    with allure.step("Verify navigation to shop.php"):
        expect(page).to_have_url("http://10.40.226.200/BC_Team_2/shop.php")

    with allure.step("Verify shop search input and shoplist table are visible"):
        expect(page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")).to_be_visible()
        expect(page.locator("#shoplist")).to_be_visible()

    with allure.step("Verify at least one article row is visible"):
        cell = page.locator('xpath=//*[@id="shoplist"]/tbody/tr[2]/td[1]')
        expect(cell).to_be_visible()

    with allure.step("Verify first 'Einkaufen' button is visible"):
        expect(page.get_by_role("link", name="Einkaufen").first).to_be_visible()

    with allure.step("Verify navigation links and cart counter are visible/enabled"):
        expect(page.get_by_role("link", name="Login")).to_be_enabled()
        expect(page.get_by_role("link", name="Home")).to_be_visible()
        expect(page.get_by_role("link", name="About")).to_be_visible()
        expect(page.get_by_role("link", name="Shop")).to_be_visible()
        expect(page.get_by_role("link", name="Contact")).to_be_visible()
