
from playwright.sync_api import expect


# # dies ist der codegen code, der auf der website recorded wurde
# page.goto("http://10.40.226.200/BC_Team_2/shoppingcart.php")
 
#     page.get_by_role("button", name="Warenkorb löschen").click()
#     expect(page.locator("h1")).to_contain_text("Dein Warenkorb:")
#     expect(page.locator("#shopcart")).to_contain_text("Der Warenkorb ist leer.")




def test_delete_button_clears_cart(page):
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")
    page.get_by_role("link", name="Einkaufen").nth(2).click()
    page.locator("#cartCount").click()

    page.goto("http://10.40.226.200/BC_Team_2/shoppingcart.php")

    # sanity: cart ist wirklich gefüllt (sonst gibt es evtl. keinen delete button)
    expect(page.locator("#carttable")).to_be_visible()

  
    page.locator('xpath=//*[@id="setcart"]/button[1]').click()
   

    
    expect(page.locator("h1")).to_contain_text("Dein Warenkorb")
    expect(page.locator("#shopcart")).to_contain_text("Der Warenkorb ist leer")
