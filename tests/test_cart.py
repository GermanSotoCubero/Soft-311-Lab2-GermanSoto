import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage


def run():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        cart = CartPage(page)

        # Navegar al sitio
        page.goto(
            "https://storedemo.testdino.com/products",
            wait_until="domcontentloaded",
        )

        # Esperar productos visibles
        page.wait_for_selector('a[href^="/product/"]')

        # Abrir primer producto
        cart.click_first_product()

        # Esperar navegación al producto
        page.wait_for_timeout(2000)

        # Agregar producto al carrito
        cart.add_product_to_cart()

        # Esperar actualización
        page.wait_for_timeout(2000)

        # Abrir carrito
        cart.open_cart()

        # Esperar navegación
        page.wait_for_timeout(3000)

        # Validar URL del carrito
        assert "cart" in page.url.lower()

        print("CART FLOW TEST PASSED")

        browser.close()


if __name__ == "__main__":
    run()