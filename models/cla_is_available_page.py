from playwright.sync_api import Page
from models.base_page import BasePage


class CLAIsAvailablePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.check_financial_button = page.get_by_role('button', name='Check if you qualify financially')

    def navigate(self):
        self.page.goto("https://checklegalaid.service.gov.uk/legal-aid-available?hlpas=yes", timeout=5000)

    def click_check_financial(self):
        self.check_financial_button.click()