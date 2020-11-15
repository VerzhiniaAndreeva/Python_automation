from selenium.webdriver.common.by import By
from PageObjects.basePage import BasePage


class SignIn(BasePage):

    @property
    def lnk_signIn(self):
        return BasePage().findElement(By.CLASS_NAME, '.login')

    @property
    def fld_emailAddress(self):
        return BasePage().findElement(By.ID, 'email_create')

    def select_lnk_signIn(self):
        return self.lnk_signIn.click()

    def enterInfield_fld_emailAddress(self, text):
        return self.enter_in_field(text)