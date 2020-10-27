import unittest
from Tests import test_cases
from PageObjects import dresses_page
from Common.driver_initialize import DriverInitialize
from PageObjects.login_page import LoginPage

class MyTestCaseDresses(unittest.TestCase):
    def test_dresses(self):
        test_cases.MyTestCase.setUp(self)
        test_cases.MyTestCase.test_login(self)
        dresses_page.selectDressTab(self)


if __name__ == '__main__':
    unittest.main()
