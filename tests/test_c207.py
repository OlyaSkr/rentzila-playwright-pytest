import pytest

from pages.login_page import Login
from data.test_data import Data


class TestLogin:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.login = Login(self.page)

    def test_login_with_phone_without_zero_code(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.set_email(Data.phone_without_zero_code)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/phone_without_zero_code_error.png", full_page=True)

    def test_login_with_phone_without_last_number(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.set_email(Data.phone_without_last_number)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/phone_without_last_number_error.png", full_page=True)

    def test_login_with_phone_with_dash(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.set_email(Data.phone_with_dash)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/phone_with_dash_error.png", full_page=True)

    def test_login_with_phone_with_space(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.set_email(Data.phone_with_space)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/phone_with_space_error.png", full_page=True)

    def test_login_with_phone_with_brackets(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.set_email(Data.phone_with_brackets)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/phone_with_brackets_error.png", full_page=True)

    def test_login_with_phone_without_code_with_brackets(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.set_email(Data.phone_without_code_with_brackets)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/phone_without_code_with_brackets_error.png", full_page=True)

    def test_login_with_phone_with_eleven_numbers(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.set_email(Data.phone_with_eleven_numbers)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/phone_with_eleven_numbers_error.png", full_page=True)

    def test_login_with_phone_with_other_country_code(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.set_email(Data.phone_with_other_country_code)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/phone_with_other_country_code_error.png", full_page=True)

    def test_login_with_phone_without_code(self, test_setup):
        self.login.click_the_button()
        self.login.set_password(Data.password)
        self.login.set_email(Data.phone_without_code)
        self.login.submit_form()

        # check results
        self.login.check_invalid_email_input()
        self.page.screenshot(path="Screenshots/phone_without_code_error.png", full_page=True)
