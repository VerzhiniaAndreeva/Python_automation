import unittest
from Tests.base_test import BaseTest
from PageObjects.login_page import LoginPage


class MyTestCase(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage()
        self.assertEqual("Automation Practice Website", self.loginPage.getHeaderText())

if __name__ == '__main__':
    unittest.main()
