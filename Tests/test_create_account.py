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
            .enterInfield_fld_emailAddress('v.a.andreeva@free.fr')\
            .use_btn_submitCreate()

        self.assertEqual("CREATE AN ACCOUNT", self.homePage.getHeaderText())
        signInPage\
            .selectGender('Ms')\
            .enterInField_fld_customer_firstname('Very')\
            .enterInField_fld_customer_lastname('Andrea')\
            .enterInField_fld_password("123ergggggg")\
            .enterInField_fld_address("St.George str, 9")\
            .enterInField_fld_city("Assenovgrad")\
            .select_ddl_state('1')\
            .enterInField_fld_postcode("12345")\
            .select_ddl_country('21')\
            .enterInField_fld_phone_mobile("0889476987")\
            .enterInField_fld_alias("Professor Folk 2")\
            .use_btn_submitAccount()

        self.assertEqual("MY ACCOUNT", self.homePage.getHeaderText())

        signInPage\
            .logout()


if __name__ == '__main__':
    unittest.main()
