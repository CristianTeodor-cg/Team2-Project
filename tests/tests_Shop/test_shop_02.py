import allure
from playwright.sync_api import expect


@allure.feature("Shop")
@allure.story("Product search")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Shop product search filters results by keyword from first product")
def test_shop_product_search(page):

    with allure.step("Open shop page"):
        page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    with allure.step("Verify search box is visible and enabled"):
        search_box = page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")
        expect(search_box).to_be_visible()
        expect(search_box).to_be_enabled()

    with allure.step("Verify table headers are visible"):
        expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Name")).to_be_visible()

    rows = page.get_by_role("row").filter(has=page.locator("td"))

    with allure.step("Verify at least one product row exists"):
        expect(rows).not_to_have_count(0)

    with allure.step("Derive search keyword from first product name"):
        first_product_name = rows.first.locator("td").nth(0).inner_text().strip()
        search_keyword = first_product_name.split()[0]
        assert search_keyword != ""
        allure.attach(first_product_name, "First product name", allure.attachment_type.TEXT)
        allure.attach(search_keyword, "Search keyword", allure.attachment_type.TEXT)

    with allure.step("Enter keyword into search box"):
        search_box.fill(search_keyword)

    filtered_rows = page.get_by_role("row").filter(has=page.locator("td"))

    with allure.step("Verify filtered results are not empty"):
        expect(filtered_rows).not_to_have_count(0)
        filtered_count = filtered_rows.count()
        allure.attach(str(filtered_count), "Filtered row count", allure.attachment_type.TEXT)

    with allure.step("Verify at least one filtered product name contains the keyword"):
        match_found = False
        for i in range(filtered_count):
            product_name = filtered_rows.nth(i).locator("td").nth(0).inner_text().strip()
            if search_keyword.lower() in product_name.lower():
                match_found = True
                break

        assert match_found, f"No product name matches search keyword '{search_keyword}'"