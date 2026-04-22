from playwright.sync_api import expect


def test_shop_product_search_no_results(page):
    # Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    # Locate search box
    search_box = page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")
    expect(search_box).to_be_visible()
    expect(search_box).to_be_enabled()

    # Verify table headers are visible
    expect(page.get_by_role("columnheader", name="Name")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()

    # Get existing product rows
    rows = page.get_by_role("row").filter(has=page.locator("td"))
    expect(rows).not_to_have_count(0)

    # Create a keyword that cannot match any product
    first_product_name = rows.first.locator("td").nth(0).inner_text().strip()
    search_keyword = f"{first_product_name}_NO_MATCH_12345"

    # Perform search
    search_box.fill(search_keyword)

    # After search: no product rows should be present
    filtered_rows = page.get_by_role("row").filter(has=page.locator("td"))
    
    
    # Flag that tracks whether ANY matching product is still visible
    # We start with False, assuming no match was found

    match_found = False

    # Iterate over all product rows that are still present after searching
    for i in range(filtered_rows.count()):

        
        #Extract the product name from the first column (Name column)
        # - nth(i): selects the i-th row
        # - locator("td").nth(0): selects the first table cell (product name)
        # - inner_text(): reads the visible text
        # - strip(): removes leading/trailing whitespace
        product_name = (
            filtered_rows.nth(i)
            .locator("td")
            .nth(0)
            .inner_text()
            .strip()
        )

        
        # Check whether the product name contains the search keyword
        # - lower() is used on both sides to make the comparison
        #   case-insensitive (e.g. "Bohne" == "bohne")

        if search_keyword.lower() in product_name.lower():
            
            # A matching product was found, which should NOT happen
            # in a "no results expected" search
            match_found = True
            break


    # Final assertion:
    # - assert not match_found means:
    #   "I expect ZERO products to match the search keyword"
    # - If match_found is True, the test fails with a clear message
    assert not match_found, (
        f"Found a product matching '{search_keyword}', "
        "but no results were expected"
    )

    # Column headers should still be visible
    expect(page.get_by_role("columnheader", name="Name")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()