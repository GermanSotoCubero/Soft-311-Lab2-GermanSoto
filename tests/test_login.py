import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def run():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        login = LoginPage(page)

        # Navegar a la página de login
        login.navigate()

        # Esperar que cargue la página
        page.wait_for_load_state("domcontentloaded")

        # Realizar login
        login.login(
            "test@test.com",
            "123456"
        )

        # Esperar un momento después del login
        page.wait_for_timeout(3000)

        # Validar que la URL cambió luego del login
        assert "login" not in page.url.lower()

        print("LOGIN TEST PASSED")

        browser.close()


if __name__ == "__main__":
    run()