class LoanPage:
    def __init__(self, page):
        self.page = page
        self.loan_amount_input = page.locator('input[name="amount"]')
        self.loan_terms_input = page.locator('select[name="term"]')
        self.loan_button = page.locator('input[value="Apply Now"]')
        self.success_message = page.locator('text=Loan Application Submitted')

    async def request_loan(self, amount, term):
        await self.loan_amount_input.fill(str(amount))
        await self.loan_terms_input.select_option(term)
        await self.loan_button.click()

    async def is_loan_application_successful(self):
        return await self.success_message.is_visible()