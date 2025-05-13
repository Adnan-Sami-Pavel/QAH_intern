from playwright.sync_api import sync_playwright

def test_account_overview():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com/parabank/index.htm')

        login_page = LoginPage(page)
        login_page.login('validUsername', 'validPassword')

        account_overview_page = AccountOverviewPage(page)
        assert account_overview_page.is_account_details_visible() == True
        account_overview_page.view_account_activity()

        browser.close()