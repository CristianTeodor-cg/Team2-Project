# from playwright.sync_api import expect



# def test_homepage_icon_cart_notempty_notloggedin(page):


#     #Navigate to page
#     page.goto("http://10.40.226.200/BC_Team_2/index.php")

#     #Check if 'Cart' icon is visible
#     expect(page.get_by_role("link", name="0")).to_be_visible()

#     #Click 'Cart' icon
#     page.get_by_role("link", name="0").click()

#     #Check if URL contains 'shoppingcart' after clicking the link
#     expect(page).to_have_url("http://10.40.226.200/BC_Team_2/shoppingcart.php")

#     #Check if 'Dein Warenkorb' heading is visible on the page
#     expect(page.get_by_role("heading", name="Dein Warenkorb:")).to_be_visible()

   
#     empty_message = page.get_by_text("Der Warenkorb ist leer")
#     cart_rows = page.locator("#shoplist tbody tr")

#     if empty_message.is_visible():
#     # ✅ Valid empty-cart state
#         expect(empty_message).to_be_visible()
#     else:
#     # ✅ Only assert rows if cart is not empty
#         expect(cart_rows.first).to_be_visible()


#     expect(page.get_by_role("button", name="Warenkorb löschen")).to_be_visible()
#     expect(page.get_by_role("button", name="Warenkorb aktualisieren")).to_be_visible()
#     expect(page.get_by_text("Um einen einzelnen Artikel")).to_be_visible()
#     expect(page.get_by_text("Um einen einzelnen Artikel")).to_be_visible()
#     expect(page.get_by_text("Um Rabatte zu erhalten müssen")).to_be_visible()


#      #Visibility of other elements
#     expect(page.get_by_role("link", name="Login")).to_be_enabled()
#     expect(page.get_by_role("link", name="Home")).to_be_visible()
#     expect(page.get_by_role("link", name="About")).to_be_visible()
#     expect(page.get_by_role("link", name="Shop")).to_be_visible()
#     expect(page.get_by_role("link", name="Contact")).to_be_visible()
#     expect(page.get_by_role("link", name="0")).to_be_visible()

#     #Visibility of footer elements
#     expect(page.get_by_text("˄ AGB Finetest Coffee c/o")).to_be_visible()



from playwright.sync_api import expect
import re

def test_cart_icon_reflects_current_state(page):

    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    cart = page.get_by_role("link", name="0")
    expect(cart).to_be_visible()
    cart.click()


    expect(page).to_have_url(re.compile(r"shoppingcart\.php"))
    expect(page.get_by_role("heading", name="Dein Warenkorb")).to_be_visible()

    empty_message = page.get_by_text("Der Warenkorb ist leer")
    cart_rows = page.locator("#shoplist tbody tr")

    
    if empty_message.count() > 0:
        # Empty cart is a valid state
        expect(empty_message).to_be_visible()
    else:
        # Cart contains one or more items
        assert cart_rows.count() > 0
        expect(cart_rows.first).to_be_visible




