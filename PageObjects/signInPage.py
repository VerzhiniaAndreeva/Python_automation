from selenium.webdriver.common.by import By

from Common.do import Do
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

    def select_lnk_signIn(self):
        Do().click(self.lnk_signIn)
        return self

    def loseFocus(self):
        element = By.ID, 'email'
        Do().click(element)
        return self

    def use_btn_submitCreate(self):
        Do().click(self.btn_submitCreate)
        Wait().ForElementDisplayed(self.fld_customerFirstname)
        return self

    def enterInfield_fld_emailAddress(self, email):
        Do().sendKeys(self.fld_emailAddress, email)
        return self