from playwright.sync_api import sync_playwright

def test_request_loan():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com/parabank/loan.htm')

        loan_page = LoanPage(page)
        loan_page.request_loan(5000, '24')

        assert loan_page.is_loan_application_successful() == True
        browser.close()