import pytest

from pages.login_page import Login
from data.test_data import Data


class TestLogin:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.login = Login(self.page)

    def test_login_with_valid_phone_password(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.phone)
        self.login.set_password(Data.password)
        self.login.submit_form()
        self.login.click_the_avatar_image()
        self.login.click_the_my_profile_button()
        self.login.check_my_profile_page_title()
        self.login.scroll_into_view_phone()
        self.login.check_phone_input_form(Data.phone_profile)

    def test_login_without_plus_in_phone(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.phone_without_plus)
        self.login.set_password(Data.password)
        self.login.submit_form()
        self.login.click_the_avatar_image()
        self.login.click_the_my_profile_button()
        self.login.check_my_profile_page_title()
        self.login.scroll_into_view_phone()
        self.login.check_phone_input_form(Data.phone_profile)

    def test_login_without_plus_code_in_phone(self, test_setup):

        self.login.click_the_button()
        self.login.set_email(Data.phone_without_plus_code)
        self.login.set_password(Data.password)
        self.login.submit_form()
        self.login.click_the_avatar_image()
        self.login.click_the_my_profile_button()
        self.login.check_my_profile_page_title()
        self.login.scroll_into_view_phone()
        self.login.check_phone_input_form(Data.phone_profile)