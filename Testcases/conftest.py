import os

from selenium import webdriver
from Utilities.ReadProperties import ReadConfig


class ConfTest:
    """Below method is used to get the web driver"""

    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': ReadConfig.get_download_dir()}
        options.add_experimental_option('prefs', prefs)
        options.add_argument("--window-size=3860,2160")
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        return driver


    # def get_driver(self):
    #     options = webdriver.ChromeOptions()
    #     prefs = {'download.default_directory': ReadConfig.get_download_dir()}
    #     options.add_experimental_option('prefs', prefs)
    #     options.add_argument("--window-size=3860,2160")
    #     # options.add_argument('--headless')
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--disable-gpu')
    #     self.driver = webdriver.Chrome(options=options, executable_path=ReadConfig.get_chrome_driver_directory())
    #     self.driver.set_window_size(3860, 2160)
    #     print('window size :', self.driver.get_window_size())
    #     print("Current session is {}".format(self.driver.session_id))
    #     return self.driver

    # def get_driver(self):
    #     options = webdriver.ChromeOptions()
    #     prefs = {'download.default_directory': self.p.get_download_dir()}
    #     options.add_experimental_option('prefs', prefs)
    #     options.add_argument("--window-size=3860,2160")
    #     # options.add_argument('--headless')
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--disable-gpu')
    #     self.driver = webdriver.Chrome(options=options, executable_path=self.p.get_driver_path())
    #     self.driver.set_window_size(3860, 2160)
    #     print('window size :', self.driver.get_window_size())
    #     print("Current session is {}".format(self.driver.session_id))
    #     return self.driver

    def get_download_dir(self):
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd, 'Downloads')
        return download_path


def get_driver():
    return None
