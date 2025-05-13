class TransferFundsPage:
    def __init__(self, page):
        self.page = page
        self.from_account_dropdown = page.locator('select[name="fromAccountId"]')
        self.to_account_dropdown = page.locator('select[name="toAccountId"]')
        self.amount_input = page.locator('input[name="amount"]')
        self.transfer_button = page.locator('input[value="Transfer"]')
        self.success_message = page.locator('text=Transfer Complete!')

    async def transfer_funds(self, from_account, to_account, amount):
        await self.from_account_dropdown.select_option(from_account)
        await self.to_account_dropdown.select_option(to_account)
        await self.amount_input.fill(str(amount))
        await self.transfer_button.click()

    async def is_transfer_successful(self):
        return await self.success_message.is_visible()