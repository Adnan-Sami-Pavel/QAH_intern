class ContactUpdatePage:
    def __init__(self, page):
        self.page = page
        self.address_input = page.locator('input[name="address"]')
        self.phone_input = page.locator('input[name="phone"]')
        self.email_input = page.locator('input[name="email"]')
        self.submit_button = page.locator('input[value="Update Info"]')

    async def update_contact_info(self, address, phone, email):
        await self.address_input.fill(address)
        await self.phone_input.fill(phone)
        await self.email_input.fill(email)
        await self.submit_button.click()
    async def is_update_successful(self):
        return await self.page.locator('text=Contact Information Updated').is_visible()
