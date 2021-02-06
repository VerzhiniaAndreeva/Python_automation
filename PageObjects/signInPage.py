from selenium.webdriver.common.by import By

from Common.do import Do
from Common.get import Get
from PageObjects.basePage import BasePage
from Common.wait import Wait


class SignIn(BasePage):

    @property
    def lnk_signIn(self):
        return By.CLASS_NAME, 'login'

    @property
    def fld_emailAddress(self):
        return By.ID, 'email_create'

    @property
    def form_createAccount(self):
        return By.ID, 'create-account_form'

    @property
    def btn_submitCreate(self):
        return By.ID, 'SubmitCreate'

    @property
    def fld_customerFirstname(self):
        return By.ID, 'customer_firstname'

    @property
    def fld_customerLastname(self):
        return By.ID, 'customer_lastname'

    @property
    def rbt_genderFemale(self):
        return By.ID, 'id_gender2'

    @property
    def rbt_genderMale(self):
        return By.ID, 'id_gender1'

    @property
    def fld_email(self):
        return By.ID, 'email'

    @property
    def fld_password(self):
        return By.ID, 'passwd'

    @property
    def fld_firstname(self):
        return By.ID, 'firstname'

    @property
    def fld_lastname(self):
        return By.ID, 'lastname'

    @property
    def ddl_days(self):
        return By.ID, 'days'

    @property
    def ddl_months(self):
        return By.ID, 'months'

    @property
    def ddl_years(self):
        return By.ID, 'years'

    @property
    def fld_address(self):
        return By.ID, 'address1'

    @property
    def fld_city(self):
        return By.ID, 'city'

    @property
    def fld_postcode(self):
        return By.ID, 'postcode'

    @property
    def fld_phone_mobile(self):
        return By.ID, 'phone_mobile'

    @property
    def ddl_state(self):
        return By.ID, 'id_state'

    @property
    def ddl_country(self):
        return By.ID, 'id_country'

    @property
    def fld_alias(self):
        return By.ID, 'alias'

    @property
    def btn_submitAccount(self):
        return By.ID, 'submitAccount'

    @property
    def btn_logout(self):
        return By.CLASS_NAME, 'logout'

    @property
    def fld_first_name(self):
        return By.ID, 'firstname'

    @property
    def fld_last_name(self):
        return By.ID, 'lastname'

    def icon_heart(self):
        return By.CLASS_NAME, 'icon-heart'

    def select_lnk_signIn(self):
        Do().click(self.lnk_signIn)
        return self

    def use_btn_submitCreate(self):
        Do().click(self.btn_submitCreate)
        Wait().ForElementDisplayed(self.fld_customerFirstname)
        return self

    def enterInfield_fld_emailAddress(self, email):
        Do().sendKeys(self.fld_emailAddress, email)
        return self

    def enterInField_fld_customer_firstname(self, firstName):
        Do().sendKeys(self.fld_customerFirstname, firstName)
        Wait().ForElementPresent(self.fld_customerLastname)
        return self

    def enterInField_fld_customer_lastname(self, lastName):
        Do().sendKeys(self.fld_customerLastname, lastName)
        Wait().ForElementPresent(self.fld_password)
        return self

    def selectGender(self, gender):
        if gender == "Mrs":
            Do.click(self.rbt_genderMale)
            return self
        else:
            Do().click(self.rbt_genderFemale)
            return self

    def enterInField_fld_password(self, password):
        Do().sendKeys(self.fld_password, password)
        Wait().ForElementPresent(self.fld_firstname)
        return self

    def enter_birthday_date(self, day, month, year):
        Do().selectDropDownOptoin(self.ddl_days, day)
        Do().selectDropDownOptoin(self.ddl_months, month)
        Do().selectDropDownOptoin(self.ddl_years, year)
        return self

    def enterInField_fld_address(self, address):
        Do().sendKeys(self.fld_address, address)
        Wait().ForElementPresent(self.fld_city)
        return self

    def enterInField_fld_city(self, city):
        Do().sendKeys(self.fld_city, city)
        Wait().ForElementPresent(self.fld_postcode)
        return self

    def enterInField_fld_postcode(self, postcode):
        Do().sendKeys(self.fld_postcode, postcode)
        Wait().ForElementPresent(self.fld_phone_mobile)
        return self

    def enterInField_fld_phone_mobile(self, phone_mobile):
        Do().sendKeys(self.fld_phone_mobile, phone_mobile)
        Wait().ForElementPresent(self.fld_postcode)
        return self

    def select_ddl_state(self, state):
        Do().selectDropDownOptoin(self.ddl_state, state)
        return self

    def select_ddl_country(self, country):
        Do().selectDropDownOptoin(self.ddl_country, country)
        return self

    def enterInField_fld_alias(self, alias):
        Do().sendKeys(self.fld_alias, alias)
        Wait().ForElementPresent(self.fld_postcode)
        return self

    def use_btn_submitAccount(self):
        Do().click(self.btn_submitAccount)
        Wait().ForElementNotDisplayed(self.fld_alias)
        return self

    def logout(self):
        Do().click(self.btn_logout)
        return self

    def get_email_text(self):
        return Get().elementText(self.fld_email)

    def get_first_name(self):
        return Get().elementText(self.fld_first_name)

    def get_last_name(self):
        return Get().elementText(self.fld_last_name)