import os
import time
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Page_of_objects.CqubeUi.BasePage import Base
from Utilities.ReadProperties import ReadConfig


def get_download_dir():
    cwd = os.path.dirname(__file__)
    download_path = os.path.join(cwd, '../../Downloads')
    return download_path


class Teacherattendance(Base):
    """ List of selenium locator of summary statistics screen """

    teacher_attendance = "menu-item-1"
    Average_Teachers_Reporting_Attendance_tab = (By.XPATH, "//mat-tab-header/div/div/div/div[1]")
    L = r'L\.|[^\d.]'
    K = r'K\.|[^\d.]'
    avg_teacher_present_attendance_value = "//app-big-number/div/div[1]/h1"
    avg_teacher_attendance_text = (By.XPATH, "//app-big-number/div/div[2]")
    district_header = (By.XPATH, "//tr/th[1]/div/div[1]")
    district_column = (By.XPATH, "//div/div/app-material-heat-chart-table/div/table/tbody/tr/td[1]")
    teachers_reporting_teacher_attendance_column = (By.XPATH, "//tr/td[2]/div")
    teachers_reporting_teacher_attendance_header = (
        By.XPATH, "//app-material-heat-chart-table/div/table/thead/tr/th[2]")
    fullscreen_button = (By.ID, "fullscreen-button")
    download_button = (By.ID, "downloadButton")
    map_view_of_teacher_attendance_tab = (By.XPATH, "//mat-tab-header/div/div/div/div[2]")
    csv_download = (By.ID, "download-csv")
    pdf_download = (By.ID, "download-pdf")
    avg_teacher_present_1 = (By.XPATH, "//div[@role='tab'][1]")
    calender_startdate = (By.ID, "mat-date-range-input-15")
    calender_enddate = (By.CLASS_NAME, "mat-end-date mat-date-range-input-inner ng-valid ng-touched ng-dirty")
    calender_open = "//button[@aria-label='Open calendar']"
    calender_open1 = "//button[@aria-label='Open calendar']"

    click_to_select_start_year = (By.XPATH, "(//button[@type='button'])[7]")

    select_start_year = "//button[@type='button']/div[contains(text(),{})]"
    select_start_month = "//button[@type='button']/div[contains(text(),'{}')]"
    select_start_date = "//button[@type='button']/div[contains(text(),{})]"

    click_to_select_end_year = "(//button[@type='button'])[7]"

    select_end_year = "//button[@type='button']/div[contains(text(),{})]"
    select_end_month = "//button[@type='button']/div[contains(text(),'{}')]"
    select_end_date = "//button[@type='button']/div[contains(text(),{})]"

    click_avg_teacher_attenadance_tab = (By.XPATH, " //div[text()='Average Teachers Present']")
    total_enrolment_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_enrolment_label = (By.XPATH, "//div[@class='report-name text-center']")
    school_report = (By.XPATH, "//span[text()='School Report']")
    unit_level_report = (By.XPATH, "//span[text()='Unit level report']")
    clear_button = (By.XPATH, "//mat-icon[text()='clear']")
    start_date = (By.XPATH, "//input[@placeholder='Start date']")
    end_date = (By.XPATH, "//input[@placeholder='End date']")
    first_district_tab = (By.XPATH, "(//th[1])[1]")
    dropdown_option_name = "//div[starts-with(@id,'a') and contains(@id,'-{}')]/span"
    table_headers = '//table/thead/tr/th'
    click_table_header = "(//th[@role='columnheader'])[{}]"
    list_of_option = (By.XPATH, "(//mat-select[@role='combobox'])[1]")
    options_list = "(//mat-option[@role='option'])[{}]"
    no_of_rows = (By.XPATH, "(//table[@class='mat-table cdk-table mat-sort'])[1]//tr[position()]//td[1]")
    dp = "//*[@id='mat-option-{}']"
    map_is_displayed = "//div[@id='map']"
    start_number = (By.XPATH, "//input[@id='fromRange']")
    end_number = (By.XPATH, "//input[@id='toRange']")
    pagination_teacher_present = (By.ID, "mat-select-0")
    pagination_bar_graph = (By.ID, "mat-select-2")
    pagination_school_teacher_present = (By.XPATH, "(//*[@role='combobox'])[3]")
    map = "//div[@id='map']"
    school_wise_percent_teacher_attendance = "//tbody/tr/td[6]"
    udise_code_search_bar = "(//input[@type='number'])[3]"
    option_list = "//*[@role='option']"
    number_options1 = "//*[starts-with(@id,'mat-option') and contains(@id,'-{}')]"
    number_options2 = "//mat-option[@role='option'][{}]"
    option_tab1 = "mat-select-0"
    option_tab2 = "mat-select-2"
    option_tab3 = "(//*[@role='combobox'])[3]"
    no_of_rows1 = "(//table[@class='mat-table cdk-table mat-sort'])[1]//tr[position()]//td[1]"
    no_of_rows2 = "(//table[@class='mat-table cdk-table mat-sort'])[2]//tr[position()]//td[1]"
    number_option_text1 = "(//*[@id='mat-select-value-1'])/span/span"
    number_option_text2 = "(//*[@id='mat-select-value-3'])/span/span"
    number_option_text3 = "(//*[@id='mat-select-value-5'])/span/span"
    after_date_selection = (By.TAG_NAME, "mat-date-range-input")
    calender = "//mat-datepicker-content/div[2]"
    no_data_found_text = "//div[text()=' No Data Found ']"
    click_on_table = "(//span[@class='clickable ng-star-inserted'])[1]"
    get_District_name_text = "//*[@id='mat-tab-content-0-0']/div/app-teacher-attendance-summary/div/div[2]/div[" \
                             "1]/app-breadcrumb-component/div/div[3]"
    click_on_District_name_in_BreadCrumb = "//app-breadcrumb-component/div/div[5]"
    click_on_State_name_in_BreadCrumb = "//app-breadcrumb-component/div/div[1]"
    click_on_Block_Name_In_BreadCrumb = "//app-breadcrumb-component/div/div[5]"
    click_on_Cluster_Name_In_BreadCrumb = "//app-breadcrumb-component/div/div[7]"
    district_Name = "(//div[text()='District'])[1]"
    block_Name = "(//div[text()='Block'])[1]"
    cluster_Name = "(//div[text()='Cluster'])[1]"
    school_wise_table = "(//app-material-heat-chart-drilldown-table/div/table/tbody)[2]/tr"
    unitBox_from = "fromRange"
    first_box = "20"
    second_box = "90"
    unitBox_to = "toRange"
    no_of_district = "leaflet-interactive"
    udise_code = '20010704002'
    district_officer = (By.ID, "district")
    dropdown_value = (By.XPATH, "//div[starts-with(@id,'a') and contains(@id,"'-'"{}" + ")]")
    district_dropdown = (By.ID, "districtfilter")
    block_dropdown = (By.ID, "blockfilter")
    submit_btn = (By.ID, "submit")
    metrics_dropdown_value = (By.XPATH, "//div[starts-with(@id,'a') and contains(@id,"'-'"{}" + ")]")

    def __init__(self, driver):
        super().__init__(driver)
        self.homepage = driver
        self.driver = driver
        self.count = 0

    def test_click_on_teacher_attendance_menu(self):
        self.driver.find_element(By.ID, self.teacher_attendance).click()

    def click_Average_Teachers_Reporting_Attendance(self):
        return self.get_attribute_value('aria-selected', self.Average_Teachers_Reporting_Attendance_tab)

    def get_avg_teacher_attendance_value(self):
        return self.driver.find_element(By.XPATH, self.avg_teacher_present_attendance_value).text

    def get_avg_teacher_attendance_text(self):
        return self.get_web_element_text(self.avg_teacher_attendance_text)

    def click_district_header(self):
        self.click(self.district_header)

    def get_district_column(self):
        return self.get_attribute_value('aria-sort', self.district_header)

    def click_teachers_reporting_teacher_attendance_header(self):
        self.click(self.teachers_reporting_teacher_attendance_header)

    def get_teachers_reporting_teacher_attendance_column(self):
        return self.get_attribute_value('aria-sort', self.teachers_reporting_teacher_attendance_column)

    def click_fullscreen_button(self):
        self.click(self.fullscreen_button)

    def click_download_button(self):
        self.click(self.download_button)

    def click_average_teacher_present_tab(self):
        self.click(self.map_view_of_teacher_attendance_tab)

    def get_attribute_average_teacher_present(self):
        return self.get_attribute_value('aria-selected', self.map_view_of_teacher_attendance_tab)

    def click_download_csv_button(self):
        self.click(self.csv_download)

    def click_download_pdf_button(self):
        self.click(self.pdf_download)

    def click_average_teacher_present1(self):
        self.click(self.avg_teacher_present_1)

    def click_to_calender_button(self):
        self.driver.find_element(By.XPATH, self.calender_open1).click()

    def click_on_avg_teacher_attendance_tab(self):
        self.click(self.click_avg_teacher_attenadance_tab)

    def get_total_Enrolment_value(self):
        return self.get_web_element_text(self.total_enrolment_value)

    def get_total_Enrolment_label(self):
        return self.get_web_element_text(self.total_enrolment_label)

    def click_download_School_report_button(self):
        self.click(self.school_report)

    def click_download_unit_level_button(self):
        self.click(self.school_report)

    def click_clear_button(self):
        self.click(self.clear_button)

    def get_start_date_attribute_value(self):
        return self.get_attribute_value('value', self.start_date)

    def get_end_date_attribute_value(self):
        return self.get_attribute_value('value', self.end_date)

    def click_first_district_tab(self):
        click_table_header = self.driver.find_element(self.first_district_tab)
        click_table_header.click()
        print(click_table_header.get_attribute('aria-sort'))

    def validate_drill_down_table_sorting(self):
        self.table_count = self.driver.find_elements(By.XPATH, self.table_headers)
        print(len(self.table_count))
        for i in range(1, len(self.table_count)):
            time.sleep(2)
            sorting_test = self.driver.find_element(By.XPATH, self.click_table_header.format(i))

            sorting_test.click()
            time.sleep(3)
            result = sorting_test.get_attribute('aria-sort')
            if 'ascending' == result:
                print("data sorted in acending order")
            else:
                self.count = self.count + 1
            sorting_test.click()
            time.sleep(3)
            second = sorting_test.get_attribute('aria-sort')
            if 'descending' == second:
                print("data sorted in descending order")
            else:
                self.count = self.count + 1
        return self.count

    def validate_sorting(self):
        self.table_headers1 = self.driver.find_elements(By.XPATH, '//table/thead/tr/th')
        print(len(self.table_headers1))
        for i in range(1, len(self.table_headers1) - 1):

            sorting_test = self.driver.find_element(By.XPATH, self.click_table_header.format(i))
            sorting_test.click()
            time.sleep(3)
            result = sorting_test.get_attribute('aria-sort')
            if 'ascending' == result:
                print("Table sorted in ascending order")
            else:
                self.count = self.count + 1
            sorting_test.click()
            time.sleep(3)
            second = sorting_test.get_attribute('aria-sort')
            if 'descending' == second:
                print("Table sorted in descending order")
            else:
                self.count = self.count + 1
        return self.count

    def click_map_view_of_Teachers_Attendance_tab(self):
        self.click(self.map_view_of_teacher_attendance_tab)
        return self.get_attribute_value('aria-selected', self.map_view_of_teacher_attendance_tab)

    def validate_start_date_attribute(self):
        return self.get_attribute_value('name', self.start_number)

    def validate_end_date_attribute(self):
        return self.get_attribute_value('name', self.end_number)

    def get_map_tooltip_info_validation(self):

        lst = self.driver.find_elements(By.CLASS_NAME, self.no_of_district)
        print("No of District", len(lst) - 1)
        print(len(lst))
        gray_marks = 0
        yellow_marks = 0
        time.sleep(2)
        map_data = []

        # for x in range(1, 3):
        for x in range(1, len(lst)):
            if lst[x].get_attribute('fill') == "#d8ead3":
                yellow_marks = yellow_marks + 1
            else:
                gray_marks = gray_marks + 1
            act = ActionChains(self.driver)
            act.move_to_element(lst[x]).perform()

            act.pause(3)
            time.sleep(2)
            print('option mouse overing is completed')
            # txt = self.driver.find_element(By.XPATH, "//div[@class='leaflet-pane leaflet-tooltip-pane']")
            # map_data.append(txt.text)
        return map_data

    def validate_district_markers(self):
        lst = self.driver.find_elements(By.CLASS_NAME, self.no_of_district)
        print("No of Block", len(lst) - 1)

        gray_marks = 0
        yellow_marks = 0
        time.sleep(2)
        # for x in range(1, 3):
        for x in range(1, len(lst)):
            if lst[x].get_attribute('fill') == '#6e6d6d':
                yellow_marks = yellow_marks + 1
            else:
                gray_marks = gray_marks + 1
            act = ActionChains(self.driver)
            act.move_to_element(lst[x]).click(lst).perform()
            act.move_to_element(lst[x]).perform()
            act.pause(3)
            time.sleep(2)
            print('option mouse overing is completed')
            # txt = self.driver.find_element(By.XPATH, "//div[@class='leaflet-pane leaflet-tooltip-pane']")
            # map_data.append(txt.text)

    def click_pagination_teacher_present(self):
        self.click(self.pagination_teacher_present)

    def validate_pagination_teacher_present(self):
        # self.driver.find_element(By.ID, "mat-select-0").click()
        # time.sleep(3)
        options = self.driver.find_elements(By.XPATH, self.option_list)
        for i in range(len(options)):
            self.driver.find_element(By.XPATH, self.number_options1.format(i)).click()
            time.sleep(2)

            time.sleep(3)
            no_of_rows = self.driver.find_elements(By.XPATH, self.no_of_rows1)

            get_option_text = self.driver.find_element(By.XPATH, self.number_option_text1).text
            time.sleep(1)
            print(get_option_text, ' option is selected')
            time.sleep(2)
            # self.driver.find_element(By.ID, "mat-select-0").click()
            # time.sleep(2)
            if int(len(no_of_rows)) <= int(get_option_text):
                print(get_option_text, "Pagination is Working ")
            else:
                print(int(no_of_rows), get_option_text, " Pagination is not working ")
            self.driver.find_element(By.ID, self.option_tab1).click()
            time.sleep(3)

        return options

    def click_pagination_bar_graph(self):
        self.click(self.pagination_bar_graph)

    def validate_pagination_teacher_present_bar_graph(self):
        options = self.driver.find_elements(By.XPATH, self.option_list)
        print(len(options))
        for i in range(4, len(options) + 4):
            # print("//*[starts-with(@id,'mat-option') and contains(@id,'-{}')]".format(i))
            self.driver.find_element(By.XPATH, self.number_options1.format(i)).click()
            time.sleep(3)
            get_option_text = self.driver.find_element(By.XPATH, self.number_option_text2).text
            self.driver.find_element(By.ID, self.option_tab2).click()
            time.sleep(1)
            print(get_option_text, ' option is selected')
            time.sleep(2)
        return options

    def click_pagination_school_teacher_present(self):
        self.click(self.pagination_school_teacher_present)

    def validation_pagination_school_teacher_present(self):
        options = self.driver.find_elements(By.XPATH, self.option_list)
        print(len(options) + 1)
        for i in range(1, len(options) + 1):
            self.driver.find_element(By.XPATH, self.number_options2.format(i)).click()
            time.sleep(5)
            no_of_rows = self.driver.find_elements(By.XPATH, self.no_of_rows2)
            get_option_text = self.driver.find_element(By.XPATH, self.number_option_text3).text
            time.sleep(1)
            print(get_option_text, ' option is selected')
            if int(len(no_of_rows)) == int(get_option_text):
                print(get_option_text, "Pagination is Working ")
            else:
                print(len(no_of_rows), get_option_text, " Pagination is not working ")
            self.driver.find_element(By.XPATH, self.option_tab3).click()
            time.sleep(3)
        return options

    def map_displayed_validation(self):
        map = self.driver.find_element(By.XPATH, self.map)
        time.sleep(3)
        if map.is_displayed() == True:
            print("Map Is Displayed")
            assert True
        else:
            print("Map Is Not Displayed")
            assert False
        return map

    def validate_search_box_udise(self):
        lst1 = self.driver.find_elements(By.XPATH, self.school_wise_percent_teacher_attendance)
        print(len(lst1))
        self.driver.find_element(By.XPATH, self.udise_code_search_bar).send_keys(self.udise_code)
        time.sleep(3)
        lst2 = self.driver.find_elements(By.XPATH, self.school_wise_percent_teacher_attendance)
        print(len(lst2))
        if len(lst1) != len(lst2):
            print("search tab is working ")
            assert True
        else:
            print("search tab is not working")
            assert False

    def validate_after_selection_of_date_displayed(self):
        return self.get_attribute_value("role", self.after_date_selection)

    def validate_calender_displayed(self):
        calender_displayed = self.driver.find_element(By.XPATH, self.calender)
        time.sleep(3)
        if calender_displayed.is_displayed():
            time.sleep(2)
            print("Calender Open Successfully")
            assert True
        else:
            print("calender Button Not Working")
            assert False
        return calender_displayed

    def validate_District_level_drilldown(self):
        big_number1 = self.driver.find_element(By.XPATH, self.avg_teacher_present_attendance_value)
        a1 = big_number1.text
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        print(click_on_District.text)
        click_on_District.click()
        time.sleep(3)
        big_number2 = self.driver.find_element(By.XPATH, self.avg_teacher_present_attendance_value)
        a2 = big_number2.text
        print(a1, a2)
        if a1 != a2:
            print("Average % Teachers Present is Displayed")
            assert True
        else:
            print(a1, a2, "Average % Teachers Present is not Displayed")
            assert False
        return big_number1, big_number2

    def validate_District_name_in_bread_crumb(self):
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_District.click()
        time.sleep(3)
        get_District_text = self.driver.find_element(By.XPATH, self.get_District_name_text)
        print(get_District_text.text)
        if len(get_District_text.text) > 0 or get_District_text.text != '':
            print(get_District_text.text, "is Displayed")
            assert True
        else:
            print(get_District_text.text, "is not Displayed")
            assert False

        return get_District_text

    def validate_State_name_in_bread_Crumb(self):
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_District.click()
        time.sleep(3)
        click_on_state = self.driver.find_element(By.XPATH, self.click_on_State_name_in_BreadCrumb)
        click_on_state.click()
        time.sleep(3)
        table_name = self.driver.find_element(By.XPATH, self.district_Name).text
        print(table_name)
        if table_name == "District":
            print("All the district belongs to that state")
            assert True
        else:
            print("district  not belongs to that state")
            assert False
        return table_name

    def validate_Block_level_drilldown(self):
        big_number1 = self.driver.find_element(By.XPATH, self.avg_teacher_present_attendance_value)
        a1 = big_number1.text
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)

        click_on_District.click()

        time.sleep(3)
        click_on_block = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_block.click()
        time.sleep(3)
        big_number3 = self.driver.find_element(By.XPATH, self.avg_teacher_present_attendance_value)
        a3 = big_number3.text
        time.sleep(3)

        print(a1, a3)
        time.sleep(3)
        if a1 != a3:
            print("Average % Teachers Present is Displayed")
            assert True
        else:
            print(a1, a3, "Average % Teachers Present is not Displayed")
            assert False

    def validate_block_name_in_Bread_Crumb(self):
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_District.click()
        time.sleep(3)
        click_on_block = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_block.click()
        time.sleep(3)
        get_text_block = self.driver.find_element(By.XPATH, self.click_on_Block_Name_In_BreadCrumb)
        print(get_text_block.text)
        if len(get_text_block.text) > 0 or get_text_block.text != '':
            print(" text is Displayed")
            assert True
        else:
            print("text is not Displayed")
            assert False

    def validate_District_name_in_Bread_Crumb(self):
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_District.click()
        time.sleep(3)
        table_name = self.driver.find_element(By.XPATH, self.block_Name).text
        print(table_name)
        if table_name == "Block":
            print("All the block belongs to that district")
            assert True
        else:
            print("block not belongs to that district")
            assert False

    def validate_cluster_level_drilldown(self):
        big_number1 = self.driver.find_element(By.XPATH, self.avg_teacher_present_attendance_value)
        a1 = big_number1.text
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_District.click()
        time.sleep(3)
        click_on_block = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_block.click()
        time.sleep(3)
        click_on_cluster = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_cluster.click()
        time.sleep(3)
        big_number3 = self.driver.find_element(By.XPATH, self.avg_teacher_present_attendance_value)
        a3 = big_number3.text
        time.sleep(3)

        print(a1, a3)
        time.sleep(3)
        if a1 != a3:
            print("Average % Teachers Present is Displayed")
            assert True
        else:
            print(a1, a3, "Average % Teachers Present is not Displayed")
            assert False

    def validate_cluster_in_breadcrumb(self):

        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_District.click()
        time.sleep(3)
        click_on_block = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_block.click()
        time.sleep(3)
        click_on_cluster = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_cluster.click()
        time.sleep(3)
        get_text_cluster = self.driver.find_element(By.XPATH, self.click_on_Cluster_Name_In_BreadCrumb).text
        print(get_text_cluster)
        if len(get_text_cluster) > 0 or get_text_cluster != '':
            print(" text is Displayed")
            assert True
        else:
            print("text is not Displayed")
            assert False

    def validate_data_belongs_to_block_breadcrumb(self):
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_District.click()
        time.sleep(3)
        click_on_block = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_block.click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_on_Block_Name_In_BreadCrumb).click()
        table_name = self.driver.find_element(By.XPATH, self.cluster_Name).text
        print(table_name)
        if table_name == "Cluster":
            print("All the cluster belongs to that block")
            assert True
        else:
            print("cluster  not belongs to that block")
            assert False

    def validate_data_belongs_to_District_breadcrumb(self):
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_District.click()
        time.sleep(3)
        click_on_block = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_block.click()
        time.sleep(3)
        click_on_cluster = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_cluster.click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_on_District_name_in_BreadCrumb).click()
        table_name = self.driver.find_element(By.XPATH, self.block_Name).text
        print(table_name)
        if table_name == "Block":
            print("All the block belongs to that district")
            assert True
        else:
            print("block  not belongs to that district")
            assert False

    def validate_data_belongs_to_State_breadcrumb(self):
        click_on_District = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_District.click()
        time.sleep(3)
        click_on_block = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_block.click()
        time.sleep(3)
        click_on_cluster = self.driver.find_element(By.XPATH, self.click_on_table)
        click_on_cluster.click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_on_State_name_in_BreadCrumb).click()
        table_name = self.driver.find_element(By.XPATH, self.district_Name).text
        print(table_name)
        if table_name == "District":
            print("All the district belongs to that state")
            assert True
        else:
            print("district  not belongs to that state")
            assert False

    def validate_Markers_colours(self):
        self.driver.find_element(By.XPATH, "//*[@id='map']/div[2]/div[2]/div/span[1]/button").click()
        c1 = self.driver.find_elements(By.CLASS_NAME, self.no_of_district)
        for i in range(len(c1)):
            if c1[i].get_attribute('fill') == "#d8ead3":
                print("gray colour legend is selected")
            else:
                print("lagend card is not working")

    def select_date_from_calender(self):
        reads = ReadConfig()
        month = reads.get_school_attendance_monthname() + ""
        start_date = reads.get_school_attendance_startdate() + ""
        end_date = reads.get_school_attendance_enddate() + ""
        now = datetime.now()
        self.year = now.strftime("%Y")
        self.date = now.strftime("%d")
        self.month = now.strftime("%B").upper()
        self.driver.find_element(By.XPATH, self.calender_open).click()
        time.sleep(1)
        self.click(self.click_to_select_start_year)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_start_year.format(self.year)).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_start_month.format(month)).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_start_date.format(start_date)).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_end_date.format(end_date)).click()
        time.sleep(1)

    def validate_Appty_button_unitbox(self):
        element_1 = self.driver.find_element(By.ID, self.unitBox_from)
        element_1.send_keys(self.first_box)
        element_2 = self.driver.find_element(By.ID, self.unitBox_to)
        element_2.send_keys(self.second_box)

    def test_district_officer_button_click(self):
        self.click(self.district_dropdown)
        time.sleep(3)
        self.click(self.district_dropdown)
        time.sleep(2)
        opts = self.driver.find_element(By.XPATH, "//*[@role='option'][1]")
        opts.click()
        self.click(self.submit_btn)
        time.sleep(2)

    def get_each_dropdown_value_id(self, metrics_dropdown_id):
        metrics_dropdown_value = self.metrics_dropdown_value
        metrics_dropdown_value = list(metrics_dropdown_value)
        metrics_dropdown_value[1] = metrics_dropdown_value[1].format(metrics_dropdown_id)
        metrics_dropdown_value = tuple(metrics_dropdown_value)
        res = self.get_web_element((By.XPATH, str(metrics_dropdown_value[1])))
        return res

    def test_block_officer_button_click(self):
        self.click(self.block_dropdown)
        time.sleep(3)
        self.click(self.block_dropdown)
        time.sleep(2)
        opts = self.driver.find_element(By.XPATH, "//*[@role='option'][1]")
        opts.click()
        self.click(self.submit_btn)
        time.sleep(2)
