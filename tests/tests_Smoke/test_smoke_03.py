import pytest
from playwright.sync_api import expect
import allure
@allure.severity(allure.severity_level.BLOCKER)
def test_shop(page):

    response = page.goto("http://10.40.226.200/BC_Team_2/shop.php")
    assert response is not None
    assert response.status == 200

    page.goto("http://10.40.226.200/BC_Team_2/shop.php")


    expect(page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")).to_be_visible()
    
    #Check if shoplist table is visible
    expect(page.locator("#shoplist")).to_be_visible()

    #Check there is at least 1 article visible 
    cell = page.locator('xpath=//*[@id="shoplist"]/tbody/tr[2]/td[1]')
    expect(cell).to_be_visible()

    #Search field is visble
    expect(page.get_by_role("textbox", name="Durchsuche verfügbare Artikel")).to_be_visible()

    # 'Einkaufen' button is accessible
    expect(page.get_by_role("link", name="Einkaufen").first).to_be_visible()

    #Visibility of other elements
    expect(page.get_by_role("link", name="Login")).to_be_enabled()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="About")).to_be_visible()
    expect(page.get_by_role("link", name="Shop")).to_be_visible()
    expect(page.get_by_role("link", name="Contact")).to_be_visible()
    expect(page.get_by_role("link", name="0")).to_be_visible()





