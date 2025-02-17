from playwright.sync_api import Page
from models.base_page import BasePage



class CLANotEligiblePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def navigate(self):
        self.page.goto("https://checklegalaid.service.gov.uk/result/not-eligible", timeout=5000)