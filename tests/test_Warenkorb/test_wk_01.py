from playwright.sync_api import expect



def test_cart_show_status_empty(page):


    #Start on any page like
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    #Check if Click on image redirects into cart AND shows two information
    page.get_by_role("link", name="0").click()
    
    expect(page.locator("h1")).to_contain_text("Dein Warenkorb:")
    expect(page.locator("#shopcart")).to_contain_text("Der Warenkorb ist leer")
