from playwright.sync_api import expect


def test_shop_open_darjeeling_tea_modal_via_product_name(page):
    # Navigate directly to shop
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")
    page.wait_for_load_state("networkidle")

    # Click on product NAME (text link)
    product_name_link = page.get_by_role(
        "link",
        name="Darjeeling Tee",
        exact=True
    )
    expect(product_name_link).to_be_visible()
    product_name_link.click()

    # Verify product modal is visible
    product_modal = page.get_by_text(
        "Darjeeling Tee - Schwarzer",
        exact=False
    )
    expect(product_modal).to_be_visible()

    # Close modal (optional but recommended)
    close_button = page.get_by_text("×", exact=True)
    expect(close_button).to_be_visible()
    close_button.click()
