from playwright.sync_api import Page
from models.base_page import BasePage



class CLAYourOutgoingsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def navigate(self):
         self.page.goto("https://checklegalaid.service.gov.uk/outgoings", timeout=5000)

    def set_rent_amount(self,amount):
         self.page.get_by_role("group", name="Rent").get_by_label("Amount").click()
         self.page.get_by_role("group", name="Rent").get_by_label("Amount").fill(amount)

    def set_rent_frequency(self, frequency):
         self.page.get_by_role("group", name="Rent").get_by_label("Frequency").select_option(frequency)

    def set_maintenance_amount(self, amount):
         self.page.get_by_role("group", name="Maintenance").get_by_label("Amount").click()
         self.page.get_by_role("group", name="Maintenance").get_by_label("Amount").fill(amount)

    def set_maintenance_frequency(self,frequency):
         self.page.get_by_role("group", name="Maintenance").get_by_label("Frequency").select_option(frequency)

    def set_monthly_income_contribution(self, amount):
         self.page.get_by_role("textbox", name="Monthly Income Contribution").click()
         self.page.get_by_role("textbox", name="Monthly Income Contribution").fill(amount)

    def click_review_answers(self):
         self.page.get_by_role("button", name="Review your answers").click()