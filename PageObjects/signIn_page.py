from selenium.webdriver.common.by import By
from PageObjects.basePage import BasePage


class SignIn(BasePage):

    @property
    def lnk_signIn(self):
        return BasePage().findElement(By.CLASS_NAME, '.login')

    def select_lnk_signIn(self):
        return self.lnk_signIn.click()