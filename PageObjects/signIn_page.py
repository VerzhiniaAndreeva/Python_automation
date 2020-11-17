from selenium.webdriver.common.by import By
from PageObjects.basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignIn(BasePage):

    @property
    def lnk_signIn(self):
        return BasePage().findElement(By.CLASS_NAME, 'login')

    @property
    def fld_emailAddress(self):
        return BasePage().findElement(By.ID, 'email_create')

    def select_lnk_signIn(self):
        return self.lnk_signIn.click()

    def fld_emailAddress_is_displayed(self):
        return self.fld_emailAddress.is_displayed()

    def wait_for_emailAddress_visibility(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.fld_emailAddress))

    def enterInfield_fld_emailAddress(self):
        return self.fld_emailAddress.send_keys('v.andreeva@free.fr')