import unittest
from PageObjects.signInPage import SignIn
from Tests.base_test import BaseTest
from PageObjects.homePage import HomePage


class MyTestCaseCreateAccount(BaseTest):

    def test_Create_Account(self):

        self.homePage = HomePage()

        self.assertEqual("Automation Practice Website", self.homePage.getHeaderText())

        signInPage = SignIn()

        signInPage\
            .select_lnk_signIn()

        self.assertEqual("AUTHENTICATION", self.homePage.getHeaderText())

        signInPage\
            .enterInfield_fld_emailAddress('v.andreeva@free.fr')\
            .use_btn_submitCreate()

        self.assertEqual("CREATE AN ACCOUNT", self.homePage.getHeaderText())

if __name__ == '__main__':
    unittest.main()
