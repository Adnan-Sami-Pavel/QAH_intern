from playwright.sync_api import sync_playwright

def test_find_transaction():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com/parabank/transactionSearch.htm')

        transactions_page = TransactionsPage(page)
        transactions_page.find_transaction('Deposit')

        assert transactions_page.is_transaction_found() == True
        browser.close()