# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import allure
from adcm_pytest_plugin.utils import wait_until_step_succeeds

from tests.ui_tests.app.page.common.base_page import (
    BasePageObject,
    PageHeader,
    PageFooter,
)
from tests.ui_tests.app.page.login.login_page_locators import LoginPageLocators


class LoginPage(BasePageObject):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url, "/login")
        self.header = PageHeader(self.driver, self.base_url)
        self.footer = PageFooter(self.driver, self.base_url)

    @allure.step('Check elements on login page')
    def check_all_elements(self):
        self.header.check_unauth_page_elements()
        self.assert_displayed_elements([
            LoginPageLocators.login_form_block,
            LoginPageLocators.login_input,
            LoginPageLocators.password_input,
            LoginPageLocators.login_btn,
        ])
        self.footer.check_all_elements()

    @allure.step('Get warning text on login page')
    def get_login_warning_text(self, timeout: int = None) -> str:
        def get_text():
            assert self.find_element(LoginPageLocators.login_warning).text != ""
        wait_until_step_succeeds(get_text, period=1, timeout=timeout or self.default_loc_timeout)
        return self.find_element(LoginPageLocators.login_warning).text

    @allure.step('Check warning text on login page')
    def check_error_message(self, message):
        self.wait_element_visible(LoginPageLocators.login_warning)
        current_error = self.get_login_warning_text()
        with allure.step(f"Check message '{message}'"):
            assert current_error == message, f"There should be error '{message}' and not '{current_error}'"

    @allure.step('Check login button unavailable')
    def check_check_login_button_unavailable(self):
        assert self.find_element(LoginPageLocators.login_btn).get_attribute("disabled") == "true"

    @allure.step('Fill login form with {username}: {password}')
    def fill_login_user_form(self, username, password):
        self.wait_element_visible(LoginPageLocators.login_form_block)
        self.clear_by_keys(LoginPageLocators.login_input)
        self.set_locator_value(locator=LoginPageLocators.login_input, value=username)
        self.clear_by_keys(LoginPageLocators.password_input)
        self.set_locator_value(locator=LoginPageLocators.password_input, value=password)

    @allure.step('Login with {username}: {password}')
    def login_user(self, username, password):
        self.fill_login_user_form(username, password)
        self.find_and_click(locator=LoginPageLocators.login_btn)