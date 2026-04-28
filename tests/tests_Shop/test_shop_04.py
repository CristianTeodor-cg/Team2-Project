from playwright.sync_api import expect


def test_shop_sort_products_by_name(page):
    page.goto("http://10.40.226.200/BC_Team_2/")
    page.get_by_role("link", name="Shop").click()
    page.wait_for_load_state("networkidle")

    # Ensure A–Z sorting (toggle-safe)
    sort_link = page.get_by_role("link", name="Name")
    sort_link.click()
    page.wait_for_timeout(300)
    sort_link.click()

    # ✅ Collect ONLY product names (no headers)
    product_names = page.locator(
        "table tbody tr td:first-child a"
    ).all_inner_texts()

    # Sanity check
    assert len(product_names) > 0, "Keine Produktnamen gefunden"

    # Assert alphabetical order (locale & case safe)
    expected = sorted(product_names, key=lambda s: s.casefold())

    assert product_names == expected, (
        "Produkte sind nicht alphabetisch nach Name sortiert"
    )
