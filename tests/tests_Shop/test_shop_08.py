from playwright.sync_api import expect


def test_shop_add_article_to_cart(page):

    # Navigate directly to shop page
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    # Click on first "Einkaufen" link (add to cart)
    add_to_cart_button = page.get_by_role("link", name="Einkaufen").first
    expect(add_to_cart_button).to_be_visible()
    expect(add_to_cart_button).to_be_enabled()
    add_to_cart_button.click()

    # Verify cart counter shows "1"
    cart_counter = page.get_by_role("link", name="1", exact=True)
    expect(cart_counter).to_be_visible()
