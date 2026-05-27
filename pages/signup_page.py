class SignUpPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(
            "https://storedemo.testdino.com/signup"
        )

    def sign_up(
        self,
        first_name,
        last_name,
        email,
        password
    ):

        self.page.get_by_label(
            "First Name *"
        ).fill(first_name)

        self.page.get_by_label(
            "Last Name *"
        ).fill(last_name)

        self.page.get_by_label(
            "Email Address *"
        ).fill(email)

        self.page.get_by_label(
            "Password *"
        ).fill(password)

        self.page.get_by_role(
            "button",
            name="Create Account"
        ).click()

    def get_current_url(self):
        return self.page.url