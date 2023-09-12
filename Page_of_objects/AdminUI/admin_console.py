import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Page_of_objects.CqubeUi.BasePage import Base
from Utilities.ReadProperties import ReadConfig


class AdminConsole(Base):
    username = 'userName'
    password = 'password'
    login_btn = "loginBtn"
    health_monitor = "dashboardCard0"
    usage_dashboard = "usage_dashboard"
    debugger = "dashboardCard1"
    schema_generator_icon = "dashboardCard2"
    user_logo_menu = "user_menulist"
    hamburger_menu = "hamburger"
    logout_btn = "logout"
    a = "State Vidya Samiksha Kendra"
    home_btn = "home"
    dimension_radio = "dimension_radio"
    event_radio = "event_radio"
    schemas = "schema"
    upload_btn = 'fileupload'
    file_path = ''
    download_btn = 'download'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.count = 0

    def open_cqube_admin_application(self):
        self.get_url(ReadConfig.get_application_url())

    def open_cqube_application(self):
        print(ReadConfig.get_application_url())
        self.get_url(ReadConfig.get_application_url())
        time.sleep(5)

    def get_user_id(self):
        user_id = self.get_web_elements(self.username)
        return user_id

    def get_password(self):
        password = self.get_web_elements(self.password)
        return password

    def test_click_login(self):
        self.click(self.login_btn)

    def login_to_admin_console(self):
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_username())
        self.driver.find_element(By.ID, self.password).send_keys(ReadConfig.get_password())
        time.sleep(2)
        self.click(self.login_btn)

    def open_login_page_invalid_password(self):
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_username())
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_negative_password())
        time.sleep(2)
        self.click(self.login_btn)

    def open_login_page_invalid_username(self):
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_negative_username())
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_password())
        time.sleep(2)
        self.click(self.login_btn)

    def open_login_page_blank_username(self):
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_username_blank())
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_password())
        time.sleep(2)
        self.click(self.login_btn)

    def open_login_page_blank_password(self):
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_username())
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_blank_password())
        time.sleep(2)
        self.click(self.login_btn)

    def open_login_page_blank_username_password(self):
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_username_blank())
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.get_blank_password())
        time.sleep(2)
        self.click(self.login_btn)

    def check_admin_console_login_and_logout(self):
        self.login_to_admin_console()
        time.sleep(2)
        self.driver.find_element(By.ID,self.logout_btn).click()
        time.sleep(2)
        if 'login' in self.driver.current_url:
            print('Login & Logout buttons are working as expected ')
            assert True
        else:
            print('Login & Logout buttons are not working ')
            self.cout = self.count + 1
            assert False

    def click_on_hamburger_menu_button(self):
        self.driver.find_element(By.ID, self.hamburger_menu).click()

    def click_on_health_monitor_dashboard_icon(self):
        self.driver.find_element(By.ID, self.health_monitor).click()

    def click_on_usage_dashboard_icon(self):
        self.driver.find_element(By.ID, self.usage_dashboard).click()

    def click_on_debugger_dashboard_icon(self):
        self.driver.find_element(By.ID, self.debugger).click()

    def click_on_the_user_logo(self):
        self.driver.find_element(By.ID, self.user_logo_menu).click()

    def click_on_home_button(self):
        self.driver.find_element(By.ID, self.home_btn).click()

    def click_on_logout_button(self):
        self.click_on_the_user_logo()
        self.driver.find_element(By.ID, self.logout_btn).click()
        time.sleep(2)
        if 'login' in self.driver.current_url:
            print('Logout button is working as expected.')
            assert True
        else:
            print('Logout button is not working!!! ')
            assert False

    def check_dropdown_options(self):
        dropdown = Select(self.driver.find_element(By.ID, self.schemas))
        if len(dropdown.options) != 0:
            print(' Dropdown having Options')
            assert True
        else:
            print(" Dropdown does not having Options ")
            self.count = self.count + 1
            assert False
        return self.count

    def click_on_event_radio_btn(self):
        click_radio = self.driver.find_element(By.ID, self.event_radio)
        click_radio.click()

    def select_dropdown_options(self):
        sel_options = Select(self.driver.find_element(By.ID, self.schemas))
        for i in range(1, len(sel_options.options)):
            sel_options.select_by_index(i)
            print(sel_options.options[i].text, ' is dropdown options is selected. ')
            if sel_options.options[i].is_selected():
                assert True
            else:
                self.count = self.count + 1
                assert False
        return self.count

    def check_dimension_debugger_of_file(self):
        sel_options = Select(self.driver.find_element(By.ID, self.schemas))
        sel_options.select_by_visible_text('district')
        self.driver.find_element(By.ID, self.upload_btn).click()
        filepath = self.driver.find_element(By.XPATH, self.file_path)
        filepath.send_keys()
        filepath.click()
        self.driver.find_element(By.ID, self.debugger).click()
        time.sleep(3)

    def check_event_debugger_of_file(self):
        sel_options = Select(self.driver.find_element(By.ID, self.schemas))
        sel_options.select_by_visible_text("teacherspresent")
        self.driver.find_element(By.ID, self.upload_btn).click()
        filepath = self.driver.find_element(By.XPATH, self.file_path)
        filepath.send_keys()
        filepath.click()
        self.driver.find_element(By.ID, self.debugger).click()
        time.sleep(3)

    def check_dimension_debugger_of_pdf_file(self):
        sel_options = Select(self.driver.find_element(By.ID, self.schemas))
        sel_options.select_by_visible_text('district')
        self.driver.find_element(By.ID, self.upload_btn).click()
        filepath = self.driver.find_element(By.XPATH, self.file_path)
        filepath.send_keys()
        filepath.click()
        self.driver.find_element(By.ID, self.debugger).click()
        time.sleep(3)

    def check_dimension_debugger_of_json_file(self):
        sel_options = Select(self.driver.find_element(By.ID, self.schemas))
        sel_options.select_by_visible_text('district')
        self.driver.find_element(By.ID, self.upload_btn).click()
        filepath = self.driver.find_element(By.XPATH, self.file_path)
        filepath.send_keys()
        filepath.click()
        self.driver.find_element(By.ID, self.debugger).click()
        time.sleep(3)

    def check_input_fields_accepted_values(self):
        username = self.driver.find_element(By.ID, self.username)
        username.clear()
        username.send_keys('admin')
        time.sleep(1)
        if 'admin' in self.driver.page_source:
            print("Username Input field is accepted value ")
            assert True
        else:
            self.count = self.count + 1
            print(' Username Input box is not accepting the values ')
        password = self.driver.find_element(By.ID, self.password)
        password.clear()
        password.send_keys('Tibil@123')
        time.sleep(1)
        if 'Tibil@123' in self.driver.page_source:
            print(" Password Input field is accepted the value ")
            assert True
        else:
            self.count = self.count + 1
            assert False
        return self.count

