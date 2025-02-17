from playwright.sync_api import Page
from models.base_page import BasePage



class CLAYourIncomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.continue_button = page.get_by_role("button", name="Continue")
        self.maintenance_received_amount_input = page.locator("#your_income-maintenance-per_interval_value")
        self.maintenance_received_amount_frequency_select = page.locator("#your_income-maintenance-interval_period")
        self.your_income_pension_per_interval_input =page.locator("#your_income-pension-per_interval_value")
        self.your_income_pension_per_interval_frequency = page.locator("#your_income-pension-interval_period")
        self.your_income_other_income_per_interval_value = page.locator("#your_income-other_income-per_interval_value")
        self.your_income_other_income_per_interval_frequency = page.locator("#your_income-other_income-interval_period")

    def navigate(self):
         self.page.goto("https://checklegalaid.service.gov.uk/income", timeout=15000)

    def click_continue_button(self):
         self.continue_button.click()

    def set_maintenance_received_amount(self,amount):
         self.maintenance_received_amount_input.click()
         self.maintenance_received_amount_input.fill(amount)

    def set_maintenance_received_frequency(self,frequency):
         self.maintenance_received_amount_frequency_select.select_option(frequency)

    def set_pension_received_amount(self,amount):
         self.your_income_pension_per_interval_input.click()
         self.your_income_pension_per_interval_input.fill(amount)

    def set_pension_received_frequency(self,frequency):
         self.your_income_pension_per_interval_frequency.select_option(frequency)

    def set_other_income_amount(self,amount):
         self.your_income_other_income_per_interval_value.click()
         self.your_income_other_income_per_interval_value.fill(amount)

    def set_other_income_frequency(self,frequency):
         self.your_income_other_income_per_interval_frequency.select_option(frequency)