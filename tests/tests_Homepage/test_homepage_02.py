from playwright.sync_api import expect



def test_homepage_link_agb(page):


    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    #Check if 'AGB' link is visible
    expect(page.get_by_role("link", name="AGB")).to_be_visible()

    #Click 'AGB' link
    page.get_by_role("link", name="AGB").click()

    #Check if URL contains 'agb' after clicking the link
    expect(page).to_have_url("http://10.40.226.200/BC_Team_2/agb.php")

    #Check if 'AGB' heading is visible on the page
    expect(page.get_by_text("Allgemeine Geschäftsbedingungen Version 2.0.3 vom 01.02.2022 1.")).to_be_visible()

    #Visibility of other elements
    expect(page.get_by_role("link", name="Login")).to_be_enabled()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="About")).to_be_visible()
    expect(page.get_by_role("link", name="Shop")).to_be_visible()
    expect(page.get_by_role("link", name="Contact")).to_be_visible()
    expect(page.get_by_role("link", name="0")).to_be_visible()

