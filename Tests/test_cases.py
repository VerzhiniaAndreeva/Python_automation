import unittest
from Common.driver_initialize import DriverInitialize
from PageObjects.login_page import LoginPage


class MyTestCase(unittest.TestCase):

    driver = None
    def setUp(self):
        test_Settings = DriverInitialize.getTestJsonFileSettings(self)
        base_URL = DriverInitialize.getJsonFileAttributeValue(test_Settings, "instance")
        browserType = DriverInitialize.getJsonFileAttributeValue(test_Settings, "browser")
        resolution = DriverInitialize.getJsonFileAttributeValue(test_Settings, "resolution").split(',')

        self.driver = DriverInitialize.initialize(browserType)
        self.driver.set_window_size(resolution[0], resolution[1])
        self.driver.maximize_window()
        self.driver.get(base_URL)
        print("Setup executed")

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.assertEqual(self.loginPage.getHeaderText(), "Automation Practice Website")

    def tearDown(self):
        self.driver.quit()
        print("tearDown executed")

if __name__ == '__main__':
    unittest.main()
