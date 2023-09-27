import logging
import os
import time
import sys

sys.path.append(os.getcwd())
from Page_of_objects.CqubeUi.homepage import Homepage
from Page_of_objects.CqubeUi.loginpage import loginpage
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestDashboard:
    homepage = None
    driver = None
    loginpage = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.homepage = Homepage(cls.driver)
        cls.loginpage = loginpage(cls.driver)
        # cls.menu = menu(cls.driver)

        cls.logger = CustomLogger.setup_logger('Dashboard', ReadConfig.get_logs_directory() + "/Dashboard.log",
                                               level=logging.DEBUG)

    '''scripts to validate title'''

    def test_validate_title(self):
        self.logger.info("*************** Tc_cQube_homepage_001 Testing Started *****************")
        self.loginpage.open_cqube_application()
        time.sleep(2)
        a = "State Vidya Samiksha Kendra"
        print(a)
        if a in self.driver.page_source:
            self.logger.info("*************** Title is displaying *****************")
        else:
            self.logger.error("********************* Title is not displaying ***********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_001 Testing completed *****************")

    '''scripts to validate state name'''

    def test_validate_state_name(self):
        self.logger.info("*************** Tc_cQube_homepage_002 Testing Started *****************")
        self.loginpage.open_cqube_application()
        time.sleep(2)
        a = "Jharkhand"
        print(a)
        if a in self.driver.page_source:
            self.logger.info("*************** Title is displaying *****************")
        else:
            self.logger.error("********************* Title is not displaying ***********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_002 Testing completed *****************")

    '''scripts to validate the login page is displaying or not'''

    def test_check_whether_login_page_displayed(self):
        self.logger.info("*************** Tc_cQube_loginpage_003 Testing Started *****************")
        self.loginpage.open_cqube_application()
        if "login" in self.driver.current_url:
            assert True
            self.logger.info("***********  Login screen is displayed ************** ")
        else:
            self.logger.error("************* Login page is not displayed **************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_003 Testing completed *****************")

    '''scripts to check the login is working or not'''

    def test_loginpage(self):
        self.logger.info("*************** Tc_cQube_loginpage_004 Testing Started *****************")
        self.loginpage.open_cqube_application()
        self.loginpage.open_login_page()
        time.sleep(4)
        if "summary-statistics" in self.driver.current_url:
            assert True
            self.logger.info("***********  Login screen is displayed ************** ")
        else:
            self.logger.error("************* Login page is not displayed **************")
            assert False
        self.logger.info("*************** Tc_cQube_loginpage_004  Testing Ended *****************")

    '''scripts to check the login is happening or not with invalid credintials'''

    def test_check_whether_landing_page_is_not_displayed_user_is_in_login_page(self):
        self.logger.info("*************** Tc_cQube_loginpage_005 Testing Started *****************")
        self.loginpage.open_cqube_application()
        self.loginpage.open_login_page_invalid_password()
        time.sleep(3)
        if "Invalid Credentials" in self.driver.page_source:
            assert True
            self.logger.info("landing page is not displayed")

        else:
            self.logger.error("user is in login page")
            assert False
        self.logger.info("*************** Tc_cQube_loginpage_005  Testing Ended *****************")

    '''scripts to check the login is happening or not with invalid credintials'''

    def test_check_whether_landing_page_is_not_displayed_user_is_in_login_page1(self):
        self.logger.info("*************** Tc_cQube_loginpage_006 Testing Started *****************")
        self.loginpage.open_cqube_application()
        self.loginpage.open_login_page_invalid_username()
        time.sleep(3)
        if "Invalid Credentials" in self.driver.page_source:
            assert True
            self.logger.info("landing page is not displayed")
        else:
            self.logger.error("user is in login page")
            assert False
        self.logger.info("*************** Tc_cQube_loginpage_006  Testing Ended *****************")

    '''scripts to check the login is happening or not with invalid credintials'''

    def test_check_whether_landing_page_is_not_displayed_user_is_in_login_page0(self):
        self.logger.info("*************** Tc_cQube_loginpage_007 Testing Started *****************")
        self.loginpage.open_cqube_application()
        self.loginpage.open_login_page_blank_password()
        time.sleep(3)
        if "Invalid Credentials" in self.driver.page_source:
            assert True
            self.logger.info("landing page is not displayed")
        else:
            self.logger.error("user is in login page")
            assert False
        self.logger.info("*************** Tc_cQube_loginpage_007  Testing Ended *****************")

    '''scripts to check the login is happening or not with invalid credintials'''

    def test_check_whether_landing_page_is_not_displayed_user_is_in_login_page2(self):
        self.logger.info("*************** Tc_cQube_loginpage_008 Testing Started *****************")
        self.loginpage.open_cqube_application()
        self.loginpage.open_login_page_blank_username_password()
        time.sleep(3)
        if "Invalid Credentials" in self.driver.page_source:
            assert True
            self.logger.info("landing page is not displayed")
        else:
            self.logger.error("user is in login page")
            assert False
        self.logger.info("*************** Tc_cQube_loginpage_008  Testing Ended *****************")
