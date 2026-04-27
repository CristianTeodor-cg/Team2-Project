import pytest
import allure
from playwright.sync_api import expect
import uuid

class AppPage:
    def __init__(self, page):
        self.page = page


    def login(self, username, password):

        
        self.page.locator("#login-username").click()
        self.page.locator("#login-username").type(username)
        self.page.locator("#login-password").click()
        self.page.locator("#login-password").type(password)
        self.page.locator("#login-submit").click()

    def register(self, username, password1, paswword2):

        self.page.locator("#register-username").click()
        self.page.locator("#register-username").type(username)
        


