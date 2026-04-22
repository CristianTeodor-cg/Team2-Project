from playwright.sync_api import expect



def test_shop_show_article(page):


    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    #Check if 'Column Header' are visible
    expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Name")).to_be_visible()

    
    rows = page.get_by_role("row").filter(has=page.locator("td"))
    expect(rows).not_to_have_count(0)

    count = rows.count()

    for i in range(count):
        row = rows.nth(i)

        name = row.locator("td").nth(0)
        price = row.locator("td").nth(1)
        image = row.locator("td img")
        add_button = row.get_by_role("link", name="Einkaufen")

        expect(name).to_be_visible()
        expect(name).not_to_have_text("")

        expect(price).to_be_visible()
        expect(price).to_contain_text("€")

        expect(image).to_be_visible()
        src = image.get_attribute("src")
        assert src is not None
        assert src.startswith("data:image/")

        
        # Ensure image is really loaded
        assert image.evaluate("img => img.complete && img.naturalWidth > 0")



        expect(add_button).to_be_visible()
        expect(add_button).to_be_enabled()



   