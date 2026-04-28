import allure
from playwright.sync_api import expect


def test_homepage_link_shop(page):

    with allure.step("Navigate to homepage"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify 'Shop' link is visible"):
        expect(page.get_by_role("link", name="Shop")).to_be_visible()

    with allure.step("Click 'Shop' link"):
        page.get_by_role("link", name="Shop").click()

    with allure.step("Verify URL is shop.php"):
        expect(page).to_have_url("http://10.40.226.200/BC_Team_2/shop.php")

    with allure.step("Verify shop search field + shoplist are visible"):
        expect(page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")).to_be_visible()
        expect(page.locator("#shoplist")).to_be_visible()

    with allure.step("Verify at least one article is visible"):
        cell = page.locator('xpath=//*[@id="shoplist"]/tbody/tr[2]/td[1]')
        expect(cell).to_be_visible()

    with allure.step("Verify search field and 'Einkaufen' button are visible"):
        expect(page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")).to_be_visible()
        expect(page.get_by_role("link", name="Einkaufen").first).to_be_visible()

    with allure.step("Verify navigation links + cart counter are visible/enabled"):
        expect(page.get_by_role("link", name="Login")).to_be_enabled()
        expect(page.get_by_role("link", name="Home")).to_be_visible()
        expect(page.get_by_role("link", name="About")).to_be_visible()
        expect(page.get_by_role("link", name="Shop")).to_be_visible()
        expect(page.get_by_role("link", name="Contact")).to_be_visible()
        expect(page.get_by_role("link", name="0")).to_be_visible()