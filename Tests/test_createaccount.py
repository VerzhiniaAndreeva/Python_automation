import unittest
from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.signIn_page import SignIn
from Tests.base_test import BaseTest
from PageObjects.login_page import LoginPage


class MyTestCaseCreateAccount(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage()
        self.assertEqual("Automation Practice Website", self.loginPage.getHeaderText())
        signInPage = SignIn()
        signInPage.select_lnk_signIn()
        self.assertEqual("AUTHENTICATION", self.loginPage.getHeaderText())
        signInPage.enterInfield_fld_emailAddress('v.andreeva@free.fr')
        signInPage.use_btn_submitCreate()
        self.assertEqual("CREATE AN ACCOUNT", self.loginPage.getHeaderText())


if __name__ == '__main__':
    unittest.main()
