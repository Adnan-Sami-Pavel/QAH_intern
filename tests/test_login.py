from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com/parabank/index.htm')

        login_page = LoginPage(page)
        login_page.login('validUsername', 'validPassword')

        assert login_page.is_login_successful() == True
        browser.close()