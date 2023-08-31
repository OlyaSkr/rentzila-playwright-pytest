from playwright.sync_api import Page, expect


class Login:

    def __init__(self, page: Page):
        self.page = page

        self.__enter_btn = self.page.locator('//*[text()="Вхід"]')
        self.__email_input = self.page.locator('[id="email"]')
        self.__password_input = self.page.locator('[id="password"]')
        self.__submit_btn = self.page.locator('//button[text()="Увійти"]')
        self.__empty_email_click_msg = self.page.locator('//form/div[1]/p')
        self.__empty_password_click_msg = self.page.locator('//form/div[2]/div[1]/p')
        self.__hidden_password_btn = self.page.locator('[data-testid="reactHookButton"]')
        self.__avatar_image = self.page.locator('[alt="Avatar"]')
        self.__email_data = self.page.locator('[data-testid="email"]')
        self.__logout_btn = self.page.locator('//*[text()="Вихід"]')
        self.__my_profile_btn = self.page.locator('[data-testid="profile"]')
        self.__phone_input = self.page.locator('[data-testid="input_OwnerProfileNumber"]')
        self.__wrong_email_msg = self.page.locator('//*[contains(text(),"Неправильний формат")]')
        self.__non_exist_email_msg = self.page.locator('[data-testid="errorMessage"]')
        self.__wrong_password_msg = self.page.locator('//*[contains(text(),"Пароль повинен")]')

    def click_the_button(self) -> None:
        self.__enter_btn.click()

    def set_email(self, email) -> None:
        self.__email_input.fill(email)

    def set_password(self, password) -> None:
        self.__password_input.fill(password)

    def submit_form(self) -> None:
        self.__submit_btn.click()

    def check_empty_email_click_result(self) -> None:
        self.__empty_email_click_msg.wait_for(state='visible')
        assert self.__empty_email_click_msg.text_content() == 'Поле не може бути порожнім', \
            f'Expected an empty email click massage, got "{self.__empty_email_click_msg.text_content()}" instead'

    def check_empty_password_click_result(self) -> None:
        self.__empty_password_click_msg.wait_for(state='visible')
        assert self.__empty_password_click_msg.text_content() == 'Поле не може бути порожнім', \
            f'Expected an empty password click massage, got "{self.__empty_password_click_msg.text_content()}" instead'

    def check_output_form(self, password) -> None:
        assert self.__password_input.text_content() == f'Password:{password}', \
            f'Expected {password}, got "{self.__password_input.text_content()}" instead'

    def click_the_hidden_password_button(self) -> None:
        self.__hidden_password_btn.click()

    def check_password_input(self, password) -> None:
        expect(self.__password_input).to_have_value(password)

    def check_avatar_is_visible(self) -> None:
        self.__avatar_image.is_visible()

    def click_the_avatar_image(self) -> None:
        self.__avatar_image.click()

    def check_email_is_displayed(self, email) -> None:
        expect(self.__email_data).to_have_text(f'{email}')

    def click_the_logout_button(self) -> None:
        self.__logout_btn.click()

    def click_the_my_profile_button(self) -> None:
        self.__my_profile_btn.click()

    def check_my_profile_page_title(self) -> None:
        expect(self.page).to_have_title('Сервіс пошуку та подачі оголошень спецтехніки та послуг Rentzila')

    def scroll_into_view_phone(self) -> None:
        self.__phone_input.scroll_into_view_if_needed()

    def check_phone_input_form(self, phone) -> None:
        expect(self.__phone_input).to_have_value(phone)

    def check_invalid_email_input(self) -> None:
        self.__wrong_email_msg.wait_for(state='visible')
        assert self.__wrong_email_msg.text_content() == 'Неправильний формат email або номера телефону', \
            f'Expected an invalid email input message, got {self.__wrong_email_msg.text_content()}'

    def check_non_exist_email_input(self) -> None:
        self.__non_exist_email_msg.wait_for(state='visible')
        assert self.__non_exist_email_msg.text_content() == 'Невірний e-mail або пароль', \
            f'Expected a non-exist email input message, got {self.__non_exist_email_msg.text_content()}'

    def check_invalid_password_input(self) -> None:
        self.__wrong_password_msg.wait_for(state='visible')
        assert self.__wrong_password_msg.text_content() == 'Пароль повинен містити як мінімум 1 цифру, 1 велику літеру і 1 малу літеру, також не повинен містити кирилицю та пробіли', \
            f'Expected an invalid password input message, got {self.__wrong_password_msg.text_content()}'

