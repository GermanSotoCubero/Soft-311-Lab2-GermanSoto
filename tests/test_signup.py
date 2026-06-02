import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.signup_page import SignUpPage


def test_signUp():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        signup = SignUpPage(page)

        # Navegar al Sign Up
        signup.navigate()

        page.wait_for_load_state("domcontentloaded")

        # Ejecutar registro
        signup.sign_up(
            first_name="German",
            last_name="Soto",
            email="german2000@test.com",
            password="Password123!"
        )

        # Esperar un momento para validar navegación
        page.wait_for_timeout(3000)

        # Validar que cambió la URL
        current_url = signup.get_current_url()
        # page.wait_for_load_state("networkidle")

        page.screenshot(
            path="screenshots/signup.png"
        )

        assert current_url != "https://storedemo.testdino.com/signup", \
            f"Expected navigation after sign up but stayed on {current_url}"

        print("TEST PASSED")

        browser.close()
