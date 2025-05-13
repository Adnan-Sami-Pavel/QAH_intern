from playwright.sync_api import sync_playwright

def test_update_contact_info():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com/parabank/updateContact.htm')
        contact_update_page = ContactUpdatePage(page)
        contact_update_page.update_contact_info('4567 Oak St', '9876543210', 'newemail@example.com')

        assert contact_update_page.is_update_successful() == True
        browser.close()
