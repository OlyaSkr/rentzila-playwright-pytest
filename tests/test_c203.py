import pytest

from pages.login_page import Login
from data.test_data import Data


class TestLogin:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.login = Login(self.page)

    def test_login_with_space_in_email(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_with_space)
        self.login.set_password(Data.password)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/email_with_space_error.png", full_page=True)

    def test_login_with_cyrillic_in_email(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_cyrillic)
        self.login.set_password(Data.password)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/email_with_cyrillic_error.png", full_page=True)

    def test_login_without_symbol_in_email(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_without_symbol)
        self.login.set_password(Data.password)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/email_without_symbol_error.png", full_page=True)

    def test_login_without_dot_in_email(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_without_dot)
        self.login.set_password(Data.password)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/email_without_dot_error.png", full_page=True)

    def test_login_without_com_in_email(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_without_com)
        self.login.set_password(Data.password)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/email_without_com_error.png", full_page=True)

    def test_login_without_gmail_in_email(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_without_gmail)
        self.login.set_password(Data.password)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/email_without_gmail_error.png", full_page=True)

    def test_login_without_gmail_com_in_email(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_without_gmail_com)
        self.login.set_password(Data.password)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/email_without_gmail_com_error.png", full_page=True)

    def test_login_with_non_exist_email(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_valid)
        self.login.set_password(Data.password)
        self.login.submit_form()

        # check results
        self.login.check_non_exist_email_input()
        self.page.screenshot(path="Screenshots/non_exist_email_error.png", full_page=True)

    def test_login_with_space_in_password(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_valid)
        self.login.set_password(Data.password_with_space)
        self.login.submit_form()

        # check results
        self.login.check_invalid_password_input()
        self.page.screenshot(path="Screenshots/password_with_space_error.png", full_page=True)

    def test_login_with_begin_space_in_password(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_valid)
        self.login.set_password(Data.password_with_begin_space)
        self.login.submit_form()

        # check results
        self.login.check_invalid_password_input()
        self.page.screenshot(path="Screenshots/password_with_begin_space_error.png", full_page=True)

    def test_login_with_non_exist_password(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_valid)
        self.login.set_password(Data.password_non_exist)
        self.login.submit_form()

        # check results
        self.login.check_non_exist_email_input()
        self.page.screenshot(path="Screenshots/password_non_exist_error.png", full_page=True)

    def test_login_without_uppercase_in_password(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_valid)
        self.login.set_password(Data.password_without_uppercase)
        self.login.submit_form()

        # check results
        self.login.check_invalid_password_input()
        self.page.screenshot(path="Screenshots/password_without_uppercase_error.png", full_page=True)

    def test_login_without_lowercase_in_password(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_valid)
        self.login.set_password(Data.password_without_lowercase)
        self.login.submit_form()

        # check results
        self.login.check_invalid_password_input()
        self.page.screenshot(path="Screenshots/password_without_lowercase_error.png", full_page=True)

    def test_login_cyrillic_password(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.email_valid)
        self.login.set_password(Data.password_cyrillic)
        self.login.submit_form()

        # check results
        self.login.check_invalid_password_input()
        self.page.screenshot(path="Screenshots/password_cyrillic_error.png", full_page=True)



