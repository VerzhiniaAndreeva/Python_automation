import unittest
from PageObjects.dresses_page import Dresses
from Tests.base_test import BaseTest
from PageObjects.login_page import LoginPage

class MyTestCaseDresses(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.assertEqual(self.loginPage.getHeaderText(), "Automation Practice Website")
        dressesPage = Dresses(self.driver)
        dressesPage.selectDressTab()
        dressesPage.selectCasualDressesCategory()

if __name__ == '__main__':
    unittest.main()
