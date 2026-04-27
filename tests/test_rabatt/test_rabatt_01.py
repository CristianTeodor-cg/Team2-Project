from page_objects import AppPage

from playwright.sync_api import expect

def test_Rabattfunktion_im_Warenkorb(page):


    #Start on any page like
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    app=AppPage.AppPage(page)

    # dieser Test kontrolliert, ob im Warenkorb die Rabattfunktion nutzbar ist; sie funktioniert nur im eingeloggten Zustand 

    
    page.locator("#accountbar > a").click()
    app.login("MarkusTE", "Mark0426TE") 
    #expect(page.locator("#loginContainer")).to_be_visible() 


# als initiales Setup: Löschen des Warenkorbes:
    page.locator('//*[@id="shoppingcart"]').click()
    page.get_by_role("button", name="Warenkorb löschen").click()
    

# die folgenden Schritte inkl. Änderung der Item-Anzahl sollen erfolgen



# Schritt 1 ergibt keinen Rabatt, da die Item-Zahl zu gering ist
   
   # in den Shop gehen, "Ratingen" auswählen

    page.goto('//*shop.php"]').click()
    page.get_by_role("link", name="Einkaufen").click()



# zum Warenkorb gehen
  
    
    page.locator('//*[@id="shoppingcart"]').click()
    page.locator("input[name=\"quantity[12]\"]").click()

    # zeigt Itemzahl < 10, demnach kein Rabatt ausgewiesen


    expect(page.locator("#rabatt")).to_contain_text("Rabatt: 0,00 €")
    expect(page.locator("#form")).to_contain_text("Es fehlen noch 87,02 €, um 5€ Nachlass auf den gesamten Einkauf zu erhalten")









    # Schritt 2 zeigt eine Itemzahl > 10, demnach ist der Rabatt bei 10%

      # in den Shop gehen, "Ratingen" auswählen

    page.locator('//*shop.php"]').click()
    page.get_by_role("link", name="Einkaufen").click()



    # zum Warenkorb gehen
  
    
    page.locator('//*[@id="shoppingcart"]').click()
    page.locator("input[name=\"quantity[15]\"]").click()
    page.locator("input[name=\"quantity[15]\"]").fill("10")
    page.get_by_role("button", name="Warenkorb aktualisieren").click()
    expect(page.locator("#carttable")).to_contain_text("2,00 €")
    expect(page.get_by_text("Rabatt: 2,00 €")).to_be_visible()



    # Schritt 3 zeigt Itemzahl > 20, der Rabatt geht auf 20% und die Gesamtsumme des Warenkorb > 100 EUR, so dass noch zusätzlich 5,00 EUR abgezogen werden

   
    page.locator('//*[@id="shoppingcart"]').click()
    page.locator("input[name=\"quantity[12]\"]").click()
    page.locator("input[name=\"quantity[12]\"]").fill("21")
    page.locator("input[name=\"quantity[12]\"]").press("Enter")
    page.get_by_role("button", name="Warenkorb aktualisieren").click()
    expect(page.locator("#carttable")).to_contain_text("Rabatt")
    
    expect(page.locator("#carttable")).to_contain_text("18,88 €")
    
    
    
    # Gesamtsumme = Warenwert abzgl. Rabatt inkl. 5,00 EUR Reduktion, wenn Warenwert > 100 EUR
    
    page.get_by_text("Warenwert: 228,69 €").click()
    expect(page.locator("#rabatt")).to_contain_text("Rabatt: 25,87 €")
    expect(page.locator("#gsum")).to_contain_text("Gesamtsumme: 202,82 €")