import unittest
from PageObjects.dressesPage import Dresses
from Tests.base_test import BaseTest
from PageObjects.homePage import HomePage

class MyTestCaseDresses(BaseTest):

    def test_Select_Casual_Dresses(self):

        self.homePage = HomePage()

        self.assertEqual("Automation Practice Website", self.homePage.getHeaderText())

        dressesPage = Dresses()

        dressesPage\
            .select_tab_dressesTab()\
            .select_lnk_casualDresses()

if __name__ == '__main__':
    unittest.main()
