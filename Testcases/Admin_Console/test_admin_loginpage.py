import logging
import time

from selenium.webdriver.common.by import By

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
        cls.logger = CustomLogger.setup_logger('Admin_Dashboard',
                                               ReadConfig.get_logs_directory() + "/admin_console.log",
                                               level=logging.DEBUG)

    ''' Verify the navigated to admin login page '''

    def test_admin_login_page(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_001 Testing Started *****************")
        if 'admin' in self.driver.current_url and 'State Vidya Samiksha Kendra' in self.driver.page_source:
            print('Admin Console Login page is Displayed')
            self.logger.log("Admin Console URL is Working as Expected ")
            assert True
        else:
            print('Admin Console Login Page is not Displayed ')
            self.logger.error(" Admin Login Page is not Displayed ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_001 Testing Completed *****************")

    ''' Verify the Title of the Page '''

    def test_validate_admin_login_screen(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_002 Testing Started *****************")
        if 'admin/login' in self.driver.current_url:
            self.logger.log("*************** Title is displaying *****************")
        else:
            self.logger.error("********************* Title is not displaying ***********")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_002 Testing completed *****************")

    def test_input_fields_username_password(self):
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

    def test_invalid_username_and_valid_password(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_007 Testing Started *****************")
        self.admin.open_login_page_invalid_username()
        if 'Invalid credentials' in self.driver.page_source:
            self.logger.info(" Invalid Credentials Error message is displayed ")
            assert True
        else:
            self.logger.error(" Invalid Credentials Error message is displayed ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_007 Testing Started *****************")

    def test_valid_username_invalid_password(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_008 Testing Started *****************")
        self.admin.open_login_page_invalid_password()
        if 'Invalid credentials' in self.driver.page_source:
            self.logger.info(" Invalid Credentials Error message is displayed ")
            assert True
        else:
            self.logger.error(" Invalid Credentials Error message is displayed ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_008 Testing Started *****************")

    ''' Admin Console Dashboard Scripts '''

    def test_menu_dashboard_cards_presence(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_009 Testing Started *****************")
        self.admin.login_to_admin_console()
        result = self.admin.verify_admin_console_dashboard_cards()
        if result == 0:
            self.logger.info(" Admin Console Dashboard Cards are Displayed ")
            assert True
        else:
            self.logger.error(" Admin Console - Dashboard Cards are Missing ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_009 Testing Started *****************")

    def test_click_on_system_monitor_card(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_010 Testing Started *****************")
        self.admin.login_to_admin_console()
        result = self.admin.check_navigation_to_system_monitor()
        if result == 0:
            self.logger.info(" System Monitor Card is Working ")
            assert True
        else:
            self.logger.error(" System Monitor Card is Not Working ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_010 Testing Started *****************")

    def test_click_on_data_debugger_card(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_011 Testing Started *****************")
        self.admin.login_to_admin_console()
        result = self.admin.check_navigation_to_data_debugger()
        if result == 0:
            self.logger.info(" Data Debugger Card is Working ")
            assert True
        else:
            self.logger.error(" Data Debugger Card is Not Working ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_011 Testing Started *****************")

    def test_check_navigation_to_schema_generator(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_012 Testing Started *****************")
        self.admin.login_to_admin_console()
        result = self.admin.check_navigation_to_schema_generator()
        if result == 0:
            self.logger.info(" Schema Generator Card is Working ")
            assert True
        else:
            self.logger.error(" Schema Generator Card is Not Working ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_012 Testing Started *****************")

    def test_click_on_hamburger_menu(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_013 Testing Started *****************")
        self.admin.login_to_admin_console()
        self.admin.click_on_hamburger_menu_button()
        result = self.admin.get_count_of_menu_buttons()
        if result != 0 and result > 0:
            self.logger.info(" Hamburger Menu having Options ", result)
            assert True
        else:
            self.logger.error(" Hamburger Menu Options are not displaying ", result)
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_013 Testing Started *****************")

    def test_click_on_dashboard_link(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_014 Testing Started *****************")
        self.admin.login_to_admin_console()
        result = self.admin.check_navigation_to_data_debugger()
        res = self.admin.click_on_dashboard_button_from_menu()
        if res == 0:
            self.logger.info(" Dashboard Menu button is working ")
            assert True
        else:
            self.logger.error(" Dashboard Menu button is not working ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_014 Testing Started *****************")

    def test_click_on_data_debugger_link(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_015 Testing Started *****************")
        self.admin.login_to_admin_console()
        res = self.admin.click_on_debugger_button_from_menu()
        if res == 0:
            self.logger.info(" Debugger Menu button is working ")
            assert True
        else:
            self.logger.error(" Debugger Menu button is not working ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_015 Testing Started *****************")

    def test_click_on_schema_generator_link(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_016 Testing Started *****************")
        self.admin.login_to_admin_console()
        res = self.admin.click_on_schema_generator_button_from_menu()
        if res == 0:
            self.logger.info(" Schema Generator Menu button is working ")
            assert True
        else:
            self.logger.error(" Schema Generator Menu button is not working ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_016 Testing Started *****************")

    def test_click_on_user_icon(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_017 Testing Started *****************")
        self.admin.login_to_admin_console()
        self.admin.click_on_the_user_logo()
        self.logger.info("*************** Tc_cQube_AdminConsole_017 Testing Started *****************")

    def test_click_on_logout_button(self):
        self.logger.info("*************** Tc_cQube_AdminConsole_018 Testing Started *****************")
        self.admin.login_to_admin_console()
        result = self.admin.click_on_logout_button()
        if result == 0:
            self.logger.info(" Logout button is working ")
            assert True
        else:
            self.logger.error(" Logout button is not working ")
            assert False
        self.logger.info("*************** Tc_cQube_AdminConsole_018 Testing Started *****************")
