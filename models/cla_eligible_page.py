from playwright.sync_api import Page
from models.base_page import BasePage



class CLAEligiblePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    async def navigate(self):
        self.page.goto("https://checklegalaid.service.gov.uk/result/eligible", timeout=5000)