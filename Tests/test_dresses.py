import unittest
from Tests import test_cases
from PageObjects import dresses_page
from Common.driver_initialize import DriverInitialize
from PageObjects.login_page import LoginPage

class MyTestCaseDresses(unittest.TestCase):
    def test_dresses(self):
        test_cases.MyTestCase.setUp()
        test_cases.MyTestCase.test_login()
        dresses_page.selectDressTab()


if __name__ == '__main__':
    unittest.main()
