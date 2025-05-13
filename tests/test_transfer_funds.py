from playwright.sync_api import sync_playwright

def test_transfer_funds():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com/parabank/transfer.htm')

        transfer_page = TransferFundsPage(page)
        transfer_page.transfer_funds('1', '2', 100)

        assert transfer_page.is_transfer_successful() == True
        browser.close()