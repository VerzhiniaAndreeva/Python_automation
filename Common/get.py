from Common.driver_initialize import DriverInitialize


class Get:

    @property
    def driver(self):
        return DriverInitialize().getDriver()

    def elementDisplayed(self, elementLocator):
        element = self.driver.find_element(*elementLocator)
        return element.is_displayed

    def elementText(self, elementLocator):
        element = self.driver.find_element(*elementLocator)
        return element.text