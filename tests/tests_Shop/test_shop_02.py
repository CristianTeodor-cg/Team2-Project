from playwright.sync_api import expect



def test_shop_product_search(page):


    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    search_box = page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")
    expect(search_box).to_be_visible()
    expect(search_box).to_be_enabled()

   
    #Verify that all table column headers are visible
    #This ensures the table structure is correct

    expect(page.get_by_role("columnheader", name="Bild")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Hinzufügen")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Preis")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Name")).to_be_visible()

    
    rows = page.get_by_role("row").filter(has=page.locator("td"))
    
    # Ensure that at least one product row exists
    expect(rows).not_to_have_count(0)

    
    # Take the first product name dynamically
    first_product_name = rows.first.locator("td").nth(0).inner_text().strip()

    # Derive a keyword from the product name (first word)
    search_keyword = first_product_name.split()[0]

    # Safety check (optional but good practice)
    assert search_keyword != ""

    # Enter the dynamically derived keyword
    search_box.fill(search_keyword)

    
    # Re-locate product rows after filtering
    filtered_rows = page.get_by_role("row").filter(has=page.locator("td"))
    expect(filtered_rows).not_to_have_count(0)

    filtered_count = filtered_rows.count()

    
    
    match_found = False

    for i in range(filtered_count):
        product_name = filtered_rows.nth(i).locator("td").nth(0).inner_text().strip()

        if search_keyword.lower() in product_name.lower():
            match_found = True
            break

    assert match_found, f"No product name matches search keyword '{search_keyword}'"












