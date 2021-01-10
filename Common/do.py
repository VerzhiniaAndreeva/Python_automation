from Common.driver_initialize import DriverInitialize


class Do:

    @property
    def driver(self):
        return DriverInitialize().getDriver()

    def click(self, elementLocator):
        self.driver.find_element(elementLocator[0], elementLocator[1]).click()

    def sendKeys(self, elementLocator, text):
        self.driver.find_element(elementLocator[0], elementLocator[1]).send_keys(text)