from Common.driver_initialize import DriverInitialize


class Get:

    @property
    def driver(self):
        return DriverInitialize().getDriver()

    def elementDisplayed(self, elementLocator):
        element = self.driver.find_element(elementLocator[0], elementLocator[1])
        return element.is_displayed

    def elementText(self, elementLocator):
        element = self.driver.find_element(elementLocator[0], elementLocator[1])
        return element.text