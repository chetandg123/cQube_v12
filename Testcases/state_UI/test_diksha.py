import logging
import os
import time
import re

from numpy.distutils.system_info import p
from selenium.webdriver.common.alert import Alert
from Page_of_objects.CqubeUi.diksha import Diksha
from Page_of_objects.CqubeUi.homepage import Homepage
from Page_of_objects.CqubeUi.summary_statistics import Summarystatistics
from Page_of_objects.CqubeUi.teacher_attendance import Teacherattendance
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestDashboard:
    homepage = None
    summarystatistics = None
    teacherattendance = None
    diksha = None
    driver = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.implicitly_wait(50)
        cls.homepage = Homepage(cls.driver)
        cls.summarystatistics = Summarystatistics(cls.driver)
        cls.teacherattendance = Teacherattendance(cls.driver)
        cls.diksha = Diksha(cls.driver)
        cls.homepage.open_cqube_application()
        cls.homepage.open_login_page()
        cls.summarystatistics.test_click_on_state_button()
        time.sleep(8)
        cls.diksha.test_click_on_diksha_menu()
        cls.logger = CustomLogger.setup_logger('diksha', ReadConfig.get_logs_directory() +
                                               "/diksha.log", level=logging.DEBUG)

    """Check whether diksha page is displaying or not"""

    def test_diksha_page(self):
        self.logger.info("*************** Tc_cQube_diksha_001 Testing started *****************")
        time.sleep(8)
        # self.diksha.test_click_on_diksha_menu()
        if "DIKSHA- ETB and eContent" in self.driver.page_source:
            print("DIKSHA- ETB and eContent is displaying")
            self.logger.info("*********** Diksha page is displaying ****************")
        else:
            print("DIKSHA- ETB and eContent page is not displaying")
            self.logger.error("*********** Diksha page is not displaying ****************")
        self.logger.info("*************** Tc_cQube_diksha_001 Testing ended *****************")

    # etb_coverage_status
    """Check whether etb_coverage_status tab is opening or not"""

    def test_click_on_the_etb_coverage_status_tab_button(self):
        self.logger.info("*************** Tc_cQube_diksha_002 Testing started *****************")
        time.sleep(8)
        etb_coverage_status = self.diksha.click_ETB_Coverage_Status()
        time.sleep(6)
        if "true" == etb_coverage_status:
            print("ETB Coverage Status tab is opening")
            self.logger.info("*********** etb_coverage_status_tab is selecting ***************")
        else:
            self.logger.error("*********** etb_coverage_status_tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_002 Testing ended *****************")

    """Check whether home button is working or not"""

    def test_home_button(self):
        self.logger.info("*************** Tc_cQube_diksha_003 Testing Started *****************")
        time.sleep(8)
        self.homepage.test_click_on_home_button()
        time.sleep(6)
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_003 Testing ended *****************")

    """Check whether font size decrease button is working or not"""

    def test_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_diksha_004 Testing started *****************")
        time.sleep(8)
        res = self.homepage.test_click_on_a_minus_button()
        time.sleep(6)
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
            print("A- button is clicked")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            print("A- button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_004 Testing ended *****************")

    """Check whether font size increase button is working or not"""

    def test_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_diksha_005 Testing started *****************")
        time.sleep(8)
        res = self.homepage.test_click_on_a_plus_button()
        time.sleep(6)
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A+ button is clicked and working as expected")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A+ button is clicked and not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_005 Testing Ended *****************")

    """Check whether font size default button is working or not"""

    def test_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_diksha_006 Testing started *****************")
        time.sleep(8)
        res = self.homepage.test_click_on_a_plus_button()
        time.sleep(6)
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
            print("A button is clicked and its working ")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            print("A button is clicked and it is not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_006 Testing Ended *****************")

    """Check whether logout button is working or not"""

    def test_logout(self):
        self.logger.info("*************** Tc_cQube_diksha_007 Testing Started *****************")
        time.sleep(8)
        self.homepage.test_click_logout_button()
        time.sleep(6)
        if "login" in self.driver.current_url:
            print("Logout button is working")
            self.logger.info("*********** Logout button is working *********")
        else:
            self.logger.error("*********** Logout button is not working *********")
            print("Logout button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_007 Testing ended *****************")

    """Check whether key metric are displaying or not"""

    def test_validate_total_etb_and_quality_metrics(self):
        self.logger.info("*************** Tc_cQube_diksha_008 Testing started *****************")
        time.sleep(6)
        total_etb = self.diksha.get_total_ETBs_value()
        total_etb_value = re.sub(self.diksha.L, "", total_etb)
        total_etb_text = self.diksha.get_total_ETBs_text()
        if total_etb_text is not None:
            print("total_etb Card Value is showing")
            self.logger.info("*********** total_etb Card Value is showing ***************")
        else:
            print("total_etb Card Value is Missing")
            self.logger.error("*************** total_etb Card Value is Missing ************")
            assert False
        if float(total_etb_value) >= 0 and total_etb_value is not None:
            print("total_etb Card Values is showing")
            self.logger.info("*********** total_etb Card Values is showing ***************")
        else:
            print("total_etb Card Value is not showing")
            self.logger.error("*************** total_etb Card Values is Missing ************")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_008 Testing Ended. *****************")

    """Check whether key metric are displaying or not"""

    def test_validate_total_qr_codes_metrics(self):
        self.logger.info("*************** Tc_cQube_diksha_009 Testing started *****************")
        time.sleep(8)
        total_qr_codes = self.diksha.get_total_qr_codes_value()
        total_qr_codes_value = re.sub(self.diksha.L, "", total_qr_codes)
        total_qr_codes_text = self.diksha.get_total_qr_codes_text()
        if total_qr_codes_text is not None:
            print("total_qr_codes Card Value is showing")
            self.logger.info("*********** total_qr_codes Card Value is showing ***************")
        else:
            print("total_qr_codes Card Value is Missing")
            self.logger.error("*************** total_qr_codes Card Value is Missing ************")
            assert False
        if float(total_qr_codes_value) >= 0 and total_qr_codes_value is not None:
            print("total_qr_codes Card Values is showing")
            self.logger.info("*********** total_qr_codes Card Values is showing ***************")
        else:
            print("total_qr_codes Card Value is not showing")
            self.logger.error("*************** total_qr_codes Card Values is Missing ************")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_009 Testing Ended. *****************")

    """Check whether key metric are displaying or not"""

    def test_validate_content_coverage_on_qr_metrics(self):
        self.logger.info("*************** Tc_cQube_diksha_010 Testing started *****************")
        time.sleep(8)
        content_coverage_on_qr = self.diksha.get_content_coverage_on_QR_value()
        content_coverage_on_qr_value = re.sub(self.diksha.L, "", content_coverage_on_qr)
        content_coverage_on_qr_text = self.diksha.get_content_coverage_on_QR_text()
        if content_coverage_on_qr_text is not None:
            print("content_coverage_on_QR Card Value is showing")
            self.logger.info("*********** content_coverage_on_QR Card Value is showing ***************")
        else:
            print("content_coverage_on_QR Card Value is Missing")
            self.logger.error("*************** content_coverage_on_QR Card Value is Missing ************")
            assert False
        if float(content_coverage_on_qr_value) >= 0 and content_coverage_on_qr_value is not None:
            print("content_coverage_on_QR Card Values is showing")
            self.logger.info("*********** content_coverage_on_QR Card Values is showing ***************")
        else:
            print("content_coverage_on_QR Card Value is not showing")
            self.logger.error("*************** content_coverage_on_QR Card Values is Missing ************")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_010 Testing Ended. *****************")

    """Check whether each dropdown is selecting and selected metric is displaying in the legend"""

    def test_dropdown(self):
        self.logger.info("*************** Tc_cQube_diksha_011 Testing started *****************")
        time.sleep(8)
        self.diksha.click_dropdown()
        time.sleep(6)
        options = self.diksha.get_metrics_dropdown_values()
        for dropdown in range(len(options)):
            opts = self.diksha.get_each_dropdown_value_id(dropdown)
            opt_text = opts.text
            opts.click()
            time.sleep(8)
            if opt_text in self.driver.page_source:
                print("Metric in  dropdown and legend is same")
                self.logger.info("*********** Metric in  dropdown and legend is same **************")
            else:
                self.logger.error("*********** Metric in  dropdown and legend is not same **************")
                assert False
            self.diksha.click_dropdown()
            time.sleep(2)
        self.logger.info("*************** Tc_cQube_diksha_011 Testing started *****************")

    """Check whether download csv button is working or not"""

    def test_download_button_diksha_pdf(self):
        self.logger.info("*************** Tc_cQube_diksha_012 Testing started *****************")
        time.sleep(8)
        self.diksha.click_dropdown()
        time.sleep(6)
        options = self.diksha.get_metrics_dropdown_values()
        for dropdown in range(len(options)):
            opts = self.diksha.get_each_dropdown_value_id(dropdown)
            opts.click()
            self.teacherattendance.click_download_button()
            time.sleep(5)
            self.file_name = p.get_download_dir() + "/ETB Coverage Status.csv"
            print(self.file_name)
            if os.path.isfile(self.file_name) is True:
                print("file is downloaded")
                os.remove(self.file_name)
            elif ' No Data Found' in self.driver.page_source:
                self.teacherattendance.click_download_button()
                time.sleep(5)
                alert = Alert(self.driver)
                a = alert.text
                print(a)
                message = " No Data Found "
                if a == message:
                    print("No data found alert is displaying")
                else:
                    assert False
            else:
                print("file is not downloaded")
                assert False
            self.diksha.click_dropdown()
            self.logger.info("*************** Tc_cQube_diksha_012 Testing ended *****************")

    """Check whether fullscreen button is working or not"""

    def test_full_screen_avg_teacher_tab(self):
        self.logger.info("*************** Tc_cQube_diksha_013 Testing started *****************")
        time.sleep(8)
        self.teacherattendance.click_fullscreen_button()
        time.sleep(6)
        is_full_screen = self.driver.execute_script(
            "return window.screen.width == screen.width && window.screen.height == screen.height;")
        print(is_full_screen)
        assert is_full_screen
        self.logger.info("*************** Tc_cQube_diksha_013 Testing ended *****************")

    # Content_coverage_on_qr
    """Check whether content_coverage_on_qr_tab is displaying or not"""

    def test_click_on_the_content_coverage_on_qr_tab_button(self):
        self.logger.info("*************** Tc_cQube_diksha_014 Testing started *****************")
        time.sleep(8)
        self.diksha.content_coverage_on_qr_tab()
        time.sleep(6)
        content_coverage_on_qr = self.diksha.click_content_coverage_on_qr()
        time.sleep(3)
        if "true" == content_coverage_on_qr:
            print("content_coverage_on_qr tab is opening")
            self.logger.info("*********** Tab is selecting ***************")
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_014 Testing ended *****************")

    def test_content_home_button(self):
        self.logger.info("*************** Tc_cQube_diksha_015 Testing Started *****************")
        time.sleep(8)
        self.diksha.content_coverage_on_qr_tab()
        time.sleep(7)
        self.homepage.test_click_on_home_button()
        time.sleep(6)
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_015 Testing ended *****************")

    """Check whether font size decrease button is working or not"""

    def test_content_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_diksha_016 Testing started *****************")
        time.sleep(8)
        self.diksha.content_coverage_on_qr_tab()
        time.sleep(4)
        res = self.homepage.test_click_on_a_minus_button()
        time.sleep(6)
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
            print("A- button is clicked")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            print("A- button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_016 Testing ended *****************")

    """Check whether font size increase button is working or not"""

    def test_content_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_diksha_017 Testing started *****************")
        time.sleep(8)
        self.diksha.content_coverage_on_qr_tab()
        time.sleep(6)
        res = self.homepage.test_click_on_a_plus_button()
        time.sleep(6)
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A+ button is clicked and working as expected")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A+ button is clicked and not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_017 Testing Ended *****************")

    """Check whether font size default button is working or not"""

    def test__content_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_diksha_018 Testing started *****************")
        time.sleep(8)
        self.diksha.content_coverage_on_qr_tab()
        time.sleep(6)
        res = self.homepage.test_click_on_a_plus_button()
        time.sleep(6)
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
            print("A button is clicked and its working ")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            print("A button is clicked and it is not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_018 Testing Ended *****************")

    """Check whether big number of total meals is displaying or not"""

    def test_validate_Total_meals_served_metrics(self):
        self.logger.info("*************** Tc_cQube_diksha_019 Testing started *****************")
        time.sleep(8)
        self.diksha.click_content_coverage_on_qr()
        time.sleep(5)
        card_value = self.diksha.get_content_coverage_on_QR_value()
        card_title = self.diksha.get_content_coverage_on_QR_text()
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

    """Check whether table header is sorting or not"""

    def test_click_the_table_headers_validate_sorting(self):
        self.logger.info("**************** Tc_cQube_diksha_020 is Started ... *************** ")
        self.diksha.click_content_coverage_on_qr()
        result = self.diksha.check_table_subject_headers_clickable()
        if result == 0:
            self.logger.info("********** program sorting functionality is working ******************")
            assert True
        else:
            self.logger.error("***************** program sorting functionality is not working  ...**************")
            assert False
        result = self.diksha.test_check_class_headers_clickable()
        if result == 0:
            self.logger.info("********** nishtha started sorting functionality is working ******************")
            assert True
        else:
            self.logger.error("*********** nishtha started sorting functionality is not working  ********")
            assert False
        self.logger.info("**************** Tc_cQube_diksha_018 is Ended ... *************** ")

    """Check whether logout button is working or not"""

    def test_content_logout(self):
        self.logger.info("*************** Tc_cQube_diksha_021 Testing Started *****************")
        time.sleep(8)
        self.homepage.test_click_logout_button()
        time.sleep(6)
        if "login" in self.driver.current_url:
            print("Logout button is working")
            self.logger.info("*********** Logout button is working *********")
        else:
            self.logger.error("*********** Logout button is not working *********")
            print("Logout button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_021 Testing ended *****************")

    # learning session
    """Check whether learning_session_tab is displaying or not"""

    def test_click_on_the_learning_session_tab_button(self):
        self.logger.info("*************** Tc_cQube_diksha_022 Testing started *****************")
        time.sleep(8)
        self.diksha.learning_session_tab()
        learning_session = self.diksha.click_learning_session()
        time.sleep(3)
        if "true" == learning_session:
            print("learning_session tab is opening")
            self.logger.info("*********** Tab is selecting ***************")
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_022 Testing ended *****************")

    """Check whether home button is working or not"""

    def test_learning_home_button(self):
        self.logger.info("*************** Tc_cQube_diksha_023 Testing Started *****************")
        time.sleep(8)
        self.diksha.learning_session_tab()
        time.sleep(7)
        self.homepage.test_click_on_home_button()
        time.sleep(6)
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_023 Testing ended *****************")

    """Check whether font size decrease button is working or not"""

    def test_learning_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_diksha_024 Testing started *****************")
        time.sleep(8)
        self.diksha.learning_session_tab()
        time.sleep(4)
        res = self.homepage.test_click_on_a_minus_button()
        time.sleep(6)
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
            print("A- button is clicked")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            print("A- button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_024 Testing ended *****************")

    """Check whether font size increase button is working or not"""

    def test_learning_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_diksha_025 Testing started *****************")
        time.sleep(8)
        self.diksha.learning_session_tab()
        time.sleep(6)
        res = self.homepage.test_click_on_a_plus_button()
        time.sleep(6)
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A+ button is clicked and working as expected")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A+ button is clicked and not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_025 Testing Ended *****************")

    """Check whether font size default button is working or not"""

    def test_learning_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_diksha_026 Testing started *****************")
        time.sleep(8)
        self.diksha.learning_session_tab()
        time.sleep(6)
        res = self.homepage.test_click_on_a_plus_button()
        time.sleep(6)
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
            print("A button is clicked and its working ")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            print("A button is clicked and it is not working")
            assert False
        self.logger.info("*************** Tc_cQube_diksha_026 Testing Ended *****************")
