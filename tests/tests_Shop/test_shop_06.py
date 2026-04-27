from playwright.sync_api import expect


def test_shop_article_details_via_name(page):
    # -----------------------------------------
    # 1. Navigate to the shop overview page
    # -----------------------------------------
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    # -----------------------------------------
    # 2. Verify that the product list table
    #    structure is visible and correct
    # -----------------------------------------
    expect(page.get_by_role("columnheader", name="Name")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()

    # -----------------------------------------
    # 3. Locate all product rows (exclude header)
    # -----------------------------------------
    rows = page.get_by_role("row").filter(has=page.locator("td"))

    # Ensure at least one product is displayed
    expect(rows).not_to_have_count(0)

    # -----------------------------------------
    # 4. Click the first product name link
    #    to open the detail page
    # -----------------------------------------
    # Read the product name dynamically (no hard‑coding)
    first_product_name = rows.first.locator("td").nth(0).inner_text().strip()

    # Click the product name link in the first row
    rows.first.locator("td").nth(0).get_by_role("link").click()

    # -----------------------------------------
    # 5. Verify we are on the product detail page
    # -----------------------------------------
    # Product image must be visible
    expect(page.locator("#dc-img")).to_be_visible()

    # Page heading must match the clicked product name
    expect(
        page.get_by_role("heading", name=first_product_name)
    ).to_be_visible()

    # -----------------------------------------
    # 6. Verify product description / information
    # -----------------------------------------
    description = page.locator("#dc-info")
    expect(description).to_be_visible()

    # -----------------------------------------
    # 7. Verify product price is shown
    # -----------------------------------------
    price = page.locator("#dc-price")
    expect(price).to_be_visible()

    # Check that the price contains a currency symbol
    assert "€" in price.inner_text()

    # -----------------------------------------
    # 8. Verify stock availability information
    # -----------------------------------------
    availability_number = page.locator("#dc-nr")
    expect(availability_number).to_be_visible()

    # Extract and validate that the stock number is numeric
    stock_value = availability_number.inner_text().strip()
    assert stock_value.isdigit(), "Stock value is not a number"

    # -----------------------------------------
    # 9. Verify quantity input field
    # -----------------------------------------
    quantity = page.locator("#dc-quantity")
    expect(quantity).to_be_visible()

    # Input fields store their value in the 'value' attribute
    quantity_value = quantity.input_value()
    assert quantity_value.isdigit(), "Quantity is not a number"

    # -----------------------------------------
    # 10. Verify add‑to‑cart functionality is available
    # -----------------------------------------
    expect(
        page.get_by_role("button", name="In den Warenkorb legen")
    ).to_be_visible()

    # -----------------------------------------
    # 11. Verify recommended articles section
    # -----------------------------------------
    # Check that the recommendation heading is displayed
    expect(page.get_by_text("Das könnte Ihnen auch gefallen")).to_be_visible()

    # Ensure at least one recommended product is shown
    recommended_items = page.locator(".featprod")
    expect(recommended_items).not_to_have_count(0)
