import unittest
from PageObjects.signIn_page import SignIn
from Tests.base_test import BaseTest
from PageObjects.login_page import LoginPage

class MyTestCaseCreateAccount(BaseTest):

    def createAccount(self):
        self.loginPage = LoginPage()
        self.assertEqual("Automation Practice Website", self.loginPage.getHeaderText())
        signInPage = SignIn()
        signInPage.select_lnk_signIn()
        signInPage.enterInfield_fld_emailAddress('v.andreeva@free.fr')

if __name__ == '__main__':
    unittest.main()
