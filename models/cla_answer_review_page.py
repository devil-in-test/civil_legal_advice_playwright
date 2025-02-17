from playwright.sync_api import Page
from models.base_page import BasePage



class CLAAnswerReviewPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.confirm_button = page.get_by_role("button", name="Confirm")

    def navigate(self):
        self.page.goto("https://checklegalaid.service.gov.uk/review", timeout=5000)

    def click_confirm_button(self):
        self.confirm_button.click()