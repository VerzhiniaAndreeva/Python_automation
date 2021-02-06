import unittest
from PageObjects.signInPage import SignIn
from PageObjects.dressesPage import Dresses
from Tests.base_test import BaseTest
from PageObjects.homePage import HomePage


class MyTestCaseDresses(BaseTest):

   def test_casual_dresses(self):

        self.homePage = HomePage()

        self.assertEqual("Automation Practice Website", self.homePage.getHeaderText())

        dressesPage = Dresses()

        dressesPage\
            .select_tab_dressesTab()\
            .select_lnk_casualDresses()\
            .select_product()\
            .add_to_cart()\
            .proceed_to_checkout()\
            .standard_chekcout()

        signInPage = SignIn()

        self.assertEqual("AUTHENTICATION", self.homePage.getHeaderText())

        signInPage \
                .enterInfield_fld_emailAddress('v1.andreeva@free.fr') \
                .use_btn_submitCreate()

        signInPage \
            .selectGender('Ms') \
            .enterInField_fld_customer_firstname('Very') \
            .enterInField_fld_customer_lastname('Andrea') \
            .enterInField_fld_password("123ergggggg") \
            .enterInField_fld_address("St.George str, 9") \
            .enterInField_fld_city("Assenovgrad") \
            .select_ddl_state('1') \
            .enterInField_fld_postcode("12345") \
            .select_ddl_country('21') \
            .enterInField_fld_phone_mobile("0889476987") \
            .enterInField_fld_alias("Professor Folk 2") \
            .use_btn_submitAccount()

        self.assertEqual("ADDRESSES", self.homePage.getHeaderText())

        dressesPage \
            .use_btn_process_address()

        self.assertEqual("SHIPPING", self.homePage.getHeaderText())

if __name__ == '__main__':
        unittest.main()
