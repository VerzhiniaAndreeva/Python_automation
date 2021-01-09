import unittest
from Tests.base_test import BaseTest
from PageObjects.homePage import HomePage


class MyTestCase(BaseTest):

    def test_Check_Home_Page_Header(self):

        self.homePage = HomePage()

        self.assertEqual("Automation Practice Website", self.homePage.getHeaderText())


if __name__ == '__main__':
    unittest.main()
