import re
from decimal import Decimal, ROUND_HALF_UP
from playwright.sync_api import expect

def _eur_to_decimal(text: str) -> Decimal:
    # "3,99 €" -> Decimal("3.99") ; toleriert NBSP/Whitespace
    t = text.replace("\xa0", " ").replace("€", "").strip()
    t = t.replace(".", "").replace(",", ".")
    return Decimal(t)

def _decimal_to_eur(value: Decimal) -> str:
    v = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{v:.2f}".replace(".", ",") + " €"

def test_cart_update_quantity_above_stock_shows_error(page):
    page.goto("http://10.40.226.200/BC_Team_2/shop.php")
    page.get_by_role("link", name="Einkaufen").nth(1).click()
    page.get_by_role("link", name="1").click()

    page.goto("http://10.40.226.200/BC_Team_2/shoppingcart.php")
    expect(page.locator("#carttable")).to_be_visible()

    page.goto("http://10.40.226.200/BC_Team_2/shop.php")
    page.get_by_role("link", name="Einkaufen").nth(1).click()
    page.get_by_role("link", name="1").click()

    page.goto("http://10.40.226.200/BC_Team_2/shoppingcart.php")
    cart = page.locator("#carttable")
    expect(cart).to_be_visible()

    header = cart.locator("tr").first
    headers = header.locator("th")
    if headers.count() == 0:
        headers = header.locator("td")

    header_texts = [headers.nth(i).inner_text().strip().lower() for i in range(headers.count())]

    def idx(col_name: str) -> int:
        for i, t in enumerate(header_texts):
            if col_name in t:
                return i
        return -1

    idx_qty   = idx("anzahl")
    idx_stock = idx("bestand")
    idx_unit  = idx("einzelpreis")
    idx_total = idx("gesamtpreis")

    if -1 in (idx_qty, idx_stock, idx_unit, idx_total):
        raise AssertionError(f"Spalten nicht gefunden. Header: {header_texts}")

    rows = cart.locator("tr")
    row_count = rows.count()

    tested = False
    for r in range(1, row_count):
        row = rows.nth(r)
        qty_input = row.locator("input[name^='quantity['], input[type='number']").first
        if qty_input.count() == 0:
            continue  # keine Produktzeile

        cells = row.locator("td")
        if cells.count() == 0:
            continue

        stock_txt = cells.nth(idx_stock).inner_text()
        m = re.search(r"\d+", stock_txt)
        if not m:
            continue

        stock = int(m.group())
        invalid_qty = stock + 1

        qty_input.click()
        qty_input.fill(str(invalid_qty))

        tested = True
        break

    if not tested:
        raise AssertionError("Keine Produktzeile mit Quantity-Input und Bestand gefunden – Warenkorb evtl. leer?")

    page.get_by_role("button", name="Warenkorb aktualisieren").click()

    expect(page.locator("#setcart")).to_contain_text(
        re.compile(r"\.?\s*Es kann nur die aktuell verfügbare Menge bestellt werden\.")
    )