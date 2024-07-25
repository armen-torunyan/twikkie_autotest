# import email
import random
import time
from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base import base_page
from base.base_page import BasePage
import utilities.custom_logger as cl
import logging
from selenium import webdriver

from pages.login_page.login_page import LoginPage
from utilities import get_data_from_email


class SettingsCompanyPage(BasePage):
    """
    *****

    Each page should have the appropriate page methods.
    In the page class you should add the appropriate methods for that page.

    *****
    """

    log = cl.custom_logger(logging.DEBUG)

    # Locators
    settings_icon_xpath_locator = '//div[@class="deshborad_setting"]'
    company_module_xpath_locator = '//div[@class="deshborad_setting_menu_list_item"]//a[contains(text(),"Company")]'
    company_information_text_xpath_locator = "//h4[contains(text(),'Company Information')]"
    domain_name_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Domain Name")]'
    company_name_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Company Name")]'
    contact_person_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Contact Person")]'
    contact_phone_number_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Contact Phone Number")]'
    contact_email_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Contact Email ")]'
    sub_companies_enabled_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Sub-companies enabled")]'
    language_preference_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Language Preference")]'
    country_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Country")]'
    address_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Address")]'
    default_currency_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Default Currency")]'
    industry_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Industry")]'
    timezone_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Timezone")]'
    public_event_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Public Event")]'
    custom_event_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Custom Event")]'
    colour_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Colour ")]'
    logo_text_xpath_locator = '//div[@class="left_part_content"]//label[contains(text(),"Logo")]'
    edit_icon_xpath_locator = '//div[@class="edit_form"]'
    green_colour_xpath_locator = '//div[@class="colorpicker"]'
    # filled_domain_name_text_xpath_locator = f'//div[@class="right_part_content"]//p[contains(text(), {p_text})]'
    company_name_filled_text_xpath_locator = "//div[@class='right_part_content']"

    domain_name_field_xpath_locator = '//input[@placeholder="Domain name"]'
    company_name_field_xpath_locator = '//input[@placeholder="company name"]'
    first_and_last_names_field_xpath_locator = '//input[@placeholder="ayushi mishra"]'

    first_name_field_xpath_locator = f'({first_and_last_names_field_xpath_locator})[1]'
    last_name_field_xpath_locator = f'({first_and_last_names_field_xpath_locator})[2]'

    dropdowns_xpath_locator = '//div//select[@class="form-control"]'
    language_dropdown_xpath_locator = f'({dropdowns_xpath_locator})[1]'
    country_dropdown_xpath_locator = f'({dropdowns_xpath_locator})[2]'
    default_currency_xpath_locator = f'({dropdowns_xpath_locator})[3]'
    industry_xpath_locator = f'({dropdowns_xpath_locator})[4]'
    timezone_xpath_locator = f'({dropdowns_xpath_locator})[5]'
    public_event_xpath_locator = f'({dropdowns_xpath_locator})[6]'
    custom_event_xpath_locator = f'({dropdowns_xpath_locator})[7]'

    contact_email_field_xpath_locator = '//input[@placeholder="Email"]'
    address_field_xpath_locator = '//input[@placeholder="Address"]'
    submit_button_xpath_locator = '//button[@class="save"]'
    cancel_button_xpath_locator = '//button[@class="cancel"]'

    # Test data
    TWIKKIE_URL = 'http://172.105.53.207/'
    COMPANY_NAME_DEMO = 'Demo ltd'
    CONTACT_PERSON = 'Demo Test'
    NEW_COMPANY_NAME = 'new'
    NEW_FIRST_NAME = 'Jane'
    NEW_LAST_NAME = 'James'
    FIRST_NAME = 'Gagik'
    LAST_NAME = 'Vardanyan'
    COMPANY_NAME = 'testauto'
    ALREADY_TAKEN_COMPANY_NAME = 'Demo ltd'
    PHONE = '09068371399'
    EMAIL = 'demo@twikkie.com'
    SUB_COMPANIES_ENABLED = 'No'
    LANGUAGE_PREFERENCE = 'English'
    COUNTRY = 'Nigeria'
    TIMEZONE = 'Africa/Lagos'
    PUBLIC_EVENT = 'Nigeria Public Holidays'
    ADDRESS = 'Adonts'
    CONTACT_PERSON_NAME = 'Gagik Vardanyan'
    VALID_PASSWORD = "Demo123#"
    DOMAIN_NAME = "Demo"
    NEW_DOMAIN_NAME = "TEST"
    WRONG_DOMAIN_NAME = "Wrong"
    LOGIN_PAGE_TEXT = 'Company Login'
    VALID_DOMAIN = 'Twikkie_Demo'
    INVALID_PASSWORD = 'DEMO'
    VALID_USERNAME1 = 'vardanyan.gago@gmail.com'
    VALID_PASSWORD1 = 'User123456'
    VALID_USERNAME2 = 'gagiktest05@gmail.com'
    VALID_PASSWORD2 = 'User123456'
    NEW_VALID_USERNAME = 'gagikvardanyan613@gmail.com'
    URL_ADMIN_SUBDIRECTORY = '/admin'
    URL_COMPANY_SUBDIRECTORY = '/company'
    URL_SIGNUP_SUBDIRECTORY = 'signup'
    URL_SETTINGS_SUBDIRECTORY = 'settings'
    URL_COMPANY_SETTING_SUBDIRECTORY = 'companysetting'
    GREEN_COLOR = 'background-color: rgb(98, 179, 59);'

    # EMAIL DATA
    user = 'gagiktest05@gmail.com'
    password = 'enggxzorbndjspax'
    imap_url = 'imap.gmail.com'

    # Validation and error messages
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_settings_icon_presence(self):
        return self.element_presence_check(self.settings_icon_xpath_locator)

    def check_edit_icon_presence(self):
        return self.element_presence_check(self.edit_icon_xpath_locator)

    def check_company_module_presence(self):
        return self.element_presence_check(self.company_module_xpath_locator)

    def click_on_setting_icon(self):
        return self.element_click(self.settings_icon_xpath_locator)

    def click_on_first_name_field(self):
        return self.element_click(self.first_name_field_xpath_locator)

    def click_on_edit_icon(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.edit_icon_xpath_locator))
            )
            element.click()
            return element
        except:
            return None

    def click_on_company_module(self):
        return self.element_click(self.company_module_xpath_locator)

    def check_company_information_text_presence(self):
        return self.element_presence_check(self.domain_name_text_xpath_locator)

    def get_colour_locator(self):
        return self.get_element(self.green_colour_xpath_locator)

    def get_first_name_field_locator(self):
        return self.get_element(By.XPATH, f'({self.first_and_last_names_field_xpath_locator})[1]')

    def fill_input_field(self, text, locator):
        return self.send_keys(text, locator)

    # def get_filled_input_field(self, p_text):
    #     return self.get_text(f'//div[@class="right_part_content"]//p[contains(text(),{p_text})]')

    def get_filled_input_field(self, p_text):
        return self.get_text('//div[@class="right_part_content"]//p[contains(text(), "{}")]'.format(p_text))

    def get_text_from_company_name_field(self):
        return self.get_text(self.company_name_filled_text_xpath_locator)

    def get_submit_button(self):
        return self.get_element(self.submit_button_xpath_locator)

    def click_on_cancel_button(self):
        return self.element_click(self.cancel_button_xpath_locator, locator_type='xpath')

    def click_on_submit_button(self):
        return self.element_click(self.submit_button_xpath_locator, locator_type='xpath')

    def get_domain_name_filed(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.domain_name_field_xpath_locator))
            )
            return element
        except:
            return None

    def get_selected_option_text_from_dropdown(self):
        return self.get_text(self.language_dropdown_xpath_locator)

    def get_dropdown(self, index):
        return self.get_element(f'({self.dropdowns_xpath_locator})[{index}]')

    def fill_address_input_field(self, address):
        return self.send_keys(address, self.address_field_xpath_locator)

    def check_domain_name_has_readonly_attribute(self):
        element = self.get_domain_name_filed()
        if element is None:
            raise Exception("Domain name field element not found")

        is_readonly = element.get_attribute("readonly")
        return is_readonly is not None

    def check_logo_color(self):
        time.sleep(3)
        element = self.get_element(By.XPATH, self.green_colour_xpath_locator)
        background_color = element.get_attribute("style")
        return background_color == self.GREEN_COLOR

    def fill_otp(self):
        login_page = LoginPage(self.driver)
        time.sleep(10)
        otp = get_data_from_email.get_latest_otp(self.user, self.password, self.imap_url)
        login_page.fill_otp_field(otp)
        login_page.click_on_verify_button()
        time.sleep(10)
        login_page.click_on_later_button()
        time.sleep(1)

    def edit_company_name_from_company_module(self, company_name):
        self.click_on_setting_icon()
        self.click_on_company_module()
        time.sleep(10)
        self.click_on_edit_icon()
        time.sleep(2)
        self.clear_input_fields(self.company_name_field_xpath_locator)
        self.fill_input_field(company_name,
                              self.company_name_field_xpath_locator)
        self.scroll_into_view(self.submit_button_xpath_locator)
        self.click_on_submit_button()

    def edit_first_and_last_name_from_company_module(self, first_name, last_name):
        self.click_on_setting_icon()
        self.click_on_company_module()
        time.sleep(5)
        self.click_on_edit_icon()
        time.sleep(2)
        self.element_click(self.first_name_field_xpath_locator)
        self.clear_input_fields(self.first_name_field_xpath_locator)
        self.fill_input_field(first_name, self.first_name_field_xpath_locator)
        self.element_click(self.last_name_field_xpath_locator)
        self.clear_input_fields(self.last_name_field_xpath_locator)
        self.fill_input_field(last_name, self.last_name_field_xpath_locator)
        self.scroll_into_view(self.submit_button_xpath_locator)
        self.click_on_submit_button()
        time.sleep(2)

    def edit_email_address_from_company_module(self, email):
        self.click_on_setting_icon()
        self.click_on_company_module()
        time.sleep(5)
        self.click_on_edit_icon()
        self.clear_input_fields(self.contact_email_field_xpath_locator)
        self.fill_input_field(email, self.contact_email_field_xpath_locator)
        self.scroll_into_view(self.submit_button_xpath_locator)
        self.click_on_submit_button()

    def clear_first_name_field(self):
        return self.clear_input_fields(self.first_name_field_xpath_locator)

    def navigate_to_edit_form(self):
        self.click_on_setting_icon()
        self.click_on_company_module()
        time.sleep(5)
        self.click_on_edit_icon()

    # def edit_texts_from_company_module_fields(self, fields_texts):
    #     self.click_on_setting_icon()
    #     self.click_on_company_module()
    #     time.sleep(10)
    #
    #     for field, text in fields_texts:
    #         self.click_on_edit_icon()
    #         time.sleep(2)
    #         self.clear_input_fields(field)
    #         self.fill_input_field(text, field)
    #         self.scroll_into_view(self.submit_button_xpath_locator)
    #         self.click_on_submit_button()
    #         time.sleep(2)

    def navigate_to_settings_company_module(self):
        login_page = LoginPage(self.driver)
        time.sleep(1)
        login_page.click_on_login_button()
        login_page.click_on_later_button()
        self.click_on_setting_icon()
        self.click_on_company_module()

    def navigate_to_the_settings_page(self):
        login_page = LoginPage(self.driver)
        login_page.click_on_login_button()
        login_page.click_on_later_button()
        self.click_on_setting_icon()

    def select_random_option_from_dropdown(self, locator):
        try:
            select_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
            select = Select(select_element)

            all_options = select.options
            random_option = random.choice(all_options)

            select.select_by_visible_text(random_option.text)

            return random_option.text

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_automatically_selected_currency(self, currency_locator):
        try:
            currency_select_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, currency_locator))
            )
            currency_select = Select(currency_select_element)
            selected_currency = currency_select.first_selected_option

            return selected_currency.text

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_text_from_dropdown(self, locator):
        self.get_text(locator)

    def validate_company_module_page_data(self):
        if self.get_filled_input_field(self.DOMAIN_NAME) != self.DOMAIN_NAME:
            raise ValueError("DOMAIN_NAME does not match")
        if self.get_filled_input_field(self.COMPANY_NAME_DEMO) != self.COMPANY_NAME_DEMO:
            raise ValueError("COMPANY_NAME_DEMO does not match")
        if self.get_filled_input_field(self.CONTACT_PERSON) != self.CONTACT_PERSON:
            raise ValueError("CONTACT_PERSON does not match")
        if self.get_filled_input_field(self.PHONE) != self.PHONE:
            raise ValueError("PHONE does not match")
        if self.get_filled_input_field(self.EMAIL) != self.EMAIL:
            raise ValueError("EMAIL does not match")
        if self.get_filled_input_field(self.SUB_COMPANIES_ENABLED) != self.SUB_COMPANIES_ENABLED:
            raise ValueError("SUB_COMPANIES_ENABLED does not match")
        if self.get_filled_input_field(self.LANGUAGE_PREFERENCE) != self.LANGUAGE_PREFERENCE:
            raise ValueError("LANGUAGE_PREFERENCE does not match")
        if self.get_filled_input_field(self.COUNTRY) != self.COUNTRY:
            raise ValueError("COUNTRY does not match")
        if self.get_filled_input_field(self.TIMEZONE) != self.TIMEZONE:
            raise ValueError("TIMEZONE does not match")
        if self.get_filled_input_field(self.PUBLIC_EVENT) != self.PUBLIC_EVENT:
            raise ValueError("PUBLIC_EVENT does not match")

    def check_company_module_detail_page_appear(self):
        self.element_presence_check(self.domain_name_text_xpath_locator)
        self.element_presence_check(self.company_name_text_xpath_locator)
        self.element_presence_check(self.contact_person_text_xpath_locator)
        self.element_presence_check(self.contact_phone_number_text_xpath_locator)
        self.element_presence_check(self.contact_email_text_xpath_locator)
        self.element_presence_check(self.sub_companies_enabled_text_xpath_locator)
        self.element_presence_check(self.language_preference_text_xpath_locator)
        self.element_presence_check(self.country_text_xpath_locator)
        self.element_presence_check(self.address_text_xpath_locator)
        self.element_presence_check(self.default_currency_text_xpath_locator)
        self.element_presence_check(self.industry_text_xpath_locator)
        self.element_presence_check(self.timezone_text_xpath_locator)
        self.element_presence_check(self.public_event_text_xpath_locator)
        self.element_presence_check(self.custom_event_text_xpath_locator)
        self.element_presence_check(self.country_text_xpath_locator)
        self.element_presence_check(self.logo_text_xpath_locator)

    # def choose_options_from_dropdowns_and_validate_choosen_option_text(self):
    #     selected_language = self.select_random_option_from_dropdown(self.language_dropdown_xpath_locator)
    #     selected_country = self.select_random_option_from_dropdown(self.country_dropdown_xpath_locator)
    #     self.fill_address_input_field(self.ADDRESS)
    #     selected_default_currency = self.select_random_option_from_dropdown(self.default_currency_xpath_locator)
    #     selected_industry = self.select_random_option_from_dropdown(self.industry_xpath_locator)
    #     selected_timezone = self.select_random_option_from_dropdown(self.timezone_xpath_locator)
    #     selected_public_event = self.select_random_option_from_dropdown(self.public_event_xpath_locator)
    #     selected_custom_event = self.select_random_option_from_dropdown(self.custom_event_xpath_locator)
    #     self.click_on_submit_button()
    #
    #     assert (self.get_filled_input_field(self.language_dropdown_xpath_locator) == selected_language)
    #     assert (self.get_filled_input_field(self.country_dropdown_xpath_locator) == selected_country)
    #     assert (self.get_filled_input_field(self.default_currency_xpath_locator) == selected_default_currency)
    #     assert (self.get_filled_input_field(self.industry_xpath_locator) == selected_industry)
    #     assert (self.get_filled_input_field(self.timezone_xpath_locator) == selected_timezone)
    #     assert (self.get_filled_input_field(self.public_event_xpath_locator) == selected_public_event)
    #     assert (self.get_filled_input_field(self.custom_event_xpath_locator) == selected_custom_event)

