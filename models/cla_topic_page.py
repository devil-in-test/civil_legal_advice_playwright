from playwright.sync_api import Page
from models.base_page import BasePage


class CLATopicPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.debt_button = page.get_by_role("button", name="Debt Bankruptcy, repossession")

    def navigate(self):
        self.page.goto("https://checklegalaid.service.gov.uk/scope/diagnosis", timeout=5000)

    def click_debt_topic(self):
        self.debt_button.click()