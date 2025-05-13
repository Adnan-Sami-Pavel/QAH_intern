class LogoutPage:
    def __init__(self, page):
        self.page = page
        self.logout_button = page.locator('a[href="/parabank/logout.htm"]')

    async def logout(self):
        await self.logout_button.click()
