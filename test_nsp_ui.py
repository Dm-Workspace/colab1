# test_nsp_ui.py
from playwright.sync_api import sync_playwright

def test_homepage_title(base_url):
    """
    UI-тест: открываем сайт и проверяем заголовок окна
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(base_url)
        title = page.title()
        assert "Nature's Sunshine" in title
        browser.close()
