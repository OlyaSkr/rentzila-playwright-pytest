import pytest

from pages.login_page import Login
from data.test_data import Data


class TestLogin:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.login = Login(self.page)

    def test_login_with_valid_credentials(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email)
        self.login.set_password(Data.password)
        self.login.click_the_hidden_password_button()

        # check results
        self.login.check_password_input(Data.password)
        self.page.screenshot(path="Screenshots/show_password.png", full_page=True)

        self.login.click_the_hidden_password_button()
        self.page.screenshot(path="Screenshots/hidden_password.png", full_page=True)

        self.login.submit_form()

        # check results
        self.login.check_avatar_is_visible()

        self.login.click_the_avatar_image()

        # check results
        self.login.check_email_is_displayed(Data.email)
        self.login.click_the_logout_button()

    def test_login_with_uppercase_email(self, test_setup):
        self.login.click_the_button()
        self.login.set_email(Data.uppercase_email)
        self.login.set_password(Data.password)
        self.login.click_the_hidden_password_button()

        # check results
        self.login.check_password_input(Data.password)
        self.page.screenshot(path="Screenshots/show_password1.png", full_page=True)

        self.login.click_the_hidden_password_button()
        self.page.screenshot(path="Screenshots/hidden_password1.png", full_page=True)

        self.login.submit_form()

        # check results
        self.login.check_avatar_is_visible()

        self.login.click_the_avatar_image()

        # check results
        self.login.check_email_is_displayed(Data.email)
        self.login.click_the_logout_button()






