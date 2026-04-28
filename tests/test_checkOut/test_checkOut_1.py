import allure
from playwright.sync_api import expect
from page_objects import AppPage


@allure.feature("Shop")
@allure.story("Article list")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Shop shows articles with valid name, price, image and action")


def test_checkOut(page):


    _USER = "tester"
    _PASSWORD = "passwort1"
    app = AppPage.AppPage(page)


    with allure.step("Open index page"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify Login link is enabled"):
        expect(page.get_by_role("link", name="Login")).to_be_enabled()

    with allure.step("Open login dialog"):
        page.locator("#accountbar > a").click()

    with allure.step(f"Login as '{_USER}'"):
        app.login(_USER, _PASSWORD)


    with allure.step("Navigate to shop"):
        page.get_by_role("link", name="Shop").click()
        page.wait_for_timeout(7000)

    with allure.step("Select a product to add to shopping cart"):
        link = page.locator("#shoplist > tbody > tr:nth-child(4) > td:nth-child(4) > a")
        expect(link).to_be_visible()
        link.click()

        # link = page.get_by_role("link", name="Kaffee Ratingen")
        # link.wait_for()
        # link.click()
        # page.get_by_role("button", name="In den Warenkorb legen").click()


    #page.get_by_role("link", name="Kaffee Ratingen").click()

    #Insert 1 cofee
        
    with allure.step("Navigate to shopping cart"):
        page.locator("#shoppingcart").click()

    with allure.step("Zur kasse is visible"):
        expect(page.get_by_role("button", name="Zur Kasse")).to_be_visible

    with allure.step("Navigate to checkout"):
        
        btn = page.locator("#shopcart > div:nth-child(2) > form:nth-child(3) > input.kaufen")
        expect(btn).to_be_visible()
        btn.click()


    with allure.step("Verify possible payment methods and order button"):
        expect(page.get_by_role("button", name="Bestellen")).to_be_visible()
        expect(page.get_by_role("radio", name="Sofortüberweisung")).to_be_visible()
        expect(page.get_by_role("radio", name="Kreditkarte")).to_be_visible()
        expect(page.get_by_role("radio", name="PayPal")).to_be_visible()
        expect(page.get_by_role("radio", name="Auf Rechnung")).to_be_visible()

    with allure.step("Select Paypal"):
        page.get_by_role("radio", name="PayPal").check()

    with allure.step("Order process"):
        page.get_by_role("button", name="Bestellen").click()

    with allure.step("Verify order success"):
        h2 = page.locator("body > content > div > h2")
        expect(h2).to_be_visible()
        expect(h2).to_contain_text("Ihre Bestellung wurde bestätigt!")
