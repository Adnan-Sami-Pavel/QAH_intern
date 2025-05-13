class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator('input[name="customer.firstName"]')
        self.last_name_input = page.locator('input[name="customer.lastName"]')
        self.address_input = page.locator('input[name="customer.address.street"]')
        self.city_input = page.locator('input[name="customer.address.city"]')
        self.email_input = page.locator('input[name="customer.email"]')
        self.phone_input = page.locator('input[name="customer.phoneNumber"]')
        self.username_input = page.locator('input[name="customer.username"]')
        self.password_input = page.locator('input[name="customer.password"]')
        self.submit_button = page.locator('input[value="Register"]')

    async def register(self, first_name, last_name, address, city, email, phone, username, password):
        await self.first_name_input.fill(first_name)
        await self.last_name_input.fill(last_name)
        await self.address_input.fill(address)
        await self.city_input.fill(city)
        await self.email_input.fill(email)
        await self.phone_input.fill(phone)
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.submit_button.click()
