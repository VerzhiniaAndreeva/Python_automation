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

    @property
    def btn_submitCreate(self):
        return BasePage().findElement(By.ID, 'SubmitCreate')

    def select_lnk_signIn(self):
        return self.lnk_signIn.click()

    def fld_emailAddress_is_displayed(self):
        return self.fld_emailAddress.is_displayed()

    def use_btn_submitCreate(self):
        return self.btn_submitCreate.click()

    def wait_for_emailAddress_visibility(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.fld_emailAddress))

    def enterInfield_fld_emailAddress(self, email):
        return self.fld_emailAddress.send_keys(email)

    def wait_for_elementToBeClickable(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.btn_submitCreate))

