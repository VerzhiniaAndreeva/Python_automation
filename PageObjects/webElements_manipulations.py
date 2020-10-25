from PageObjects import element
from PageObjects import locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import action_builder

class Maniplations:

    def __init__(self, driver):
        self.driver = driver

    def click_button(self, element):
        element = self.driver.find_element(element.GO_BUTTON)
        element.click()