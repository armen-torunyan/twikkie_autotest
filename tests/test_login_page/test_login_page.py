import logging
import time

import pytest
from pytest import mark
import utilities.custom_logger as cl
from pages.login_page.login_page import LoginPage


@mark.regression
@mark.smoke
def test_login_button(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_button} >>>>>>>>>>>>>>>>> started")
    assert user_login_page.verify_login_button()
    log.info(f"{test_login_button} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_navigation_to_domain_page(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_navigation_to_domain_page} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    assert user_login_page.verify_domain_page() == user_login_page.LOGIN_PAGE_TEXT
    log.info(f"{test_navigation_to_domain_page} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_page_items(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_page_items} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    assert user_login_page.check_domain_name_field_presence()
    assert user_login_page.check_submit_button_presence()
    assert user_login_page.check_signup_link_text_button_presence()
    log.info(f"{test_login_page_items} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_navigation_to_signup_page(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_navigation_to_signup_page} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    assert user_login_page.verify_navigation_to_signup_page()
    log.info(f"{test_navigation_to_signup_page} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_domain_name_input(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_navigation_to_signup_page} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.enter_domain_name(user_login_page.DOMAIN_NAME)
    assert user_login_page.get_domain_name() == user_login_page.DOMAIN_NAME
    log.info(f"{test_navigation_to_signup_page} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_without_inputting_domain(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_without_inputting_domain} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.click_on_submit_button()
    assert user_login_page.validate_domain_field_validation_message()
    log.info(f"{test_login_without_inputting_domain} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_via_wrong_domain(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_via_wrong_domain} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.WRONG_DOMAIN_NAME)
    assert user_login_page.get_wrong_domain_error_message() == user_login_page.WRONG_DOMAIN_NAME_ERROR_MESSAGE
    log.info(f"{test_login_via_wrong_domain} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_navigation_to_login_page(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_navigation_to_login_page} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    assert user_login_page.verify_email_address_field()
    log.info(f"{test_navigation_to_login_page} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_page_items(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_page_items} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    assert user_login_page.verify_email_address_field()
    assert user_login_page.verify_password_field()
    assert user_login_page.validate_remember_me_checkbox_displays()
    assert user_login_page.validate_forget_password_button()
    log.info(f"{test_login_page_items} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_navigate_to_forgot_password_page(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_navigate_to_forgot_password_page} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.navigate_to_forget_password_page()
    assert user_login_page.validate_forgot_password_page()
    log.info(f"{test_navigate_to_forgot_password_page} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_empty_fields_TC_16(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_empty_fields_TC_16} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.click_on_login_button()
    assert user_login_page.get_username_required_error_message() == user_login_page.USERNAME_REQUIRED_ERROR_MESSAGE
    assert user_login_page.get_password_required_error_message() == user_login_page.PASSWORD_REQUIRED_ERROR_MESSAGE
    log.info(f"{test_login_with_empty_fields_TC_16} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_empty_email_field_TC_17(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_empty_email_field_TC_17} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.fill_login_password(user_login_page.VALID_PASSWORD)
    user_login_page.click_on_login_button()
    assert user_login_page.get_username_required_error_message() == user_login_page.USERNAME_REQUIRED_ERROR_MESSAGE
    log.info(f"{test_login_with_empty_email_field_TC_17} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_empty_password_field_TC_18(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_empty_password_field_TC_18} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.fill_login_email(user_login_page.VALID_USERNAME)
    user_login_page.click_on_login_button()
    assert user_login_page.get_password_required_error_message() == user_login_page.PASSWORD_REQUIRED_ERROR_MESSAGE
    log.info(f"{test_login_with_empty_password_field_TC_18} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_invalid_email_format_TC_19(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_invalid_email_format_TC_19} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.fill_login_email(user_login_page.INVALID_FORMAT_USERNAME)
    user_login_page.click_on_login_button()
    assert (user_login_page.get_username_invalid_format_error_message() ==
            user_login_page.USERNAME_INVALID_FORMAT_ERROR_MESSAGE)
    log.info(f"{test_login_with_invalid_email_format_TC_19} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_invalid_email_and_valid_password_TC_20(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_invalid_email_and_valid_password_TC_20} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.INVALID_FORMAT_USERNAME, user_login_page.VALID_PASSWORD)
    user_login_page.click_on_login_button()
    assert (user_login_page.get_username_invalid_format_error_message() ==
            user_login_page.USERNAME_INVALID_FORMAT_ERROR_MESSAGE)
    log.info(f"{test_login_with_invalid_email_and_valid_password_TC_20} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_valid_email_and_invalid_password_TC_21(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_valid_email_and_invalid_password_TC_21} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.INVALID_PASSWORD)
    user_login_page.click_on_login_button()
    assert user_login_page.validate_invalid_password_error_message
    log.info(f"{test_login_with_valid_email_and_invalid_password_TC_21} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_invalid_email_and_invalid_password_TC_22(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_invalid_email_and_invalid_password_TC_22} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.INVALID_USERNAME, user_login_page.INVALID_PASSWORD)
    user_login_page.click_on_login_button()
    assert user_login_page.INVALID_EMAIL_ADDRESS_ERROR_MESSAGE
    log.info(f"{test_login_with_invalid_email_and_invalid_password_TC_22} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_valid_login_TC_23(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_valid_login_TC_23} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    assert user_login_page.validate_welcome_message()
    log.info(f"{test_valid_login_TC_23} >>>>>>>>>>>>>>>>> finished")