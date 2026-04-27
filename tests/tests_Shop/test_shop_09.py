
from playwright.sync_api import expect


def test_shop_open_and_close_coffee_modal(page):
    # Navigate to start page
    page.goto("http://10.40.226.200/BC_Team_2/")

    # Open shop
    page.get_by_role("link", name="Shop").click()

    # Open coffee product
    product_link = page.get_by_role(
        "link",
        name="Kaffee do it yourself",
        exact=True
    )
    expect(product_link).to_be_visible()
    product_link.click()

    # Verify coffee modal is visible
    coffee_modal = page.get_by_text("× Kaffee do it yourself -")
    expect(coffee_modal).to_be_visible()

    # Close coffee modal
    close_button = page.get_by_text("×")
    close_button.click()
