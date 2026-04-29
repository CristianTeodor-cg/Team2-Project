import pytest
from playwright.sync_api import expect
import allure
@allure.severity(allure.severity_level.MINOR)

def test_shop(page):

    response = page.goto("http://10.40.226.200/BC_Team_2/shop.php#footer")
    assert response is not None
    assert response.status == 200

    
    footer_contact = page.locator("footer >> #contactdata")
    footer_contact.scroll_into_view_if_needed()

    expect(footer_contact).to_be_visible()




