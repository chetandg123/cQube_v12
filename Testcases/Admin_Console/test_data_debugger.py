import logging
import os.path
import time

from selenium.webdriver.common.by import By

from Page_of_objects.AdminUI.admin_console import AdminConsole
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestDebugger:
    admin = None
    homepage = None
    nas = None
    driver = None
    GetData = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.admin = AdminConsole(cls.driver)
        cls.admin.open_cqube_admin_application()
        cls.admin.open_login_page()
        cls.admin.click_on_debugger_dashboard_icon()
        cls.logger = CustomLogger.setup_logger('Admin_Dashboard_Debugger',
                                               ReadConfig.get_logs_directory() + "/admin_console.log",
                                               level=logging.DEBUG)

    def test_debugger_dashboard_screen(self):
        self.logger.info("*************** Tc_cQube_Debugger_001 Testing Started *****************")
        self.admin.click_on_home_button()
        self.admin.click_on_debugger_dashboard_icon()
        if 'debugger' in self.driver.current_url:
            self.logger.log("Debugger Dashboard is Displayed")
            assert True
        else:
            self.logger.error(" Debugger Dashboard is not Displayed ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_001 Testing Completed *****************")

    def test_check_radio_buttons(self):
        self.logger.info("*************** Tc_cQube_Debugger_002 Testing Started *****************")
        radio_btn = self.driver.find_element(By.ID, self.admin.dimension_radio)
        result = radio_btn.is_selected()
        if result:
            self.logger(' Dimension Radio icon is Selected ')
            assert True
        else:
            self.logger.error(" Dimension Radio icon is not Selected ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_002 Testing Completed *****************")

    def test_dimension_dropdown_options_presence(self):
        self.logger.info("*************** Tc_cQube_Debugger_003 Testing Started *****************")
        result = self.admin.check_dropdown_options()
        if result == 0:
            self.logger.log(" Dimension Dropdown having options ")
            assert True
        else:
            self.logger.error(" Dimension Dropdown options are not present ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_003 Testing Completed *****************")

    def test_check_event_dropdown_options_presence(self):
        self.logger.info("*************** Tc_cQube_Debugger_004 Testing Started *****************")
        self.admin.click_on_event_radio_btn()
        result = self.admin.check_dropdown_options()
        if result == 0:
            self.logger.log(" Event Dropdown having options ")
            assert True
        else:
            self.logger.error(" Event Dropdown options are not present ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_004 Testing Completed *****************")

    def test_select_dimension_dropdown_options(self):
        self.logger.info("*************** Tc_cQube_Debugger_005 Testing Started *****************")
        result = self.admin.select_dropdown_options()
        if result == 0:
            self.logger.log("Dimension Dropdown Options are selectable")
            assert True
        else:
            self.logger.error("Dimension Dropdown Options are not selectable. ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_005 Testing Completed *****************")

    def test_select_event_dropdown_options(self):
        self.logger.info("*************** Tc_cQube_Debugger_006 Testing Started *****************")
        self.admin.click_on_event_radio_btn()
        result = self.admin.select_dropdown_options()
        if result == 0:
            self.logger.log("Event Dropdown Options are selectable. ")
            assert True
        else:
            self.logger.error("Event Dropdown Options are not selectable. ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_006 Testing Completed *****************")

    def test_click_on_upload_file_button(self):
        self.logger.info("*************** Tc_cQube_Debugger_007 Testing Started *****************")
        result = self.driver.find_element(By.ID, self.admin.upload_btn)
        result.click()
        res = result.get_attribute('')
        if res == 0:
            self.logger.log("Clicked on Upload button . ")
            assert True
        else:
            self.logger.error("Upload File button is not clicked. ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_007 Testing Completed *****************")

    def test_dimension_file_debugger(self):
        self.logger.info("*************** Tc_cQube_Debugger_008 Testing Started *****************")
        res = self.admin.check_dimension_debugger_of_file()
        if res:
            self.logger.log(" Dimension file debugging is working . ")
            assert True
        else:
            self.logger.error(" Dimension file debugger is not working  ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_008 Testing Completed *****************")

    def test_event_file_debugger(self):
        self.logger.info("*************** Tc_cQube_Debugger_009 Testing Started *****************")
        res = self.admin.check_event_debugger_of_file()
        if res:
            self.logger.log(" Event file debugging is working . ")
            assert True
        else:
            self.logger.error(" Event file debugger is not working  ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_009 Testing Completed *****************")

    def test_mandatory_error_message(self):
        self.logger.info("*************** Tc_cQube_Debugger_012 Testing Started *****************")
        self.driver.find_element(By.ID, self.admin.debugger).click()
        time.sleep(2)
        if 'choose a option' in self.driver.page_source and 'upload the file' in self.driver.page_source:
            self.logger.info(' Mandatory Error message is Displayed ')
            assert True
        else:
            self.logger.error(" Dropdown selection & file upload error message is not displayed")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_012 Testing Completed *****************")

    def test_event_file_upload_without_selection_of_dropdown(self):
        self.logger.info("*************** Tc_cQube_Debugger_013 Testing Started *****************")
        self.driver.find_element(By.ID, self.admin.event_radio).click()
        self.driver.find_element(By.ID, self.admin.upload_btn).click()
        filepath = self.driver.find_element(By.XPATH, self.admin.file_path)
        filepath.send_keys()
        filepath.click()
        self.driver.find_element(By.ID, self.admin.debugger).click()
        time.sleep(2)
        if 'choose a option' in self.driver.page_source:
            self.logger.info(' Mandatory Error message is Displayed ')
            assert True
        else:
            self.logger.error(" Dropdown selection & file upload error message is not displayed")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_013 Testing Completed *****************")

    def test_pdf_file_uploading_error_messages(self):
        self.logger.info("*************** Tc_cQube_Debugger_014 Testing Started *****************")
        self.admin.check_dimension_debugger_of_pdf_file()
        if 'select file csv or xlsx' in self.driver.page_source:
            self.logger.info(" File Upload Supports CSV & xlsx Error message Displayed")
            assert True
        else:
            self.logger.error(" File Upload is not showing error for PDF file ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_014 Testing Completed *****************")

    def test_json_file_uploading_error_messages(self):
        self.logger.info("*************** Tc_cQube_Debugger_015 Testing Started *****************")
        self.admin.check_dimension_debugger_of_json_file()
        if 'select file csv or xlsx' in self.driver.page_source:
            self.logger.info(" File Upload Supports CSV & xlsx Error message Displayed")
            assert True
        else:
            self.logger.error(" File Upload is not showing error for PDF file ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_015 Testing Completed *****************")

    def test_invalid_dimension_file_debugger(self):
        self.logger.info("*************** Tc_cQube_Debugger_016 Testing Started *****************")
        res = self.admin.check_dimension_debugger_of_file()
        if res:
            self.logger.log(" Invalid Dimension file debugging is working . ")
            assert True
        else:
            self.logger.error(" In Dimension file debugger is not working  ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_016 Testing Completed *****************")

    def test_invalid_event_file_debugger(self):
        self.logger.info("*************** Tc_cQube_Debugger_017 Testing Started *****************")
        res = self.admin.check_event_debugger_of_file()
        if res:
            self.logger.log(" Invalid Event file debugging is working . ")
            assert True
        else:
            self.logger.error(" Invalid Event file debugger is not working  ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_017 Testing Completed *****************")

    def test_debugged_result_csv_download(self):
        self.logger.info("*************** Tc_cQube_Debugger_017 Testing Started *****************")
        self.test_invalid_dimension_file_debugger()
        self.driver.find_element(By.ID, self.admin.download_btn).click()
        self.file_dir = ReadConfig()
        result = self.file_dir.get_download_dir() + 'debugger.csv'
        if os.path.isfile(result):
            self.logger.info(" Debugged CSV File is Downloaded ")
            assert True
        else:
            self.logger.error(" Download Button is Not Working ")
            assert False
        self.logger.info("*************** Tc_cQube_Debugger_017 Testing Completed *****************")
