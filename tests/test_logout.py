from playwright.sync_api import sync_playwright

def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com/parabank/index.htm')

        login_page = LoginPage(page)
        login_page.login('validUsername', 'validPassword')

        logout_page = LogoutPage(page)
        logout_page.logout()

        assert page.locator('text=You have been logged out').is_visible()
        browser.close()