import allure
from playwright.sync_api import expect


@allure.feature("Shop")
@allure.story("Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add first article to cart updates cart counter to 1")
def test_shop_add_article_to_cart(page):

    with allure.step("Open shop page"):
        page.goto("http://10.40.226.200/BC_Team_2/shop.php")

    with allure.step("Click first 'Einkaufen' (add to cart)"):
        add_to_cart_button = page.get_by_role("link", name="Einkaufen").first
        expect(add_to_cart_button).to_be_visible()
        expect(add_to_cart_button).to_be_enabled()
        add_to_cart_button.click()

    with allure.step("Verify cart counter shows '1'"):
        cart_counter = page.get_by_role("link", name="1", exact=True)
        expect(cart_counter).to_be_visible()