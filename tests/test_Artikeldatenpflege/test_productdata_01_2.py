
from page_objects import AppPage
from playwright.sync_api import expect

def test_Product_data_base_check_shown_data_base_table(page):

    # Start on any page like
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    app = AppPage.AppPage(page)

    # Check if "Admin" link in the right upper corner redirects to product data web page
    page.locator("#accountbar > a").click()
    app.login("MarkusTE", "Mark0426TE")

    # ✅ WICHTIG: korrekt auf "eingeloggt" warten (statt loginContainer)
    expect(page.locator("#accountbar")).to_contain_text("Logout")

    # öffne Artikelpflege-Page
    page.goto(
        "http://10.40.226.200/BC_Team_2/artikeldatenpflege.php",
        wait_until="domcontentloaded"
    )

    # zeige die Tabellenelemente auf der Seite zum Pflegen der Artikeldaten
    # ✅ Strict-Mode-sicher
    expect(page.get_by_role("heading", name="Artikeldatenpflege")).to_be_visible()

    expect(page.locator("#td_productname1")).to_contain_text("Nivea Creme")
    expect(page.locator("#td_preis1")).to_contain_text("1.99")
    expect(page.locator("#td_bestand1")).to_contain_text("6")

    # leere Felder laut Original HTML
    expect(page.locator("#td_beschreibung1")).to_have_text("")
    expect(page.locator("#td_blob1")).to_have_text("")

    # Icons prüfen (stabiler als "to_contain_text('img src=...')")
    expect(page.locator("#td_product_editButton1 img")).to_have_attribute("src", "img/edit.png")
    expect(page.locator("#td_product_deleteButton1 img")).to_have_attribute("src", "img/no.png")

    # Platzhalter für spätere, noch unbekannte Elemente:
    # expect(page.locator("#...")).to_be_visible()