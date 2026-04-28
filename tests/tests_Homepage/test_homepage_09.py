import allure
from playwright.sync_api import expect
import re


def test_cart_icon_reflects_current_state(page):

    with allure.step("Open homepage"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Open shopping cart via cart icon"):
        cart = page.get_by_role("link", name="0")
        expect(cart).to_be_visible()
        cart.click()

    with allure.step("Verify navigation to shoppingcart.php and heading is visible"):
        expect(page).to_have_url(re.compile(r"shoppingcart\.php"))
        expect(page.get_by_role("heading", name="Dein Warenkorb")).to_be_visible()

    empty_message = page.get_by_text("Der Warenkorb ist leer")
    cart_rows = page.locator("#shoplist tbody tr")

    with allure.step("Verify cart state (empty OR contains rows)"):
        empty_count = empty_message.count()
        rows_count = cart_rows.count()

        allure.attach(str(empty_count), name="Empty message count", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(rows_count), name="Cart rows count", attachment_type=allure.attachment_type.TEXT)

        if empty_count > 0:
            # Empty cart is a valid state
            expect(empty_message).to_be_visible()
        else:
            # Cart contains one or more items
            assert rows_count > 0
            expect(cart_rows.first).to_be_visible()
