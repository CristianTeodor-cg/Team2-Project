from page_objects import AppPage
from playwright.sync_api import expect


def test_Product_data_base_edit_product_entry(page):

    # Start on index page
    

    app = AppPage.AppPage(page)

    # Login as Admin
    page.locator("#accountbar > a").click()
    app.login("MarkusTE", "Mark0426TE")

    # ✅ WICHTIG: warten, bis Login wirklich abgeschlossen ist
    expect(page.locator("#accountbar")).to_contain_text("Logout")

    # ✅ Danach erst zur Artikeldatenpflege navigieren
    page.goto(
        "http://10.40.226.200/BC_Team_2/artikeldatenpflege.php",
        wait_until="domcontentloaded"
    )

    # --- Seitenüberschrift eindeutig prüfen (Strict-Mode-sicher) ---
    expect(
        page.get_by_role("heading", name="Artikeldatenpflege")
    ).to_be_visible()

    # --- Tabelleninhalte prüfen ---
    expect(page.locator("#td_productname1")).to_contain_text("Nivea Creme")
    expect(page.locator("#td_preis1")).to_contain_text("1.99")
    expect(page.locator("#td_bestand1")).to_contain_text("6")

    # leere Felder laut HTML
    expect(page.locator("#td_beschreibung1")).to_have_text("")
    expect(page.locator("#td_blob1")).to_have_text("")

    # --- Edit-Button (Icon) prüfen ---
    edit_icon = page.locator("#td_product_editButton1 img")
    expect(edit_icon).to_have_attribute("src", "img/edit.png")

    # --- Delete-Button (Icon) prüfen ---
    delete_icon = page.locator("#td_product_deleteButton1 img")
    expect(delete_icon).to_have_attribute("src", "img/no.png")