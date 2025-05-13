class UINavigationPage:
    def __init__(self, page):
        self.page = page

    async def check_ui_elements(self):
        return await self.page.locator('text=Home').is_visible()