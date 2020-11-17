import unittest
from PageObjects.signIn_page import SignIn
from Tests.base_test import BaseTest
from PageObjects.login_page import LoginPage

class MyTestCaseCreateAccount(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage()
        self.assertEqual("Automation Practice Website", self.loginPage.getHeaderText())
        signInPage = SignIn()
        signInPage.select_lnk_signIn()
        signInPage.wait_for_emailAddress_visibility()
        signInPage.enterInfield_fld_emailAddress()

if __name__ == '__main__':
    unittest.main()
