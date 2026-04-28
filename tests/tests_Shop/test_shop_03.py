import allure
from playwright.sync_api import expect


@allure.feature("Shop")
@allure.story("Product search - no results")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Shop search returns no matching products for non-existent keyword")
def test_shop_product_search_no_results(page):
    with allure.step("Open shop page"):
        page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    with allure.step("Verify search box is visible and enabled"):
        search_box = page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")
        expect(search_box).to_be_visible()
        expect(search_box).to_be_enabled()

    with allure.step("Verify table headers are visible (pre-search)"):
        expect(page.get_by_role("columnheader", name="Name")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()

    rows = page.get_by_role("row").filter(has=page.locator("td"))

    with allure.step("Verify at least one product row exists"):
        expect(rows).not_to_have_count(0)

    with allure.step("Create a keyword that cannot match any product"):
        first_product_name = rows.first.locator("td").nth(0).inner_text().strip()
        search_keyword = f"{first_product_name}_NO_MATCH_12345"
        allure.attach(first_product_name, name="First product name", attachment_type=allure.attachment_type.TEXT)
        allure.attach(search_keyword, name="Search keyword", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Perform search"):
        search_box.fill(search_keyword)

    filtered_rows = page.get_by_role("row").filter(has=page.locator("td"))

    with allure.step("Verify no product name matches the search keyword"):
        match_found = False

        for i in range(filtered_rows.count()):
            product_name = (
                filtered_rows.nth(i)
                .locator("td")
                .nth(0)
                .inner_text()
                .strip()
            )

            if search_keyword.lower() in product_name.lower():
                match_found = True
                break

        assert not match_found, (
            f"Found a product matching '{search_keyword}', "
            "but no results were expected"
        )

    with allure.step("Verify table headers are still visible (post-search)"):
        expect(page.get_by_role("columnheader", name="Name")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()