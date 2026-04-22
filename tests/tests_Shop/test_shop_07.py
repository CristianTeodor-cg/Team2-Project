from playwright.sync_api import expect


def test_shop_search_exact_product_name(page):

    # Navigate to shop
    page.goto("http://10.40.226.200/BC_Team_2/")
    page.get_by_role("link", name="Shop").click()

    # Search field
    search_input = page.get_by_role(
        "textbox",
        name="Durchsuche verfügbare Artikel"
    )

    expect(search_input).to_be_visible()
    expect(search_input).to_be_enabled()

    # Search for product
    search_input.fill("Zartbitterschokolade")
    search_input.press("Enter")

    # Exact product must be visible
    product_link = page.get_by_role("link", name="Kaffee Mülheim", exact=True)
    expect(product_link).to_be_visible()