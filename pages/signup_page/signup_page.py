import time
from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
import utilities.custom_logger as cl
import logging


class SignupPage(BasePage):
    """
    *****

    Each page should have the appropriate page methods.
    In the page class you should add the appropriate methods for that page.

    *****
    """

    log = cl.custom_logger(logging.DEBUG)

    # Locators
    twikkie_homepage_text_xpath_locator = '//div[@class="right_part_content_outer"]/h1'
    homepage_about_tab_xpath_locator = '//li[@class="nav_home_menu"]/a[text()="About"]'
    homepage_pricing_tab_xpath_locator = '//li[@class="nav_home_menu"]/a[text()="Pricing"]'
    homepage_partners_tab_xpath_locator = '//li[@class="nav_home_menu"]/a[text()="Partners"]'
    homepage_components_tab_xpath_locator = '//li[@class="nav_home_menu"]/a[text()="Components"]'
    try_for_free_button_xpath_locator = '//button[@class="btn-free"]'
    request_demo_button_xpath_locator = '//button[@class="btn-demo"]'
    signup_welcome_text_xpath_locator = "//h4[contains(text(),'Welcome to Twikkie!')]"
    # first_name_field_xpath_locator = '//div[@class="name_outer"]//label[text()="First Name"]/following-sibling::input]'
    first_name_field_xpath_locator = '//input[@placeholder="Enter your First name"]'
    last_name_field_xpath_locator = '//input[@placeholder="Enter your Last name"]'
    company_name_field_xpath_locator = '//input[@placeholder="Enter your company name"]'
    domain_name_field_xpath_locator = '//input[@placeholder="One word with no space"]'
    company_email_field_xpath_locator = '//input[@placeholder="Enter your Email"]'
    company_phone_field_xpath_locator = '//input[@placeholder="Enter your Phone no."]'
    submit_button_xpath_locator = '//div[@class="Sign_Up_btn"]'
    terms_and_conditions_checkbox_xpath_locator = '//div//input[@id="flexCheckDefault"]'
    dropdown_xpath_locator = '//div//select[@class="form-control"]'
    country_dropdown_list_xpath_locator = '//select[@class="form-control"]/option'
    first_name_validation_message_xpath_locator = "//div[contains(text(),'The first name is required!')]"
    last_name_validation_message_xpath_locator = "//div[contains(text(),'The last name is required!')]"
    company_name_validation_message_xpath_locator = "//div[contains(text(),'The company name is required!')]"
    domain_name_validation_message_xpath_locator = "//div[contains(text(),'Domain name is required!')]"
    company_email_validation_message_xpath_locator = "//div[contains(text(),' Company email address is required.')]"
    company_phone_validation_message_xpath_locator = "//div[contains(text(),'A company phone number is required.')]"
    invalid_phone_format_validation_message_xpath_locator = "//div[contains(text(),'Invalid phone number!')]"
    company_country_validation_message_xpath_locator = "//div[contains(text(),'Country is required!')]"
    signup_submit_form_error_message_xpath_locator = "//h4[contains(text(),'  Please read and accept the Terms & Conditions. ')]"
    invalid_email_format_validation_message_xpath_locator = "//div[contains(text(),'Your email address must be valid.')]"
    registered_email_id_error_message_xpath_locator = "//h4[contains(text(),'We are sorry, but the email ID you provided seems to already exist in our system. Try logging in or using a different email ID.')]"
    already_taken_company_name_error_message_xpath_locator = "//h4[contains(text(),'Our system shows that a company with the same name already exists.')]"
    terms_accept_checkbox_xpath_locator = '//input[@style="outline: red solid 1px;"]'
    operation_successful_xpath_locator = "//h4[contains(text(),'Operation Successful. ')]"
    setup_twikkie_company_account_message_xpath_locator = "//h4[contains(text(),'Please hold tight as we set up your Twikkie Company Account')]"
    signup_confirmation_message_xpath_locator = '//div[@class="welcome_twikkie_right_part_heading"]/h4[contains(text(),"Check your email!")]'
    # successfully_registered_email_xpath_locator = f'//div[@class="welcome_twikkie_right_part_heading"]/p/a[contains(text(),"{email}")]'
    personnel_tab_xpath_locator = '//div[@id="headingOne"]//p[contains(text()," Personnel")]'
    self_service_xpath_locator = "//a[contains(text(),' Self Service ')]"
    profile_checkbox_xpath_locator = '//div[@class="active_box"]//input'
    account_delete_button_xpath_locator = '//span[@class="filter_delete_item"]'
    captcha_element_xpath_locator = '//div[@class="captcha_bar"]'

    # Test data
    TWIKKIE_URL = 'http://172.105.53.207/'
    FIRST_NAME = 'Jane'
    LAST_NAME = 'James'
    COMPANY_NAME = 'demo1'
    ALREADY_TAKEN_COMPANY_NAME = 'Demo ltd'
    PHONE = '00000000000'
    INVALID_PHONE_NUMBER = '00'
    REGISTERED_EMAIL = "demo@twikkie.com"
    UNREGISTERED_EMAIL = "kelir86121@apn7.com"
    VALID_PASSWORD = "Demo123#"
    DOMAIN_NAME_3 = "autotesting"
    DOMAIN_NAME = "Demo"
    NEW_DOMAIN_NAME = "TEST"
    WRONG_DOMAIN_NAME = "Wrong"
    LOGIN_PAGE_TEXT = 'Company Login'
    VALID_DOMAIN = 'Twikkie_Demo'
    INVALID_FORMAT_USERNAME = 'demo@twikkie.'
    INVALID_USERNAME = 'demo@twikie.com'
    INVALID_PASSWORD = 'DEMO'
    VALID_USERNAME1 = 'vardanyan.gago@gmail.com'
    VALID_USERNAME3 = 'gagikvardanyan613@gmail.com'
    VALID_PASSWORD1 = 'User123456'
    URL_ADMIN_SUBDIRECTORY = '/admin'
    URL_COMPANY_SUBDIRECTORY = '/company'
    URL_SIGNUP_SUBDIRECTORY = 'signup'
    COUNTRY_NAME = 'Armenia'

    #email data

    user = 'gagikvardanyan613@gmail.com'
    password = 'fdjtpxaxagcrqkyq'
    imap_url = 'imap.gmail.com'

    # Validation and error messages
    FIRST_NAME_FIELD_VALIDATION_MESSAGE = 'The first name is required!'
    LAST_NAME_FIELD_VALIDATION_MESSAGE = 'The last name is required!'
    COMPANY_NAME_FIELD_VALIDATION_MESSAGE = 'The company name is required!'
    DOMAIN_NAME_FIELD_VALIDATION_MESSAGE = 'Domain name is required!'
    COMPANY_EMAIL_FIELD_VALIDATION_MESSAGE = 'Company email address is required.'
    COMPANY_PHONE_FIELD_VALIDATION_MESSAGE = 'A company phone number is required.'
    COMPANY_COUNTRY_DROPDOWN_VALIDATION_MESSAGE = 'Country is required!'
    SIGNUP_SUBMIT_FORM_ERROR_MESSAGE = 'Please read and accept the Terms & Conditions.'
    REGISTERED_EMAIL_ERROR_MESSAGE = 'We are sorry, but the email ID you provided seems to already exist in our system. Try logging in or using a different email ID.'
    PHONE_INVALID_FORMAT_VALIDATION_MESSAGE = 'Invalid phone number!'
    INVALID_EMAIL_FORMAT_VALIDATION_MESSAGE = 'Your email address must be valid.'
    ALREADY_TAKEN_COMPANY_NAME_ERROR_MESSAGE = 'Our system shows that a company with the same name already exists.'
    OPERATION_SUCCESSFUL_VALIDATION_MESSAGE = 'Operation Successful.'
    SETUP_TWIKKIE_COMPANY_ACCOUNT_MESSAGE = 'Please hold tight as we set up your Twikkie Company Account'
    SIGNUP_CONFIRMATION_MESSAGE = 'Check your email!'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_homepage_text(self):
        return self.element_presence_check(self.twikkie_homepage_text_xpath_locator)

    def verify_homepage_about_tab(self):
        return self.is_element_present(self.homepage_about_tab_xpath_locator)

    def verify_homepage_pricing_tab(self):
        return self.is_element_present(self.homepage_pricing_tab_xpath_locator)

    def verify_homepage_partners_tab(self):
        return self.is_element_present(self.homepage_partners_tab_xpath_locator)

    def verify_homepage_components_tab(self):
        return self.is_element_present(self.homepage_components_tab_xpath_locator)

    def verify_try_for_free_button(self):
        return self.is_element_present(self.try_for_free_button_xpath_locator)

    def verify_request_demo_button(self):
        return self.is_element_present(self.request_demo_button_xpath_locator)

    def click_on_signup_tab(self):
        self.element_click(self.try_for_free_button_xpath_locator)

    def validate_first_name_field_displayed(self):
        return self.get_element(self.first_name_field_xpath_locator).is_displayed()

    def validate_last_name_field_displayed(self):
        return self.get_element(self.last_name_field_xpath_locator).is_displayed()

    def validate_company_name_field_displayed(self):
        return self.get_element(self.company_name_field_xpath_locator).is_displayed()

    def validate_domain_name_field_displayed(self):
        return self.get_element(self.domain_name_field_xpath_locator).is_displayed()

    def validate_company_email_field_displayed(self):
        return self.get_element(self.company_email_field_xpath_locator).is_displayed()

    def validate_company_phone_field_displayed(self):
        return self.get_element(self.company_phone_field_xpath_locator).is_displayed()

    # def get_registered_user_email_locator(self, email):
    #     return self.get_element(f'//div[@class="welcome_twikkie_right_part_heading"]/p/a[contains(text(),"{email}")]')
    #
    # def get_registered_email(self, email):
    #     return self.get_text(self.get_registered_user_email_locator(email))

    def accept_cookies(self):
        self.element_click('//div[@class="Cookie_btn"]//button[1]')

    def click_on_submit_button(self):
        self.element_click(self.submit_button_xpath_locator)

    def click_on_self_service_tab(self):
        self.element_click(self.self_service_xpath_locator)

    def click_on_profile_checkbox(self):
        self.element_click(self.profile_checkbox_xpath_locator)

    def click_on_delete_button(self):
        self.element_click(self.account_delete_button_xpath_locator)

    def get_first_name_field_validation_message(self):
        return self.get_text(self.first_name_validation_message_xpath_locator)

    def get_signup_confirmation_message(self):
        return self.get_text(self.signup_confirmation_message_xpath_locator)

    # def get_check_your_email_text(self):
    #     return self.get_text(self.check_your_email_text_xpath_locator)

    def get_last_name_field_validation_message(self):
        return self.get_text(self.last_name_validation_message_xpath_locator)

    def get_company_name_field_validation_message(self):
        return self.get_text(self.company_name_validation_message_xpath_locator)

    def get_domain_name_field_validation_message(self):
        return self.get_text(self.domain_name_validation_message_xpath_locator)

    def get_company_email_field_validation_message(self):
        return self.get_text(self.company_email_validation_message_xpath_locator)

    def get_company_name_field_error_message(self):
        return self.get_text(self.already_taken_company_name_error_message_xpath_locator)

    def get_company_phone_field_validation_message(self):
        return self.get_text(self.company_phone_validation_message_xpath_locator)

    def get_company_phone_field_validation_message_with_invalid_format(self):
        return self.get_text(self.invalid_phone_format_validation_message_xpath_locator)

    def get_company_country_dropdown_validation_message(self):
        return self.get_text(self.company_country_validation_message_xpath_locator)

    def get_operation_successful_validation_message(self):
        return self.get_text(self.operation_successful_xpath_locator)

    def get_signup_form_error_message(self):
        return self.get_text(self.signup_submit_form_error_message_xpath_locator)

    def get_phone_invalid_format_validation_message(self):
        return self.get_text(self.invalid_phone_format_validation_message_xpath_locator)

    def get_email_invalid_format_validation_message(self):
        return self.get_text(self.invalid_email_format_validation_message_xpath_locator)

    def fill_signup_first_name(self, name):
        return self.send_keys(name, self.first_name_field_xpath_locator)

    def fill_signup_last_name(self, name):
        return self.send_keys(name, self.first_name_field_xpath_locator)

    def fill_company_name(self, company):
        return self.send_keys(company, self.company_name_field_xpath_locator)

    def fill_company_phone(self, phone):
        return self.send_keys(phone, self.company_phone_field_xpath_locator)

    def fill_domain_name(self, domain):
        return self.send_keys(domain, self.domain_name_field_xpath_locator)

    def click_on_checkbox(self):
        return self.element_click(self.terms_and_conditions_checkbox_xpath_locator)

    def check_active_checkbox_presence(self):
        return self.element_presence_check(self.terms_accept_checkbox_xpath_locator)

    def get_signup_registered_email_error_message(self):
        return self.get_text(self.registered_email_id_error_message_xpath_locator)

    def fill_company_email(self, email):
        return self.send_keys(email, self.company_email_field_xpath_locator)

    def choose_country_from_dropdown(self, country):
        self.select_item_from_drop_down_list(self.get_element(self.dropdown_xpath_locator), 'text', country)

    def user_signup(self, firstname, lastname, company, domain, email, phone):
        try:
            self.send_keys(firstname, self.first_name_field_xpath_locator)
            self.send_keys(lastname, self.last_name_field_xpath_locator)
            self.send_keys(company, self.company_name_field_xpath_locator)
            self.send_keys(domain, self.domain_name_field_xpath_locator)
            self.send_keys(email, self.company_email_field_xpath_locator)
            self.send_keys(phone, self.company_phone_field_xpath_locator)
            self.choose_country_from_dropdown('Armenia')
            self.click_on_checkbox()
            self.element_click(self.submit_button_xpath_locator)
        except:
            self.log.info("UNABLE TO SIGNUP")
            print_stack()

    def click_on_dropdown(self):
        return self.element_click(self.dropdown_xpath_locator)

    def dropdown_list_options(self):
        return self.get_element(self.country_dropdown_list_xpath_locator)

    def get_dropdown_element_text(self):
        return self.get_text(self.dropdown_list_options)

    def check_checkbox_selected(self):
        return self.get_element(self.terms_and_conditions_checkbox_xpath_locator).is_selected()

    def get_selected_country(self):
        return self.get_text(self.dropdown_xpath_locator)

    def get_perosneel_tab(self):
        return self.get_text(self.personnel_tab_xpath_locator)

    def click_on_personeel_tab(self):
        self.element_click(self.personnel_tab_xpath_locator)

    def verify_dropdown_list_countries(self):
        options_list_1 = SignupPage.get_options(self.driver)
        options_string = '\n'.join(options_list_1)
        expected_options_string = self.get_selected_country()
        return options_string == expected_options_string

    def account_deletion(self):
        self.click_on_personeel_tab()
        self.click_on_self_service_tab()
        self.click_on_profile_checkbox()
        self.click_on_delete_button()

    def get_captcha_element(self):
        return self.get_element(self.captcha_element_xpath_locator)

    @staticmethod
    def get_options(driver):
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//select[@class="form-control"]'))
        )
        time.sleep(5)
        options = select_element.find_elements(By.XPATH, './/option')
        options_list = [option.text for option in options]
        print(options_list)
        return options_list
