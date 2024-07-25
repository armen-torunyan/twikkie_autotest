import logging

from pytest import mark
from selenium.webdriver.common.by import By

import utilities.custom_logger as cl
from utilities.util import Util
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
    user_signup_page.accept_cookies()
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
    random_domain_name = Util.rand_str()
    random_company_name = Util.rand_str()
    log.info(f"{test_signup_with_already_registered_email_TC_9} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.user_signup(user_signup_page.FIRST_NAME,
                                 user_signup_page.LAST_NAME,
                                 random_company_name,
                                 random_domain_name,
                                 user_signup_page.REGISTERED_EMAIL,
                                 user_signup_page.PHONE)
    assert (user_signup_page.get_signup_registered_email_error_message() ==
            user_signup_page.REGISTERED_EMAIL_ERROR_MESSAGE)
    log.info(f"{test_signup_with_already_registered_email_TC_9} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_with_same_phone_number_TC_10(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    random_email = Util.random_email()
    random_company_name = Util.rand_str()
    random_domain_name = Util.rand_str()
    log.info(f"{test_signup_with_same_phone_number_TC_10} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.user_signup(user_signup_page.FIRST_NAME,
                                 user_signup_page.LAST_NAME,
                                 random_company_name,
                                 random_domain_name,
                                 random_email,
                                 user_signup_page.PHONE)
    assert (user_signup_page.get_operation_successful_validation_message() ==
            user_signup_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    log.info(f"{test_signup_with_same_phone_number_TC_10} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_with_already_taken_company_name_TC_11(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    random_domain_name = Util.rand_str()
    log.info(f"{test_signup_with_already_taken_company_name_TC_11} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.user_signup(user_signup_page.FIRST_NAME,
                                 user_signup_page.LAST_NAME,
                                 user_signup_page.ALREADY_TAKEN_COMPANY_NAME,
                                 random_domain_name,
                                 user_signup_page.UNREGISTERED_EMAIL,
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
    user_signup_page.accept_cookies()
    user_signup_page.fill_company_phone(user_signup_page.INVALID_PHONE_NUMBER)
    user_signup_page.click_on_submit_button()
    assert (user_signup_page.get_company_phone_field_validation_message_with_invalid_format() ==
            user_signup_page.PHONE_INVALID_FORMAT_VALIDATION_MESSAGE)
    log.info(f"{test_signup_phone_field_with_invalid_format_TC_12} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_with_invalid_email_format_TC_14(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_with_invalid_email_format_TC_14} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.user_signup(user_signup_page.FIRST_NAME,
                                 user_signup_page.LAST_NAME,
                                 user_signup_page.COMPANY_NAME,
                                 user_signup_page.DOMAIN_NAME,
                                 user_signup_page.INVALID_FORMAT_USERNAME,
                                 user_signup_page.PHONE)
    assert (user_signup_page.get_email_invalid_format_validation_message() ==
            user_signup_page.INVALID_EMAIL_FORMAT_VALIDATION_MESSAGE)
    log.info(f"{test_signup_with_invalid_email_format_TC_14} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_dropdown_countries_TC_15(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_dropdown_countries_TC_15} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    assert user_signup_page.verify_dropdown_list_countries()
    log.info(f"{test_signup_dropdown_countries_TC_15} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_country_selection_from_dropdown_TC_16(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_country_selection_from_dropdown_TC_16} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.choose_country_from_dropdown(user_signup_page.COUNTRY_NAME)
    assert user_signup_page.COUNTRY_NAME in user_signup_page.get_selected_country()
    log.info(f"{test_signup_country_selection_from_dropdown_TC_16} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_terms_accept_checkbox_TC_17(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    log.info(f"{test_signup_terms_accept_checkbox_TC_17} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.click_on_checkbox()
    assert user_signup_page.check_checkbox_selected()
    log.info(f"{test_signup_terms_accept_checkbox_TC_17} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_signup_with_fill_in_all_required_fields_TC_18(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    random_email = Util.random_email()
    random_company_name = Util.rand_str()
    random_domain_name = Util.rand_str()
    log.info(f"{test_signup_with_fill_in_all_required_fields_TC_18} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.user_signup(user_signup_page.FIRST_NAME,
                                 user_signup_page.LAST_NAME,
                                 random_company_name,
                                 random_domain_name,
                                 random_email,
                                 user_signup_page.PHONE)
    assert (user_signup_page.get_operation_successful_validation_message() ==
            user_signup_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    log.info(f"{test_signup_with_fill_in_all_required_fields_TC_18} >>>>>>>>>>>>> >>>> finished")


@mark.regression
@mark.smoke
def test_signup_confirmation_message_TC_19(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_signup_page = SignupPage(driver)
    random_email = Util.random_email()
    random_company_name = Util.rand_str()
    random_domain_name = Util.rand_str()
    log.info(f"{test_signup_confirmation_message_TC_19} >>>>>>>>>>>>>>>>> started")
    user_signup_page.click_on_signup_tab()
    user_signup_page.accept_cookies()
    user_signup_page.user_signup(user_signup_page.FIRST_NAME,
                                 user_signup_page.LAST_NAME,
                                 random_company_name,
                                 random_domain_name,
                                 random_email,
                                 user_signup_page.PHONE)
    assert (user_signup_page.get_signup_confirmation_message() ==
            user_signup_page.SIGNUP_CONFIRMATION_MESSAGE)
    log.info(f"{test_signup_confirmation_message_TC_19} >>>>>>>>>>>>> >>>> finished")





































# @mark.regression
# @mark.smoke
# def test_signup_email_confirmation_message_TC_20(driver):
#     log = cl.custom_logger(logging.DEBUG)
#     user_signup_page = SignupPage(driver)
#     random_email = Util.random_email()
#     random_company_name = Util.rand_str()
#     random_domain_name = Util.rand_str()
#     log.info(f"{test_signup_email_confirmation_message_TC_20} >>>>>>>>>>>>>>>>> started")
#     user_signup_page.click_on_signup_tab()
#     user_signup_page.accept_cookies()
#     user_signup_page.user_signup(user_signup_page.FIRST_NAME,
#                                  user_signup_page.LAST_NAME,
#                                  random_company_name,
#                                  random_domain_name,
#                                  random_email,
#                                  user_signup_page.PHONE)
#     assert (user_signup_page.get_signup_confirmation_message() ==
#             user_signup_page.SIGNUP_CONFIRMATION_MESSAGE)
#     log.info(f"{test_signup_email_confirmation_message_TC_20} >>>>>>>>>>>>> >>>> finished")


# @mark.regression
# @mark.smoke
# def test_delete_account(driver):
#     log = cl.custom_logger(logging.DEBUG)
#     user_signup_page = SignupPage(driver)
#     user_login_page = LoginPage(driver)
#     log.info(f"{test_delete_account} >>>>>>>>>>>>>>>>> started")
#     user_login_page.navigate_to_domain_page()
#     user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_3)
#     user_login_page.user_login(user_signup_page.VALID_USERNAME3, user_signup_page.VALID_PASSWORD1)
#     time.sleep(10)
#     otp = get_data_from_email.get_latest_otp(user_signup_page.user, user_signup_page.password, user_signup_page.imap_url)
#     time.sleep(10)
#     user_login_page.fill_otp_field(otp)
#     user_login_page.click_on_verify_button()
#     user_login_page.click_on_later_button()
#     time.sleep(1)
#     user_signup_page.account_deletion()
#     time.sleep(100)
#     log.info(f"{test_delete_account} >>>>>>>>>>>>> >>>> finished")
