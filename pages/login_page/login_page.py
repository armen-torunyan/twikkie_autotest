import time
from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
import utilities.custom_logger as cl
import logging

from utilities import get_data_from_email


class LoginPage(BasePage):
    """
    *****

    Each page should have the appropriate page methods.
    In the page class you should add the appropriate methods for that page.

    *****
    """

    log = cl.custom_logger(logging.DEBUG)

    # Locators
    login_navi_button_xpath_locator = '//button[@class="btn-login"]'
    domain_page_text_xpath_locator = '//div[@class="twikkie_main_head_right_part_heading"]/h4'
    username_field_xpath_locator = '//input[@id="userName"]'
    password_field_id_locator = "password"
    login_button_xpath_locator = '//div//button[@class="btn btn-submit btn-login login_button_content"]'
    signup_link_text_button_xpath_locator = '//div[@class="form-group"]/p/a'
    submit_button_xpath_locator = '//button[@class="login_popup_btn"]'
    domain_name_id_locator = "companyName"
    remember_me_checkbox_id_locator = 'flexCheckDefault'
    welcome_text_xpath_locator = "//h3[contains(text(),'Welcome to Twikkie!')]"
    invalid_password_message_xpath_locator = '//div[@class="messageBackground errorbackground"]/h4]'
    login_welcome_back_text_xpath_locator = "//h4[contains(text(),'Welcome Back!')]"
    later_button_xpath_locator = '//button[@class="later_btn"]'
    dashboard_list_xpath_locator = '//div[@id="headingOne"]'
    signup_link_xpath_locator = "//a[contains(text(),' Sign Up')]"
    username_required_error_message_xpath_locator = "//div[contains(text(),'A username or email address is required.')]"
    username_invalid_format_error_message_xpath_locator = "//div[contains(text(),'Your email address must be valid.')]"
    password_required_error_message_xpath_locator = '//div[contains(text(),"The password entered doesn\'t match")]'
    domain_filed_validation_message_xpath_locator = "//div/div[contains(text(), 'Please enter your domain name.')]"
    domain_name_error_message_xpath_locator = '//div[@class="messageBackground errorbackground"]/h4'
    remember_me_checkbox_xpath_locator = '//input[@class="form-check"]'
    forgot_password_xpath_locator = '//div[@class="forget_password"]'
    forgot_password_title_xpath_locator = '//div[@class="forget_password_right_part_heading"]/h4'
    profile_details_dropdown_icon_xpath_locator = '//i[@class="fa fa-caret-down"]'
    dropdown_logout_button_xpath_locator = "//a[contains(text(),'Log Out')]"
    dashboard_text_xpath_locator = "//h3[contains(text(),'Dashboard')]"
    invalid_credentials_xpath_locator = "//h4[contains(text(),' Invalid Credentials! ')]"
    otp_field_xpath_locator = '//input[@id="otp"]'

    signup_page_main_text_xpath_locator = '//div[@class="heading_outer"]'
    verify_otp_text_xpath_locator = "//h4[contains(text(),'Verify OTP !')]"
    verify_button_xpath_locator = '//button[@class="btn btn-submit btn-login login_button_content"]'
    otp_required_validation_message_xpath_locator = "//div/div[contains(text(), ' OTP is required to proceed.')]"
    invalid_otp_error_message_xpath_locator = "//h4[contains(text(),'Invalid OTP')]"
    locked_account_validation_message_xpath_locator = "//h4[contains(text(),'Your account has been locked, please check your email for further steps to follow')]"
    forgot_password_email_field_xpath_locator = '//input[@id="exampleInputEmail1"]'
    reset_password_button_xpath_locator = '//div[@class="forget_btn"]'
    confirm_password_field_xpath_locator = '//input[@id="password2"]'
    submit_password_reset_xpath_locator = '//button[@class="btn btn-submit btn-login login_button_content"]'
    reset_password_text_xpath_locator = "//h4[contains(text(),'Reset Password!')]"
    operation_successful_xpath_locator = "//h4[contains(text(),'Operation Successful. ')]"
    personnel_tab_xpath_locator = '//div[@id="headingOne"]//p[contains(text()," Personnel")]'

    # Test data
    VALID_USERNAME = "demo@twikkie.com"
    VALID_PASSWORD = "Demo123#"
    INVALID_OTP = "1"
    DOMAIN_NAME = "Demo"
    DOMAIN_NAME_2 = "testauto"
    DOMAIN_NAME_3 = "autotesting"
    DOMAIN_NAME_TESTAUTO = "testauto"
    WRONG_DOMAIN_NAME = "Wrong"
    INVALID_DOMAIN_NAME = "de"
    LOGIN_PAGE_TEXT = 'Company Login'
    VALID_DOMAIN = 'Twikkie_Demo'
    INVALID_FORMAT_USERNAME = 'demo@twikkie.'
    INVALID_USERNAME = 'demo@twikie.com'
    INVALID_PASSWORD = 'DEMO'
    VALID_USERNAME1 = 'vardanyan.gago@gmail.com'
    VALID_PASSWORD1 = 'User123456'
    VALID_USERNAME2 = 'gagiktest05@gmail.com'
    VALID_PASSWORD2 = 'User123456'
    VALID_USERNAME3 = 'gagikvardanyan613@gmail.com'
    NEW_PASSWORD = 'U7L2CoOy'
    URL_ADMIN_SUBDIRECTORY = 'admin'
    URL_COMPANY_SUBDIRECTORY = 'company'
    URL_LOGIN_SUBDIRECTORY = 'login'
    URL_VERIFY_OTP_SUBDIRECTORY = 'verify_otp'
    RESET_PASSWORD_TEXT = 'Reset Password!'
    INVALID_OTP_TEXT = 'Invalid OTP'
    TWIKKIE_LOGIN_PAGE = 'http://172.105.53.207/company'

    #EMAIL DATA
    user = 'gagiktest05@gmail.com'
    password = 'enggxzorbndjspax'
    imap_url = 'imap.gmail.com'


    # Error and validation messages
    DOMAIN_NAME_ERROR_MESSAGE = 'This Domain Does Not Exist In Our System'
    USERNAME_REQUIRED_ERROR_MESSAGE = 'A username or email address is required.'
    PASSWORD_REQUIRED_ERROR_MESSAGE = "The password entered doesn't match"
    USERNAME_INVALID_FORMAT_ERROR_MESSAGE = 'Your email address must be valid.'
    INVALID_PASSWORD_ERROR_MESSAGE = 'Invalid Password '
    INVALID_EMAIL_ADDRESS_ERROR_MESSAGE = 'Invalid Email Address '
    INVALID_CREDENTIALS = 'Invalid Credentials!'
    OTP_REQUIRED_VALIDATION_MESSAGE = 'OTP is required to proceed.'
    INVALID_OTP_ERROR_MESSAGE = 'Invalid OTP'
    LOCKED_ACCOUNT_VALIDATION_MESSAGE = 'Your account has been locked, please check your email for further steps to follow'
    OPERATION_SUCCESSFUL_VALIDATION_MESSAGE = 'Operation Successful.'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_login_button(self):
        return (self.is_element_present(self.login_navi_button_xpath_locator) and
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 self.login_navi_button_xpath_locator))))

    def navigate_to_domain_page(self):
        self.element_click(self.login_navi_button_xpath_locator)

    def verify_domain_page(self):
        return self.get_text(self.domain_page_text_xpath_locator)

    def get_reset_password_page_text(self):
        return self.get_text(self.reset_password_text_xpath_locator)

    def get_operation_successful_validation_message(self):
        return self.get_text(self.operation_successful_xpath_locator)

    def check_domain_name_field_presence(self):
        return self.element_presence_check(self.domain_name_id_locator, 'id')

    def check_submit_button_presence(self):
        return self.element_presence_check(self.submit_button_xpath_locator)

    def check_signup_link_text_button_presence(self):
        return self.element_presence_check(self.signup_link_text_button_xpath_locator)

    def check_login_welcome_back_text_presence(self):
        return self.element_presence_check(self.login_welcome_back_text_xpath_locator)

    def verify_navigation_to_signup_page(self):
        self.element_click(self.signup_link_text_button_xpath_locator)
        return self.element_presence_check(self.signup_page_main_text_xpath_locator)

    def enter_domain_name(self, domain_name):
        self.send_keys(domain_name, self.domain_name_id_locator, locator_type='id')

    def get_domain_name(self):
        return self.get_element(self.domain_name_id_locator, 'id').get_attribute('value')

    def verify_email_address_field(self):
        return self.is_element_present(self.username_field_xpath_locator)

    def verify_password_field(self):
        return self.is_element_present(self.password_field_id_locator, 'id')

    def user_login(self, username, password):
        try:
            self.send_keys(username, self.username_field_xpath_locator, locator_type='xpath')
            self.send_keys(password, self.password_field_id_locator, locator_type='id')
            self.accept_cookies()
            self.element_click(self.login_button_xpath_locator, locator_type='xpath')
            # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
            #                                                                            self.login_button_xpath_locator)))
            # element.click()
        except:
            self.log.info("UNABLE TO LOGIN")
            print_stack()

    def submit_domain_name(self, domain_name):
        self.send_keys(domain_name, self.domain_name_id_locator, locator_type='id')
        self.element_click(self.submit_button_xpath_locator, locator_type='xpath')

    def click_on_submit_button(self):
        self.element_click(self.submit_button_xpath_locator, locator_type='xpath')

    def click_on_reset_password_button(self):
        self.element_click(self.reset_password_button_xpath_locator)

    def submit_reset_password_button(self):
        self.element_click(self.submit_password_reset_xpath_locator)

    def click_on_later_button(self):
        self.element_click(self.later_button_xpath_locator, locator_type='xpath')

    def validate_welcome_message(self):
        return self.get_element(self.welcome_text_xpath_locator, locator_type='xpath').is_displayed()

    def validate_signup_link(self):
        return self.get_element(self.signup_link_xpath_locator, locator_type='xpath').is_displayed()

    def validate_verify_otp_text(self):
        return self.get_element(self.verify_otp_text_xpath_locator).is_displayed()

    def click_on_signup_link(self):
        return self.element_click(self.signup_link_xpath_locator, locator_type='xpath')

    def validate_domain_field_validation_message(self):
        return self.get_element(self.domain_filed_validation_message_xpath_locator).is_displayed()

    def validate_domain_field_error_message(self):
        return self.get_element(self.domain_name_error_message_xpath_locator).is_displayed()

    def validate_remember_me_checkbox_displays(self):
        return self.get_element(self.remember_me_checkbox_xpath_locator).is_displayed()

    def click_on_login_button(self):
        self.element_click(self.login_button_xpath_locator)

    def navigate_to_forget_password_page(self):
        self.element_click(self.forgot_password_xpath_locator)

    def change_password(self, email, domain_name, new_password, confirm_password):
        self.navigate_to_new_url('http://172.105.53.207/company')
        self.navigate_to_domain_page()
        self.submit_domain_name(domain_name)
        self.navigate_to_forget_password_page()
        self.fill_forgot_password_email_field(email)
        self.click_on_reset_password_button()
        time.sleep(10)
        link = get_data_from_email.get_latest_email(self.user, self.password, self.imap_url)
        self.navigate_to_new_url(link)
        time.sleep(3)
        self.submit_reset_password(new_password, confirm_password)

    # def change_password_and_login_via_new_password(self, email, domain_name, new_password, confirm_password):
    #     self.navigate_to_domain_page()
    #     self.submit_domain_name(domain_name)
    #     self.accept_cookies()
    #     self.navigate_to_forget_password_page()
    #     self.fill_forgot_password_email_field(email)
    #     self.click_on_reset_password_button()
    #     time.sleep(10)
    #     link = get_data_from_email.get_latest_email()
    #     self.navigate_to_new_url(link)
    #     time.sleep(3)
    #     self.submit_reset_password(new_password, confirm_password)
    #     self.submit_domain_name(domain_name)
    #     self.user_login(email, new_password)

    def validate_forget_password_button(self):
        return self.is_element_present(self.forgot_password_xpath_locator)

    def validate_forgot_password_page(self):
        return self.is_element_present(self.forgot_password_title_xpath_locator)

    def get_domain_name_error_message(self):
        return self.get_text(self.domain_name_error_message_xpath_locator)

    def get_username_required_error_message(self):
        return self.get_text(self.username_required_error_message_xpath_locator)

    def get_username_invalid_format_error_message(self):
        return self.get_text(self.username_invalid_format_error_message_xpath_locator)

    def get_locked_account_validation_message(self):
        return self.get_text(self.locked_account_validation_message_xpath_locator)

    def get_password_required_error_message(self):
        return self.get_text(self.password_required_error_message_xpath_locator)

    def get_invalid_credentials_error_message(self):
        return self.get_text(self.invalid_credentials_xpath_locator)

    def get_otp_required_validation_message(self):
        return self.get_text(self.otp_required_validation_message_xpath_locator)

    def get_invalid_otp_error_message(self):
        return self.get_text(self.invalid_otp_error_message_xpath_locator)

    def get_otp_filed(self):
        return self.get_element(self.otp_field_xpath_locator)

    def navigate_to_new_url(self, url):
        self.driver.get(url)

    def validate_invalid_password_error_message(self):
        return self.get_element(self.INVALID_PASSWORD_ERROR_MESSAGE).is_displayed()

    def validate_invalid_email_error_message(self):
        return self.get_element(self.INVALID_EMAIL_ADDRESS_ERROR_MESSAGE).is_displayed()

    def fill_login_password(self, password):
        return self.send_keys(password, self.password_field_id_locator, locator_type='id')

    def fill_forgot_password_email_field(self, password):
        return self.send_keys(password, self.forgot_password_email_field_xpath_locator)

    def fill_invalid_otp_code_multiple_times(self):
        for _ in range(8):
            self.fill_otp_field(self.INVALID_OTP)
            time.sleep(1)
            self.click_on_verify_button()

    # def fill_invalid_otp_code_multiple_times(self):
    #     for _ in range(7):
    #         self.get_otp_filed().clear()
    #         time.sleep(1)
    #         self.fill_otp_field(self.INVALID_OTP)
    #         self.click_on_verify_button()

    # def clear_otp_field(self):
    #     otp_field = self.get_otp_filed()
    #     otp_field.clear()

    def fill_confirm_password_field(self, password):
        return self.send_keys(password, self.confirm_password_field_xpath_locator)

    def submit_reset_password(self, password, confirm_password):
        self.fill_login_password(password)
        self.fill_confirm_password_field(confirm_password)
        self.submit_reset_password_button()

    def fill_login_email(self, password):
        return self.send_keys(password, self.username_field_xpath_locator, locator_type='xpath')

    def click_on_logout_button(self):
        self.element_click(self.profile_details_dropdown_icon_xpath_locator)
        self.element_click(self.dropdown_logout_button_xpath_locator)

    def fill_otp_field(self, otp):
        self.send_keys(otp, self.otp_field_xpath_locator, locator_type='xpath')

    def click_on_verify_button(self):
        self.element_click(self.verify_button_xpath_locator)

    def validate_dashboard_text(self):
        return self.is_element_present(self.dashboard_text_xpath_locator)

    def accept_cookies(self):
        self.element_click('//div[@class="Cookie_btn"]//button[1]')

    def navigate_back_and_forward(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                         self.dashboard_text_xpath_locator)))
        self.driver.back()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                         self.forgot_password_xpath_locator)))

        self.driver.forward()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                        self.dashboard_text_xpath_locator)))
