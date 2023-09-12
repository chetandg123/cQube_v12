import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Page_of_objects.CqubeUi.BasePage import Base


def get_download_dir():
    cwd = os.path.dirname(__file__)
    download_path = os.path.join(cwd, '../../Downloads')
    return download_path


class Nas(Base):
    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"
    state_officer = (By.ID, "state")
    nas_menu = (By.ID, "menu-item-5")
    district_Wise_Performance = (By.XPATH, "//mat-tab-group/mat-tab-header/div/div/div/div")
    grade_and_Subject_Performance = (By.XPATH, "//mat-tab-group/mat-tab-header/div/div/div/div[2]")
    total_schools_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_schools_label = (By.XPATH, "//app-big-number/div/div[2]")
    total_Students_Surveyed_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_Students_Surveyed_label = (By.XPATH, "//app-big-number/div/div[2]")
    total_teachers_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_teachers_label = (By.XPATH, "//app-big-number/div/div[2]")
    fullscreen_button = (By.ID, "fullscreen-button")
    download_button = (By.ID, "downloadButton")
    logout_button = (By.ID, "signOut")
    grade_wise = (By.ID, "filter-Grade")
    grade = (By.ID, "filter-Grade")
    options_dropdown = "//*[@role='option']"
    grade_values = (By.XPATH, options_dropdown)
    grade_dropdown_value = (By.XPATH, "//div[starts-with(@id,'a') and contains(@id,"'-'"{}" + ")]")
    subject = (By.ID, 'filter-Subject')
    subject_values = (By.XPATH, options_dropdown)
    subject_dropdown_value = (By.XPATH, "//div[starts-with(@id,'a') and contains(@id,"'-'"{}" + ")]")
    learning_outcome = (By.ID, 'filter-Learning Outcome Code')
    learning_outcome_values = (By.XPATH, options_dropdown)
    learning_outcome_dropdown_value = (By.XPATH, "//div[starts-with(@id,'a') and contains(@id,"'-'"{}" + ")]")
    state_option = (By.XPATH, options_dropdown)
    state_values = (By.XPATH, options_dropdown)
    chart_value = (By.TAG_NAME, "td")
    level = "state"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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

    def get_map_tooltip_info_validation(self):
        lst = self.driver.find_elements(By.CLASS_NAME, "leaflet-interactive")
        print("No of States", len(lst) - 1)
        blue_marks = 0
        white_marks = 0
        self.map_data = []
        for x in range(1, len(lst) - 1):
            if lst[x].get_attribute('fill') == '#FFFFFF':
                white_marks = white_marks + 1
            else:
                blue_marks = blue_marks + 1
            act = ActionChains(self.driver)
            act.move_to_element(lst[x]).perform()
            act.pause(4)
            # txt = self.driver.find_element(By.XPATH, "//div[@class='leaflet-pane leaflet-tooltip-pane']")
            # map_data.append(txt.text)
        # return map_data

    def click_on_access_nas_menu(self):
        self.click(self.nas_menu)

    def click_menu(self):
        self.click(self.nas_menu)

    def test_click_on_state_button(self):
        self.click(self.state_officer)

    def click_district_Wise_Performance_tab(self):
        self.click(self.district_Wise_Performance)

    def click_grade_and_subject_Performance_tab(self):
        self.click(self.grade_and_Subject_Performance)

    def click_district_wise_performance(self):
        return self.get_attribute_value('aria-selected', self.district_Wise_Performance)

    def get_district_Wise_Performance_tab(self):
        return self.get_attribute_value('aria-selected', self.district_Wise_Performance)

    def click_grade_and_subject_performance(self):
        return self.get_attribute_value('aria-selected', self.grade_and_Subject_Performance)

    def get_grade_and_Subject_Performance(self):
        return self.get_attribute_value('aria-selected', self.grade_and_Subject_Performance)

    def get_total_schools_value(self):
        return self.get_web_element_text(self.total_schools_value)

    def get_total_schools_label(self):
        return self.get_web_element_text(self.total_schools_label)

    def get_total_Students_Surveyed_value(self):
        return self.get_web_element_text(self.total_Students_Surveyed_value)

    def get_total_Students_Surveyed_label(self):
        return self.get_web_element_text(self.total_Students_Surveyed_label)

    def get_total_teachers_value(self):
        return self.get_web_element_text(self.total_teachers_value)

    def get_total_teachers_label(self):
        return self.get_web_element_text(self.total_teachers_label)

    def click_fullscreen_button(self):
        self.click(self.fullscreen_button)

    def click_download_button(self):
        self.click(self.download_button)

    def test_click_logout_button(self):
        self.click(self.logout_button)

    def get_data(self):
        res = self.get_web_elements(self.chart_value)
        return res

    """ This function is used to click on grade drop down"""

    def click_on_grade(self):
        self.click(self.grade_wise)

    """ This function is used to get grade values"""

    def get_grade_values(self):
        grade_values = self.get_web_elements(self.grade_values)
        return grade_values

    """ This function is used to click on subject drop down"""

    def click_on_subject(self):
        self.click(self.subject)

    def get_subject_values(self):
        subject_values = self.get_web_elements(self.subject_values)
        return subject_values

    """ This function is used to click on learning outcome drop down"""

    def click_on_learning_outcome(self):
        self.click(self.learning_outcome)

    """ This function is used to get learning outcome values"""

    def get_learning_outcome_values(self):
        learning_outcome_values = self.get_web_elements(self.learning_outcome_values)
        return learning_outcome_values

    def get_each_dropdown_value_id(self, grade_id):
        grade_dropdown_value = self.grade_dropdown_value
        grade_dropdown_value = list(grade_dropdown_value)
        grade_dropdown_value[1] = grade_dropdown_value[1].format(grade_id)
        grade_dropdown_value = tuple(grade_dropdown_value)
        res = self.get_web_element((By.XPATH, str(grade_dropdown_value[1])))
        return res
