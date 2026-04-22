from playwright.sync_api import expect



def test_homepage_link_about(page):


    #Navigate to page
    page.goto("http://10.40.226.200/BC_Team_2/index.php")

    #Check if 'Home' link is visible
    expect(page.get_by_role("link", name="About")).to_be_visible()

    #Click 'Home' link
    page.get_by_role("link", name="About").click()

    #Check if URL contains 'index' after clicking the link
    expect(page).to_have_url("http://10.40.226.200/BC_Team_2/about.php")

    #Check if 'About' heading, content is visible on the page
    expect(page.get_by_text("Über uns Unser Anspruch")).to_be_visible()

    #Visibility of footer elements
    expect(page.get_by_text("˄ AGB Finetest Coffee c/o")).to_be_visible()


     #Visibility of other elements
    expect(page.get_by_role("link", name="Login")).to_be_enabled()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="About")).to_be_visible()
    expect(page.get_by_role("link", name="Shop")).to_be_visible()
    expect(page.get_by_role("link", name="Contact")).to_be_visible()
    expect(page.get_by_role("link", name="0")).to_be_visible()





