import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Page_of_objects.CqubeUi.BasePage import Base


class nishtha(Base):
    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"
    state_officer = (By.ID, "state")
    nishtha_menu = (By.ID, "menu-item-7")
    level = "state"

    Implementation_Status_tab = (By.XPATH, "//*[contains(text(),'Implementation Status')]")
    Course_medium_tab = (By.XPATH, "//*[contains(text(),'Courses and Mediums status')]")
    Potential_Base_tab = (By.XPATH, "//*[contains(text(),'% against Potential Base')]")
    District_wise_tab = (By.XPATH, "//*[contains(text(),'District wise Status')]")
    Course_wise_tab = (By.XPATH, "//*[contains(text(),'Course wise Status')]")

    implementation_tab_status = "//div[@role='tab'][1]"
    course_medium_tab_status = "//div[@role='tab'][2]"
    potential_tab_status = "//div[@role='tab'][3]"
    district_wise_tab_status = "//div[@role='tab'][4]"
    course_wise_tab_status = "//div[@role='tab'][5]"
    program_selection = "//div[starts-with(@id,'a') and contains(@id,'-{}')]"
    program_title = "//div[starts-with(@id,'a') and contains(@id,'-{}')]/span"
    tab_status = 'aria-selected'
    # Courses and Medium status
    state_colmn = (By.XPATH, "//*[@role='row']/td[1]")
    course_launch = (By.XPATH, "//*[@role='row']/td[2]")
    Medium = (By.XPATH, "//*[@role='row']/td[3]")
    CM_status = (By.ID, "mat-tab-label-0-1")
    dropdown_options = (By.XPATH, "//div[@role='option']/span")
    Choose_Program = (By.XPATH, "//div[@role='combobox']/input")
    choose_states = (By.XPATH, "//*[@id='filter-State/UT']/div/div/div[3]/input")
    total_enrolment_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_enrolment_label = (By.XPATH, "//app-big-number/div/div[2]")
    total_completion_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_completion_label = (By.XPATH, "//app-big-number/div/div[2]")
    total_Certification_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_Certification_label = (By.XPATH, "//app-big-number/div/div[2]")
    total_Mediums_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_Mediums_label = (By.XPATH, "//app-big-number/div/div[2]")

    Program_header = "//div[contains(text(),'Program Name')]"
    nishtha_Started_header = "//div[contains(text(),'Nishtha Started')]"
    # medium_header = "//div[contains(text(),'Total Mediums')]"

    program_sort = "//th[@role='columnheader'][1]"
    nishtha_started_sort = "//th[@role='columnheader'][2]"
    medium_sort = "//th[@role='columnheader'][3]"

    state_values = "//td[1]"
    course_values = "//td[2]"
    medium_values = "//td[3]"

    program_name_column = "//div/table/tbody/tr[{}]/td[1]"
    total_course_column = "//div/table/tbody/tr[{}]/td[2]"
    medium_column = "//div/table/tbody/tr[{}]/td[3]"

    total_course_launched_header = "//div[contains(text(),'Total Courses Launched')]"
    medium_header = "//div[contains(text(),'Total Mediums')]"

    total_course_launched_sort = "//th[@role='columnheader'][2]"

    download_button = (By.ID, "downloadButton")

    stacked_bars = (By.CSS_SELECTOR, "rect.highcharts-point")
    home_button = (By.ID, "homeButton")
    logout_button = (By.ID, "signOut")
    fullscreen_button = (By.ID, "fullscreen-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.count = 0

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

    def click_on_access_nishtha_menu(self):
        self.click(self.nishtha_menu)

    def click_menu(self):
        self.click(self.nishtha_menu)

    def test_click_on_state_button(self):
        self.click(self.state_officer)

    def test_click_on_home_button(self):
        self.click(self.home_button)

    def test_click_logout_button(self):
        self.click(self.logout_button)

    def click_on_implementation_tab(self):
        self.click(self.implementation_tab_status)

    def click_on_course_and_medium_tab(self):
        self.click(self.Course_medium_tab)

    def click_on_potential_tab(self):
        self.click(self.Potential_Base_tab)

    def click_on_district_status_tab(self):
        self.click(self.District_wise_tab)

    def click_on_course_status_tab(self):
        self.click(self.Course_wise_tab)

    def click_implementation_status_tab(self):
        self.click(self.Implementation_Status_tab)

    def click_implementation_status(self):
        result = self.driver.find_element(By.XPATH, self.implementation_tab_status).get_attribute('aria-selected')
        return result
        # return self.get_attribute_value('aria-selected', self.Implementation_Status_tab)

    def click_course_and_medium_status(self):
        result = self.driver.find_element(By.XPATH, self.course_medium_tab_status).get_attribute('aria-selected')
        return result

    def click_per_against_potential_base(self):
        result = self.driver.find_element(By.XPATH, self.potential_tab_status).get_attribute('aria-selected')
        return result

    def click_course_wise_status(self):
        result = self.driver.find_element(By.XPATH, self.course_wise_tab_status).get_attribute('aria-selected')
        return result

    def click_district_wise_status(self):
        result = self.driver.find_element(By.XPATH, self.district_wise_tab_status).get_attribute('aria-selected')
        return result

    def click_course_and_medium_status1(self):
        return self.get_attribute_value('aria-selected', self.course_medium_tab_status)

    def get_implementation_status_tab(self):
        return self.get_attribute_value('aria-selected', self.Implementation_Status_tab)

    def get_total_Enrolment_value(self):
        return self.get_web_element_text(self.total_enrolment_value)

    def get_total_Enrolment_label(self):
        return self.get_web_element_text(self.total_enrolment_label)

    def get_total_completion_value(self):
        return self.get_web_element_text(self.total_completion_value)

    def get_total_completion_label(self):
        return self.get_web_element_text(self.total_completion_label)

    def get_total_Certification_value(self):
        return self.get_web_element_text(self.total_Certification_value)

    def get_total_Certification_label(self):
        return self.get_web_element_text(self.total_Certification_value)

    def get_total_Mediums_value(self):
        return self.get_web_element_text(self.total_Mediums_value)

    def get_total_Mediums_label(self):
        return self.get_web_element_text(self.total_Mediums_label)

    def get_count_of_bars_in_chart(self):
        return self.get_web_elements(self.stacked_bars)

    def click_fullscreen_button(self):
        self.click(self.fullscreen_button)

    def check_table_program_headers_clickable(self):
        status = self.driver.find_element(By.XPATH, self.program_sort).get_attribute('aria-sort')
        self.driver.find_element(By.XPATH, self.Program_header).click()
        time.sleep(2)
        now = self.driver.find_element(By.XPATH, self.program_sort).get_attribute('aria-sort')
        sort = "descending"
        if now == 'ascending' or sort:
            assert True
        else:
            print(status, now, 'Table value order is not changed so sorting is not working')
            self.count = self.count + 1
        self.driver.find_element(By.XPATH, self.Program_header).click()
        time.sleep(2)
        sec_click = self.driver.find_element(By.XPATH, self.program_sort).get_attribute('aria-sort')
        sort = "descending"
        if sec_click == 'ascending' or sort:
            assert True
        else:
            self.count = self.count + 1
        return self.count

    def test_check_nishtha_started_headers_clickable(self):
        status = self.driver.find_element(By.XPATH, self.nishtha_started_sort).get_attribute('aria-sort')
        self.driver.find_element(By.XPATH, self.nishtha_Started_header).click()
        now = self.driver.find_element(By.XPATH, self.nishtha_started_sort).get_attribute('aria-sort')
        sort = "descending"
        if now == 'ascending' or sort:
            assert True
        else:
            print(status, now, "********Course launched Header sorting is not working ***********")
            self.count = self.count + 1
        self.driver.find_element(By.XPATH, self.nishtha_Started_header).click()
        sec_click = self.driver.find_element(By.XPATH, self.nishtha_started_sort).get_attribute('aria-sort')
        sort = "descending"
        if sec_click == 'ascending' or sort:
            assert True
        else:
            print(status, now, "********Course launched Header sorting is not working ***********")
            self.count = self.count + 1
        return self.count

    '''Function to check with state values '''

    def test_check_program_table_values(self):
        program_values = []
        state_name = self.driver.find_elements(By.XPATH, self.state_values)
        for i in range(1, len(state_name)):
            program_list = self.driver.find_element(By.XPATH, self.program_name_column.format(i))
            program_values.append(program_list.text)
        for j in range(len(program_values)):
            st_name = program_values[j]
            if st_name != st_name.lower() and st_name != st_name.upper() and "_" not in st_name:
                print("************ State Names are In Camel Cases *****************")
            else:
                print("**************** State Name are not in Camel Cases ")
                self.count = self.count + 1
        if len(program_values) == len(state_name) - 1:
            print("************ State Table values are showing ****************")
            assert True
        else:
            print("************ State names are not showing **************")
            self.count = self.count + 1
        return self.count

    '''Function to check with course values '''

    def test_check_course_table_values(self):
        course_tablevals = []
        course_name = self.driver.find_elements(By.XPATH, self.course_values)
        for i in range(1, len(course_name)):
            state_list = self.driver.find_element(By.XPATH, self.total_course_column.format(i))
            course_tablevals.append(state_list.text)
            time.sleep(2)
        if len(course_tablevals) == len(course_name) - 1:
            assert True
            print("************ Course Table Values are showing ****************")
        else:
            print("************ Course Values are not showing **************")
            self.count = self.count + 1
        for i in range(len(course_tablevals)):
            if course_tablevals[i] is not str and course_tablevals[i] is not None:
                print("*********** Course Values are Integers  *************")
                assert True
            else:
                print("*********** Course Values are Not Integers *************")
                self.count = self.count + 1
        return self.count

    '''Function to check with medium values '''

    def test_check_medium_table_values(self):
        medium_tablevals = []
        medium_val = self.driver.find_elements(By.XPATH, self.medium_values)
        for i in range(1, len(medium_val)):
            state_list = self.driver.find_element(By.XPATH, self.medium_column.format(i))
            medium_tablevals.append(state_list.text)
        if len(medium_tablevals) == len(medium_val) - 1:
            assert True
        else:
            print(len(medium_tablevals), len(medium_val),
                  "************ Medium Values are not showing **************")
            self.count = self.count + 1
        for i in range(len(medium_tablevals)):
            if medium_tablevals[i] is not str:
                print("*********** Medium Values are Integers  *************")
                assert True
            else:
                print("*********** Course Values are Not Integers *************")
                self.count = self.count + 1
        return self.count

    def check_table_course_program_headers_clickable(self):
        status = self.driver.find_element(By.XPATH, self.program_sort).get_attribute('aria-sort')
        self.driver.find_element(By.XPATH, self.Program_header).click()
        time.sleep(2)
        now = self.driver.find_element(By.XPATH, self.program_sort).get_attribute('aria-sort')
        sort = "descending"
        if now == 'ascending' or sort:
            assert True
        else:
            print(status, now, 'Table value order is not changed so sorting is not working')
            self.count = self.count + 1
        self.driver.find_element(By.XPATH, self.Program_header).click()
        time.sleep(2)
        sec_click = self.driver.find_element(By.XPATH, self.program_sort).get_attribute('aria-sort')
        sort = "descending"
        if sec_click == 'ascending' or sort:
            assert True
        else:
            self.count = self.count + 1
        return self.count

    '''Function to check course table header - sorting functionality is working or not '''

    def test_check_table_courses_headers_clickable(self):
        status = self.driver.find_element(By.XPATH, self.total_course_launched_sort).get_attribute('aria-sort')
        self.driver.find_element(By.XPATH, self.total_course_launched_header).click()
        now = self.driver.find_element(By.XPATH, self.total_course_launched_sort).get_attribute('aria-sort')
        sort = "descending"
        if now == 'ascending' or sort:
            assert True
        else:
            print(status, now, "********Course launched Header sorting is not working ***********")
            self.count = self.count + 1
        self.driver.find_element(By.XPATH, self.total_course_launched_header).click()
        sec_click = self.driver.find_element(By.XPATH, self.total_course_launched_sort).get_attribute('aria-sort')
        sort = "descending"
        if sec_click == 'ascending' or sort:
            assert True
        else:
            print(status, now, "********Course launched Header sorting is not working ***********")
            self.count = self.count + 1
        return self.count

    '''Function to check medium table header - sorting functionality is working or not '''

    def test_check_table_mediums_headers_clickable(self):
        status = self.driver.find_element(By.XPATH, self.medium_sort).get_attribute('aria-sort')
        self.driver.find_element(By.XPATH, self.medium_header).click()
        now = self.driver.find_element(By.XPATH, self.medium_sort).get_attribute('aria-sort')
        if status != now:
            assert True
            print("*********** Courses Launched table header is Sorting working *****************")
        else:
            print(status, now, "******** Course launched Header sorting is not working ***********")
            self.count = self.count + 1
        self.driver.find_element(By.XPATH, self.total_course_launched_header).click()
        sec_click = self.driver.find_element(By.XPATH, self.total_course_launched_sort).get_attribute('aria-sort')
        sort = "descending"
        if sec_click == 'ascending' or sort:
            assert True
        else:
            print(status, now, "******** Medium Header sorting is not working ***********")
            self.count = self.count + 1
        return self.count

    '''Function to check with state values '''



    def click_download_button(self):
        self.click(self.download_button)

    def get_course_wise_stacked_bar_tooltip_validation(self):
        lst = self.get_count_of_bars_in_chart()
        if len(lst) == 0:
            self.count = self.count + 1
        else:
            for x in range(len(lst) - 1):
                act = ActionChains(self.driver)
                act.move_to_element(lst[x]).perform()
                act.pause(5)
            return self.count
