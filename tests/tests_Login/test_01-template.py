# from playwright.sync_api import expect


# # to be used as template for tests
# # the tests run in the background, so no chrome instance opens
# # to have a chrome instance open:  terminal cmd : pytest --headed or pytest --headed --slowmo=500(for slower browser)
# # proposed naming convention : test_testArea_testName_number  eg. test_logIn_logInPositiv_01


# def test_login_flow(page):
#     page.goto("http://10.40.226.200/BC_Team_2/index.php")

#     expect(page.get_by_role("link", name="Home")).to_be_visible()
#     expect(page.get_by_role("link", name="About")).to_be_visible()
#     expect(page.get_by_role("link", name="Shop")).to_be_visible()
#     expect(page.get_by_role("link", name="Contact")).to_be_visible()
#     expect(page.get_by_role("link", name="Login")).to_be_visible()
#     expect(page.get_by_role("link", name="0")).to_be_visible()

#     page.get_by_role("link", name="Login").click()

#     expect(page.get_by_role("textbox", name="Username")).to_be_visible()
#     expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
#     expect(page.get_by_role("button", name="Login")).to_be_visible()





#     # page.get_by_role("link", name="Login").click()
#     # expect(page.get_by_role("textbox", name="Username")).to_be_visible()
#     # expect(page.get_by_role("textbox", name="Passwort")).to_be_visible()
#     # expect(page.get_by_role("button", name="Login")).to_be_visible()
#     # expect(page.get_by_role("link", name="Anmelden")).to_be_visible()
#     # page.get_by_role("textbox", name="Username").click()
#     # page.get_by_role("textbox", name="Username").fill("assad")
#     # page.get_by_role("textbox", name="Passwort").click()
#     # page.get_by_role("textbox", name="Passwort").fill("asdasd")
#     # expect(page.get_by_text("Dieser User existiert nicht.")).to_be_visible()
#     # page.get_by_role("textbox", name="Username").dblclick()
#     # page.get_by_role("textbox", name="Username").fill("tester")
#     # page.get_by_role("button", name="Login").click()
#     # expect(page.get_by_text("Benutzername oder Passwort")).to_be_visible()
#     # page.get_by_role("textbox", name="Passwort").click()
#     # page.get_by_role("textbox", name="Passwort").fill("Passwort1")
#     # page.get_by_role("button", name="Login").click()
#     # page.get_by_role("textbox", name="Username").click()
#     # page.get_by_role("textbox", name="Passwort").click()
#     # page.get_by_role("textbox", name="Passwort").fill("Passwort1")
#     # page.get_by_role("button", name="Login").click()
#     # page.get_by_role("textbox", name="Username").click()
#     # page.get_by_role("textbox", name="Username").dblclick()
#     # page.get_by_role("textbox", name="Username").fill("Tester")
#     # page.get_by_role("textbox", name="Username").press("Tab")
#     # page.get_by_role("textbox", name="Passwort").fill("passwort1")
#     # expect(page.get_by_text("Account ist gesperrt")).to_be_visible()
#     # page.get_by_role("textbox", name="Passwort").click()
#     # page.get_by_role("textbox", name="Passwort").fill("")
#     # page.get_by_role("textbox", name="Passwort").click()
#     # page.get_by_role("textbox", name="Passwort").fill("Passwort1")
#     # page.get_by_role("button", name="Login").click()
#     # page.get_by_role("textbox", name="Username").fill("tester")
#     # page.get_by_role("textbox", name="Username").press("Tab")
#     # page.get_by_role("textbox", name="Passwort").fill("passwort1")
#     # page.get_by_role("button", name="Login").click()
#     # expect(page.get_by_role("link", name="Profil")).to_be_visible()
#     # page.get_by_role("link", name="Logout").click()
#     # page.get_by_role("link", name="Login").click()
#     # page.get_by_role("textbox", name="Username").click()
#     # page.get_by_role("textbox", name="Username").fill("tester")
#     # page.get_by_role("textbox", name="Username").press("Tab")
#     # page.get_by_role("textbox", name="Passwort").fill("passwort1")
#     # page.get_by_role("button", name="Login").click()
#     # expect(page.get_by_role("link", name="Logout")).to_be_visible()
#     # expect(page.get_by_role("cell", name="tester")).to_be_visible()
