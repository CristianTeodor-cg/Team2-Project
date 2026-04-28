import allure
from playwright.sync_api import expect


@allure.feature("Shop")
@allure.story("Product search - exact name")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Searching exact product name shows expected product link")
def test_shop_search_exact_product_name(page):

    with allure.step("Open start page and navigate to Shop"):
        page.goto("http://10.40.226.200/BC_Team_2/")
        page.get_by_role("link", name="Shop").click()

    with allure.step("Verify search input is visible and enabled"):
        search_input = page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")
        expect(search_input).to_be_visible()
        expect(search_input).to_be_enabled()

    with allure.step("Search for product 'Zartbitterschokolade'"):
        search_input.fill("Zartbitterschokolade")
        search_input.press("Enter")
        allure.attach("Zartbitterschokolade", name="Search keyword", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Verify expected product link is visible (exact match)"):
        product_link = page.get_by_role("link", name="Kaffee Mülheim", exact=True)
        expect(product_link).to_be_visible()