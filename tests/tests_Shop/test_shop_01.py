import allure
from playwright.sync_api import expect


@allure.feature("Shop")
@allure.story("Article list")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Shop shows articles with valid name, price, image and action")
def test_shop_show_article(page):

    with allure.step("Open shop page"):
        page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    with allure.step("Verify table headers are visible"):
        expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
        expect(page.get_by_role("columnheader", name="Name")).to_be_visible()

    rows = page.get_by_role("row").filter(has=page.locator("td"))

    with allure.step("Verify at least one product row exists"):
        expect(rows).not_to_have_count(0)

    count = rows.count()
    allure.attach(str(count), name="Product row count", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Validate each product row (name, price, image, action)"):
        for i in range(count):
            row = rows.nth(i)

            name = row.locator("td").nth(0)
            price = row.locator("td").nth(1)
            image = row.locator("td img")
            add_button = row.get_by_role("link", name="Einkaufen")

            expect(name).to_be_visible()
            expect(name).not_to_have_text("")

            expect(price).to_be_visible()
            expect(price).to_contain_text("€")

            expect(image).to_be_visible()
            src = image.get_attribute("src")
            assert src is not None
            assert src.startswith("data:image/")

            assert image.evaluate("img => img.complete && img.naturalWidth > 0")

            expect(add_button).to_be_visible()
            expect(add_button).to_be_enabled()