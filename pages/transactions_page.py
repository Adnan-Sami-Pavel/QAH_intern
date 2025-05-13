class TransactionsPage:
    def __init__(self, page):
        self.page = page
        self.transaction_history = page.locator('.transactionHistory')

    async def find_transaction(self, search_text):
        await self.page.fill('input[name="search"]', search_text)
        await self.page.locator('input[value="Find Transactions"]').click()

    async def is_transaction_found(self):
        return await self.transaction_history.is_visible()
