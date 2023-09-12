
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Page_of_objects.CqubeUi.BasePage import Base


class Udise(Base):
    """ List of selenium locator of summary statistics screen """

    udise = (By.ID, "menu-item-4")
    L = r'L\.|[^\d.]'
    K = r'K\.|[^\d.]'
    district_wise_performance = (By.XPATH, "//mat-tab-group/mat-tab-header/div/div/div/div")
    Total_Students = (By.XPATH, "//div[1]/div/app-big-number/div/div[1]/h1")
    Total_Students_text = (By.XPATH, "//div[1]/div/app-big-number/div/div[2]")
    PTR_value = (By.XPATH, "//div[2]/div/app-big-number/div/div[1]/h1")
    PTR_text = (By.XPATH, "//div[2]/div/app-big-number/div/div[2]")
    schools_with_toilets_value = (By.XPATH, "//div[3]/div/app-big-number/div/div[1]/h1")
    schools_with_toilets_text = (By.XPATH, "//div[3]/div/app-big-number/div/div[2]")
    schools_having_electricity_value = (By.XPATH, "//div[4]/div/app-big-number/div/div[1]/h1")
    schools_having_electricity_text = (By.XPATH, "//div[4]/div/app-big-number/div/div[2]")
    schools_having_drinking_water_value = (By.XPATH, "//div[5]/div/app-big-number/div/div[1]/h1")
    schools_having_drinking_water_text = (By.XPATH, "//div[5]/div/app-big-number/div/div[2]")
    metrics_dropdown = (By.ID, "filter-Metric")
    pgi_metric_dropdown = (By.XPATH, "//div[@role='option']/span")
    metrics_dropdown_value = (By.XPATH, "//div[starts-with(@id,'a') and contains(@id,"'-'"{}" + ")]")
    legend_text = (By.XPATH, "//*[@id='map']/div[2]/div[2]/div/strong")
    map = (By.XPATH, "//*[@id='map']")
    download_button = (By.ID, "downloadButton")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_click_on_udise_menu(self):
        self.click(self.udise)

    def click_district_wise_performance(self):
        return self.get_attribute_value('aria-selected', self.district_wise_performance)

    def get_Total_Students_value(self):
        return self.get_web_element_text(self.Total_Students)

    def get_Total_Students_text(self):
        return self.get_web_element_text(self.Total_Students_text)

    def get_PTR_value(self):
        return self.get_web_element_text(self.PTR_value)

    def get_PTR_text(self):
        return self.get_web_element_text(self.PTR_text)

    def get_schools_with_toilets_value(self):
        return self.get_web_element_text(self.schools_with_toilets_value)

    def get_schools_with_toilets_text(self):
        return self.get_web_element_text(self.schools_with_toilets_text)

    def get_schools_having_electricity_value(self):
        return self.get_web_element_text(self.schools_having_electricity_value)

    def get_schools_having_electricity_text(self):
        return self.get_web_element_text(self.schools_having_electricity_text)

    def get_schools_having_drinking_water_value(self):
        return self.get_web_element_text(self.schools_having_drinking_water_value)

    def get_schools_having_drinking_water_text(self):
        return self.get_web_element_text(self.schools_having_drinking_water_text)


    def click_download_button(self):
        self.click(self.download_button)

    def click_dropdown(self):
        self.click(self.metrics_dropdown)

    def get_metrics_dropdown_values(self):
        metric_dropdown_options = self.get_web_elements(self.pgi_metric_dropdown)
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

    """THis functionality is to get map information"""

    def get_map_information(self):
        map_info = self.get_web_elements(self.map)
        return map_info

    """ This function is to get map tooltip value"""

    def get_map_tooltip_info_validation(self):
        lst = self.driver.find_elements(By.CLASS_NAME, "leaflet-interactive")
        print("No of District", len(lst) - 1)
        blue_marks = 0
        white_marks = 0
        time.sleep(2)
        for x in range(1, len(lst)):
            if lst[x].get_attribute('fill') == '#FFFFFF':
                white_marks = white_marks + 1
            else:
                blue_marks = blue_marks + 1
            act = ActionChains(self.driver)
            act.move_to_element(lst[x]).perform()
            act.pause(3)
            time.sleep(2)
            print('option mouse overing is completed')

