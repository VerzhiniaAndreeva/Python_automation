from unittest import TestCase
from Common.driver_initialize import DriverInitialize

class BaseTest(TestCase):

    driver = None

    def setUp(self):
        test_Settings = DriverInitialize.getTestJsonFileSettings(self)
        base_URL = DriverInitialize.getJsonFileAttributeValue(self, test_Settings, "instance")
        browserType = DriverInitialize.getJsonFileAttributeValue(self, test_Settings, "browser")
        resolution = DriverInitialize.getJsonFileAttributeValue(self, test_Settings, "resolution").split(',')

        self.driver = DriverInitialize.initialize(self, browserType)
        self.driver.set_window_size(resolution[0], resolution[1])
        self.driver.maximize_window()
        self.driver.get(base_URL)

        return self.driver

    def tearDown(self):
        self.driver.quit()