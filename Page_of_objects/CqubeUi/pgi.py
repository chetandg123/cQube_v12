import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Page_of_objects.CqubeUi.BasePage import Base



class Pgi(Base):
    """ List of selenium locator of summary statistics screen """

    pgi = (By.XPATH, "//app-side-nav/aside/div/ul/li[3]/div/i/img")
    L = r'L\.|[^\d.]'
    K = r'K\.|[^\d.]'
    district_wise_performance = (By.XPATH, "//mat-tab-group/mat-tab-header/div/div/div/div")
    learning_outcome_value = (By.XPATH, "//div[1]/div/app-big-number/div/div[1]/h1")
    learning_outcome_text = (By.XPATH, "//div[1]/div/app-big-number/div/div[2]")
    infrastructure_value = (By.XPATH, "//div[2]/div/app-big-number/div/div[1]/h1")
    infrastructure_text = (By.XPATH, "//div[2]/div/app-big-number/div/div[2]")
    governance_process_value = (By.XPATH, "//div[3]/div/app-big-number/div/div[1]/h1")
    governance_process_text = (By.XPATH, "//div[3]/div/app-big-number/div/div[2]")
    metrics_dropdown = (By.ID, "filter-Metric")
    pgi_metric_dropdown = (By.XPATH, "//div[@role='option']/span")
    metrics_dropdown_value = (By.XPATH, "//div[starts-with(@id,'a') and contains(@id,"'-'"{}" + ")]")
    legend_text = (By.XPATH, "//*[@id='map']/div[2]/div[2]/div/strong")
    map = (By.XPATH, "//*[@id='map']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_click_on_pgi_menu(self):
        self.click(self.pgi)

    def click_district_wise_performance(self):
        return self.get_attribute_value('aria-selected', self.district_wise_performance)

    def get_learning_outcome_value(self):
        return self.get_web_element_text(self.learning_outcome_value)

    def get_learning_outcome_text(self):
        return self.get_web_element_text(self.learning_outcome_text)

    def get_infrastructure_value(self):
        return self.get_web_element_text(self.infrastructure_value)

    def get_infrastructure_text(self):
        return self.get_web_element_text(self.infrastructure_text)

    def get_governance_process_value(self):
        return self.get_web_element_text(self.governance_process_value)

    def get_governance_process_text(self):
        return self.get_web_element_text(self.governance_process_text)

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
        map_data = []
        # for x in range(1, 3):
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
            # txt = self.driver.find_element(By.XPATH, "//div[@class='leaflet-pane leaflet-tooltip-pane']")
            # map_data.append(txt.text)
        # return map_data
