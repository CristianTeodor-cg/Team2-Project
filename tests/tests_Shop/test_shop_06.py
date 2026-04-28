import allure
from playwright.sync_api import expect


@allure.feature("Shop")
@allure.story("Product search - partial name")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Searching partial name 'bo' shows product 'Bohne'")
def test_shop_search_partial_name_shows_bohne(page):

    with allure.step("Open start page"):
        page.goto("http://10.40.226.200/BC_Team_2/")

    with allure.step("Open shop"):
        page.get_by_role("link", name="Shop").click()

    with allure.step("Locate search field and verify it is usable"):
        search_input = page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")
        expect(search_input).to_be_visible()
        expect(search_input).to_be_enabled()

    with allure.step("Search for partial product name 'bo'"):
        search_input.fill("bo")
        allure.attach("bo", name="Search keyword", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Verify product 'Bohne' is visible"):
        product_link = page.get_by_role("link", name="Bohne", exact=True)
        expect(product_link).to_be_visible()

    with allure.step("Clear search field"):
        search_input.fill("")
        expect(search_input).to_have_value("")