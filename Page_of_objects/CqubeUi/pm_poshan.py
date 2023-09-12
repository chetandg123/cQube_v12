import os
import time

from selenium.webdriver.common.by import By

from Page_of_objects.CqubeUi.BasePage import Base


class pm_poshan(Base):
    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"
    state_officer = (By.ID, "state")
    pm_poshan_menu = (By.ID, "menu-item-3")
    progress_status_tab = (By.XPATH, "//div/app-pmposhan/div[2]/mat-tab-group/mat-tab-header/div/div/div/div")
    total_districts_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_districts_label = (By.XPATH, "//app-big-number/div/div[2]")
    total_schools_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_schools_label = (By.XPATH, "//app-big-number/div/div[2]")
    total_meals_served_value = (By.XPATH, "//app-big-number/div/div[1]/h1")
    total_meals_served_label = (By.XPATH, "//app-big-number/div/div[2]")
    dropdown = (By.XPATH, "//div/div/div/div/div/ng-select/div/div")
    metrics_options = (By.XPATH, "//div/div/div/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]")
    # fullscreen_button = (By.ID, "/html/body/app-root/app-layout/div/div[2]/div/app-student-attendance/div["
                                # "2]/div/button/img")
    download_button = (By.ID, "downloadButton")
    logout_button = (By.ID, "signOut")
    fullscreen_button = (By.ID, "fullscreen-button")
    pm_poshan_metric_dropdown = (By.XPATH, "//div[@role='option']/span")
    legend_text = (By.XPATH, "//*[@id='map']/div[2]/div[2]/div/strong")
    metrics_dropdown = (By.ID, "filter-Metric")
    metrics_dropdown_value = (By.XPATH, "//div[starts-with(@id,'a') and contains(@id,"'-'"{}" + ")]")




    def __init__(self, driver):
        super().__init__(driver)

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

    def click_on_access_pm_poshan_menu(self):
        self.click(self.pm_poshan_menu)

    def click_menu(self):
        self.click(self.pm_poshan_menu)

    def test_click_on_state_button(self):
        self.click(self.state_officer)

    def click_progress_status_tab(self):
        self.click(self.progress_status_tab)

    def get_progress_status_tab(self):
        return self.get_attribute_value('aria-selected', self.progress_status_tab)

    def get_total_districts_value(self):
        return self.get_web_element_text(self.total_districts_value)

    def get_total_districts_label(self):
        return self.get_web_element_text(self.total_districts_label)

    def get_total_schools_value(self):
        return self.get_web_element_text(self.total_schools_value)

    def get_total_schools_label(self):
        return self.get_web_element_text(self.total_schools_label)

    def get_total_meal_served_value(self):
        return self.get_web_element_text(self.total_meals_served_value)

    def get_Total_meals_served_label(self):
        return self.get_web_element_text(self.total_meals_served_label)

    def get_dropdown_values(self):
        dropdown_options = self.get_web_elements(self.metrics_options)
        return dropdown_options

    def test_click_dropdown(self):
        self.click(self.dropdown)

    def click_fullscreen_button(self):
        self.click(self.fullscreen_button)


    def click_download_button(self):
        self.click(self.download_button)

    def test_click_logout_button(self):
        self.click(self.logout_button)

    def get_download_dir(self):
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd, '../../Downloads')
        return download_path

    def click_dropdown(self):
        self.click(self.metrics_dropdown)

    def get_metrics_dropdown_values(self):
        metric_dropdown_options = self.get_web_elements(self.pm_poshan_metric_dropdown)
        return metric_dropdown_options


    """This functionality is to get id of each metric in dropdown"""

    def get_each_dropdown_value_id(self, metrics_dropdown_id):
        metrics_dropdown_value = self.metrics_dropdown_value
        metrics_dropdown_value = list(metrics_dropdown_value)
        metrics_dropdown_value[1] = metrics_dropdown_value[1].format(metrics_dropdown_id)
        metrics_dropdown_value = tuple(metrics_dropdown_value)
        res = self.get_web_element((By.XPATH, str(metrics_dropdown_value[1])))
        return res

    """ This functionality is to get legend text"""

    def get_legend_text(self):
        return self.get_web_element_text(self.legend_text)
