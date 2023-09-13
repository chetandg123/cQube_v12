import configparser
import os


# config = configparser.RawConfigParser()
# config.read(os.getcwd()+'../Configurations/config.ini')

# config = configparser.RawConfigParser()
# config.read('../Configurations/config.ini')


class ReadConfig:
    """Method that returns the application url"""

    def __int__(self, driver):
        self.driver = driver

    @staticmethod
    def get_config_ini_path():
        cwd = os.path.dirname(__file__)
        ini = os.path.join(cwd, '../Configurations/config.ini')
        return ini

    @staticmethod
    def get_application_url():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        url = config.get('config', 'url')
        return url

    @staticmethod
    def get_username():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path)
        username = config.get('config', 'username')
        return username

    @staticmethod
    def get_admin_application_url():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        url = config.get('config', 'adminURL')
        print('url of app ', url)
        return url

    @staticmethod
    def get_admin_username():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        admin_username = config.get('config', 'admin_username')
        return admin_username

    @staticmethod
    def get_admin_password():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        admin_password = config.get('config', 'admin_password')
        return admin_password

    @staticmethod
    def get_negative_username():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        username = config.get('config', 'username1')
        return username

    @staticmethod
    def get_username_blank():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        username = config.get('config', 'username_blank')
        return username

    @staticmethod
    def get_password():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        password = config.get('config', 'password')
        return password

    @staticmethod
    def get_negative_password():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        password = config.get('config', 'password1')
        return password

    @staticmethod
    def get_blank_password():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        password = config.get('config', 'password_blank')
        return password

    @staticmethod
    def get_school_attendance_monthname():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        month = config.get('config', 'month_name')
        return month

    @staticmethod
    def get_school_attendance_startdate():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        start_date = config.get('config', 'start_date')
        return start_date

    @staticmethod
    def get_school_attendance_enddate():
        path = ReadConfig()
        config = configparser.RawConfigParser()
        config.read(path.get_config_ini_path())
        end_date = config.get('config', 'end_date')
        return end_date

    """Method that returns the downloads dir path """

    @staticmethod
    def get_download_dir():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("Utilities", "")
        download_path = os.path.join(current_directory, 'Downloads')
        return download_path

    """Method that returns the drivers dir path """

    @staticmethod
    def get_chrome_driver_directory():
        # current_directory = os.path.dirname(__file__)
        # current_directory = current_directory.replace("Utilities", "")
        # chrome_directory_path = os.path.join(current_directory, '../Driver/chromedriver')
        # return chrome_directory_path
        cwd = os.path.dirname(__file__)
        driver_path = os.path.join(cwd, '../Driver/chrome')
        return driver_path

    """Method that returns the screenshots dir path """

    @staticmethod
    def get_screenshot_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("Utilities", "")
        screenshot_directory = os.path.join(current_directory, 'Screenshots')
        return screenshot_directory

    """Method that returns the logs dir path """

    @staticmethod
    def get_logs_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("Utilities", "")
        logs_directory = os.path.join(current_directory, 'Logs')
        return logs_directory
