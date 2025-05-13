class BillPayPage:
    def __init__(self, page):
        self.page = page
        self.payee_name_input = page.locator('input[name="payeeName"]')
        self.account_number_input = page.locator('input[name="accountNumber"]')
        self.amount_input = page.locator('input[name="amount"]')
        self.submit_button = page.locator('input[value="Pay"]')
        self.success_message = page.locator('text=Bill Payment Complete!')

    async def pay_bill(self, payee_name, account_number, amount):
        await self.payee_name_input.fill(payee_name)
        await self.account_number_input.fill(account_number)
        await self.amount_input.fill(str(amount))
        await self.submit_button.click()

    async def is_payment_successful(self):
        return await self.success_message.is_visible()