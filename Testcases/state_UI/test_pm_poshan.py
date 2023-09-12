import logging
import os
import time
import sys

sys.path.append(os.getcwd())
from Page_of_objects.CqubeUi.homepage import Homepage
from Page_of_objects.CqubeUi.pm_poshan import pm_poshan
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestDashboard:
    homepage = None
    pm_poshan = None
    driver = None
    GetData = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.implicitly_wait(30)
        cls.homepage = Homepage(cls.driver)
        cls.pm_poshan = pm_poshan(cls.driver)
        cls.homepage.open_cqube_application()
        cls.homepage.open_login_page()
        cls.homepage.test_click_on_state_button()
        cls.pm_poshan.click_on_access_pm_poshan_menu()
        cls.logger = CustomLogger.setup_logger('Dashboard', ReadConfig.get_logs_directory() + "/Dashboard.log",
                                               level=logging.DEBUG)

    '''This Test script checking the navigation is happening or not '''

    def test_check_navigation_to_pm_poshan(self):
        self.logger.info("*************** Tc_cQube_001 Testing Started *****************")
        time.sleep(6)
        if 'pmposhan' in self.driver.current_url and 'PM POSHAN' in self.driver.page_source:
            self.logger.info("******************* pm poshan Dashboard is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** pm poshan Dashboard Button is not Working ******************")
            assert False
        self.pm_poshan.click_menu()
        self.logger.info("*************** Tc_cQube_001 Testing Ended *****************")

    '''Test Scripts to Click on the progress status Tab '''

    def test_click_on_the_progress_status_tab_button(self):
        self.logger.info("*************** Tc_cQube_002 Testing started *****************")
        time.sleep(5)
        self.pm_poshan.click_progress_status_tab()
        time.sleep(5)
        pm_poshan = self.pm_poshan.get_progress_status_tab()
        if "true" == pm_poshan:
            self.logger.info("*********** Tab is selecting ***************")
            assert True
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube_002 Testing ended *****************")

    '''This Test script checking the A- Button '''

    def test_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_003 Testing Started *****************")
        res = self.pm_poshan.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_003 Testing completed *****************")

    '''This Test script checking the A Plus Button '''

    def test_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_004 Testing Started *****************")
        res = self.pm_poshan.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_004 Testing completed *****************")

    '''This Test script checking Default A  Button'''

    def test_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_005 Testing Started *****************")
        res = self.pm_poshan.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_005 Testing completed *****************")

    '''Test Script to check the options in the dropdown is selecting or not '''


    def test_legend(self):
        self.logger.info("*************** Tc_cQube_006 Testing Started *****************")
        time.sleep(8)
        self.pm_poshan.click_dropdown()
        time.sleep(2)
        options = self.pm_poshan.get_metrics_dropdown_values()
        for dropdown in range(len(options)):
            opts = self.pm_poshan.get_each_dropdown_value_id(dropdown)
            opt_text = opts.text
            opts.click()
            time.sleep(3)
            legend = self.pm_poshan.get_legend_text()
            if opt_text in legend:
                print("Metric in  dropdown and legend is same")
                self.logger.info("*********** Metric in  dropdown and legend is same **************")
            else:
                self.logger.error("*********** Metric in  dropdown and legend is not same **************")
                assert False
            self.pm_poshan.click_dropdown()
            time.sleep(2)
        self.logger.info("*************** Tc_cQube_006 Testing Started *****************")


    '''Test Script to Validate the total districts big number Card'''

    def test_validate_Total_Districts_metrics(self):
        self.logger.info("*************** Tc_cQube_007 Testing started *****************")
        time.sleep(5)
        self.pm_poshan.click_progress_status_tab()
        time.sleep(5)
        card_value = self.pm_poshan.get_total_districts_value()
        card_title = self.pm_poshan.get_total_districts_label()
        value = "0"
        if card_title is not None:
            self.logger.info("*********** Total Content card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total Content card values are Missing ************")
            assert False
        if str(card_value) >= value and card_value is not None:
            self.logger.info("*********** Total Content card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total Content card values are Missing ************")
            assert False

    '''Test Script to Validate the total schools big number Card'''

    def test_validate_Total_schools_metrics(self):
        self.logger.info("***************Tc_cQube_008 Testing started *****************")
        time.sleep(5)
        self.pm_poshan.click_progress_status_tab()
        time.sleep(5)
        card_value = self.pm_poshan.get_total_schools_value()
        card_title = self.pm_poshan.get_total_schools_label()
        value = "0"
        if card_title is not None:
            self.logger.info("*********** Total Content card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total Content card values are Missing ************")
            assert False
        if str(card_value) >= value and card_value is not None:
            self.logger.info("*********** Total Content card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total Content card values are Missing ************")
            assert False

    '''Test Script to Validate the total meals served big number Card'''

    def test_validate_Total_meals_served_metrics(self):
        self.logger.info("***************Tc_cQube_009 Testing started *****************")
        time.sleep(5)
        self.pm_poshan.click_progress_status_tab()
        time.sleep(5)
        card_value = self.pm_poshan.get_total_meal_served_value()
        card_title = self.pm_poshan.get_Total_meals_served_label()
        value = "0"
        if card_title is not None:
            self.logger.info("*********** Total Content card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total Content card values are Missing ************")
            assert False
        if str(card_value) >= value and card_value is not None:
            self.logger.info("*********** Total Content card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total Content card values are Missing ************")
            assert False

    '''This Test script checking full screen button is working or not'''

    def test_full_screen(self):
        self.logger.info("*************** Tc_cQube_010 Testing started *****************")
        self.pm_poshan.click_fullscreen_button()
        time.sleep(3)
        is_full_screen = self.driver.execute_script(
            "return window.screen.width == screen.width && window.screen.height == screen.height;")
        print(is_full_screen)
        assert is_full_screen
        self.logger.info("*************** Tc_cQube_010 Testing ended *****************")

    '''This Test script checking download button is working or not'''

    def test_download_button(self):
        self.logger.info("*************** Tc_cQube_011 Testing started *****************")
        p = pm_poshan(self)
        self.pm_poshan.click_download_button()
        time.sleep(5)
        self.file_name = p.get_download_dir() + "/Progress Status.csv"
        print(self.file_name)
        if os.path.isfile(self.file_name):
            print("file is downloaded")
            os.remove(self.file_name)
            assert True
        else:
            print("file is not downloaded")
            assert False

    '''This Test script checking logout button is working or not'''

    def test_block_click_logout_btn(self):
        self.logger.info("*************** Tc_cQube_012 Testing ended *****************")
        self.pm_poshan.click_progress_status_tab()
        time.sleep(2)
        self.pm_poshan.test_click_logout_button()
        time.sleep(3)
        if 'login' in self.driver.current_url:
            self.logger.info("*******************  pm poshan page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** pm poshan Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")
