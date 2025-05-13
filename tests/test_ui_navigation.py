from playwright.sync_api import sync_playwright

def test_ui_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://parabank.parasoft.com')

        ui_navigation_page = UINavigationPage(page)
        assert ui_navigation_page.check_ui_elements() == True
        browser.close()