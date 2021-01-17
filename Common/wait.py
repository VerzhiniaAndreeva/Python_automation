from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Common.driver_initialize import DriverInitialize


class Wait:

    @property
    def driver(self):
        return DriverInitialize().getDriver()

    def ForElementDisplayed(self, elementLocator):
        wait = WebDriverWait(self.driver, 20, 0.1)
        wait.until(expected_conditions.visibility_of_element_located((elementLocator)), "Timeout reached! Element was not displayed")

    def ForElementNotDisplayed(self, elementLocator):
        wait = WebDriverWait(self.driver, 20, 0.1)
        wait.until_not(expected_conditions.presence_of_element_located((elementLocator)), "Timeout reached! Element was still displayed")

    def ForElementPresent(self,elementLocator):
        wait = WebDriverWait(self.driver, 20, 0.1)
        wait.until(expected_conditions.presence_of_element_located((elementLocator)), "Timeout reached! Element was not present")