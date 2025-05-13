from playwright.sync_api import sync_playwright

def test_pay_bill():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com/parabank/billpay.htm')

        bill_pay_page = BillPayPage(page)
        bill_pay_page.pay_bill('Electric Co.', '123456', 50)

        assert bill_pay_page.is_payment_successful() == True
        browser.close()