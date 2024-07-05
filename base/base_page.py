import json
import time
import xml.etree.ElementTree as ET
from traceback import print_stack

import psycopg2
from selenium.webdriver.support.select import Select

from base.selenium_driver import SeleniumDriver
from utilities.util import Util

from zipfile import ZipFile
from contextlib import closing


class BasePage(SeleniumDriver):

    """
    *****
    
    Put in this class common methods which can be used in all pages in project.
    
    *****
    """

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_server_title(self, title_to_verify):
        """
        Verify the page Title
        :param title_to_verify: Title on the page which needs to be verified
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def find_element_by_selector_and_text(self, selector, text):
        """
        Find the page element by selector and text
        :param selector: The selectors list
        :param text: The unique text by which the method can find exact element
        :return webElement: Search element
        """
        try:
            for domElement in selector:
                if domElement.text == text:
                    return domElement
        except:
            self.log.error("Failed to get element in the page")
            print_stack()
            return None

    def find_element_by_selector_and_text_contains(self, selector, text):
        """
        Find the page element by selector and text
        :param selector: The selectors list
        :param text: The unique text by which the method can find exact element
        :return webElement: Search element
        """
        try:
            for dom_element in selector:
                if text in dom_element.text:
                    return dom_element
        except:
            self.log.error("Failed to get element in the page")
            print_stack()
            return None

    def select_item_from_drop_down_list(self, element, option, value):
        """
        Use the method to chose item from select list
        The method uses Selenium native select class
        :param element: WebElement
        :param option: Select option, Example - index, value, text
        :param value: The appropriate option value
        :return:
        """
        try:
            select = Select(element)
            if option == "index":
                select.select_by_index(value)
            if option == "value":
                select.select_by_value(value)
            if option == "text":
                select.select_by_visible_text(value)
        except:
            self.log.error("Cant select from List")
            print_stack()

    def select_item_from_drop_down_list_using_loop(self, list_selector, list_item_selector, value):
        """
        Use the method to chose item from select list
        The method uses Selenium native select class
        :param list_selector: Drop down list selector
        :param list_item_selector: Drop down list items selector
        :param value: The appropriate option value
        :return:
        """
        try:
            el = self.get_element(list_selector)
            el.click()
            time.sleep(3)
            items = self.get_element_list(list_item_selector)
            for item in items:
                if item.text == value:
                    item.click()
                    break
        except:
            self.log.error("Cant select from List")
            print_stack()

    def browser_logger(self, method_name):
        """
        The method gets the browser log from btowser console
        :param method_name: As a param set the method name to write it in log file
        :return:
        """
        log_entries = self.driver.get_log("browser")
        logFile = open("browserConsoleLog.log", "a")
        for log_entry in log_entries:
            logFile.write(f"\n {method_name}<<<<<<< " +
                          "\n Log Level = " + log_entry['level'] +
                          "\n Log TimeStamp = " + str(log_entry["timestamp"]) +
                          "\n Log Message = " + log_entry['message'] +
                          "\n >>>>>>>")
        logFile.close()

