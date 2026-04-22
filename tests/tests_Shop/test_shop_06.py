from playwright.sync_api import expect


def test_shop_search_partial_name_shows_bohne(page):

    # Navigate to start page
    page.goto("http://10.40.226.200/BC_Team_2/")

    # Open shop
    page.get_by_role("link", name="Shop").click()

    # Locate search field
    search_input = page.get_by_role(
        "textbox",
        name="Durchsuche verfügbare Artikel"
    )

    expect(search_input).to_be_visible()
    expect(search_input).to_be_enabled()

    # Enter partial product name
    search_input.fill("bo")

    # Verify product "Bohne" is visible
    product_link = page.get_by_role("link", name="Bohne", exact=True)
    expect(product_link).to_be_visible()

    # Clear search field again
    search_input.fill("")
    expect(search_input).to_have_value("")
