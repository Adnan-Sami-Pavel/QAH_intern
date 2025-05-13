from playwright.sync_api import sync_playwright

def test_successful_registration():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com/parabank/register.htm')

        registration_page = RegistrationPage(page)
        registration_page.register('John', 'Doe', '1234 Elm St', 'New York', 'john@example.com', '1234567890', 'johndoe', 'password123')

        assert page.locator('text=Your account was created successfully!').is_visible()
        browser.close()