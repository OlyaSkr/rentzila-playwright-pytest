import pytest

from pages.login_page import Login
from data.test_data import Data


class TestLogin:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.login = Login(self.page)

    def test_login_with_no_credentials(self, test_setup):

        self.login.click_the_button()
        self.login.submit_form()
        self.login.check_empty_email_click_result()

        # check results
        self.login.check_empty_password_click_result()
        self.page.screenshot(path="Screenshots/no_credentials_error.png", full_page=True)

    def test_login_with_no_password(self, test_setup):
        self.login.click_the_button()
        self.login.set_email(Data.email)
        self.login.submit_form()

        # check results
        self.login.check_empty_password_click_result()
        self.page.screenshot(path="Screenshots/empty_password_error.png", full_page=True)

    def test_login_with_no_email(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.submit_form()

        # check results
        self.login.check_empty_email_click_result()
        self.page.screenshot(path="Screenshots/empty_email_error.png", full_page=True)
