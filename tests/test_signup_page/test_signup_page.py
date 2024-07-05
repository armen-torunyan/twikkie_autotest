import logging
import time
from telnetlib import EC

import pytest
from pytest import mark
from selenium.webdriver.common.by import By

import utilities.custom_logger as cl
from pages.signup_page.signup_page import SignupPage


@mark.regression
@mark.smoke
def test_user_can_successfully_launch_url_TC_1(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_user_can_successfully_launch_url_TC_1} >>>>>>>>>>>>>>>>> started")
    assert user_signup_page.TWIKKIE_URL == driver.current_url
    assert user_signup_page.verify_homepage_text()
    log.info(f"{test_user_can_successfully_launch_url_TC_1} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_user_can_successfully_launch_url_TC_2(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_user_can_successfully_launch_url_TC_2} >>>>>>>>>>>>>>>>> started")
    assert user_signup_page.TWIKKIE_URL == driver.current_url
    log.info(f"{test_user_can_successfully_launch_url_TC_2} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_homepage_page_menu_TC_3(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_homepage_page_menu_TC_3} >>>>>>>>>>>>>>>>> started")
    assert user_signup_page.verify_homepage_about_tab()
    assert user_signup_page.verify_homepage_pricing_tab()
    assert user_signup_page.verify_homepage_partners_tab()
    assert user_signup_page.verify_homepage_components_tab()
    assert user_signup_page.verify_request_demo_button()
    assert user_signup_page.verify_try_for_free_button()
    log.info(f"{test_homepage_page_menu_TC_3} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_button_TC_4(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_button_TC_4} >>>>>>>>>>>>>>>>> started")
    assert user_signup_page.verify_try_for_free_button()
    user_signup_page.click_on_signup_tab()
    driver.find_element(By.XPATH, user_signup_page.signup_welcome_text_xpath_locator)
    driver.implicitly_wait(10)
    assert user_signup_page.URL_SIGNUP_SUBDIRECTORY in driver.current_url
    log.info(f"{test_signup_button_TC_4} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_form_displays_TC_5(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_form_displays_TC_5} >>>>>>>>>>>>>>>>> started")
    assert user_signup_page.verify_try_for_free_button()
    user_signup_page.click_on_signup_tab()
    assert user_signup_page.validate_first_name_field_displayed()
    assert user_signup_page.validate_last_name_field_displayed()
    assert user_signup_page.validate_company_name_field_displayed()
    assert user_signup_page.validate_domain_name_field_displayed()
    assert user_signup_page.validate_company_name_field_displayed()
    assert user_signup_page.validate_company_phone_field_displayed()
    log.info(f"{test_signup_form_displays_TC_5} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_with_blank_forms_TC_6(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_with_blank_forms_TC_6} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.click_on_submit_button()
    assert (user_signup_page.get_signup_form_error_message() ==
            user_signup_page.SIGNUP_SUBMIT_FORM_ERROR_MESSAGE)
    assert user_signup_page.URL_SIGNUP_SUBDIRECTORY in driver.current_url
    log.info(f"{test_signup_with_blank_forms_TC_6} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_fields_validation_messages_TC_7(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_fields_validation_messages_TC_7} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.click_on_submit_button()
    assert (user_signup_page.get_first_name_field_validation_message() ==
            user_signup_page.FIRST_NAME_FIELD_VALIDATION_MESSAGE)
    assert (user_signup_page.get_last_name_field_validation_message() ==
            user_signup_page.LAST_NAME_FIELD_VALIDATION_MESSAGE)
    assert (user_signup_page.get_company_name_field_validation_message() ==
            user_signup_page.COMPANY_NAME_FIELD_VALIDATION_MESSAGE)
    assert (user_signup_page.get_domain_name_field_validation_message() ==
            user_signup_page.DOMAIN_NAME_FIELD_VALIDATION_MESSAGE)
    assert (user_signup_page.get_company_email_field_validation_message() ==
            user_signup_page.COMPANY_EMAIL_FIELD_VALIDATION_MESSAGE)
    assert (user_signup_page.get_company_phone_field_validation_message() ==
            user_signup_page.COMPANY_PHONE_FIELD_VALIDATION_MESSAGE)
    assert (user_signup_page.get_company_country_dropdown_validation_message() ==
            user_signup_page.COMPANY_COUNTRY_DROPDOWN_VALIDATION_MESSAGE)
    log.info(f"{test_signup_fields_validation_messages_TC_7} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_with_partially_blank_fields_TC_8(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_with_partially_blank_fields_TC_8} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.fill_signup_first_name(user_signup_page.FIRST_NAME)
    user_signup_page.fill_signup_last_name(user_signup_page.LAST_NAME)
    user_signup_page.fill_company_name(user_signup_page.COMPANY_NAME)
    user_signup_page.click_on_submit_button()
    assert (user_signup_page.get_company_phone_field_validation_message() ==
            user_signup_page.COMPANY_PHONE_FIELD_VALIDATION_MESSAGE)
    assert (user_signup_page.get_domain_name_field_validation_message() ==
            user_signup_page.DOMAIN_NAME_FIELD_VALIDATION_MESSAGE)
    assert (user_signup_page.get_company_email_field_validation_message() ==
            user_signup_page.COMPANY_EMAIL_FIELD_VALIDATION_MESSAGE)
    assert (user_signup_page.get_company_country_dropdown_validation_message() ==
            user_signup_page.COMPANY_COUNTRY_DROPDOWN_VALIDATION_MESSAGE)
    assert (user_signup_page.get_signup_form_error_message() ==
            user_signup_page.SIGNUP_SUBMIT_FORM_ERROR_MESSAGE)
    log.info(f"{test_signup_with_partially_blank_fields_TC_8} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_with_already_registered_email_TC_9(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_with_already_registered_email_TC_9} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.user_signup(user_signup_page.FIRST_NAME, user_signup_page.LAST_NAME, user_signup_page.COMPANY_NAME,
                                 user_signup_page.NEW_DOMAIN_NAME, user_signup_page.REGISTERED_EMAIL,
                                 user_signup_page.PHONE)
    assert (user_signup_page.get_signup_registered_email_error_message() ==
            user_signup_page.REGISTERED_EMAIL_ERROR_MESSAGE)
    log.info(f"{test_signup_with_already_registered_email_TC_9} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_with_already_taken_company_name_TC_11(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_with_already_taken_company_name_TC_11} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.user_signup(user_signup_page.FIRST_NAME, user_signup_page.LAST_NAME, user_signup_page.ALREADY_TAKEN_COMPANY_NAME,
                                 user_signup_page.NEW_DOMAIN_NAME, user_signup_page.UNREGISTERED_EMAIL,
                                 user_signup_page.PHONE)
    assert (user_signup_page.get_company_name_field_error_message() ==
            user_signup_page.ALREADY_TAKEN_COMPANY_NAME_ERROR_MESSAGE)
    log.info(f"{test_signup_with_already_taken_company_name_TC_11} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_phone_field_with_invalid_format_TC_12(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_phone_field_with_invalid_format_TC_12} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.fill_company_phone(user_signup_page.INVALID_PHONE_NUMBER)
    user_signup_page.click_on_submit_button()
    assert (user_signup_page.get_company_phone_field_validation_message() ==
            user_signup_page.PHONE_INVALID_FORMAT_VALIDATION_MESSAGE)
    log.info(f"{test_signup_phone_field_with_invalid_format_TC_12} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_with_invalid_email_format_TC_14(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_with_invalid_email_format_TC_14} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    # user_signup_page.fill_signup_first_name(user_signup_page.FIRST_NAME)
    # user_signup_page.fill_signup_last_name(user_signup_page.LAST_NAME)
    # user_signup_page.fill_company_name(user_signup_page.COMPANY_NAME)
    # user_signup_page.fill_domain_name(user_signup_page.DOMAIN_NAME)
    # user_signup_page.fill_company_phone(user_signup_page.PHONE)
    # user_signup_page.fill_company_email(user_signup_page.INVALID_FORMAT_USERNAME)
    # user_signup_page.click_on_submit_button()
    user_signup_page.user_signup(user_signup_page.FIRST_NAME, user_signup_page.LAST_NAME, user_signup_page.COMPANY_NAME,
                                 user_signup_page.DOMAIN_NAME, user_signup_page.INVALID_FORMAT_USERNAME,
                                 user_signup_page.PHONE)
    assert (user_signup_page.get_email_invalid_format_validation_message() ==
            user_signup_page.INVALID_EMAIL_FORMAT_VALIDATION_MESSAGE)
    log.info(f"{test_signup_with_invalid_email_format_TC_14} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_terms_accept_checkbox_TC_17(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_terms_accept_checkbox_TC_17} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.click_on_checkbox()
    assert user_signup_page.check_checkbox_selected()
    log.info(f"{test_signup_terms_accept_checkbox_TC_17} >>>>>>>>>>>>>>>>> finished")
