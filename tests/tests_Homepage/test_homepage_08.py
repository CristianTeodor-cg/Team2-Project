from playwright.sync_api import expect



def test_homepage_icon_cart_empty(page):


    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    #Check if 'Cart' icon is visible
    expect(page.get_by_role("link", name="0")).to_be_visible()

    #Click 'Cart' icon
    page.get_by_role("link", name="0").click()

    #Check if URL contains 'shoppingcart' after clicking the link
    expect(page).to_have_url("http://10.40.226.200/BC_Team_2/shoppingcart.php")

    #Check if 'Dein Warenkorb' heading is visible on the page
    expect(page.get_by_role("heading", name="Dein Warenkorb:")).to_be_visible()

    #Check if 'Der Warenkorb ist leer' message is visible on the page
    expect(page.get_by_role("heading", name="Der Warenkorb ist leer")).to_be_visible()


     #Visibility of other elements
    expect(page.get_by_role("link", name="Login")).to_be_enabled()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="About")).to_be_visible()
    expect(page.get_by_role("link", name="Shop")).to_be_visible()
    expect(page.get_by_role("link", name="Contact")).to_be_visible()
    expect(page.get_by_role("link", name="0")).to_be_visible()





