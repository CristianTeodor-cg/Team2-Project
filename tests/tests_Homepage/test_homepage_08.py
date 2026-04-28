import allure
from playwright.sync_api import expect


def test_homepage_icon_cart_empty(page):

    with allure.step("Navigate to homepage"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify empty cart icon ('0') is visible"):
        expect(page.get_by_role("link", name="0")).to_be_visible()

    with allure.step("Click cart icon"):
        page.get_by_role("link", name="0").click()

    with allure.step("Verify navigation to shopping cart page"):
        expect(page).to_have_url("http://10.40.226.200/BC_Team_2/shoppingcart.php")

    with allure.step("Verify cart page headings (empty cart)"):
        expect(page.get_by_role("heading", name="Dein Warenkorb:")).to_be_visible()
        expect(page.get_by_role("heading", name="Der Warenkorb ist leer")).to_be_visible()

    with allure.step("Verify navigation links and cart counter are visible/enabled"):
        expect(page.get_by_role("link", name="Login")).to_be_enabled()
        expect(page.get_by_role("link", name="Home")).to_be_visible()
        expect(page.get_by_role("link", name="About")).to_be_visible()
        expect(page.get_by_role("link", name="Shop")).to_be_visible()
        expect(page.get_by_role("link", name="Contact")).to_be_visible()
        expect(page.get_by_role("link", name="0")).to_be_visible()