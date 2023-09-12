from selenium.webdriver.common.by import By
from Page_of_objects.CqubeUi.BasePage import Base


class Summarystatistics(Base):
    """ List of selenium locator of summary statistics screen """

    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"
    state_officer = (By.ID, "state")
    click_summary_statistics_btn = (By.ID, "menu-item-0")
    L = r'L\.|[^\d.]'
    K = r'K\.|[^\d.]'

    '''teacher attendance Card '''
    TA_info = (By.XPATH, "//div[1]/sb-cqube-program-card/div/img")
    TA_total_enrolment = (By.XPATH, "//div[1]/sb-cqube-program-card/div/div[2]/div/span[1]")
    TA_completion_text = (By.XPATH, "//div[1]/sb-cqube-program-card/div/div[2]/div/span[2]")
    TA_dashboard = (By.XPATH, "//*[@id='dashboard-item-0']/div/button")

    '''pgi Card '''
    pgi_info = (By.XPATH, "//div[2]/sb-cqube-program-card/div/img")
    pgi_learning_outcome = (By.XPATH, "//div[2]/sb-cqube-program-card/div/div[2]/div[1]/span[1]")
    pgi_infra_facility = (By.XPATH, "//div[2]/sb-cqube-program-card/div/div[2]/div[2]/span[1]")
    pgi_learning_outcome_text = (By.XPATH, "//div[2]/sb-cqube-program-card/div/div[2]/div[1]/span[2]")
    pgi_infra_facility_text = (By.XPATH, "//div[2]/sb-cqube-program-card/div/div[2]/div[2]/span[2]")
    pgi_dashboard = (By.XPATH, "//*[@id='dashboard-item-1']/div/button")

    '''pm_poshan Card '''
    pm_poshan_info = (By.XPATH, "//div[3]/sb-cqube-program-card/div/img")
    pm_poshan_total_dist = (By.XPATH, "//div[3]/sb-cqube-program-card/div/div[2]/div[1]/span[1]")
    pm_poshan_total_meals = (By.XPATH, "//div[3]/sb-cqube-program-card/div/div[2]/div[2]/span[1]")
    pm_poshan_total_dist_text = (By.XPATH, "//div[3]/sb-cqube-program-card/div/div[2]/div[1]/span[2]")
    pm_poshan_total_meals_text = (By.XPATH, "//div[3]/sb-cqube-program-card/div/div[2]/div[2]/span[2]")
    pm_poshan_dashboard = (By.XPATH, "//*[@id='dashboard-item-2']/div/button")

    '''udise Card '''
    udise_info = (By.XPATH, "//div[4]/sb-cqube-program-card/div/img")
    udise_total_students = (By.XPATH, "//div[4]/sb-cqube-program-card/div/div[2]/div[1]/span[1]")
    udise_PTR = (By.XPATH, "//div[4]/sb-cqube-program-card/div/div[2]/div[2]/span[1]")
    udise_total_students_text = (By.XPATH, "//div[4]/sb-cqube-program-card/div/div[2]/div[1]/span[2]")
    udise_PTR_text = (By.XPATH, "//div[4]/sb-cqube-program-card/div/div[2]/div[2]/span[2]")
    udise_dashboard = (By.XPATH, "//*[@id='dashboard-item-3']/div/button")

    '''nas Card '''
    nas_info = (By.XPATH, "//div[5]/sb-cqube-program-card/div/img")
    nas_total_schools = (By.XPATH, "//div[5]/sb-cqube-program-card/div/div[2]/div[1]/span[1]")
    nas_total_students_surveyed = (By.XPATH, "//div[5]/sb-cqube-program-card/div/div[2]/div[2]/span[1]")
    nas_total_schools_text = (By.XPATH, "//div[5]/sb-cqube-program-card/div/div[2]/div[1]/span[2]")
    nas_total_students_surveyed_text = (By.XPATH, "//div[5]/sb-cqube-program-card/div/div[2]/div[2]/span[2]")
    nas_dashboard = (By.XPATH, "//*[@id='dashboard-item-4']/div/button")

    '''diksha Card '''
    diksha_info = (By.XPATH, "//div[6]/sb-cqube-program-card/div/img")
    diksha_Overall_ETB_Coverage = (By.XPATH, "//div[6]/sb-cqube-program-card/div/div[2]/div[1]/span[1]")
    diksha_Content_Coverage_on_QR = (By.XPATH, "//div[6]/sb-cqube-program-card/div/div[2]/div[2]/span[1]")
    diksha_Overall_ETB_Coverage_text = (By.XPATH, "//div[6]/sb-cqube-program-card/div/div[2]/div[1]/span[2]")
    diksha_Content_Coverage_on_QR_text = (By.XPATH, "//div[6]/sb-cqube-program-card/div/div[2]/div[2]/span[2]")
    diksha_dashboard = (By.XPATH, "//*[@id='dashboard-item-5']/div/button")

    '''Nishtha Card '''
    nishtha_info = (By.XPATH, "//div[7]/sb-cqube-program-card/div/img")
    nishtha_total_enrolment = (By.XPATH, "//div[7]/sb-cqube-program-card/div/div[2]/div[1]/span[1]")
    nishtha_total_completion = (By.XPATH, "//div[7]/sb-cqube-program-card/div/div[2]/div[2]/span[1]")
    nishtha_enrolment_text = (By.XPATH, "//div[7]/sb-cqube-program-card/div/div[2]/div[1]/span[2]")
    nishtha_completion_text = (By.XPATH, "//div[7]/sb-cqube-program-card/div/div[2]/div[2]/span[2]")
    nishtha_dashboard = (By.XPATH, "//*[@id='dashboard-item-6']/div/button")

    home_button = (By.ID, "homeButton")
    logout_button = (By.ID, "signOut")

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    def test_click_on_state_button(self):
        self.click(self.state_officer)

    def get_nishtha_card_info(self):
        return self.get_attribute_value('title', self.nishtha_info)

    def get_nishtha_card_enrolment_value(self):
        return self.get_web_element_text(self.nishtha_total_enrolment)

    def get_nishtha_card_completion_value(self):
        return self.get_web_element_text(self.nishtha_total_completion)

    def get_nishtha_card_enrolment_text(self):
        return self.get_web_element_text(self.nishtha_enrolment_text)

    def get_nishtha_card_completion_text(self):
        return self.get_web_element_text(self.nishtha_completion_text)

    def click_on_access_nishtha_dashboard(self):
        self.click(self.nishtha_dashboard)

    def test_click_on_home_button(self):
        self.click(self.home_button)

    def test_click_logout_button(self):
        self.click(self.logout_button)

    ''' Teacher attendance '''

    def get_teacher_attendance_card_info(self):
        return self.get_attribute_value('title', self.TA_info)

    def get_teacher_attendance_card_Avg_teacher_present_value(self):
        return self.get_web_element_text(self.TA_total_enrolment)

    def get_teacher_attendance_card_Avg_teacher_present_text(self):
        return self.get_web_element_text(self.TA_completion_text)

    def click_on_access_teacher_attendance_dashboard(self):
        self.click(self.TA_dashboard)

    ''' PGI '''

    def get_pgi_card_info(self):
        return self.get_attribute_value('title', self.pgi_info)

    def get_pgi_card_learning_outcome_value(self):
        return self.get_web_element_text(self.pgi_learning_outcome)

    def get_pgi_card_infra_and_facility_value(self):
        return self.get_web_element_text(self.pgi_infra_facility)

    def get_pgi_card_learning_outcome_text(self):
        return self.get_web_element_text(self.pgi_learning_outcome_text)

    def get_pgi_card_infra_and_facility_text(self):
        return self.get_web_element_text(self.pgi_infra_facility_text)

    def click_on_access_pgi_dashboard(self):
        self.click(self.pgi_dashboard)

    ''' PM Poshan '''

    def get_pm_poshan_card_info(self):
        return self.get_attribute_value('title', self.pm_poshan_info)

    def get_pm_poshan_card_total_dist_value(self):
        return self.get_web_element_text(self.pm_poshan_total_dist)

    def get_pm_poshan_card_total_meals_value(self):
        return self.get_web_element_text(self.pm_poshan_total_meals)

    def get_pm_poshan_card_total_dist_text(self):
        return self.get_web_element_text(self.pm_poshan_total_dist_text)

    def get_pm_poshan_card_total_meals_text(self):
        return self.get_web_element_text(self.pm_poshan_total_meals_text)

    def click_on_access_pm_poshan_dashboard(self):
        self.click(self.pm_poshan_dashboard)

    ''' Udise '''

    def get_udise_card_info(self):
        return self.get_attribute_value('title', self.udise_info)

    def get_udise_card_total_students_value(self):
        return self.get_web_element_text(self.udise_total_students)

    def get_udise_card_ptr_value(self):
        return self.get_web_element_text(self.udise_PTR)

    def get_udise_card_total_students_text(self):
        return self.get_web_element_text(self.udise_total_students_text)

    def get_udise_card_ptr_text(self):
        return self.get_web_element_text(self.udise_PTR_text)

    def click_on_access_udise_dashboard(self):
        self.click(self.udise_dashboard)

    ''' NAS '''

    def get_nas_card_info(self):
        return self.get_attribute_value('title', self.nas_info)

    def get_nas_card_total_schools_value(self):
        return self.get_web_element_text(self.nas_total_schools)

    def get_nas_card_total_students_surveyed_value(self):
        return self.get_web_element_text(self.nas_total_students_surveyed)

    def get_nas_card_total_schools_text(self):
        return self.get_web_element_text(self.nas_total_schools_text)

    def get_nas_card_total_students_surveyed_text(self):
        return self.get_web_element_text(self.nas_total_students_surveyed_text)

    def click_on_access_nas_dashboard(self):
        self.click(self.nas_dashboard)

    ''' diksha '''

    def get_diksha_card_info(self):
        return self.get_attribute_value('title', self.diksha_info)

    def get_diksha_card_Overall_ETB_Coverage_value(self):
        return self.get_web_element_text(self.diksha_Overall_ETB_Coverage)

    def get_diksha_card_Content_Coverage_on_QR_value(self):
        return self.get_web_element_text(self.diksha_Content_Coverage_on_QR)

    def get_diksha_card_Overall_ETB_Coverage_text(self):
        return self.get_web_element_text(self.diksha_Overall_ETB_Coverage_text)

    def get_diksha_card_Content_Coverage_on_QR_text(self):
        return self.get_web_element_text(self.diksha_Content_Coverage_on_QR_text)

    def click_on_access_diksha_dashboard(self):
        self.click(self.diksha_dashboard)

    """This Function is used to click on the cQube dashboard"""

    def click_summary_statistics(self):
        self.click(self.click_summary_statistics_btn)
