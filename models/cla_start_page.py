from playwright.sync_api import Page
from models.base_page import BasePage


class CLAStartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.start_now_button = page.get_by_role("button", name="Start now")

    def navigate(self):
        self.page.goto("https://www.gov.uk/check-legal-aid", timeout=5000)

    def click_start_now(self):
        self.start_now_button.click()