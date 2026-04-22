from playwright.sync_api import expect



def test_shop_show_article(page):


    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")

   
    #Verify that all table column headers are visible
    #This ensures the table structure is correct

    expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Name")).to_be_visible()

    
    rows = page.get_by_role("row").filter(has=page.locator("td"))
    
    # Ensure that at least one product row exists
    expect(rows).not_to_have_count(0)


    # Get the number of product rows
    count = rows.count()


   # Loop through each product row and validate name, price, image, and action
    for i in range(count):
        row = rows.nth(i)

        # Column 1: Product name
        name = row.locator("td").nth(0)
        # Column 2: Product price
        price = row.locator("td").nth(1)
        # Column 3: Product image
        image = row.locator("td img")
        # Column 4: "Einkaufen" (Add to cart) link
        add_button = row.get_by_role("link", name="Einkaufen")

        # Validate product name, price, image, and "Einkaufen" button
        expect(name).to_be_visible()
        expect(name).not_to_have_text("")

        expect(price).to_be_visible()
        expect(price).to_contain_text("€")

        expect(image).to_be_visible()
        # Get the image source (base64 image in your app)
        src = image.get_attribute("src")
        assert src is not None
        assert src.startswith("data:image/")

        
        # Ensure image is really loaded
        assert image.evaluate("img => img.complete && img.naturalWidth > 0")


        # Validate "Einkaufen" button
        expect(add_button).to_be_visible()
        expect(add_button).to_be_enabled()



   