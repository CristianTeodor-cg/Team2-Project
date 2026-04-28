from playwright.sync_api import expect


def parse_price(price_text: str) -> float:
    """
    Converts '1,99 €' -> 1.99
    """
    return float(
        price_text
        .replace("€", "")
        .replace(",", ".")
        .strip()
    )


def test_shop_sort_products_by_price(page):
    # Navigate to start page
    page.goto("http://10.40.226.200/BC_Team_2/")
    page.get_by_role("link", name="Shop").click()
    page.wait_for_load_state("networkidle")

    # -------------------------
    # Sort by price (ascending)
    # -------------------------
    sort_price = page.get_by_role("link", name="Preis")
    expect(sort_price).to_be_visible()
    sort_price.click()

    page.wait_for_timeout(500)

    # Collect ONLY product prices (tbody, second column)
    price_texts = page.locator(
        "table tbody tr td:nth-child(2)"
    ).all_inner_texts()

    prices = [parse_price(p) for p in price_texts]

    assert len(prices) > 0, "Keine Preise gefunden"

    expected_ascending = sorted(prices)

    assert prices == expected_ascending, (
        "Produkte sind nicht aufsteigend nach Preis sortiert"
    )

    # -------------------------
    # Sort by price (descending)
    # -------------------------
    sort_price.click()
    page.wait_for_timeout(500)

    price_texts = page.locator(
        "table tbody tr td:nth-child(2)"
    ).all_inner_texts()

    prices = [parse_price(p) for p in price_texts]

    expected_descending = sorted(prices, reverse=True)

    assert prices == expected_descending, (
        "Produkte sind nicht absteigend nach Preis sortiert"
    )
