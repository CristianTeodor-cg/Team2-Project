import allure
from playwright.sync_api import expect


@allure.feature("Homepage")
@allure.story("Footer/Legal links")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Homepage 'AGB' link opens AGB page and key elements are visible")
def test_homepage_link_agb(page):

    with allure.step("Open homepage"):
        page.goto("http://10.40.226.200/BC_Team_2/index.php")

    with allure.step("Verify 'AGB' link is visible"):
        expect(page.get_by_role("link", name="AGB")).to_be_visible()

    with allure.step("Click 'AGB' link"):
        page.get_by_role("link", name="AGB").click()

    with allure.step("Verify navigation to agb.php"):
        expect(page).to_have_url("http://10.40.226.200/BC_Team_2/agb.php")

    with allure.step("Verify AGB heading/text is visible"):
        expect(
            page.get_by_text(
                "Allgemeine Geschäftsbedingungen Version 2.0.3 vom 01.02.2022 1."
            )
        ).to_be_visible()

    with allure.step("Verify navigation links and cart counter are visible/enabled"):
        expect(page.get_by_role("link", name="Login")).to_be_enabled()
        expect(page.get_by_role("link", name="Home")).to_be_visible()
