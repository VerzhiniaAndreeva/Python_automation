from selenium.webdriver.common.by import By

from Common.do import Do
from Common.driver_initialize import DriverInitialize
from Common.get import Get


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    @property
    def driver(self):
        return DriverInitialize().getDriver()

    @property
    def header(self):
        return By.CSS_SELECTOR, 'h1'

    def enter_in_field(self, elementLocator):
        Do().sendKeys(elementLocator)
        return self

    def getHeaderText(self):
        return Get().elementText(self.header)