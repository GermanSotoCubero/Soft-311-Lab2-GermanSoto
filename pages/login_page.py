class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://storedemo.testdino.com/login")

    def login(self, email, password):

        self.page.fill('input[type="email"]', email)
        self.page.fill('input[type="password"]', password)

        self.page.locator('button[data-testid="login-submit-button"]').click()