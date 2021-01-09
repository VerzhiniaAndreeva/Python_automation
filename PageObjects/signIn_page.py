from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.basePage import BasePage
from PageObjects.waits import Waits


class SignIn(BasePage):

    @property
    def lnk_signIn(self):
        return BasePage().findElement(By.CLASS_NAME, 'login')

    @property
    def fld_emailAddress(self):
        return BasePage().findElement(By.ID, 'email_create')

    @property
    def form_createAccount(self):
        return BasePage().findElement(By.ID, 'create-account_form')

    @property
    def btn_submitCreate(self):
         return BasePage().findElement(By.ID, 'SubmitCreate')

    @property
    def fld_customerFirstname(self):
        return BasePage().findElement(By.ID, 'customer_firstname')

    def select_lnk_signIn(self):
        return self.lnk_signIn.click()

    def loosFocus(self):
        element = BasePage().findElement(By.ID, 'email')
        return element.click()

    def use_btn_submitCreate(self):
        self.btn_submitCreate.click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((self.fld_customerFirstname)))

    def enterInfield_fld_emailAddress(self, email):
        return self.fld_emailAddress.send_keys(email)
