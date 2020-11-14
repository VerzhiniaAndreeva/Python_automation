from selenium.webdriver.common.by import By

from PageObjects.basePage import BasePage


class LoginPage(BasePage):

    @property
    def header(self):
        return BasePage().findElement(By.CSS_SELECTOR, 'h1')

    def getHeaderText(self):
        return self.header.text
