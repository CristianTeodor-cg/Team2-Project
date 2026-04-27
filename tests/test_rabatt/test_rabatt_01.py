from page_objects import AppPage
from playwright.sync_api import expect
import re


def test_Rabattfunktion_im_Warenkorb(page):


    
    def euro_str_to_float(value: str) -> float:
        return float(value.replace(".", "").replace(",", "."))

    #Start on any page like
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    app=AppPage.AppPage(page)

    #Click on login 
    page.locator("#accountbar > a").click()

    #Insert credentials
    app.login("MarkusTE", "Mark0426TE") 

    #Navigate to shop
    page.locator("body > header > nav > a:nth-child(3)").click()

    page.wait_for_timeout(7000)
    search = page.locator("#search")
    search.click()
    
    search.fill("")  # clear completely
    search.type("Ratingen", delay=150)



    page.locator("#search").press("Enter")
    
    #Click on Kafee Ratingen

    
    link = page.get_by_role("link", name="Kaffee Ratingen")
    link.wait_for()
    link.click()

    #page.get_by_role("link", name="Kaffee Ratingen").click()

    #Insert 1 cofee
    page.get_by_role("button", name="In den Warenkorb legen").click()

    
    #page.locator('#shoplist > tbody > tr:nth-child(14) > td:nth-child(4) > a').click()

    # page.locator(
    # '#shoplist > tbody > tr:nth-child(14) > td:nth-child(4) > a',
    # has_text="Einkaufen"
    # ).evaluate("el => el.click()")
    

    
    
    page.locator('//*[@id="shoppingcart"]').click()
        
    text = page.locator("css=#rabatt").inner_text()
    
    match = re.search(r"([0-9]+,[0-9]{2})", text)
    rabatt_str_0 = match.group(1)
    rabatt_0 = euro_str_to_float(rabatt_str_0)
    assert rabatt_0 == 0,00



    page.locator('//*[@id="carttable"]/tbody/tr[2]/td[2]/input').fill("10")
    page.locator('//*[@id="buttonRefresh"]').click()

    text = page.locator("css=#rabatt").inner_text()
    
    match = re.search(r"([0-9]+,[0-9]{2})", text)
    rabatt_str_1 = match.group(1)

    
    page.locator('//*[@id="carttable"]/tbody/tr[2]/td[2]/input').fill("20")
    page.locator('//*[@id="buttonRefresh"]').click()

    

    text = page.locator("css=#rabatt").inner_text()  
    match = re.search(r"([0-9]+,[0-9]{2})", text)
    rabatt_str_2 = match.group(1)  

    
    rabatt_1 = euro_str_to_float(rabatt_str_1)
    rabatt_2 = euro_str_to_float(rabatt_str_2)


    assert rabatt_2 > rabatt_1 > rabatt_0
   
