import time
from selenium.webdriver.common.by import By

from Page_of_objects.CqubeUi.BasePage import Base
from Utilities.ReadProperties import ReadConfig


class loginpage(Base):
    user_id = (By.ID, "username1")
    password = (By.ID, "password1")
    login = (By.ID, "login")

    def __init__(self, driver):
        super().__init__(driver)


    # List of selenium locator of dashboard screen
    user_name_field = ""
    password_filed = ""
    login_button = ""
    login_logfile = "../../../Logs/Login.log"
    dashboard_logfile = "../../../Logs/Dashboard.log"

    def open_cqube_application(self):
        print(ReadConfig.get_application_url())
        self.get_url(ReadConfig.get_application_url())
        time.sleep(5)

    def get_user_id(self):
        user_id = self.get_web_elements(self.user_id)
        return user_id

    def get_password(self):
        password = self.get_web_elements(self.password)
        return password

    def test_click_login(self):
        self.click(self.login)

    def open_login_page(self):
        self.driver.find_element(By.ID, "username1").send_keys(ReadConfig.get_username())
        self.driver.find_element(By.ID, "password1").send_keys(ReadConfig.get_password())
        time.sleep(2)
        self.click(self.login)

    def open_login_page_invalid_password(self):
        self.driver.find_element(By.ID, "username1").send_keys(ReadConfig.get_username())
        self.driver.find_element(By.ID, "password1").send_keys(ReadConfig.get_negative_password())
        time.sleep(2)
        self.click(self.login)

    def open_login_page_invalid_username(self):
        self.driver.find_element(By.ID, "username1").send_keys(ReadConfig.get_negative_username())
        self.driver.find_element(By.ID, "password1").send_keys(ReadConfig.get_password())
        time.sleep(2)
        self.click(self.login)

    def open_login_page_blank_username(self):
        self.driver.find_element(By.ID, "username1").send_keys(ReadConfig.get_username_blank())
        self.driver.find_element(By.ID, "password1").send_keys(ReadConfig.get_password())
        time.sleep(2)
        self.click(self.login)

    def open_login_page_blank_password(self):
        self.driver.find_element(By.ID, "username1").send_keys(ReadConfig.get_username())
        self.driver.find_element(By.ID, "password1").send_keys(ReadConfig.get_blank_password())
        time.sleep(2)
        self.click(self.login)

    def open_login_page_blank_username_password(self):
        self.driver.find_element(By.ID, "username1").send_keys(ReadConfig.get_username_blank())
        self.driver.find_element(By.ID, "password1").send_keys(ReadConfig.get_blank_password())
        time.sleep(2)
        self.click(self.login)