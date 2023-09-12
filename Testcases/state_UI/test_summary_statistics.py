import logging
import time
import re

from Page_of_objects.CqubeUi.homepage import Homepage
from Page_of_objects.CqubeUi.summary_statistics import Summarystatistics
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestSummarystatistics:
    homepage = None
    summarystatistics = None
    driver = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.implicitly_wait(50)
        cls.homepage = Homepage(cls.driver)
        cls.summarystatistics = Summarystatistics(cls.driver)
        cls.homepage.open_cqube_application()
        cls.homepage.open_login_page()
        cls.summarystatistics.test_click_on_state_button()
        time.sleep(5)
        cls.logger = CustomLogger.setup_logger('Summary_statistics', ReadConfig.get_logs_directory() +
                                               "/Summary_statistics.log", level=logging.DEBUG)

    '''Check whether summary statistics page is opening or not'''
    def test_summary_statistics_page(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_001 Testing started *****************")
        time.sleep(2)
        if "Summary Statistics" in self.driver.page_source:
            print("Summary page is displaying")
            self.logger.info("*********** Summary page is displaying ****************")
        else:
            print("Summary page is not displaying")
            self.logger.error("*********** Summary page is not displaying ****************")
            assert False
        self.logger.info("*************** Tc_cQube_summary_statistics_001 Testing ended *****************")

    '''Check whether home button is working or not'''
    def test_home_button(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_002 Testing Started *****************")
        self.homepage.test_click_on_home_button()
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.info("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_summary_statistics_002 Testing ended *****************")

    '''Check whether a minus button is working or not'''
    def test_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_003 Testing started *****************")
        time.sleep(4)
        res = self.homepage.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
            print("A- button is clicked")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            print("A- button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_summary_statistics_003 Testing ended *****************")

    '''Check whether a plus button is working or not'''
    def test_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_004 Testing started *****************")
        time.sleep(4)
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A+ button is clicked")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A+ button is clicked")
            assert False
        self.logger.info("*************** Tc_cQube_summary_statistics_004 Testing Ended *****************")

    '''Check whether a default button is working or not'''

    def test_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_005 Testing started *****************")
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
            print("A button is clicked")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            print("A button is clicked")
            assert False
        self.logger.info("*************** Tc_cQube_summary_statistics_005 Testing Ended *****************")

    '''Check whether logout button is working or not'''

    def test_logout(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_006 Testing Started *****************")
        time.sleep(5)
        self.homepage.test_click_logout_button()
        if "login" in self.driver.current_url:
            print("Logout button is working")
            self.logger.info("*********** Logout button is working *********")
        else:
            self.logger.error("*********** Logout button is not working *********")
            print("Logout button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_summary_statistics_006 Testing ended *****************")


    def test_validate_teacher_attendance_card_metrics(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_009 Testing Started *****************")
        time.sleep(5)
        teacher_attendance_info = self.summarystatistics.get_teacher_attendance_card_info()
        # attendance = self.summarystatistics.get_teacher_attendance_card_Avg_std_attendance_value()
        # attendance_value = re.sub(self.summarystatistics.L, "", attendance)
        present = self.summarystatistics.get_teacher_attendance_card_Avg_teacher_present_value()
        present_value = re.sub(self.summarystatistics.K, "", present)
        # attendance_text = self.summarystatistics.get_teacher_attendance_card_Avg_std_attendance_text()
        present_text = self.summarystatistics.get_teacher_attendance_card_Avg_teacher_present_text()
        if teacher_attendance_info is not None and present_text is not None:
            print("Teacher_attendance Card Value is showing")
            self.logger.info("*********** Teacher_attendance Card Value is showing ***************")
        else:
            print("Teacher_attendance Card Value is Missing")
            self.logger.error("*************** Teacher_attendance Card Value is Missing ************")
            assert False
        if float(present_value) >= 0 and present_value is not None:
            print("Teacher_attendance Card Values is showing")
            self.logger.info("*********** Teacher_attendance Card Values is showing ***************")
        else:
            print("teacher_attendance Card Value is not showing")
            self.logger.error("*************** Teacher_attendance Card Values is Missing ************")
        self.logger.info("*************** Tc_cQube_summary_statistics_009 Testing Ended. *****************")

    def test_check_navigation_to_teacher_attendance_dashboard(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_010 Testing Started *****************")
        self.summarystatistics.click_on_access_teacher_attendance_dashboard()
        time.sleep(2)
        if 'teacher-attendance' in self.driver.current_url and 'Teacher Attendance' in self.driver.page_source:
            print("teacher Attendance Dashboard is Displayed")
            self.logger.info("******************* teacher Attendance Dashboard is Displayed ********************")
        else:
            print("teacher Attendance Dashboard is not Displayed")
            self.logger.error("*************** teacher Attendance Dashboard Button is not Working ******************")
            assert False
        self.summarystatistics.click_summary_statistics()
        self.logger.info("*************** Tc_cQube_summary_statistics_010 Testing Ended *****************")




    def test_validate_pgi_card_metrics(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_013 Testing Started *****************")
        time.sleep(5)
        pgi_info = self.summarystatistics.get_pgi_card_info()
        learning_outcome = self.summarystatistics.get_pgi_card_learning_outcome_value()
        learning_outcome_value = re.sub(self.summarystatistics.L, "", learning_outcome)
        infra_facility = self.summarystatistics.get_pgi_card_infra_and_facility_value()
        infra_facility_value = re.sub(self.summarystatistics.K, "", infra_facility)
        learning_outcome_text = self.summarystatistics.get_pgi_card_learning_outcome_text()
        infra_facility_text = self.summarystatistics.get_pgi_card_infra_and_facility_text()
        if pgi_info is not None and learning_outcome_text is not None and infra_facility_text is not None:
            print("PGI Card Value is showing")
            self.logger.info("*********** PGI Card Value is showing ***************")
        else:
            print("PGI Card Value is Missing")
            self.logger.error("*************** PGI Card Value is Missing ************")
            assert False
        if float(learning_outcome_value) >= 0 and learning_outcome_value is not None:
            print("PGI Card Values is showing")
            self.logger.info("*********** PGI Card Values is showing ***************")
        else:
            print("PGI Card Value is not showing")
            self.logger.error("*************** PGI Card Values is Missing ************")
            assert False
        if float(infra_facility_value) >= 0 and infra_facility_value is not None:
            print("PGI Card Values is showing")
            self.logger.info("*********** PGI Card Values is showing ***************")
        else:
            print("PGI Card Value is not showing")
            self.logger.error("*************** PGI Card Values is Missing ************")
        self.logger.info("*************** Tc_cQube_summary_statistics_013 Testing Ended. *****************")

    def test_check_navigation_to_pgi_dashboard(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_014 Testing Started *****************")
        time.sleep(8)
        self.summarystatistics.click_on_access_pgi_dashboard()
        time.sleep(7)
        if 'pgi' in self.driver.current_url and 'Performance Grading Index ' in self.driver.page_source:
            print("PGI Dashboard is Displayed")
            self.logger.info("******************* PGI Dashboard is Displayed ********************")
        else:
            print("PGI Dashboard is not Displayed")
            self.logger.error("*************** PGI Dashboard Button is not Working ******************")
            assert False
        self.summarystatistics.click_summary_statistics()
        self.logger.info("*************** Tc_cQube_summary_statistics_014 Testing Ended *****************")

    def test_validate_pm_poshan_card_metrics(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_013 Testing Started *****************")
        time.sleep(5)
        pm_poshan_info = self.summarystatistics.get_pm_poshan_card_info()
        total_dist = self.summarystatistics.get_pm_poshan_card_total_dist_value()
        total_dist_value = re.sub(self.summarystatistics.L, "", total_dist)
        total_meals = self.summarystatistics.get_pm_poshan_card_total_meals_value()
        total_meals_value = re.sub(self.summarystatistics.K, "", total_meals)
        total_dist_text = self.summarystatistics.get_pm_poshan_card_total_dist_text()
        total_meals_text = self.summarystatistics.get_pm_poshan_card_total_meals_text()
        if pm_poshan_info is not None and total_dist_text is not None and total_meals_text is not None:
            print("Pm_poshan Card Value is showing")
            self.logger.info("*********** Pm_poshan Card Value is showing ***************")
        else:
            print("Pm_poshan Card Value is Missing")
            self.logger.error("*************** Pm_poshan Card Value is Missing ************")
            assert False
        if float(total_dist_value) >= 0 and total_dist_value is not None:
            print("Pm_poshan Card Values is showing")
            self.logger.info("*********** Pm_poshan Card Values is showing ***************")
        else:
            print("Pm_poshan Card Value is not showing")
            self.logger.error("*************** Pm_poshan Card Values is Missing ************")
            assert False
        if float(total_meals_value) >= 0 and total_meals_value is not None:
            print("Pm_poshan Card Values is showing")
            self.logger.info("*********** Pm_poshan Card Values is showing ***************")
        else:
            print("Pm_poshan Card Value is not showing")
            self.logger.error("*************** Pm_poshan Card Values is Missing ************")
        self.logger.info("*************** Tc_cQube_summary_statistics_013 Testing Ended. *****************")

    def test_check_navigation_to_pm_poshan_dashboard(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_014 Testing Started *****************")
        self.summarystatistics.click_on_access_pm_poshan_dashboard()
        time.sleep(3)
        if 'pmposhan' in self.driver.current_url and 'PM POSHAN' in self.driver.page_source:
            print("pmposhan Dashboard is Displayed")
            self.logger.info("******************* PGI Dashboard is Displayed ********************")
        else:
            print("pmposhan Dashboard is not Displayed")
            self.logger.error("*************** pmposhan Dashboard Button is not Working ******************")
            assert False
        self.summarystatistics.click_summary_statistics()
        self.logger.info("*************** Tc_cQube_summary_statistics_014 Testing Ended *****************")

    def test_validate_udise_card_metrics(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_015 Testing Started *****************")
        time.sleep(5)
        udise_info = self.summarystatistics.get_udise_card_info()
        total_students = self.summarystatistics.get_udise_card_total_students_value()
        total_students_value = re.sub(self.summarystatistics.L, "", total_students)
        ptr = self.summarystatistics.get_udise_card_ptr_value()
        ptr_value = re.sub(self.summarystatistics.K, "", ptr)
        total_students_text = self.summarystatistics.get_udise_card_total_students_text()
        ptr_text = self.summarystatistics.get_udise_card_ptr_text()
        if udise_info is not None and total_students_text is not None and ptr_text is not None:
            print("udise Card Value is showing")
            self.logger.info("*********** udise Card Value is showing ***************")
        else:
            print("udise Card Value is Missing")
            self.logger.error("*************** udise Card Value is Missing ************")
            assert False
        if float(total_students_value) >= 0 and total_students_value is not None:
            print("udise Card Values is showing")
            self.logger.info("*********** udise Card Values is showing ***************")
        else:
            print("udise Card Value is not showing")
            self.logger.error("*************** udise Card Values is Missing ************")
            assert False
        if float(ptr_value) >= 0 and ptr_value is not None:
            print("udise Card Values is showing")
            self.logger.info("*********** udise Card Values is showing ***************")
        else:
            print("udise Card Value is not showing")
            self.logger.error("*************** udise Card Values is Missing ************")
        self.logger.info("*************** Tc_cQube_summary_statistics_015 Testing Ended. *****************")

    def test_check_navigation_to_udise_dashboard(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_016 Testing Started *****************")
        time.sleep(4)
        self.summarystatistics.click_on_access_udise_dashboard()
        time.sleep(6)
        if 'udise' in self.driver.current_url and 'UDISE+' in self.driver.page_source:
            print("udise Dashboard is Displayed")
            self.logger.info("******************* udise Dashboard is Displayed ********************")
        else:
            print("udise Dashboard is not Displayed")
            self.logger.error("*************** udise Dashboard Button is not Working ******************")
            assert False
        self.summarystatistics.click_summary_statistics()
        self.logger.info("*************** Tc_cQube_summary_statistics_016 Testing Ended *****************")

    def test_validate_nas_card_metrics(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_017 Testing Started *****************")
        time.sleep(5)
        nas_info = self.summarystatistics.get_nas_card_info()
        total_schools = self.summarystatistics.get_nas_card_total_schools_value()
        total_schools_value = re.sub(self.summarystatistics.L, "", total_schools)
        total_students_surveyed = self.summarystatistics.get_nas_card_total_students_surveyed_value()
        total_students_surveyed_value = re.sub(self.summarystatistics.K, "", total_students_surveyed)
        total_schools_text = self.summarystatistics.get_nas_card_total_schools_text()
        total_students_surveyed_text = self.summarystatistics.get_nas_card_total_students_surveyed_text()
        if nas_info is not None and total_schools_text is not None and total_students_surveyed_text is not None:
            print("nas Card Value is showing")
            self.logger.info("*********** nas Card Value is showing ***************")
        else:
            print("nas Card Value is Missing")
            self.logger.error("*************** nas Card Value is Missing ************")
            assert False
        if float(total_schools_value) >= 0 and total_schools_value is not None:
            print("nas Card Values is showing")
            self.logger.info("*********** nas Card Values is showing ***************")
        else:
            print("nas Card Value is not showing")
            self.logger.error("*************** nas Card Values is Missing ************")
            assert False
        if float(total_students_surveyed_value) >= 0 and total_students_surveyed_value is not None:
            print("nas Card Values is showing")
            self.logger.info("*********** nas Card Values is showing ***************")
        else:
            print("nas Card Value is not showing")
            self.logger.error("*************** nas Card Values is Missing ************")
        self.logger.info("*************** Tc_cQube_summary_statistics_017 Testing Ended. *****************")

    def test_check_navigation_to_nas_dashboard(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_018 Testing Started *****************")
        time.sleep(4)
        self.summarystatistics.click_on_access_nas_dashboard()
        time.sleep(8)
        if 'nas' in self.driver.current_url and 'National Achievement Survey' in self.driver.page_source:
            print("nas Dashboard is Displayed")
            self.logger.info("******************* nas Dashboard is Displayed ********************")
        else:
            print("nas Dashboard is not Displayed")
            self.logger.error("*************** nas Dashboard Button is not Working ******************")
            assert False
        self.summarystatistics.click_summary_statistics()
        self.logger.info("*************** Tc_cQube_summary_statistics_018 Testing Ended *****************")

    def test_validate_diksha_card_metrics(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_017 Testing Started *****************")
        time.sleep(5)
        diksha_info = self.summarystatistics.get_diksha_card_info()
        overall_etb_coverge = self.summarystatistics.get_diksha_card_Overall_ETB_Coverage_value()
        overall_etb_coverge_value = re.sub(self.summarystatistics.L, "", overall_etb_coverge)
        overall_content_coverage = self.summarystatistics.get_diksha_card_Content_Coverage_on_QR_value()
        overall_content_coverage_value = re.sub(self.summarystatistics.K, "", overall_content_coverage)
        overall_etb_coverge_text = self.summarystatistics.get_diksha_card_Overall_ETB_Coverage_text()
        overall_content_coverage_text = self.summarystatistics.get_diksha_card_Content_Coverage_on_QR_text()
        if diksha_info is not None and overall_etb_coverge_text is not None and overall_content_coverage_text is not None:
            print("diksha Card Value is showing")
            self.logger.info("*********** diksha Card Value is showing ***************")
        else:
            print("diksha Card Value is Missing")
            self.logger.error("*************** diksha Card Value is Missing ************")
            assert False
        if float(overall_etb_coverge_value) >= 0 and overall_etb_coverge_value is not None:
            print("diksha Card Values is showing")
            self.logger.info("*********** diksha Card Values is showing ***************")
        else:
            print("diksha Card Value is not showing")
            self.logger.error("*************** diksha Card Values is Missing ************")
            assert False
        if float(overall_content_coverage_value) >= 0 and overall_content_coverage_value is not None:
            print("diksha Card Values is showing")
            self.logger.info("*********** diksha Card Values is showing ***************")
        else:
            print("diksha Card Value is not showing")
            self.logger.error("*************** diksha Card Values is Missing ************")
        self.logger.info("*************** Tc_cQube_summary_statistics_017 Testing Ended. *****************")

    def test_check_navigation_to_diksha_dashboard(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_018 Testing Started *****************")
        self.summarystatistics.click_on_access_diksha_dashboard()
        time.sleep(3)
        if 'diksha' in self.driver.current_url and 'DIKSHA- ETB and eContent' in self.driver.page_source:
            print("diksha Dashboard is Displayed")
            self.logger.info("******************* diksha Dashboard is Displayed ********************")
        else:
            print("diksha Dashboard is not Displayed")
            self.logger.error("*************** diksha Dashboard Button is not Working ******************")
            assert False
        self.summarystatistics.click_summary_statistics()
        self.logger.info("*************** Tc_cQube_summary_statistics_018 Testing Ended *****************")

    def test_validate_nishtha_card_metrics(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_015 Testing Started *****************")
        time.sleep(5)
        nishtha_info = self.summarystatistics.get_nishtha_card_info()
        enrolment = self.summarystatistics.get_nishtha_card_enrolment_value()
        enrolment_value = re.sub(self.summarystatistics.L, "", enrolment)
        completion = self.summarystatistics.get_nishtha_card_completion_value()
        completion_value = re.sub(self.summarystatistics.K, "", completion)
        enrolment_text = self.summarystatistics.get_nishtha_card_enrolment_text()
        completion_text = self.summarystatistics.get_nishtha_card_completion_text()
        if nishtha_info is not None and enrolment_text is not None and completion_text is not None:
            print("Nishtha Card Value is showing")
            self.logger.info("*********** Nishtha Card Value is showing ***************")
        else:
            print("Nishtha Card Value is Missing")
            self.logger.error("*************** Nishtha Card Value is Missing ************")
            assert False
        if float(enrolment_value) > 0 and enrolment_value is not None:
            print("Nishtha Card Values is showing")
            self.logger.info("*********** Nishtha Card Values is showing ***************")
        else:
            print("Nishtha Card Value is not showing")
            self.logger.error("*************** Nishtha Card Values is Missing ************")
            assert False
        if float(completion_value) > 0 and completion_value is not None:
            print("Nishtha Card Values is showing")
            self.logger.info("*********** Nishtha Card Values is showing ***************")
        else:
            print("Nishtha Card Value is not showing")
            self.logger.error("*************** Nishtha Card Values is Missing ************")
        self.logger.info("*************** Tc_cQube_summary_statistics_015 Testing Ended. *****************")

    """ This TestScript - Clicking the Access Dashboard of Nishtha Card"""

    def test_check_navigation_to_nishtha_dashboard(self):
        self.logger.info("*************** Tc_cQube_summary_statistics_016 Testing Started *****************")
        self.summarystatistics.click_on_access_nishtha_dashboard()
        time.sleep(2)
        if 'nishtha' in self.driver.current_url and 'NISHTHA' in self.driver.page_source:
            print("Nishtha Dashboard is Displayed")
            self.logger.info("******************* Nishtha Dashboard is Displayed ********************")
        else:
            print("Nishtha Dashboard is not Displayed")
            self.logger.error("*************** Nishtha Dashboard Button is not Working ******************")
            assert False
        self.summarystatistics.click_summary_statistics()
        self.logger.info("*************** Tc_cQube_summary_statistics_016 Testing Ended *****************")
