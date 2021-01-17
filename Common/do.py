from Common.driver_initialize import DriverInitialize
from selenium.webdriver.support.ui import Select


class Do:

    @property
    def driver(self):
        return DriverInitialize().getDriver()

    def click(self, elementLocator):
        self.driver.find_element(*elementLocator).click()

    def sendKeys(self, elementLocator, text):
        self.driver.find_element(*elementLocator).send_keys(text)

    def selectDropDownOptoin(self, elementLocator, ddl_value):
        selectOption =  Select(self.driver.find_element(*elementLocator))
        selectOption.select_by_value(ddl_value)


