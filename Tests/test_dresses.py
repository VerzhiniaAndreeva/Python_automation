import unittest
from PageObjects.dresses_page import Dresses
from Tests.base_test import BaseTest
from PageObjects.login_page import LoginPage

class MyTestCaseDresses(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage()
        self.assertEqual("Automation Practice Website", self.loginPage.getHeaderText())
        dressesPage = Dresses()
        dressesPage.select_tab_dressesTab()
        dressesPage.select_lnk_casualDresses()

if __name__ == '__main__':
    unittest.main()
