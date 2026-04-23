from playwright.sync_api import expect



def test_cart_show_added_item_in_cart_and_related_information(page):



# hier steht der input aus codegen, der auf der website recorded wurde:


# #Start on any page like
#     page.goto("http://10.40.226.200/BC_Team_2/shop.php")

#     #Check if adding one item to the cart is reflected on the shoping cart page and all other components are also shown on the cart page
   
#     page.get_by_role("link", name="Einkaufen").nth(2).click()
#     page.get_by_role("link", name="1").click()

#     page.goto("http://10.40.226.200/BC_Team_2/shoppingcart.php")

#     expect(page.locator("#carttable")).to_contain_text("Name")
#     expect(page.locator("#carttable")).to_contain_text("Anzahl")
#     expect(page.locator("#carttable")).to_contain_text("Bestand")
#     expect(page.locator("#carttable")).to_contain_text("Einzelpreis")
#     expect(page.locator("#carttable")).to_contain_text("Gesamtpreis")
#     expect(page.locator("#carttable")).to_contain_text("Rabatt")
#     expect(page.locator("#carttable")).to_contain_text("Kaffee do it yourself")
#     expect(page.locator("#carttable")).to_contain_text("")
#     expect(page.locator("#carttable")).to_contain_text("3")
#     expect(page.locator("#carttable")).to_contain_text("45,99 €")
#     expect(page.locator("#carttable")).to_contain_text("45,99 €")
#     expect(page.locator("#carttable")).to_contain_text("0,00 €")
#         expect(page.locator("button[name=\"delete\"]")).to_contain_text("Warenkorb löschen")
#     expect(page.locator("#buttonRefresh")).to_contain_text("Warenkorb aktualisieren")
#     expect(page.locator("#warenwert")).to_contain_text("Warenwert: 45,99 €")
#     expect(page.locator("#rabatt")).to_contain_text("Rabatt: 0,00 €")
#     expect(page.locator("#gsum")).to_contain_text("Gesamtsumme: 45,99 €")
#     expect(page.locator("#form")).to_contain_text("Es fehlen noch 54,01 €, um 5€ Nachlass auf den gesamten Einkauf zu erhalten")
#     expect(page.locator("input[name=\"kaufen\"]")).to_contain_text("Zur Kasse")










    #Start on any page like
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    #Check if adding one item to the cart is reflected on the shooping cart page and all other components are also shown on the cart page
   
    page.get_by_role("link", name="Einkaufen").nth(2).click()
    page.locator("#cartCount").click()

    page.goto("http://10.40.226.200/BC_Team_2/shoppingcart.php")



    expect(page.locator("#carttable")).to_contain_text("Name")
    expect(page.locator("#carttable")).to_contain_text("Anzahl")
    expect(page.locator("#carttable")).to_contain_text("Bestand")
    expect(page.locator("#carttable")).to_contain_text("Einzelpreis")
    expect(page.locator("#carttable")).to_contain_text("Gesamtpreis")
    expect(page.locator("#carttable")).to_contain_text("Kaffee do it yourself")
    
    expect(page.locator("#carttable")).to_contain_text("3")
    expect(page.locator("#carttable")).to_contain_text("45,99 €")
    
    expect(page.locator("button[name=\"delete\"]")).to_contain_text("Warenkorb löschen")
    expect(page.locator("#buttonRefresh")).to_contain_text("Warenkorb aktualisieren")
    expect(page.locator("#warenwert")).to_contain_text("Warenwert: 45,99 €")
    expect(page.locator("#rabatt")).to_contain_text("Rabatt: 0,00 €")
    expect(page.locator("#gsum")).to_contain_text("Gesamtsumme: 45,99 €")
    expect(page.locator("#form")).not_to_contain_text("Zur Kasse")