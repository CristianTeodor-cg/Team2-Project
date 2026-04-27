from page_objects import AppPage

from playwright.sync_api import expect

import re


def test_Rabattfunktion_im_Warenkorb(page):


    
    def euro_str_to_float(value: str) -> float:
        return float(value.replace(".", "").replace(",", "."))

    #Start on any page like
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    app=AppPage.AppPage(page)

    # dieser Test kontrolliert, ob im Warenkorb die Rabattfunktion nutzbar ist; sie funktioniert nur im eingeloggten Zustand 

    
    page.locator("#accountbar > a").click()
    app.login("MarkusTE", "Mark0426TE") 

    

    
   # in den Shop gehen, "Ratingen" auswählen
    
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    page.locator('#search').fill("Ratingen") 
    page.locator('//*[@id="shoplist"]/tbody/tr[12]/td[4]/a').click()
    



# zum Warenkorb gehen
  
    
    page.locator('//*[@id="shoppingcart"]').click()
    page.locator("input[name=\"quantity[12]\"]").click()

    # zeigt Itemzahl < 10, demnach kein Rabatt ausgewiesen


    expect(page.locator("#rabatt")).to_contain_text("Rabatt: 0,00 €")

    expect(page.locator("#form")).to_contain_text("Es fehlen noch")

    text = page.locator("css=#rabatt").inner_text()
    
    match = re.search(r"([0-9]+,[0-9]{2})", text)
    rabatt_str_0 = match.group(1)
    rabatt_0 = euro_str_to_float(rabatt_str_0)
    assert rabatt_0 == 0,00










    # Schritt 2 zeigt eine Itemzahl > 10, demnach ist der Rabatt bei 10%

      # in den Shop gehen, "Ratingen" auswählen


    page.locator('//*[@id="carttable"]/tbody/tr[2]/td[2]/input').fill("10")
    page.locator('//*[@id="buttonRefresh"]').click()

    text = page.locator("css=#rabatt").inner_text()
    
    match = re.search(r"([0-9]+,[0-9]{2})", text)
    rabatt_str_1 = match.group(1)


    #page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    # page.locator('#search').fill("Ratingen")
    # page.locator("#shoplist > tbody > tr:nth-child(14) > td:nth-child(1) > a").click()

    # expect(page.locator('//*[@id="dc-quantity"]')).to_be_visible()
    # page.locator('//*[@id="dc-quantity"]').fill("11")

    # page.locator('//*[@id="dc-cartbtn"]').click()

    

    # zum Warenkorb gehen
  
    
    
    # page.locator('//*[@id="shoppingcart"]').click()
    # page.locator("input[name=\"quantity[15]\"]").click()
    # page.locator("input[name=\"quantity[15]\"]").fill("10")
    # page.get_by_role("button", name="Warenkorb aktualisieren").click()
    # expect(page.locator("#carttable")).to_contain_text("2,00 €")
    # expect(page.get_by_text("Rabatt: 2,00 €")).to_be_visible()



    # Schritt 3 zeigt Itemzahl > 20, der Rabatt geht auf 20% und die Gesamtsumme des Warenkorb > 100 EUR, so dass noch zusätzlich 5,00 EUR abgezogen werden

   
    # page.locator('//*[@id="shoppingcart"]').click()
    # page.locator("input[name=\"quantity[12]\"]").click()
    # page.locator("input[name=\"quantity[12]\"]").fill("21")
    # page.locator("input[name=\"quantity[12]\"]").press("Enter")
    # page.get_by_role("button", name="Warenkorb aktualisieren").click()

    
    page.locator('//*[@id="carttable"]/tbody/tr[2]/td[2]/input').type("20")
    page.locator('//*[@id="buttonRefresh"]').click()

    

    text = page.locator("css=#rabatt").inner_text()  
    match = re.search(r"([0-9]+,[0-9]{2})", text)
    rabatt_str_2 = match.group(1)  

    
    rabatt_1 = euro_str_to_float(rabatt_str_1)
    rabatt_2 = euro_str_to_float(rabatt_str_2)


    assert rabatt_2 > rabatt_1 > rabatt_0
   
    
    
    
    # Gesamtsumme = Warenwert abzgl. Rabatt inkl. 5,00 EUR Reduktion, wenn Warenwert > 100 EUR
    
    # page.get_by_text("Warenwert: 228,69 €").click()
    # expect(page.locator("#rabatt")).to_contain_text("Rabatt: 25,87 €")
    # expect(page.locator("#gsum")).to_contain_text("Gesamtsumme: 202,82 €")