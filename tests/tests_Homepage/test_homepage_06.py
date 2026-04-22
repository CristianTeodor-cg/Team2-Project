from playwright.sync_api import expect
import re


def test_homepage_link_contact(page):


    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    #Check if 'Home' link is visible
    expect(page.get_by_role("link", name="Contact")).to_be_visible()

    #Click 'Home' link
    page.get_by_role("link", name="Contact").click()

    
    # Assert: URL contains #footer
    expect(page).to_have_url(re.compile("#footer$"))

    # Assert: footer is visible
    footer = page.locator("#footer")
    expect(footer).to_be_visible()






