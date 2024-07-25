import logging
import time

from pytest import mark
import utilities.custom_logger as cl
from pages.login_page.login_page import LoginPage
from utilities import get_data_from_email


# @pytest.fixture(scope='function')
# def change_password_fixture():
#     user_login_page = LoginPage(driver)
#     user_login_page.change_password(user_login_page.VALID_USERNAME2, user_login_page.DOMAIN_NAME_2,
#                                     user_login_page.VALID_PASSWORD2, user_login_page.VALID_PASSWORD2)


@mark.regression
@mark.smoke
def test_login_button_TC_1(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_button_TC_1} >>>>>>>>>>>>>>>>> started")
    assert user_login_page.verify_login_button()
    log.info(f"{test_login_button_TC_1} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_navigation_to_domain_page_TC_2(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_navigation_to_domain_page_TC_2} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    assert user_login_page.verify_domain_page() == user_login_page.LOGIN_PAGE_TEXT
    log.info(f"{test_navigation_to_domain_page_TC_2} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_page_items_TC_3(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_page_items_TC_3} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    assert user_login_page.check_domain_name_field_presence()
    assert user_login_page.check_submit_button_presence()
    assert user_login_page.check_signup_link_text_button_presence()
    log.info(f"{test_login_page_items_TC_3} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_navigation_to_signup_page_TC_4(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_navigation_to_signup_page_TC_4} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    assert user_login_page.verify_navigation_to_signup_page()
    log.info(f"{test_navigation_to_signup_page_TC_4} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_without_inputting_domain_TC_5(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_without_inputting_domain_TC_5} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.click_on_submit_button()
    assert user_login_page.validate_domain_field_validation_message()
    log.info(f"{test_login_without_inputting_domain_TC_5} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_domain_name_input_TC_6(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_domain_name_input_TC_6} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.enter_domain_name(user_login_page.DOMAIN_NAME)
    assert user_login_page.get_domain_name() == user_login_page.DOMAIN_NAME
    log.info(f"{test_domain_name_input_TC_6} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_domain_name_is_not_exist_TC_7(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_domain_name_is_not_exist_TC_7} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.WRONG_DOMAIN_NAME)
    assert user_login_page.get_domain_name_error_message() == user_login_page.DOMAIN_NAME_ERROR_MESSAGE
    log.info(f"{test_login_domain_name_is_not_exist_TC_7} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_via_invalid_domain_name_TC_8(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_via_invalid_domain_name_TC_8} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.INVALID_DOMAIN_NAME)
    assert user_login_page.verify_domain_page() == user_login_page.LOGIN_PAGE_TEXT
    assert user_login_page.get_domain_name_error_message() == user_login_page.DOMAIN_NAME_ERROR_MESSAGE
    log.info(f"{test_login_via_invalid_domain_name_TC_8} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_domain_name_error_message_TC_9(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_domain_name_error_message_TC_9} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.WRONG_DOMAIN_NAME)
    assert user_login_page.get_domain_name_error_message() == user_login_page.DOMAIN_NAME_ERROR_MESSAGE
    log.info(f"{test_login_domain_name_error_message_TC_9} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_navigation_to_login_page_TC_10(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_navigation_to_login_page_TC_10} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    assert user_login_page.verify_email_address_field()
    log.info(f"{test_navigation_to_login_page_TC_10} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_page_items_TC_11(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_page_items_TC_11} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    assert user_login_page.verify_email_address_field()
    assert user_login_page.verify_password_field()
    assert user_login_page.validate_remember_me_checkbox_displays()
    assert user_login_page.validate_forget_password_button()
    log.info(f"{test_login_page_items_TC_11} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_navigate_to_forgot_password_page_TC_12(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_navigate_to_forgot_password_page_TC_12} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.navigate_to_forget_password_page()
    assert user_login_page.validate_forgot_password_page()
    log.info(f"{test_navigate_to_forgot_password_page_TC_12} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_user_successfully_change_password_TC_13(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_user_successfully_change_password_TC_13} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.navigate_to_forget_password_page()
    user_login_page.fill_forgot_password_email_field(user_login_page.VALID_USERNAME2)
    user_login_page.click_on_reset_password_button()
    time.sleep(5)
    link = get_data_from_email.get_latest_email(user_login_page.user, user_login_page.password, user_login_page.imap_url)
    time.sleep(5)
    user_login_page.navigate_to_new_url(link)
    assert user_login_page.get_reset_password_page_text() == user_login_page.RESET_PASSWORD_TEXT
    user_login_page.submit_reset_password(user_login_page.NEW_PASSWORD, user_login_page.NEW_PASSWORD)
    assert (user_login_page.get_operation_successful_validation_message() ==
            user_login_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    assert user_login_page.verify_domain_page() == user_login_page.LOGIN_PAGE_TEXT
    user_login_page.change_password(user_login_page.VALID_USERNAME2, user_login_page.DOMAIN_NAME_2,
                                    user_login_page.VALID_PASSWORD2, user_login_page.VALID_PASSWORD2)
    log.info(f"{test_user_successfully_change_password_TC_13} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_user_successfully_login_with_new_password_TC_14(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_user_successfully_login_with_new_password_TC_14} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.navigate_to_forget_password_page()
    user_login_page.fill_forgot_password_email_field(user_login_page.VALID_USERNAME2)
    user_login_page.click_on_reset_password_button()
    time.sleep(10)
    link = get_data_from_email.get_latest_email(user_login_page.user, user_login_page.password, user_login_page.imap_url)
    time.sleep(8)
    user_login_page.navigate_to_new_url(link)
    user_login_page.submit_reset_password(user_login_page.NEW_PASSWORD, user_login_page.NEW_PASSWORD)
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.NEW_PASSWORD)
    assert (user_login_page.get_operation_successful_validation_message() ==
            user_login_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    time.sleep(10)
    otp = get_data_from_email.get_latest_otp(user_login_page.user, user_login_page.password, user_login_page.imap_url)
    user_login_page.fill_otp_field(otp)
    user_login_page.click_on_verify_button()
    time.sleep(5)
    assert user_login_page.URL_ADMIN_SUBDIRECTORY in driver.current_url
    user_login_page.change_password(user_login_page.VALID_USERNAME2, user_login_page.DOMAIN_NAME_2,
                                    user_login_page.VALID_PASSWORD2, user_login_page.VALID_PASSWORD2)
    time.sleep(2)
    log.info(f"{test_user_successfully_login_with_new_password_TC_14} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_via_old_password_returns_error_message_TC_15(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_via_old_password_returns_error_message_TC_15} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.navigate_to_forget_password_page()
    user_login_page.fill_forgot_password_email_field(user_login_page.VALID_USERNAME2)
    user_login_page.click_on_reset_password_button()
    time.sleep(5)
    link = get_data_from_email.get_latest_email(user_login_page.user, user_login_page.password, user_login_page.imap_url)
    time.sleep(5)
    user_login_page.navigate_to_new_url(link)
    user_login_page.submit_reset_password(user_login_page.NEW_PASSWORD, user_login_page.NEW_PASSWORD)
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    assert (user_login_page.get_invalid_credentials_error_message() ==
            user_login_page.INVALID_CREDENTIALS)
    user_login_page.change_password(user_login_page.VALID_USERNAME2, user_login_page.DOMAIN_NAME_2,
                                    user_login_page.VALID_PASSWORD2, user_login_page.VALID_PASSWORD2)
    log.info(f"{test_login_via_old_password_returns_error_message_TC_15} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_empty_fields_TC_17(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_empty_fields_TC_17} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.click_on_login_button()
    assert user_login_page.get_username_required_error_message() == user_login_page.USERNAME_REQUIRED_ERROR_MESSAGE
    assert user_login_page.get_password_required_error_message() == user_login_page.PASSWORD_REQUIRED_ERROR_MESSAGE
    log.info(f"{test_login_with_empty_fields_TC_17} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_empty_email_field_TC_18(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_empty_email_field_TC_18} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.accept_cookies()
    user_login_page.fill_login_password(user_login_page.VALID_PASSWORD)
    user_login_page.click_on_login_button()
    assert user_login_page.get_username_required_error_message() == user_login_page.USERNAME_REQUIRED_ERROR_MESSAGE
    log.info(f"{test_login_with_empty_email_field_TC_18} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_empty_password_field_TC_19(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_empty_password_field_TC_19} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.accept_cookies()
    user_login_page.fill_login_email(user_login_page.VALID_USERNAME)
    user_login_page.click_on_login_button()
    assert user_login_page.get_password_required_error_message() == user_login_page.PASSWORD_REQUIRED_ERROR_MESSAGE
    log.info(f"{test_login_with_empty_password_field_TC_19} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_invalid_email_format_TC_20(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_invalid_email_format_TC_20} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.accept_cookies()
    user_login_page.fill_login_email(user_login_page.INVALID_FORMAT_USERNAME)
    user_login_page.click_on_login_button()
    assert (user_login_page.get_username_invalid_format_error_message() ==
            user_login_page.USERNAME_INVALID_FORMAT_ERROR_MESSAGE)
    log.info(f"{test_login_with_invalid_email_format_TC_20} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_invalid_email_and_valid_password_TC_21(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_invalid_email_and_valid_password_TC_21} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.accept_cookies()
    user_login_page.user_login(user_login_page.INVALID_USERNAME, user_login_page.VALID_PASSWORD)
    user_login_page.click_on_login_button()
    assert (user_login_page.get_invalid_credentials_error_message() ==
            user_login_page.INVALID_CREDENTIALS)
    log.info(f"{test_login_with_invalid_email_and_valid_password_TC_21} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_valid_email_and_invalid_password_TC_22(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_valid_email_and_invalid_password_TC_22} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.accept_cookies()
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.INVALID_PASSWORD)
    user_login_page.click_on_login_button()
    assert (user_login_page.get_invalid_credentials_error_message() ==
            user_login_page.INVALID_CREDENTIALS)
    log.info(f"{test_login_with_valid_email_and_invalid_password_TC_22} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_with_invalid_email_and_invalid_password_TC_23(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_with_invalid_email_and_invalid_password_TC_23} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.accept_cookies()
    user_login_page.user_login(user_login_page.INVALID_USERNAME, user_login_page.INVALID_PASSWORD)
    user_login_page.click_on_login_button()
    assert (user_login_page.get_invalid_credentials_error_message() ==
            user_login_page.INVALID_CREDENTIALS)
    log.info(f"{test_login_with_invalid_email_and_invalid_password_TC_23} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_valid_login_TC_24(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_valid_login_TC_24} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.accept_cookies()
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    assert user_login_page.validate_welcome_message()
    log.info(f"{test_valid_login_TC_24} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_user_cannot_be_logged_out_after_clicking_system_back_button_TC_25(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_user_cannot_be_logged_out_after_clicking_system_back_button_TC_25} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME)
    user_login_page.accept_cookies()
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    user_login_page.navigate_back_and_forward()
    assert user_login_page.URL_ADMIN_SUBDIRECTORY in driver.current_url
    log.info(f"{test_user_cannot_be_logged_out_after_clicking_system_back_button_TC_25} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_system_back_button_TC_26(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_system_back_button_TC_26} >>>>>>>>>>>>>>>>> started")
    user_login_page.change_password(user_login_page.VALID_USERNAME2, user_login_page.DOMAIN_NAME_2,
                                    user_login_page.VALID_PASSWORD2, user_login_page.VALID_PASSWORD2)
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    time.sleep(5)
    otp = get_data_from_email.get_latest_otp(user_login_page.user, user_login_page.password, user_login_page.imap_url)
    user_login_page.fill_otp_field(otp)
    user_login_page.click_on_verify_button()
    user_login_page.click_on_later_button()
    time.sleep(2)
    user_login_page.click_on_logout_button()
    driver.back()
    assert user_login_page.URL_COMPANY_SUBDIRECTORY in driver.current_url
    log.info(f"{test_login_system_back_button_TC_26} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_login_otp_is_enable_TC_27(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_login_otp_is_enable_TC_27} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    time.sleep(5)
    assert user_login_page.URL_VERIFY_OTP_SUBDIRECTORY in driver.current_url
    assert user_login_page.validate_verify_otp_text()
    log.info(f"{test_login_otp_is_enable_TC_27} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_user_cannot_proceed_without_inputting_the_OTP_code_TC_28(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_that_user_cannot_proceed_without_inputting_the_OTP_code_TC_28} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.accept_cookies()
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    time.sleep(3)
    user_login_page.click_on_verify_button()
    assert (user_login_page.get_otp_required_validation_message() ==
            user_login_page.OTP_REQUIRED_VALIDATION_MESSAGE)
    log.info(f"{test_that_user_cannot_proceed_without_inputting_the_OTP_code_TC_28} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_user_cannot_proceed_with_invalid_OTP_code_TC_29(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_that_user_cannot_proceed_with_invalid_OTP_code_TC_29} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.accept_cookies()
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    user_login_page.fill_otp_field(user_login_page.INVALID_OTP)
    user_login_page.click_on_verify_button()
    assert (user_login_page.get_invalid_otp_error_message() ==
            user_login_page.INVALID_OTP_ERROR_MESSAGE)
    user_login_page.change_password(user_login_page.VALID_USERNAME2,
                                    user_login_page.DOMAIN_NAME_2,
                                    user_login_page.VALID_PASSWORD2,
                                    user_login_page.VALID_PASSWORD2,
                                    )
    log.info(f"{test_that_user_cannot_proceed_with_invalid_OTP_code_TC_29} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_user_cannot_attempt_wrong_OTP_more_than_7_times_TC_30(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_user_cannot_attempt_wrong_OTP_more_than_7_times_TC_30} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    time.sleep(3)
    user_login_page.fill_invalid_otp_code_multiple_times()
    assert (user_login_page.get_locked_account_validation_message() ==
            user_login_page.LOCKED_ACCOUNT_VALIDATION_MESSAGE)
    user_login_page.change_password(user_login_page.VALID_USERNAME2, user_login_page.DOMAIN_NAME_2,
                                    user_login_page.VALID_PASSWORD2, user_login_page.VALID_PASSWORD2)
    time.sleep(2)
    log.info(f"{test_user_cannot_attempt_wrong_OTP_more_than_7_times_TC_30} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_user_cannot_attempt_wrong_OTP_more_than_7_times_and_reset_password_TC_31(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_user_cannot_attempt_wrong_OTP_more_than_7_times_and_reset_password_TC_31} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    time.sleep(3)
    user_login_page.fill_invalid_otp_code_multiple_times()
    assert (user_login_page.get_locked_account_validation_message() ==
            user_login_page.LOCKED_ACCOUNT_VALIDATION_MESSAGE)
    time.sleep(10)
    link = get_data_from_email.get_latest_email(user_login_page.user, user_login_page.password, user_login_page.imap_url)
    user_login_page.navigate_to_new_url(link)
    user_login_page.submit_reset_password(user_login_page.VALID_PASSWORD2, user_login_page.VALID_PASSWORD2)
    assert (user_login_page.get_operation_successful_validation_message() ==
            user_login_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    log.info(
        f"{test_user_cannot_attempt_wrong_OTP_more_than_7_times_and_reset_password_TC_31} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_user_cannot_login_without_resecting_their_password_as_instructed_TC_32(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_user_cannot_login_without_resecting_their_password_as_instructed_TC_32} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    time.sleep(3)
    user_login_page.fill_invalid_otp_code_multiple_times()
    assert (user_login_page.get_locked_account_validation_message() ==
            user_login_page.LOCKED_ACCOUNT_VALIDATION_MESSAGE)
    user_login_page.navigate_to_new_url(user_login_page.TWIKKIE_LOGIN_PAGE)
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    user_login_page.accept_cookies()
    user_login_page.click_on_login_button()
    assert (user_login_page.get_locked_account_validation_message() ==
            user_login_page.LOCKED_ACCOUNT_VALIDATION_MESSAGE)
    user_login_page.change_password(user_login_page.VALID_USERNAME2, user_login_page.DOMAIN_NAME_2,
                                    user_login_page.VALID_PASSWORD2, user_login_page.VALID_PASSWORD2)
    time.sleep(3)
    log.info(
        f"{test_that_user_cannot_login_without_resecting_their_password_as_instructed_TC_32} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_user_successfully_resect_password_via_received_reset_password_link_sent_to_email_TC_33(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_user_successfully_resect_password_via_received_reset_password_link_sent_to_email_TC_33} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_2)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    user_login_page.accept_cookies()
    time.sleep(3)
    user_login_page.fill_invalid_otp_code_multiple_times()
    assert (user_login_page.get_locked_account_validation_message() ==
            user_login_page.LOCKED_ACCOUNT_VALIDATION_MESSAGE)
    time.sleep(5)
    link = get_data_from_email.get_latest_email(user_login_page.user, user_login_page.password, user_login_page.imap_url)
    user_login_page.navigate_to_new_url(link)
    user_login_page.submit_reset_password(user_login_page.VALID_PASSWORD2, user_login_page.VALID_PASSWORD2)
    assert (user_login_page.get_operation_successful_validation_message() ==
            user_login_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    log.info(
        f"{test_user_successfully_resect_password_via_received_reset_password_link_sent_to_email_TC_33} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_user_login_with_valid_OTP_code_TC_34(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_that_user_login_with_valid_OTP_code_TC_34} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.accept_cookies()
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    time.sleep(10)
    otp = get_data_from_email.get_latest_otp(user_login_page.user, user_login_page.password, user_login_page.imap_url)
    user_login_page.fill_otp_field(otp)
    user_login_page.click_on_verify_button()
    time.sleep(5)
    assert user_login_page.URL_ADMIN_SUBDIRECTORY in driver.current_url
    log.info(f"{test_that_user_login_with_valid_OTP_code_TC_34} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_user_can_successfully_logout_TC_35(driver):
    log = cl.custom_logger(logging.DEBUG)
    user_login_page = LoginPage(driver)
    log.info(f"{test_that_user_can_successfully_logout_TC_35} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.accept_cookies()
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    time.sleep(10)
    otp = get_data_from_email.get_latest_otp(user_login_page.user, user_login_page.password, user_login_page.imap_url)
    user_login_page.fill_otp_field(otp)
    user_login_page.click_on_verify_button()
    time.sleep(5)
    assert user_login_page.URL_ADMIN_SUBDIRECTORY in driver.current_url
    user_login_page.click_on_later_button()
    user_login_page.click_on_logout_button()
    assert user_login_page.URL_LOGIN_SUBDIRECTORY in driver.current_url
    log.info(f"{test_that_user_can_successfully_logout_TC_35} >>>>>>>>>>>>>>>>> finished")


