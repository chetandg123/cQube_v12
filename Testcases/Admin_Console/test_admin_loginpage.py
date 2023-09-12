import logging
import time

from Page_of_objects.AdminUI.admin_console import AdminConsole
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestDashboard:
    admin = None
    homepage = None
    nas = None
    driver = None
    GetData = None
    teacherattendance = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.admin = AdminConsole(cls.driver)
        cls.admin.open_cqube_admin_application()
        cls.logger = CustomLogger.setup_logger('Admin_Dashboard', ReadConfig.get_logs_directory() + "/admin_console.log",
                                               level=logging.DEBUG)

    ''' Verify the navigated to admin login page '''
    def test_admin_login_page(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_001 Testing Started *****************")
        if 'adminconsole' in self.driver.current_url and 'Admin Login' in self.driver.page_source:
            print('Admin Console Login page is Displayed')
            self.logger.log("Admin Console URL is Working as Expected ")
            assert True
        else:
            print('Admin Console Login Page is not Displayed ')
            self.logger.error(" Admin Login Page is not Displayed ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_001 Testing Completed *****************")

    ''' Verify the Title of the Page '''
    def test_validate_title(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_002 Testing Started *****************")
        if self.admin.a in self.driver.page_source:
            self.logger.log("*************** Title is displaying *****************")
        else:
            self.logger.error("********************* Title is not displaying ***********")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_002 Testing completed *****************")

    def test_input_fileds_username_password(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_003 Testing Started *****************")
        result = self.admin.check_input_fields_accepted_values()
        if result == 0:
            self.logger.log("*************** Username & Password Input fields are Accepted Values *****************")
        else:
            self.logger.error("********************* Username & Password Input fields are Not working ***********")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_003 Testing completed *****************")

    def test_login_logout_buttons(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_004 Testing Started *****************")
        result = self.admin.check_admin_console_login_and_logout()
        if result == 0:
            self.logger.log("*************** Login & Logout buttons are working  *****************")
        else:
            self.logger.error("*********************  Login & Logout buttons are Not working ***********")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_004 Testing completed *****************")

    def test_login_button_functionality(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_005 Testing Started *****************")
        self.admin.login_to_admin_console()
        if "dashboard" in self.driver.current_url:
            self.logger.log("*************** Login to admin console is working  *****************")
        else:
            self.logger.error("********************* Login to admin console is Not working ***********")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_005 Testing completed *****************")

    def test_click_on_login_btn_without_credentials(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_006 Testing Started *****************")
        self.driver.close(self.admin.login_btn)
        if 'Username is required' and 'Password is required' in self.driver.page_source:
            self.logger.info(" Mandatory username & password input field are validated ")
            assert True
        else:
            self.logger.error("Error messages are not displayed ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_006 Testing Started *****************")











    def test_loginpage(self):
        self.logger.info("*************** Tc_cQube_loginpage_004 Testing Started *****************")
        self.loginpage.open_cqube_application()
        self.loginpage.open_login_page()
        time.sleep(4)
        if "home" in self.driver.current_url:
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






