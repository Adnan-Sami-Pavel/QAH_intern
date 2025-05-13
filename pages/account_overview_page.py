class AccountOverviewPage:
    def __init__(self, page):
        self.page = page
        self.accounts_list = page.locator('.accountSummary')
        self.account_link = page.locator('a[href="/parabank/accountActivity.htm"]')

    async def is_account_details_visible(self):
        return await self.accounts_list.is_visible()

    async def view_account_activity(self):
        await self.account_link.click()