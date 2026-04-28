import allure
from playwright.sync_api import expect


def test_homepage_link_about(page):

    with allure.step("Navigate to homepage"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify 'About' link is visible"):
        expect(page.get_by_role("link", name="About")).to_be_visible()

    with allure.step("Click 'About' link"):
        page.get_by_role("link", name="About").click()

    with allure.step("Verify URL is about.php"):
        expect(page).to_have_url("http://10.40.226.200/BC_Team_2/about.php")

    with allure.step("Verify About page heading/content is visible"):
        expect(page.get_by_text("Über uns Unser Anspruch")).to_be_visible()

    with allure.step("Verify footer elements are visible"):
        expect(page.get_by_text("˄ AGB Finetest Coffee c/o")).to_be_visible()

    with allure.step("Verify navigation links and cart counter are visible/enabled"):
        expect(page.get_by_role("link", name="Login")).to_be_enabled()
        expect(page.get_by_role("link", name="Home")).to_be_visible()
        expect(page.get_by_role("link", name="About")).to_be_visible()
        expect(page.get_by_role("link", name="Shop")).to_be_visible()
        expect(page.get_by_role("link", name="Contact")).to_be_visible()
        expect(page.get_by_role("link", name="0")).to_be_visible()