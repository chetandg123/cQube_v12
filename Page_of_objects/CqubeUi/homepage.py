import time
from selenium.webdriver.common.by import By

from Page_of_objects.CqubeUi.BasePage import Base
from Utilities.ReadProperties import ReadConfig


class Homepage(Base):

    """ List of selenium locator of dashboard screen """

    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"
    login_page = "username1"
    state_officer = (By.ID, "state")
    district_officer = (By.ID, "district")
    block_officer = (By.ID, "block")
    cluster_officer = (By.ID, "cluster")
    cluster_dropdown = (By.ID, "clusterfilter")
    school_dropdown = (By.ID, "schoolfilter")
    grade_dropdown = (By.ID, "gradefilter")
    district_dropdown = (By.ID, "districtfilter")
    block_dropdown = (By.ID, "blockfilter")
    district_option1 = (By.XPATH, "//*[@id=a009eafb04fa-0]")
    block_option1 = (By.XPATH, "//*[@id=a009eafb04fa-0]")
    dropdown_options = (By.XPATH, "//div[@role='option']/span")
    dropdown_value = (By.XPATH, "//div[starts-with(@id,'a') and contains(@id,"'-'"{}" + ")]")
    student_attendance_compliance = (By.ID, "mat-tab-label-0-0")
    submit_btn = (By.ID, "submit")
    user_id = (By.ID, "username1")
    password = (By.ID, "password1")
    login = (By.ID, "login")
    home_button = (By.ID, "homeButton")
    logout_button = (By.ID, "signOut")
    student_attendance_menu = (By.ID, "menu-item-1")

    # username = (By.ID, "username1")
    # submit = (By.ID, "submit")
    # homebutton = (By.ID, "homeButton")
    # logout = (By.ID, "signOut")
    school_principal = (By.ID, "school")
    class_teacher = (By.ID, "grade")


    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.find_element(By.ID, "username1").send_keys(ReadConfig.get_username())
        self.driver.find_element(By.ID, "password1").send_keys(ReadConfig.get_password())
        time.sleep(2)
        self.click(self.login)

    def open_cqube_application(self):
        self.get_url(ReadConfig.get_application_url())
        time.sleep(5)



    def test_click_on_a_default_button(self):
        count = 0
        a_plus = self.driver.find_element(By.ID, self.a_default)
        a_plus.click()
        time.sleep(2)
        if 'style="font-size: 16px;"' in self.driver.page_source:
            self.driver.refresh()
        else:
            count = count + 1
        return count

    ''' Function to Click the A+ button '''

    def test_click_on_a_plus_button(self):
        count = 0
        a_plus = self.driver.find_element(By.ID, self.a_plus)
        a_plus.click()
        time.sleep(2)
        if 'style="font-size: 18px;"' in self.driver.page_source:
            self.driver.refresh()
        else:
            count = count + 1
        return count

    ''' Function to Click the A- button '''

    def test_click_on_a_minus_button(self):
        count = 0
        a_plus = self.driver.find_element(By.ID, self.a_minus)
        a_plus.click()
        time.sleep(2)
        if 'style="font-size: 14px;"' in self.driver.page_source:
            self.driver.refresh()
        else:
            count = count + 1
        return count

    def test_click_on_state_button(self):
        self.click(self.state_officer)

    def test_click_on_district_button(self):
        self.click(self.district_officer)

    def test_click_submit(self):
        self.click(self.submit_btn)

    def test_click_on_home_button(self):
        self.click(self.home_button)

    def test_click_logout_button(self):
        self.click(self.logout_button)

    def test_click_on_block_button(self):
        self.click(self.block_officer)

    def test_click_on_cluster_button(self):
        self.click(self.cluster_officer)

    def test_click_dist(self):
        self.click(self.district_dropdown)

    def test_click_block(self):
        self.click(self.block_dropdown)

    """This function is to get options in the dropdown"""

    def get_dropdown_values(self):
        dropdown_options = self.get_web_elements(self.dropdown_options)
        return dropdown_options


    def test_click_on_school_principal(self):
        self.click(self.school_principal)

    def test_click_on_class_teacher(self):
        self.click(self.class_teacher)

    def test_click_cluster(self):
        self.click(self.cluster_dropdown)

    def test_click_school(self):
        self.click(self.school_dropdown)

    def test_click_grade(self):
        self.click(self.grade_dropdown)

    def get_each_dropdown_value_id(self, column_id):
        dropdown_value = self.dropdown_value
        dropdown_value = list(dropdown_value)
        dropdown_value[1] = dropdown_value[1].format(column_id)
        dropdown_value = tuple(dropdown_value)
        res = self.get_web_element((By.XPATH, str(dropdown_value[1])))
        return res





