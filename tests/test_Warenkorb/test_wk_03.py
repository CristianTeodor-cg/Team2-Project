
from playwright.sync_api import expect

def test_delete_button_clears_cart(page):
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")
    page.get_by_role("link", name="Einkaufen").nth(2).click()
    page.get_by_role("link", name="1").click()

    page.goto("http://10.40.226.200/BC_Team_2/shoppingcart.php")

    # sanity: cart ist wirklich gefüllt (sonst gibt es evtl. keinen delete button)
    expect(page.locator("#carttable")).to_be_visible()

    try:
        page.get_by_role("button", name="Warenkorb löschen").click()
    except Exception:
        # Fallback, falls es kein echter ARIA-Button ist
        page.locator("text=Warenkorb löschen").first.click()

    
    expect(page.locator("h1")).to_contain_text("Dein Warenkorb")
    expect(page.locator("#shopcart")).to_contain_text("Der Warenkorb ist leer")
