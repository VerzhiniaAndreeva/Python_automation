from selenium.common.exceptions import NoSuchElementException

from Common.driver_initialize import DriverInitialize

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    @property
    def driver(self):
        return DriverInitialize().getDriver()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_go_button(self, element):
        """Triggers the search"""
        element.click()

    def click_button(self, element):
        element = self.driver.find_element(element.GO_BUTTON)
        element.click()

    def select_link(self, element):
        element = self.driver.find_element(element.GO_LINK)
        element.click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

    def findElement(self, selectorType, selector):
        return self.driver.find_element(selectorType, selector)

    def findElements(self, selectorType, selector):
        return self.driver.find_elements(selectorType, selector)