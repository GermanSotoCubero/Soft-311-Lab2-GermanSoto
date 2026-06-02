import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent)
)

from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

def test_home():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        home = HomePage(page)

        home.navigate()

        page.wait_for_load_state(
            "domcontentloaded"
        )

        title = home.get_title()

        page.screenshot(
            path="screenshots/home.png"
        )

        assert len(title) > 0

        print("HOME TEST PASSED")

        browser.close()
