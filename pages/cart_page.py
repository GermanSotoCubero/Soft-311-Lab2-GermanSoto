class CartPage:

    def __init__(self, driver):
        self.driver = driver

        # Productos
        self.products = driver.locator('a[href^="/product/"]')

        # Primer producto
        self.first_product = self.products.first

        # Botón carrito header
        self.cart_button = driver.locator('[data-testid="header-cart-icon"]')

    def click_first_product(self):
        self.first_product.click()

    def add_product_to_cart(self):
        add_button = self.driver.locator('button:has-text("Add to cart")')
        add_button.click()

    def open_cart(self):
        self.cart_button.click()
        viewCart_button = self.driver.locator('[data-testid="view-cart-button"]')
        viewCart_button.click()