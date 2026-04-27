from page_objects import AppPage

from playwright.sync_api import expect


def test_Product_data_base_edit_product_entry(page):


    #Start on any page like
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    app=AppPage.AppPage(page)

    # dieser Test kontrolliert, ob mit einem Klick auf den Stift der einzelne Produkteintrag in der Tabelle änderbar ist 


    page.locator("#accountbar > a").click()
    app.login("MarkusTE", "Mark0426TE") 
    expect(page.locator("#loginContainer")).to_be_visible() 

# die folgenden Schritte inkl.  Hochladen des Bildes sollen erfolgen


    page.goto("http://10.40.226.200/BC_Team_2/artikeldatenpflege.php")
   
    page.get_by_role("link", name="Datensatz 1 editieren").click()
    page.locator("#productname1").click()
    page.locator("#preis1").click()
    page.locator("#bestand1").click()
    page.locator("#beschreibung1").click()
    page.get_by_role("button", name="Choose File").click()
    page.get_by_role("button", name="Choose File").set_input_files("")

# an dieser Stelle failed der Test: mit set_input_files("") soll ein dediziertes Image auf dem Desktop oder anywhere else ausgewählt und in die Datenbank hochgeladen werden

    page.get_by_role("link", name="Speichern").click()

