from playwright.sync_api import expect



def test_homepage_cta_btn(page):


    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    
    cta = page.get_by_role("link", name="Auf zum Kaffee")
    expect(cta).to_be_visible()
    expect(cta).to_be_enabled()
    cta.scroll_into_view_if_needed()
    cta.click(force=True)


    #Check if URL contains 'shop' after clicking the button
    expect(page).to_have_url("http://10.40.226.200/BC_Team_2/shop.php")


    #Check if shoplist table is visible
    expect(page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")).to_be_visible()
    
    #Check if shoplist table is visible
    expect(page.locator("#shoplist")).to_be_visible()

    #Check there is at least 1 article visible 
    cell = page.locator('xpath=//*[@id="shoplist"]/tbody/tr[2]/td[1]')
    expect(cell).to_be_visible()

    #Search field is visble
    expect(page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")).to_be_visible()

    # 'Einkaufen' button is accessible
    expect(page.get_by_role("link", name="Einkaufen").first).to_be_visible()

    #Visibility of other elements
    expect(page.get_by_role("link", name="Login")).to_be_enabled()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="About")).to_be_visible()
    expect(page.get_by_role("link", name="Shop")).to_be_visible()
    expect(page.get_by_role("link", name="Contact")).to_be_visible()
    expect(page.get_by_role("link", name="0")).to_be_visible()


