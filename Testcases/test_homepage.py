import logging
import os
import time

import sys

sys.path.append(os.getcwd())
from Page_of_objects.CqubeUi.homepage import Homepage
from Testcases.conftest import ConfTest
from Utilities import CustomLogger
from Utilities.ReadProperties import ReadConfig


class TestDashboard:
    homepage = None
    driver = None

    @classmethod
    def setup(cls):
        cls.driver = ConfTest.get_driver()
        cls.driver.implicitly_wait(30)
        cls.homepage = Homepage(cls.driver)
        cls.homepage.open_cqube_application()
        cls.homepage.open_login_page()
        # cls.menu = menu(cls.driver)

        cls.logger = CustomLogger.setup_logger('Dashboard', ReadConfig.get_logs_directory() + "/Dashboard.log",
                                               level=logging.DEBUG)

    # """ Check whether homepage is displaying or not"""

    # def test_validate_homepage(self):
    #     self.logger.info("*************** Tc_cQube_homepage_001 Testing Started *****************")
    #     self.homepage.open_cqube_application()
    #     self.homepage.open_login_page()
    #     if 'home' in self.driver.current_url:
    #         self.logger.info("*************** Navigation to Homepage Screen Passed *****************")
    #     else:
    #         self.logger.error("********************* Navigation to Homepage failed  ***********")
    #         assert False
    #     self.logger.info("*************** Tc_cQube_homepage_001 Testing completed *****************")

    '''Check whether title is displaying or not'''

    def test_tittle(self):
        self.logger.info("*************** Tc_cQube_homepage_002 Testing started *****************")
        time.sleep(5)
        if "VIDYA SAMIKSHA KENDRA" in self.driver.page_source:
            self.logger.info("*************** tittle is displaying *****************")
            print("Tittle is displaying")
        else:
            self.logger.info("*************** tittle is not displaying *****************")
            print("Tittle is not displaying")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_002 Testing ended *****************")

    '''This Test script checking the A minus Button '''

    def test_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_003 Testing Started *****************")
        res = self.homepage.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_003 Testing completed *****************")

    '''This Test script checking the A Plus Button '''

    def test_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_004 Testing Started *****************")
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_004 Testing completed *****************")

    '''This Test script checking Default A  Button'''

    def test_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_homepage_005 Testing Started *****************")
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_005 Testing completed *****************")

    '''This Test script checking the state button is working or not'''

    def test_Click_on_the_state_button(self):
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Started *****************")
        self.homepage.test_click_on_state_button()
        time.sleep(5)
        if 'summary-statistics' in self.driver.current_url:
            self.logger.info("*******************  summary-statistics page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** summary-statistics Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")

    # district
    '''This Test script checking the district button is working or not'''

    def test_Click_on_the_district_button(self):
        self.logger.info("*************** Tc_cQube_homepage_007 Testing Started *****************")
        self.homepage.test_click_on_district_button()
        time.sleep(5)
        district_title = "District Officer"
        if "Hello District Officer" in self.driver.page_source:
            assert True
        else:
            assert False
        self.logger.info("*************** Tc_cQube_homepage_007 Testing ended *****************")

    '''This Test script checking the dropdown is present or not '''

    def test_district_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_008 Testing Started *****************")
        self.homepage.test_click_on_district_button()
        time.sleep(2)
        district_title = "Select District"
        if district_title in self.driver.page_source:
            assert True
        else:
            assert False
        self.logger.info("*************** Tc_cQube_homepage_008 Testing ended *****************")

    '''This Test script checking the dropdown having options or not '''

    def test_options_in_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_009 Testing Started *****************")
        self.homepage.test_click_on_district_button()
        self.homepage.test_click_dist()
        time.sleep(5)
        options = self.homepage.get_dropdown_values()
        time.sleep(2)
        if len(options) != 0:
            assert True
        else:
            assert False
        self.logger.info("*************** Tc_cQube_homepage_009 Testing Started *****************")

    def test_district_dropdown1(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        self.homepage.test_click_on_district_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            dst_optn = opts.text
            opts.click()
            time.sleep(5)
            if dst_optn in self.driver.page_source:
                assert True
            else:
                assert False
            self.homepage.test_click_dist()
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")

    def test_click_district_submit_btn(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        self.homepage.test_click_on_district_button()
        self.homepage.test_click_dist()
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_submit()
        time.sleep(2)
        if 'Summary Statistics' in self.driver.page_source:
            self.logger.info("*******************  summary-statistics page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** summary-statistics Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")

    def test_click_district_home_btn(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        self.homepage.test_click_on_district_button()
        time.sleep(2)
        self.homepage.test_click_on_home_button()
        time.sleep(3)
        if 'Hello District Officer' not in self.driver.page_source:
            self.logger.info("*******************  district officer page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** district officer Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")

    def test_click_logout_btn(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        self.homepage.test_click_on_district_button()
        time.sleep(2)
        self.homepage.test_click_logout_button()
        time.sleep(3)
        if 'login' in self.driver.current_url:
            self.logger.info("*******************  district officer page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** district officer Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")

    # =================================================================================================================================================================
    def test_Click_on_the_block_button(self):
        self.logger.info("*************** Tc_cQube_homepage_007 Testing Started *****************")
        self.homepage.test_click_on_block_button()
        time.sleep(5)
        block_title = "Block Officer"
        if "Hello Block Officer" in self.driver.page_source:
            assert True
        else:
            assert False
        self.logger.info("*************** Tc_cQube_homepage_007 Testing ended *****************")

    def test_block_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_008 Testing Started *****************")
        # self.homepage.test_click_on_district_button()
        self.homepage.test_click_on_block_button()
        time.sleep(2)
        district_title = "Select District"
        if district_title in self.driver.page_source:
            assert True
        else:
            assert False
        self.logger.info("*************** Tc_cQube_homepage_008 Testing ended *****************")

    def test_district_options_in_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_009 Testing Started *****************")
        self.homepage.test_click_on_block_button()
        self.homepage.test_click_dist()
        time.sleep(5)
        options = self.homepage.get_dropdown_values()
        time.sleep(2)
        if len(options) != 0:
            assert True
        else:
            assert False
        self.logger.info("*************** Tc_cQube_homepage_009 Testing Started *****************")

    def test_block_dropdown1(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        self.homepage.test_click_on_block_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            time.sleep(3)
            block_title = "Select Block"
            if block_title in self.driver.page_source:
                assert True
            else:
                assert False
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_008 Testing ended *****************")

    def test_block_options_in_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        self.homepage.test_click_on_block_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            time.sleep(3)
            options = self.homepage.get_dropdown_values()
            for j in range(len(options)):
                opts = self.homepage.get_each_dropdown_value_id(i)
                if len(opts) != 0:
                    assert True
                else:
                    assert False
                self.homepage.test_click_dist()
                self.logger.info("*************** Tc_cQube_homepage_009 Testing Started *****************")

    def test_block_dropdown2(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        self.homepage.test_click_on_block_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            time.sleep(3)
            options = self.homepage.get_dropdown_values()
            for j in range(len(options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                block_optn = opts.text
                opts.click()
                if block_optn in self.driver.page_source:
                    assert True
                else:
                    assert False
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")

    # def test_block_options_error_msg(self):
    #     self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
    #     self.homepage.test_click_on_block_button()
    #     time.sleep(5)
    #     self.homepage.test_click_dist()
    #     time.sleep(3)
    #     options = self.homepage.get_dropdown_values()
    #     for i in range(len(options)):
    #         opts = self.homepage.get_each_dropdown_value_id(i)
    #         opts.click()
    #         self.homepage.test_click_block()
    #         time.sleep(3)
    #         options = self.homepage.get_dropdown_values()
    #         if 'Please Select a District' in self.driver.page_source:
    #             assert True
    #         else:
    #             assert False
    #     self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")

    def test_bo_block_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_015 Testing Started *****************")
        self.homepage.test_click_on_block_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(2)
        self.homepage.test_click_submit()
        if "Please Select a Block" in self.driver.page_source:
            print("error msg is displaying")
            self.logger.error("*********** error msg is displaying *********")
        else:
            self.logger.error("*********** error msg is not displaying *********")
            print("error msg is not displaying")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_015 Testing ended *****************")

    def test_click_block_home_btn(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        self.homepage.test_click_on_block_button()
        time.sleep(2)
        self.homepage.test_click_on_home_button()
        time.sleep(3)
        if 'Hello Block Officer' not in self.driver.page_source:
            self.logger.info("*******************  block officer page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** block officer Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")

    def test_block_click_logout_btn(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")
        self.homepage.test_click_on_block_button()
        time.sleep(2)
        self.homepage.test_click_logout_button()
        time.sleep(3)
        if 'login' in self.driver.current_url:
            self.logger.info("*******************  district officer page is Displayed ********************")
            assert True
        else:
            self.logger.error("*************** district officer Button is not Working ******************")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing Ended *****************")

    '''This Test script checking homepage displaying or not '''

    def test_homepage(self):
        self.logger.info("*************** Tc_cQube_homepage_001 Testing started *****************")
        time.sleep(5)
        if "home" in self.driver.current_url:
            self.logger.info("*************** homepage is displaying *****************")
            print("Homepage is displaying ")
        else:
            self.logger.info("*************** homepage is not displaying *****************")
            print("Homepage is not displaying ")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_001 Testing ended *****************")

    '''This Test script checking the A Minus Button '''

    def test_cluster_click_the_a_minus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_003 Testing started *****************")
        res = self.homepage.test_click_on_a_minus_button()
        if res == 0:
            self.logger.info("*********** A- button is Clicked ****************")
            print("A- button is clicked")
        else:
            self.logger.error("*********** A- button is not Clicked *********")
            print("A- button is not clicked")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_003 Testing ended *****************")

    '''This Test script checking the A Plus Button '''

    def test_cluster_click_the_a_plus_button(self):
        self.logger.info("*************** Tc_cQube_homepage_004 Testing started *****************")
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A+ button is Clicked ****************")
            print("A+ button is clicked")
        else:
            self.logger.error("*********** A+ button is not Clicked *********")
            print("A+ button is clicked")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_004 Testing Ended *****************")

    '''This Test script checking Default A  '''

    def test_cluster_click_the_default_a_button(self):
        self.logger.info("*************** Tc_cQube_homepage_005 Testing started *****************")
        res = self.homepage.test_click_on_a_plus_button()
        if res == 0:
            self.logger.info("*********** A button is Clicked ****************")
            print("A button is clicked")
        else:
            self.logger.error("*********** A button is not Clicked *********")
            print("A button is clicked")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_005 Testing Ended *****************")

    def test_co_click_the_cluster_button(self):
        self.logger.info("*************** Tc_cQube_homepage_006 Testing started *****************")
        time.sleep(3)
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        cluster_tittle = "Hello Cluster Officer"
        if cluster_tittle in self.driver.page_source:
            print("Cluster officer button is clicked")
            self.logger.error("*********** cluster officer button Clicked *********")
        else:
            self.logger.error("*********** cluster officer button is not Clicked *********")
            print("Cluster officer button is clicked")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_006 Testing ended *****************")

    def test_co_district_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_007 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        district_tittle = 'Select District'
        if district_tittle in self.driver.page_source:
            print("District dropdown is present")
            self.logger.error("********** District dropdown is present *********")
        else:
            self.logger.error("*********** District dropdown is not present *********")
            print("District dropdown is not present")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_007 Testing ended *****************")

    def test_co_options_in_district_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_008 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        if len(options) != 0:
            print("options are present in the district dropdown")
            self.logger.error("*********** options are present in the district dropdown *********")
        else:
            print("options are not present in the district dropdown")
            self.logger.error("*********** options are not present in the district dropdown *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_008 Testing ended *****************")

    def test_co_block_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_009 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            time.sleep(5)
            block_tittle = 'Select Block'
            if block_tittle in self.driver.page_source:
                print("Each district options are selecting and Block dropdown is displaying")
                self.logger.error("*********** Each district options are selecting and Block dropdown is displaying "
                                  "*********")
            else:
                self.logger.error("*********** Each district options are selecting and Block dropdown is displaying "
                                  "*********")
                print("Each district options are not selecting and Block dropdown is not displaying")
                assert False
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_009 Testing ended *****************")

    def test_co_options_in_block_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_010 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            time.sleep(5)
            self.homepage.test_click_block()
            time.sleep(3)
            options_block = self.homepage.get_dropdown_values()
            print(len(options_block))
            if len(options_block) != 0:
                print("Block have options")
                self.logger.error("*********** block dropdown is having options *********")
            else:
                print("Block does not have options")
                self.logger.error("*********** block dropdown is not having options *********")
                assert False
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_010 Testing ended *****************")

    def test_co_cluster_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_011 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                time.sleep(7)
                cluster_tittle = 'Select Cluster'
                if cluster_tittle in self.driver.page_source:
                    print("Cluster dropdown is present")
                    self.logger.error("*********** cluster dropdown is present *********")
                else:
                    print("Cluster dropdown is not present")
                    self.logger.error("*********** cluster dropdown is not present *********")
                    assert False
                time.sleep(6)
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_011 Testing ended *****************")

    def test_co_options_cluster_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_012 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                if len(cluster_options) != 0:
                    print('options are present in the cluster dropdown')
                    self.logger.error("*********** options are present in the cluster dropdown *********")
                else:
                    self.logger.error("*********** options are not present in the cluster dropdown *********")
                    print('options are not present in the cluster dropdown')
                    assert False
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_012 Testing ended *****************")

    def test_co_options_selecting_cluster_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_013 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_on_cluster_button()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                for k in range(len(cluster_options)):
                    opts = self.homepage.get_each_dropdown_value_id(k)
                    cluster_option_text = opts.text
                    opts.click()
                    if cluster_option_text in self.driver.page_source:
                        print('Each cluster options are selecting')
                        self.logger.error("*********** Each cluster options are selecting *********")
                    else:
                        self.logger.error("*********** Each cluster options are not selecting *********")
                        print('cluster options are not selecting')
                        assert False
                    self.homepage.test_click_on_cluster_button()
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_013 Testing ended *****************")

    def test_co_submit_button(self):
        self.logger.info("*************** Tc_cQube_homepage_014 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_block()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_cluster()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(5)
        self.homepage.test_click_submit()
        time.sleep(3)
        if "Summary Statistics" in self.driver.page_source:
            print("submit button is working")
            self.logger.error("*********** submit button is working *********")
        else:
            self.logger.error("*********** submit button is not working *********")
            print("submit button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_014 Testing ended *****************")

    def test_co_district_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_015 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_submit()
        if "Please Select a District" in self.driver.page_source:
            print("error msg is displaying")
            self.logger.error("*********** error msg is displaying *********")
        else:
            self.logger.error("*********** error msg is not displaying *********")
            print("error msg is not displaying")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_015 Testing ended *****************")

    def test_co_block_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_016 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(3)
        self.homepage.test_click_submit()
        if "Please Select a Block" in self.driver.page_source:
            print("Please Select a Block, error msg is displaying")
            self.logger.error("*********** Please Select a Block, error msg is displaying *********")
        else:
            self.logger.error("*********** Please Select a Block, error msg is displaying *********")
            print("Please Select a Block, error msg is not displaying")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_016 Testing ended *****************")

    def test_co_cluster_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_017 Testing Started *****************")
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_block()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(3)
        self.homepage.test_click_submit()
        if "Please Select a Cluster" in self.driver.page_source:
            print("Please Select a Cluster, error msg is displaying")
            self.logger.error("*********** Please Select a Cluster, error msg is displaying *********")
        else:
            self.logger.error("*********** Please Select a Cluster, error msg is displaying *********")
            print("Please Select a Cluster, error msg is not displaying")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_017 Testing ended *****************")

    def test_co_home_button(self):
        self.logger.info("*************** Tc_cQube_homepage_018 Testing Started *****************")
        time.sleep(2)
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_on_home_button()
        if 'Please select your role' in self.driver.page_source:
            print("Home_button is working")
            self.logger.error("*********** Home_button is working *********")
        else:
            self.logger.error("*********** Home_button is not working *********")
            print("Home_button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_018 Testing ended *****************")

    def test_co_logout(self):
        self.logger.info("*************** Tc_cQube_homepage_019 Testing Started *****************")
        time.sleep(2)
        self.homepage.test_click_on_cluster_button()
        time.sleep(5)
        self.homepage.test_click_logout_button()
        if "login" in self.driver.current_url:
            print("Logout button is working")
            self.logger.error("*********** Logout button is working *********")
        else:
            self.logger.error("*********** Logout button is not working *********")
            print("Logout button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_019 Testing ended *****************")

    # '''================================================================================================================='''
    def test_sp_click_the_school_principal_button(self):
        self.logger.info("*************** Tc_cQube_homepage_020 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        cluster_tittle = "Hello School Principal"
        if cluster_tittle in self.driver.page_source:
            print("School principal button is working")
            self.logger.error("*********** School principal button is working *********")
        else:
            self.logger.error("*********** School principal button is not working *********")
            print("School principal button is not working")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_020 Testing ended *****************")

    def test_sp_district_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_021 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        district_tittle = "Select District"
        if district_tittle in self.driver.page_source:
            print("District dropdown is present in school principal page")
            self.logger.error("*********** District button is present in school principal page *********")
        else:
            self.logger.error("*********** District button is not present in school principal page *********")
            print("District dropdown is not present in school principal page")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_021 Testing ended *****************")

    def test_sp_options_in_district_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_022 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        if len(options) != 0:
            print("District options are present in the district dropdown")
            self.logger.error("*********** District options are present in the district dropdown *********")
        else:
            self.logger.error("*********** District options are not present in the district dropdown *********")
            print("District options are not present in the district dropdown")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_022 Testing ended *****************")

    def test_sp_block_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_023 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            time.sleep(5)
            block_tittle = "Select Block"
            if block_tittle in self.driver.page_source:
                print("Block dropdown is present in school principal page")
                self.logger.error("*********** Block button is present in school principal page *********")
            else:
                print("Block dropdown is present in school principal page")
                self.logger.error("*********** Block button is present in school principal page *********")
                assert False
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_023 Testing ended *****************")

    def test_sp_options_in_block_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_024 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            time.sleep(5)
            self.homepage.test_click_block()
            time.sleep(3)
            options_block = self.homepage.get_dropdown_values()
            print(len(options_block))
            if len(options_block) != 0:
                print("Block options are present in the block dropdown")
                self.logger.error("*********** Block options are present in the block dropdown *********")
            else:
                print("Block options are not present in the block dropdown")
                self.logger.error("*********** Block options are not present in the block dropdown *********")
                assert False
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_024 Testing ended *****************")

    def test_sp_cluster_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_025 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                time.sleep(5)
                cluster_tittle = "Select Cluster"
                if cluster_tittle in self.driver.page_source:
                    print("Cluster dropdown is present in school principal page")
                    self.logger.error("*********** Cluster button is present in school principal page *********")
                else:
                    print("Cluster dropdown is not present in school principal page")
                    self.logger.error("*********** Cluster button is not present in school principal page *********")
                    assert False
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_025 Testing ended *****************")

    def test_sp_options_cluster_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_026 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                if len(cluster_options) != 0:
                    print("Cluster options are present in the cluster dropdown")
                    self.logger.error("*********** Cluster options are present in the cluster dropdown *********")
                else:
                    self.logger.error("*********** Cluster options are not present in the cluster dropdown *********")
                    print('Cluster options are not present in the cluster dropdown ')
                    assert False
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_026 Testing ended *****************")

    def test_sp_school_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_027 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                for k in range(len(cluster_options)):
                    opts = self.homepage.get_each_dropdown_value_id(k)
                    opts.click()
                    time.sleep(4)
                    school_tittle = "Select School"
                    if school_tittle in self.driver.page_source:
                        print('Each cluster options are selecting and school dropdown is displaying')
                        self.logger.error("*********** Each cluster options are selecting and school dropdown is not "
                                          "displaying *********")
                    else:
                        self.logger.error("*********** Each cluster options are not selecting and school dropdown is "
                                          "not displaying *********")
                        print('Each cluster options are not selecting and school dropdown is not displaying')
                        assert False
                    self.homepage.test_click_cluster()
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_027 Testing ended *****************")

    def test_sp_options_school_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_028 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                for k in range(len(cluster_options)):
                    opts = self.homepage.get_each_dropdown_value_id(k)
                    opts.click()
                    self.homepage.test_click_school()
                    school_options = self.homepage.get_dropdown_values()
                    time.sleep(2)
                    if len(school_options) != 0:
                        print('school have options ')
                    else:
                        print('school does not have options ')
                        assert False
                    self.homepage.test_click_cluster()
                self.homepage.test_click_block()
            self.homepage.test_click_dist()

    def test_sp_options_selecting_cluster_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_029 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                for k in range(len(cluster_options)):
                    opts = self.homepage.get_each_dropdown_value_id(k)
                    opts.click()
                    self.homepage.test_click_school()
                    school_options = self.homepage.get_dropdown_values()
                    time.sleep(2)
                    for m in range(len(school_options)):
                        opts = self.homepage.get_each_dropdown_value_id(m)
                        school_option_text = opts.text
                        opts.click()
                        if school_option_text in self.driver.page_source:
                            print('Each school options are selecting')
                        else:
                            print('school options are not selecting')
                            assert False
                        self.homepage.test_click_school()
                    self.homepage.test_click_cluster()
                self.homepage.test_click_block()
            self.homepage.test_click_dist()

    def test_sp_submit_button(self):
        self.logger.info("*************** Tc_cQube_homepage_030 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(0)
        opts.click()
        self.homepage.test_click_block()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(0)
        opts.click()
        self.homepage.test_click_cluster()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(0)
        opts.click()
        time.sleep(5)
        self.homepage.test_click_school()
        time.sleep(2)
        opts = self.homepage.get_each_dropdown_value_id(0)
        opts.click()
        self.homepage.test_click_submit()
        time.sleep(3)
        if 'Summary Statistics' in self.driver.page_source:
            print("")
        else:
            assert False

    def test_sp_district_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_031 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_submit()
        if 'Please Select a District' in self.driver.page_source:
            print("")
        else:
            assert False

    def test_sp_block_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_032 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(3)
        self.homepage.test_click_submit()
        if 'Please Select a Block' in self.driver.page_source:
            print("")
        else:
            assert False

    def test_sp_cluster_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_033 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_block()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(3)
        self.homepage.test_click_submit()
        if 'Please Select a Cluster' in self.driver.page_source:
            print("")
        else:
            assert False

    def test_sp_school_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_034 Testing Started *****************")
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_block()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_cluster()
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(3)
        self.homepage.test_click_submit()
        if 'Please Select a School' in self.driver.page_source:
            print("")
        else:
            assert False

    def test_sp_home_button(self):
        self.logger.info("*************** Tc_cQube_homepage_035 Testing Started *****************")
        time.sleep(2)
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_on_home_button()
        if "Please select your role" in self.driver.page_source:
            print("")
        else:
            assert False

    def test_sp_logout(self):
        self.logger.info("*************** Tc_cQube_homepage_036 Testing Started *****************")
        time.sleep(2)
        self.homepage.test_click_on_school_principal()
        time.sleep(5)
        self.homepage.test_click_logout_button()
        if "login" in self.driver.current_url:
            print("")
        else:
            assert False

    # '''================================================================================================================='''

    def test_click_the_class_teacher_button(self):
        self.logger.info("*************** Tc_cQube_homepage_037 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        cluster_tittle = "Hello Class Teacher"
        if cluster_tittle in self.driver.page_source:
            print("")
        else:
            assert False

    def test_cl_district_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_038 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        district_tittle = "Select District"
        if district_tittle in self.driver.page_source:
            print("")
        else:
            assert False

    def test_cl_options_in_district_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_039 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        if len(options) != 0:
            print("")
        else:
            assert False

    def test_cl_block_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_040 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            time.sleep(5)
            block_tittle = "Select Block"
            if block_tittle in self.driver.page_source:
                print("")
            else:
                assert False
            self.homepage.test_click_dist()

    def test_cl_options_in_block_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_041 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            time.sleep(5)
            self.homepage.test_click_block()
            time.sleep(3)
            options_block = self.homepage.get_dropdown_values()
            print(len(options_block))
            if len(options_block) != 0:
                print('Block have options ')
            else:
                print('Block does not have options')
                assert False
            self.homepage.test_click_dist()

    def test_cl_cluster_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_042 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                time.sleep(5)
                cluster_tittle = "Select Cluster"
                if cluster_tittle in self.driver.page_source:
                    print("")
                else:
                    assert False
                self.homepage.test_click_block()
            self.homepage.test_click_dist()

    def test_cl_options_cluster_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_043 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                if len(cluster_options) != 0:
                    print('Cluster have options ')
                else:
                    print('Cluster does not have options ')
                    assert False
                self.homepage.test_click_block()
            self.homepage.test_click_dist()

    def test_cl_options_school_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_044 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                for k in range(len(cluster_options)):
                    opts = self.homepage.get_each_dropdown_value_id(k)
                    opts.click()
                    self.homepage.test_click_school()
                    school_options = self.homepage.get_dropdown_values()
                    time.sleep(2)
                    if len(school_options) != 0:
                        print('school have options ')
                    else:
                        print('school does not have options ')
                        assert False
                    self.homepage.test_click_cluster()
                self.homepage.test_click_block()
            self.homepage.test_click_dist()

    def test_cl_grade_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_045 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                for k in range(len(cluster_options)):
                    opts = self.homepage.get_each_dropdown_value_id(k)
                    opts.click()
                    self.homepage.test_click_school()
                    school_options = self.homepage.get_dropdown_values()
                    time.sleep(2)
                    for m in range(len(school_options)):
                        opts = self.homepage.get_each_dropdown_value_id(m)
                        opts.click()
                        time.sleep(3)
                        grade = "Select Grade"
                        if grade in self.driver.page_source:
                            print('Each school options are selecting and grade dropdown is displaying ')
                        else:
                            print('Each school options are selecting and grade dropdown is displaying')
                            assert False
                        self.homepage.test_click_school()
                    self.homepage.test_click_cluster()
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_045 Testing ended *****************")

    def test_cl_options_grade_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_046 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                for k in range(len(cluster_options)):
                    opts = self.homepage.get_each_dropdown_value_id(k)
                    opts.click()
                    self.homepage.test_click_school()
                    school_options = self.homepage.get_dropdown_values()
                    time.sleep(2)
                    for m in range(len(school_options)):
                        opts = self.homepage.get_each_dropdown_value_id(m)
                        opts.click()
                        time.sleep(3)
                        self.homepage.test_click_grade()
                        grade_options = self.homepage.get_dropdown_values()
                        time.sleep(2)
                        if len(grade_options) != 0:
                            print('grade have options ')
                            self.logger.error(
                                "*********** options are present in grade dropdown *********")
                        else:
                            self.logger.error(
                                "*********** options are not present in grade dropdown *********")
                            print('grade does not have options ')
                            assert False
                        self.homepage.test_click_school()
                    self.homepage.test_click_cluster()
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_046 Testing ended *****************")

    def test_cl_grade_options_selecting_dropdown(self):
        self.logger.info("*************** Tc_cQube_homepage_047 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        options = self.homepage.get_dropdown_values()
        for i in range(len(options)):
            opts = self.homepage.get_each_dropdown_value_id(i)
            opts.click()
            self.homepage.test_click_block()
            block_options = self.homepage.get_dropdown_values()
            time.sleep(3)
            for j in range(len(block_options)):
                opts = self.homepage.get_each_dropdown_value_id(j)
                opts.click()
                self.homepage.test_click_cluster()
                cluster_options = self.homepage.get_dropdown_values()
                time.sleep(3)
                for k in range(len(cluster_options)):
                    opts = self.homepage.get_each_dropdown_value_id(k)
                    opts.click()
                    self.homepage.test_click_school()
                    school_options = self.homepage.get_dropdown_values()
                    time.sleep(2)
                    for m in range(len(school_options)):
                        opts = self.homepage.get_each_dropdown_value_id(m)
                        opts.click()
                        time.sleep(3)
                        self.homepage.test_click_grade()
                        grade_options = self.homepage.get_dropdown_values()
                        time.sleep(2)
                        for n in range(len(grade_options)):
                            opts = self.homepage.get_each_dropdown_value_id(n)
                            grade_option_text = opts.text
                            opts.click()
                            if grade_option_text in self.driver.page_source:
                                print('Each grade options are selecting')
                                self.logger.error(
                                    "*********** Each grade options are selecting in class teacher page *********")
                            else:
                                self.logger.error(
                                    "*********** Each grade options are not selecting in class teacher page *********")
                                print('grade options are not selecting')
                                assert False
                            self.homepage.test_click_grade()
                        self.homepage.test_click_school()
                    self.homepage.test_click_cluster()
                self.homepage.test_click_block()
            self.homepage.test_click_dist()
            self.logger.info("*************** Tc_cQube_homepage_047 Testing ended *****************")

    def test_cl_submit_button(self):
        self.logger.info("*************** Tc_cQube_homepage_048 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(0)
        opts.click()
        self.homepage.test_click_block()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(0)
        opts.click()
        self.homepage.test_click_cluster()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(0)
        opts.click()
        time.sleep(5)
        self.homepage.test_click_school()
        time.sleep(2)
        opts = self.homepage.get_each_dropdown_value_id(0)
        opts.click()
        self.homepage.test_click_grade()
        time.sleep(2)
        opts = self.homepage.get_each_dropdown_value_id(0)
        opts.click()
        self.homepage.test_click_submit()
        time.sleep(5)
        if 'Summary Statistics' in self.driver.page_source:
            print("submit button is working in class teacher page")
            self.logger.error("*********** submit button is working in class teacher page *********")
        else:
            self.logger.error("*********** submit button is not working in class teacher page *********")
            print("submit button is not working in class teacher page")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_048 Testing ended *****************")

    def test_cl_district_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_049 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_submit()
        if 'Please Select a District' in self.driver.page_source:
            print("Please Select a District, error msg is displaying in class teacher page")
            self.logger.error("*********** Please Select a District, error msg is displaying in class teacher page "
                              "*********")
        else:
            print("Please Select a District, error msg is not displaying in class teacher page")
            self.logger.error("*********** Please Select a District, error msg is not displaying in class teacher page "
                              "*********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_049 Testing ended *****************")

    def test_cl_block_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_050 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(3)
        self.homepage.test_click_submit()
        if 'Please Select a Block' in self.driver.page_source:
            print("Please Select a Block, error msg is displaying in class teacher page")
            self.logger.error("*********** Please Select a Block, error msg is displaying in class teacher page "
                              "*********")
        else:
            print("Please Select a Block, error msg is not displaying in class teacher page")
            self.logger.error("*********** Please Select a Block, error msg is not displaying in class teacher page "
                              "*********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_050 Testing ended *****************")

    def test_cl_cluster_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_051 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_block()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(3)
        self.homepage.test_click_submit()
        if 'Please Select a Cluster' in self.driver.page_source:
            print("Please Select a Cluster, error msg is displaying in class teacher page")
            self.logger.error("*********** Please Select a cluster, error msg is displaying in class teacher page "
                              "*********")
        else:
            print("Please Select a Cluster, error msg is not displaying in class teacher page")
            self.logger.error("*********** Please Select a cluster, error msg is not displaying in class teacher page "
                              "*********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_051 Testing ended *****************")

    def test_cl_school_error_message(self):
        self.logger.info("*************** Tc_cQube_homepage_052 Testing Started *****************")
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_dist()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_block()
        time.sleep(3)
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        self.homepage.test_click_cluster()
        opts = self.homepage.get_each_dropdown_value_id(1)
        opts.click()
        time.sleep(3)
        self.homepage.test_click_submit()
        if 'Please Select a School' in self.driver.page_source:
            print("Please Select a School, error msg is displaying in class teacher page")
            self.logger.error("*********** Please Select a School, error msg is displaying in class teacher page "
                              "*********")
        else:
            self.logger.error("*********** Please Select a School, error msg is not displaying in class teacher page "
                              "*********")
            print("Please Select a School, error msg is not displaying in class teacher page")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_052 Testing ended *****************")

    def test_cl_home_button(self):
        self.logger.info("*************** Tc_cQube_homepage_053 Testing Started *****************")
        time.sleep(2)
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_on_home_button()
        if "Please select your role" in self.driver.page_source:
            print("home button is working in class teacher page")
            self.logger.error("*********** home button is working in class teacher page *********")
        else:
            self.logger.error("*********** home button is not working in class teacher page *********")
            print("home button is working in class teacher page")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_053 Testing ended *****************")

    def test_cl_logout(self):
        self.logger.info("*************** Tc_cQube_homepage_054 Testing Started *****************")
        time.sleep(2)
        self.homepage.test_click_on_class_teacher()
        time.sleep(5)
        self.homepage.test_click_logout_button()
        if "login" in self.driver.current_url:
            print("logout button is working in class teacher page")
            self.logger.error("*********** logout button is working in class teacher page *********")
        else:
            print("logout button is not working in class teacher page")
            self.logger.error("*********** logout button is not working in class teacher page *********")
            assert False
        self.logger.info("*************** Tc_cQube_homepage_054 Testing ended *****************")
