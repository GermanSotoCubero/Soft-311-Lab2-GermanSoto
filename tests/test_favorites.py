import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent)
)

from playwright.sync_api import sync_playwright
from pages.favorites_page import FavoritesPage


def test_favorites():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        favorites = FavoritesPage(page)

        page.goto(
            "https://storedemo.testdino.com/products"
        )

        page.wait_for_load_state(
            "networkidle"
        )

        favorites.open_first_product()

        print("URL:", page.url)

        favorites.add_to_favorites()

        page.wait_for_timeout(2000)

        favorites.open_favorites()

        page.screenshot(
            path="screenshots/favorites.png"
        )

        assert "/favorites" in page.url

        browser.close()