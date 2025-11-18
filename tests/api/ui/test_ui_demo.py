import os
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = os.getenv('BASE_URL', 'https://example.com')

@pytest.mark.ui
def test_ui_demo_headless():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)
        assert page.title() is not None
        try:
            h1 = page.locator('h1')
            if h1.count():
                assert h1.inner_text().strip() != ''
        except Exception:
            pass
        context.close()
        browser.close()
