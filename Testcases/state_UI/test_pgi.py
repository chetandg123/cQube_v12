import logging
import os
import time
import re

from selenium.webdriver.common.alert import Alert
from Page_of_objects.CqubeUi.homepage import Homepage
from Page_of_objects.CqubeUi.pgi import Pgi
from Page_of_objects.CqubeUi.summary_statistics import Summarystatistics
from Page_of_objects.CqubeUi.teacher_attendance import Teacherattendance
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestPgi:
    homepage = None
    summarystatistics = None
    teacherattendance = None
    pgi = None
    driver = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.implicitly_wait(50)
        cls.homepage = Homepage(cls.driver)
        cls.summarystatistics = Summarystatistics(cls.driver)
        cls.teacherattendance = Teacherattendance(cls.driver)
        cls.pgi = Pgi(cls.driver)
        cls.homepage.open_cqube_application()
        cls.homepage.open_login_page()
        cls.summarystatistics.test_click_on_state_button()
        time.sleep(7)
        cls.pgi.test_click_on_pgi_menu()
        time.sleep(8)
        cls.logger = CustomLogger.setup_logger('pgi', ReadConfig.get_logs_directory() +
                                               "/pgi.log", level=logging.DEBUG)

    """Check whether pgi page is displaying or not"""

    def test_pgi_page(self):
        self.logger.info("*************** Tc_cQube_pgi_001 Testing started *****************")
        time.sleep(8)
        if "Perfomance Grading Index" in self.driver.page_source:
            print("pgi is displaying")
            self.logger.info("*********** pgi page is displaying ****************")
        else:
            print("pgi page is not displaying")
            self.logger.error("*********** pgi page is not displaying ****************")
        self.logger.info("*************** Tc_cQube_pgi_001 Testing ended *****************")

    # district_wise_performance
    """Check whether district_wise_performance_tab is opening or not"""

    def test_click_on_the_district_wise_performance_tab_button(self):
        self.logger.info("*************** Tc_cQube_pgi_002 Testing started *****************")
        time.sleep(6)
        district_wise_performance = self.pgi.click_district_wise_performance()
        time.sleep(7)
        if "true" == district_wise_performance:
            print("district_wise_performance tab is opening")
            self.logger.info("***********district_wise_performance Tab is selecting ***************")
        else:
            self.logger.error("***********district_wise_performance Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_002 Testing ended *****************")

    """Check whether home button is working or not"""

    def test_home_button(self):
        self.logger.info("*************** Tc_cQube_pgi_003 Testing Started *****************")
        self.homepage.test_click_on_home_button()
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_003 Testing ended *****************")

    """Check whether a minus button is working or not"""

    def test_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_pgi_004 Testing started *****************")
        res = self.homepage.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
            print("A- button is clicked")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            print("A- button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_004 Testing ended *****************")

    """Check whether a plus button is working or not"""

    def test_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_pgi_005 Testing started *****************")
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A+ button is clicked and working as expected")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A+ button is clicked and not working")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_005 Testing Ended *****************")

    """Check whether a default button is working or not"""

    def test_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_pgi_006 Testing started *****************")
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
            print("A button is clicked and its working ")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            print("A button is clicked and it is not working")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_006 Testing Ended *****************")

    """Check whether logout button is working or not"""

    def test_logout(self):
        self.logger.info("*************** Tc_cQube_pgi_007 Testing Started *****************")
        time.sleep(5)
        self.homepage.test_click_logout_button()
        if "login" in self.driver.current_url:
            print("Logout button is working")
            self.logger.info("*********** Logout button is working *********")
        else:
            self.logger.error("*********** Logout button is not working *********")
            print("Logout button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_007 Testing ended *****************")

    """Check whether key metrics of learning_outcome_and_quality is displaying or not"""

    def test_validate_learning_outcome_and_quality_metrics(self):
        self.logger.info("*************** Tc_cQube_pgi_008 Testing started *****************")
        learning_outcome = self.pgi.get_learning_outcome_value()
        learning_outcome_value = re.sub(self.pgi.L, "", learning_outcome)
        learning_outcome_text = self.pgi.get_learning_outcome_text()
        if learning_outcome_text is not None:
            print("learning_outcome Card Value is showing")
            self.logger.info("*********** learning_outcome Card Value is showing ***************")
        else:
            print("learning_outcome Card Value is Missing")
            self.logger.error("*************** learning_outcome Card Value is Missing ************")
            assert False
        if float(learning_outcome_value) >= 0 and learning_outcome_value is not None:
            print("learning_outcome Card Values is showing")
            self.logger.info("*********** learning_outcome Card Values is showing ***************")
        else:
            print("learning_outcome Card Value is not showing")
            self.logger.error("*************** learning_outcome Card Values is Missing ************")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_008 Testing Ended. *****************")

    """Check whether key metrics of infrastructure_and_facility is displaying or not"""

    def test_validate_infrastructure_and_facility_metrics(self):
        self.logger.info("*************** Tc_cQube_pgi_009 Testing started *****************")
        infrastructure = self.pgi.get_infrastructure_value()
        infrastructure_value = re.sub(self.pgi.L, "", infrastructure)
        infrastructure_text = self.pgi.get_infrastructure_text()
        if infrastructure_text is not None:
            print("infrastructure Card Value is showing")
            self.logger.info("*********** infrastructure Card Value is showing ***************")
        else:
            print("infrastructure Card Value is Missing")
            self.logger.error("*************** infrastructure Card Value is Missing ************")
            assert False
        if float(infrastructure_value) >= 0 and infrastructure_value is not None:
            print("infrastructure Card Values is showing")
            self.logger.info("*********** infrastructure Card Values is showing ***************")
        else:
            print("infrastructure Card Value is not showing")
            self.logger.error("*************** infrastructure Card Values is Missing ************")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_009 Testing Ended. *****************")

    """Check whether key metrics of governance_process is displaying or not"""

    def test_validate_governance_process_metrics(self):
        self.logger.info("*************** Tc_cQube_pgi_010 Testing started *****************")
        time.sleep(6)
        governance_process = self.pgi.get_governance_process_value()
        time.sleep(6)
        governance_process_value = re.sub(self.pgi.L, "", governance_process)
        governance_process_text = self.pgi.get_governance_process_text()
        if governance_process_text is not None:
            print("governance_process Card Value is showing")
            self.logger.info("*********** governance_process Card Value is showing ***************")
        else:
            print("governance_process Card Value is Missing")
            self.logger.error("*************** governance_process Card Value is Missing ************")
            assert False
        if float(governance_process_value) >= 0 and governance_process_value is not None:
            print("governance_process Card Values is showing")
            self.logger.info("*********** governance_process Card Values is showing ***************")
        else:
            print("governance_process Card Value is not showing")
            self.logger.error("*************** governance_process Card Values is Missing ************")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_010 Testing Ended. *****************")

    """Check whether legend is working or not"""

    def test_legend(self):
        self.logger.info("*************** Tc_cQube_pgi_011 Testing started *****************")
        time.sleep(6)
        self.pgi.click_dropdown()
        time.sleep(7)
        options = self.pgi.get_metrics_dropdown_values()
        time.sleep(7)
        for dropdown in range(len(options)):
            opts = self.pgi.get_each_dropdown_value_id(dropdown)
            opt_text = opts.text
            opts.click()
            time.sleep(8)
            legend = self.pgi.get_legend_text()
            if opt_text in legend:
                print("Metric in  dropdown and legend is same")
                self.logger.info("*********** Metric in  dropdown and legend is same **************")
            else:
                self.logger.error("*********** Metric in  dropdown and legend is not same **************")
                assert False
            self.pgi.click_dropdown()
            time.sleep(2)
        self.logger.info("*************** Tc_cQube_pgi_011 Testing started *****************")

    """Check whether map is displaying or not"""

    def test_check_map_on_page(self):
        self.logger.info("*************** Tc_cQube_pgi_012 Testing started *****************")
        map_info = self.pgi.get_map_information()
        if len(map_info) > 0:
            print("Map is present on the pgi page")
            self.logger.info("*********** Map is present on the pgi page ***************")
        else:
            self.logger.error("*********** Map is not present on the pgi page ***************")
            assert False
        self.logger.info("*************** Tc_cQube_pgi_012 Testing ended *****************")

    """Check whether download csv button is working or not"""

    def test_download_button_pgi_pdf(self):
        self.logger.info("*************** Tc_cQube_pgi_013 Testing started *****************")
        time.sleep(8)
        p = Teacherattendance(self)
        self.teacherattendance.click_download_button()
        time.sleep(5)
        self.file_name = p.get_download_dir() + "/Pgi District Wise Performance.csv"
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
        self.logger.info("*************** Tc_cQube_pgi_013 Testing ended *****************")

    """Check whether full screen button is working or not"""

    def test_full_screen_avg_teacher_tab(self):
        self.logger.info("*************** Tc_cQube_pgi_014 Testing started *****************")
        self.teacherattendance.click_fullscreen_button()
        time.sleep(3)
        is_full_screen = self.driver.execute_script(
            "return window.screen.width == screen.width && window.screen.height == screen.height;")
        print(is_full_screen)
        assert is_full_screen
        self.logger.info("*************** Tc_cQube_pgi_014 Testing ended *****************")
