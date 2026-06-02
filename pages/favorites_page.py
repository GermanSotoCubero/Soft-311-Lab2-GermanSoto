class FavoritesPage:

    def __init__(self, page):
        self.page = page

        self.products = page.locator(
            'a[href^="/product/"]'
        )

    def open_first_product(self):

        self.products.first.click()

        self.page.wait_for_load_state(
            "networkidle"
        )

    def add_to_favorites(self):

        self.page.locator(
            '[data-testid="all-products-wishlist-button"]'
        ).first.click()

    def open_favorites(self):

        self.page.goto(
            "https://storedemo.testdino.com/favorites"
        )

        self.page.wait_for_load_state(
            "networkidle"
        )