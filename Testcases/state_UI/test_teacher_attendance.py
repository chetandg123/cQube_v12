import logging
import os
import time
import re

from selenium.webdriver.common.by import By
from Page_of_objects.CqubeUi.homepage import Homepage
from Page_of_objects.CqubeUi.summary_statistics import Summarystatistics
from Page_of_objects.CqubeUi.teacher_attendance import Teacherattendance, get_download_dir
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestTeacherattendance:
    homepage = None
    summarystatistics = None
    teacherattendance = None
    driver = None
    level = "state"

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.implicitly_wait(50)
        cls.homepage = Homepage(cls.driver)
        cls.summarystatistics = Summarystatistics(cls.driver)
        cls.teacherattendance = Teacherattendance(cls.driver)
        cls.homepage.open_cqube_application()
        cls.homepage.open_login_page()
        cls.summarystatistics.test_click_on_state_button()
        time.sleep(10)
        cls.teacherattendance.test_click_on_teacher_attendance_menu()
        time.sleep(10)

        cls.logger = CustomLogger.setup_logger('teacher_attendance', ReadConfig.get_logs_directory() +
                                               "/teacher_attendance.log", level=logging.DEBUG)

    """Check whether teacher_attendance page is displaying or not"""

    def test_teacher_attendance_page(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_001 Testing started *****************")
        time.sleep(8)
        if "Teacher Attendance" in self.driver.page_source and 'teacher-attendance' in self.driver.current_url:
            print("teacher_attendance page is displaying")
            self.logger.info("*********** teacher_attendance page is displaying ****************")
        else:
            print("teacher_attendance page is not displaying")
            self.logger.error("*********** teacher_attendance page is not displaying ****************")
        self.logger.info("*************** Tc_cQube_teacher_attendance_001 Testing ended *****************")

    # Average_Teachers_Reporting_Attendance
    """Check whether Average_Teachers_Reporting_Attendance tab is opening or not"""

    def test_click_on_the_average_teachers_reporting_attendance_tab_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_002 Testing started *****************")
        average_teachers_reporting = self.teacherattendance.click_Average_Teachers_Reporting_Attendance()
        if "true" == average_teachers_reporting:
            print("Average_Teachers_Reporting_Attendance tab is opening")
            self.logger.info("*********** Tab is selecting ***************")
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_002 Testing ended *****************")

    def test_validate_big_number_total_enrolment_metrics(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_003 Testing Started *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(1)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)

        card_value = self.teacherattendance.get_total_Enrolment_value()
        card_title = self.teacherattendance.get_total_Enrolment_label()
        value = "0"
        if card_title is not None:
            print(card_title)
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False
        if str(card_value) >= value and card_value is not None:
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False
        self.logger.info("***************Tc_cQube_teacher_attendance_003 Testing Ended *****************")

    def test_validate_after_changing_date_value(self):
        self.logger.info("***************Tc_cQube_teacher_attendance_004 Testing started *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(5)
        self.teacherattendance.select_date_from_calender()
        time.sleep(3)
        card_value = self.teacherattendance.get_total_Enrolment_value()
        time.sleep(3)
        card_title = self.teacherattendance.get_total_Enrolment_label()
        value = "0"
        if card_title is not None:
            print(card_title)
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False
        if str(card_value) >= value and card_value is not None:
            print(card_value)
            self.logger.info("*********** Total enrolment card values are showing ***************")
            assert True
        else:
            self.logger.error("*************** Total enrolment card values are Missing ************")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_004 Testing ended *****************")

    def test_home_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_004 Testing Started *****************")
        self.homepage.test_click_on_home_button()
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_004 Testing ended *****************")

    def test_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_005 Testing started *****************")
        res = self.homepage.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
            print("A- button is clicked")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            print("A- button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_005 Testing ended *****************")

    '''This Test script checking the A Plus Button '''

    def test_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_006 Testing started *****************")
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A+ button is clicked and working as expected")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A+ button is clicked and not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_006 Testing Ended *****************")

    '''This Test script checking Default A  '''

    def test_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_007 Testing started *****************")
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
            print("A button is clicked and its working ")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            print("A button is clicked and it is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_008 Testing Ended *****************")

    def test_logout(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_009 Testing Started *****************")
        time.sleep(5)
        self.homepage.test_click_logout_button()
        if "login" in self.driver.current_url:
            print("Logout button is working")
            self.logger.info("*********** Logout button is working *********")
        else:
            self.logger.error("*********** Logout button is not working *********")
            print("Logout button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_009 Testing ended *****************")

    def test_validate_average_per_teachers_reporting_attendance_metrics(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing started *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(5)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        avg_teacher_attendance = self.teacherattendance.get_avg_teacher_attendance_value()
        avg_teacher_attendance_value = re.sub(self.teacherattendance.L, "", avg_teacher_attendance)
        avg_teacher_attendance_text = self.teacherattendance.get_avg_teacher_attendance_text()
        if avg_teacher_attendance_text is not None:
            print("Teacher_attendance Card Value is showing")
            self.logger.info("*********** Teacher_attendance Card Value is showing ***************")
        else:
            print("Teacher_attendance Card Value is Missing")
            self.logger.error("*************** Teacher_attendance Card Value is Missing ************")
            assert False
        if float(avg_teacher_attendance_value) >= 0 and avg_teacher_attendance_value is not None:
            print("Teacher_attendance Card Values is showing")
            self.logger.info("*********** Teacher_attendance Card Values is showing ***************")
        else:
            print("Teacher_attendance Card Value is not showing")
            self.logger.error("*************** Teacher_attendance Card Values is Missing ************")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing Ended. *****************")

    def test_full_screen(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing started *****************")
        self.teacherattendance.click_fullscreen_button()
        time.sleep(3)
        is_full_screen = self.driver.execute_script(
            "return window.screen.width == screen.width && window.screen.height == screen.height;")
        print(is_full_screen)
        assert is_full_screen
        self.logger.info("*************** Tc_cQube_teacher_attendance_010 Testing ended *****************")

    # Average teacher present tab
    """Check whether average teacher present tab is opening or not"""

    def test_home_button_avg_teacher(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_013 Testing Started *****************")
        time.sleep(5)
        self.teacherattendance.click_average_teacher_present_tab()
        self.homepage.test_click_on_home_button()
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_013 Testing ended *****************")

    def test_click_the_a_minus_button_avg_teacher(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_014 Testing started *****************")
        time.sleep(5)
        self.teacherattendance.click_average_teacher_present_tab()
        res = self.homepage.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
            print("A- button is clicked")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            print("A- button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_014 Testing ended *****************")

    '''This Test script checking the A Plus Button '''

    def test_click_the_a_plus_button_avg_teacher(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_015 Testing started *****************")
        time.sleep(5)
        self.teacherattendance.click_average_teacher_present_tab()
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A+ button is clicked")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A+ button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_015 Testing Ended *****************")

    '''This Test script checking Default A  '''

    def test_click_the_default_a_button_avg_teacher(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_016 Testing started *****************")
        self.teacherattendance.click_average_teacher_present_tab()
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
            print("A button is clicked")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            print("A button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_016 Testing Ended *****************")

    def test_logout_avg_teacher(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_017 Testing Started *****************")
        self.teacherattendance.click_average_teacher_present_tab()
        time.sleep(5)
        self.homepage.test_click_logout_button()
        if "login" in self.driver.current_url:
            print("Logout button is working")
            self.logger.info("*********** Logout button is working *********")
        else:
            self.logger.error("*********** Logout button is not working *********")
            print("Logout button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_017 Testing ended *****************")

    def test_click_on_the_average_teacher_present_tab_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_011 Testing started *****************")
        self.teacherattendance.click_average_teacher_present_tab()
        average_teacher_present = self.teacherattendance.get_attribute_average_teacher_present()
        time.sleep(4)
        if "true" == average_teacher_present:
            self.logger.info("*********** Tab is selecting ***************")
            print("Tab is selecting")
        else:
            print("Tab is not selecting")
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_012 Testing ended *****************")

        '''Testing Full Screeen Button For Avg Teacher Attendance Tab'''

    def test_full_screen_avg_teacher_tab(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_012 Testing started *****************")
        self.teacherattendance.click_average_teacher_present_tab()
        self.teacherattendance.click_fullscreen_button()
        time.sleep(3)
        is_full_screen = self.driver.execute_script(
            "return window.screen.width == screen.width && window.screen.height == screen.height;")
        print(is_full_screen)
        assert is_full_screen
        self.logger.info("*************** Tc_cQube_teacher_attendance_012 Testing ended *****************")

        '''Validating Unit Level Download Button'''

    def test_unit_level_download_button(self):
        self.logger.info("***************Tc_cQube_teacher_attendance_013 Testing started *****************")
        time.sleep(5)
        # self.logger.info("*************** Tc_cQube_teacher_attendance_019 Testing started *****************")
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(2)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        if ' No Data Found' in self.driver.page_source:
            self.teacherattendance.click_download_unit_level_button()
            time.sleep(3)
        else:
            self.teacherattendance.click_download_unit_level_button()
            time.sleep(3)
            # self.teacherattendance.click_download_csv_button()
            program_name = self.driver.find_element(By.CLASS_NAME, 'program-title').text
            tab_name = self.driver.find_element(By.XPATH, "//div[@role='tab']/div").text
            self.file_name = get_download_dir() + "/" + (program_name + '_' + tab_name + self.level).replace(' ',
                                                                                                             '_') + '.csv'
            self.file_name = get_download_dir() + "/% Teachers Reporting Attendance.csv"
            print(self.file_name)
            if os.path.isfile(self.file_name) is True:
                print("file is downloaded")
                os.remove(self.file_name)
            else:
                print("file is not downloaded")
                assert False
            self.logger.info("*************** Tc_cQube_teacher_attendance_013 Testing ended *****************")

            '''Validating School Level Download Button'''

    def test_school_level_report_download_button(self):
        self.logger.info("***************Tc_cQube_teacher_attendance_014 Testing started *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        self.teacherattendance.click_clear_button()
        time.sleep(2)
        if ' No Data Found' in self.driver.page_source:
            self.teacherattendance.click_download_School_report_button()
            time.sleep(3)
        else:
            self.teacherattendance.click_download_button()
            time.sleep(5)
            self.teacherattendance.click_download_School_report_button()
            time.sleep(3)
            program_name = self.driver.find_element(By.CLASS_NAME, 'program-title').text
            tab_name = self.driver.find_element(By.XPATH, "//div[@role='tab']/div").text
            # for without filter download of csv
            self.file_name = get_download_dir() + "/" + (program_name + '_' + tab_name + self.level).replace(' ',
                                                                                                             '_') + '.csv'
            self.file_name = get_download_dir() + "/% Teachers Reporting Attendance.csv"
            print(self.file_name)
            if os.path.isfile(self.file_name) is True:
                print("file is downloaded")
                os.remove(self.file_name)
            else:
                print("file is not downloaded")
                assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_014 Testing ended *****************")

        '''Validating Clear Button'''

    def test_calender_clear_button(self):
        self.logger.info("***************Tc_cQube_teacher_attendance_016 Testing started *****************")
        time.sleep(5)
        # self.logger.info("*************** Tc_cQube_teacher_attendance_019 Testing started *****************")
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(1)
        self.teacherattendance.click_clear_button()
        time.sleep(2)
        if " No Data Found " in self.driver.page_source:
            print("Clear button is working successfully")
            assert True
        else:
            print("Clear button not working")
        self.logger.info("*************** Tc_cQube_teacher_attendance_0016 Testing ended *****************")

        '''Validating Calender is open or not'''

    def test_validate_calender(self):
        self.logger.info("***************Tc_cQube_teacher_attendance_017 Testing started *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.click_to_calender_button()

        if self.teacherattendance.validate_calender_displayed:
            time.sleep(2)
            print("Calender Open Successfully")

        else:
            print("calender Button Not Working")

        self.logger.info("*************** Tc_cQube_teacher_attendance_017 Testing ended *****************")

        '''Validating Selection of date'''

    def test_validate_date_range_selection(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_018 Testing started *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        if self.teacherattendance.validate_after_selection_of_date_displayed() == 'group':
            print("Date is selected")
            assert True
        else:
            print("Date were not selected")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_018 Testing ended *****************")

        '''Validating the apply button of unitbox'''

    def test_validate_unitbox_apply_Button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_020 Testing started *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.validate_Appty_button_unitbox()
        self.logger.info("*************** Tc_cQube_teacher_attendance_020 Testing ended *****************")

        '''Validating Error Message'''

    def test_validate_error_message(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_021 Testing started *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)

        if "No Data Found" in self.driver.page_source:
            print("No data found message display")
            assert True
        else:
            print("No data found message not be display")
            assert False

        self.logger.info("*************** Tc_cQube_teacher_attendance_021 Testing Ended *****************")

    def test_validate_drill_down_sorting(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_022 Testing Ended *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(20)
        result = self.teacherattendance.validate_drill_down_table_sorting()
        if result == 0:
            print("% Teacher Present Table Sorting is Working as Expected ")
        else:
            print(result, "% Teacher Present Table Sorting is Not Working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_022 Testing Ended *****************")

    def test_validate_drilldown_District_level(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_023 Testing Ended *****************")
        time.sleep(7)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        self.teacherattendance.validate_District_level_drilldown()
        time.sleep(3)
        if self.teacherattendance.validate_District_level_drilldown():
            print("DrillDown is Happening")
        else:
            print("DrillDown Is Not Happening")

    def test_validate_district_name_bread_crumb(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_024 Testing Start *****************")
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(3)
        a1 = self.teacherattendance.validate_District_name_in_bread_crumb()
        if a1:
            print("Ditrict name is Displayed in Breadcrumb")
            assert True
        else:
            print("Ditrict name is Not Displayed in Breadcrumb")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_024 Testing ended *****************")

    def test_validate_state_bread_crumb(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_025 Testing Start *****************")

        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(3)
        a1 = self.teacherattendance.validate_State_name_in_bread_Crumb()
        time.sleep(3)

        if a1:
            print("State Name Displayed in BreadCrumb")
            assert True
        else:
            print("State Name is Not Displayed in BreadCrumb")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_025 Testing Ended *****************")

    def test_validate_drilldown_block_level(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_026 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(5)
        self.teacherattendance.select_date_from_calender()
        time.sleep(4)
        self.teacherattendance.validate_Block_level_drilldown()
        self.logger.info("*************** Tc_cQube_teacher_attendance_026 Testing Ended *****************")

    def test_validate_block_Bread_Crumb(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_027 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(5)
        self.teacherattendance.select_date_from_calender()
        time.sleep(5)
        self.teacherattendance.validate_block_name_in_Bread_Crumb()
        self.logger.info("*************** Tc_cQube_teacher_attendance_027 Testing Ended *****************")

    def test_validate_district_bread_crumb(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_028 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(5)
        self.teacherattendance.select_date_from_calender()
        time.sleep(5)
        self.teacherattendance.validate_District_name_in_Bread_Crumb()
        self.logger.info("*************** Tc_cQube_teacher_attendance_028 Testing Ended *****************")

    def test_validate_drilldown_cluster_level(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_030 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(3)
        self.teacherattendance.validate_cluster_level_drilldown()
        self.logger.info("*************** Tc_cQube_teacher_attendance_030 Testing Ended *****************")

    def test_validate_cluster_level_breadcrumb(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_031 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(3)
        self.teacherattendance.validate_cluster_in_breadcrumb()
        self.logger.info("*************** Tc_cQube_teacher_attendance_031 Testing Ended *****************")

    def test_validate_Data_belongs_to_block_bread_crumb(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_032 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(3)
        self.teacherattendance.validate_data_belongs_to_block_breadcrumb()
        self.logger.info("*************** Tc_cQube_teacher_attendance_032 Testing Ended *****************")

    def test_validate_data_belongs_district_crumb(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_033 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()

        time.sleep(3)
        self.teacherattendance.validate_data_belongs_to_District_breadcrumb()
        self.logger.info("*************** Tc_cQube_teacher_attendance_033 Testing Ended *****************")

    def test_validate_data_belongs_state_bread_crumb(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_034 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        self.teacherattendance.validate_data_belongs_to_State_breadcrumb()
        self.logger.info("*************** Tc_cQube_teacher_attendance_034 Testing Ended *****************")

    def test_pagination_for_percent_teacher_attendance(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_035 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        self.teacherattendance.click_pagination_teacher_present()
        time.sleep(1)
        self.teacherattendance.validate_pagination_teacher_present()
        self.logger.info("*************** Tc_cQube_teacher_attendance_035 Testing Ended *****************")

    def test_pagination_for_bar_graph_attendance(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_036 Testing Start *****************")
        time.sleep(2)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(2)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        self.teacherattendance.click_pagination_bar_graph()
        time.sleep(2)
        self.teacherattendance.validate_pagination_teacher_present_bar_graph()
        self.logger.info("*************** Tc_cQube_teacher_attendance_036 Testing Ended *****************")

    def test_pagination_for_school_bar_graph_attendance(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_037 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(2)
        self.teacherattendance.select_date_from_calender()
        time.sleep(10)
        self.teacherattendance.click_pagination_school_teacher_present()
        time.sleep(2)
        self.teacherattendance.validation_pagination_school_teacher_present()
        self.logger.info("*************** Tc_cQube_teacher_attendance_037 Testing Ended *****************")

    def test_validate_Udise_search_box(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_038 Testing Start *****************")
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(5)
        self.teacherattendance.validate_search_box_udise()
        time.sleep(3)
        self.logger.info("*************** Tc_cQube_teacher_attendance_038 Testing Ended *****************")

    def test_validate_percent_teacher_present_header_sorting(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_039 Testing Start *****************")
        time.sleep(5)
        self.teacherattendance.click_on_avg_teacher_attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(5)
        result = self.teacherattendance.validate_drill_down_table_sorting()
        if result == 0:
            print(" Table Headers are sorting to asc & desc orders ")
            assert True
        else:
            print(" Sorting Functions on tables are not working ")
            assert False

        self.logger.info("*************** Tc_cQube_teacher_attendance_039 Testing Start *****************")

    def test_validate__schoolwise_percent_teacher_present_header_sorting(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_040 Testing Start *****************")
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(5)
        result = self.teacherattendance.validate_sorting()
        if result == 0:
            print(" Table Headers are sorting to asc & desc orders ")
            assert True
        else:
            print(" Sorting Functions on tables are not working ")
            assert False

        self.logger.info("*************** Tc_cQube_teacher_attendance_040 Testing Start *****************")

        ########  Map View of Teacher Attendance #########

        """Check whether Average_Teachers_Reporting_Attendance tab is opening or not"""

    def test_click_on_map_view_of_teacher_atteandance_tab(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_041 Testing started *****************")
        map_view_of_teacher_attendance = self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(5)
        if "true" == map_view_of_teacher_attendance:
            print("Average_Teachers_Reporting_Attendance tab is opening")
            self.logger.info("*********** Tab is selecting ***************")
        else:
            self.logger.error("*********** Tab is not selecting ***************")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_041 Testing ended *****************")

    def test_validate_map_displaying_or_not(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_042 Testing started *****************")
        time.sleep(3)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(5)
        self.teacherattendance.select_date_from_calender()
        time.sleep(3)
        self.teacherattendance.map_displayed_validation()
        time.sleep(1)
        self.logger.info("*************** Tc_cQube_teacher_attendance_042 Testing started *****************")

    def test_validate_calender_for_map_view_teacher_attendance_tab(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_043 Testing started *****************")
        time.sleep(2)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        if self.teacherattendance.validate_after_selection_of_date_displayed() == 'group':
            print("Date is Displayed")
            assert True
        else:
            print("Date is not Displayed")
            assert False

    def test_validate_clear_button_from2nd_tab(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_044 Testing started *****************")
        time.sleep(2)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(2)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        self.teacherattendance.click_clear_button()
        time.sleep(2)
        if " No Data Found " in self.driver.page_source:
            print("Clear button is working successfully")
            assert True
        else:
            print("Clear button not working")

        self.logger.info("*************** Tc_cQube_teacher_attendance_044 Testing Ended *****************")

    def test_calender_Displayed_or_not(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_045 Testing started *****************")
        time.sleep(2)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(3)
        self.teacherattendance.click_to_calender_button()
        time.sleep(3)
        if self.teacherattendance.validate_calender_displayed:
            time.sleep(2)
            print("Calender Open Successfully")

        else:
            print("calender Button Not Working")

        self.logger.info("*************** Tc_cQube_teacher_attendance_045 Testing Ended *****************")

    def test_validate_Date_in_time_range(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_046 Testing started *****************")
        time.sleep(2)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(3)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        if self.teacherattendance.validate_after_selection_of_date_displayed() == 'group':
            print("Date is selected")
            assert True
        else:
            print("Date were not selected")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_046 Testing Ended *****************")

    def test_validate_home_button_on_map_view_tab(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_047 Testing Started *****************")
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(3)
        self.homepage.test_click_on_home_button()
        time.sleep(3)
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_047 Testing Ended *****************")

    def test_validate_minus_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_048 Testing started *****************")
        time.sleep(2)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(3)
        res = self.homepage.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
            print("A- button is clicked")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            print("A- button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_048 Testing Ended *****************")

    def test_validate_plus_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_049 Testing started *****************")
        time.sleep(2)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(3)
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A+ button is clicked and working as expected")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A+ button is clicked and not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_049 Testing Ended *****************")

    def test_validate_default_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_050 Testing started *****************")
        time.sleep(2)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(3)
        res = self.homepage.test_click_on_a_default_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A button is clicked and working as expected")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A button is clicked and not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_050 Testing Ended *****************")

    def test_validate_logout_button(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_051 Testing Started *****************")
        time.sleep(5)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(3)
        self.homepage.test_click_logout_button()
        if "login" in self.driver.current_url:
            print("Logout button is working")
            self.logger.info("*********** Logout button is working *********")
        else:
            self.logger.error("*********** Logout button is not working *********")
            print("Logout button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_051 Testing ended *****************")

    def test_validate_user_at_level(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_052 Testing Started *****************")
        time.sleep(5)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(2)
        if "Teacher Attendance" in self.driver.page_source and 'teacher-attendance' in self.driver.current_url:
            print("teacher_attendance page is displaying")
            self.logger.info("*********** teacher_attendance page is displaying ****************")
        else:
            print("teacher_attendance page is not displaying")
            self.logger.error("*********** teacher_attendance page is not displaying ****************")
        self.logger.info("*************** Tc_cQube_teacher_attendance_052 Testing ended *****************")

    def test_map_tooltip_info_validation(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_054 Testing Started *****************")
        time.sleep(5)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(2)
        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        map_tooltip = self.teacherattendance.get_map_tooltip_info_validation()
        if map_tooltip != 0:
            print("tooltip is displayed")
            assert True
        else:
            print("tooltip is not displayed")
            assert False
        self.logger.info("*************** Tc_cQube_teacher_attendance_054 Testing Ended *****************")

    def test_validate_lagend_card(self):
        self.logger.info("*************** Tc_cQube_teacher_attendance_064 Testing Started *****************")
        time.sleep(5)
        self.teacherattendance.click_map_view_of_Teachers_Attendance_tab()
        time.sleep(2)

        self.teacherattendance.select_date_from_calender()
        time.sleep(2)
        if "Average Teachers Present:" in self.driver.page_source:
            print("legend card is displayed")
        else:
            print("legend card is not displayed")
        self.logger.info("*************** Tc_cQube_teacher_attendance_064 Testing Ended *****************")
