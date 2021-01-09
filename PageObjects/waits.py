# from selenium import webdriver
# from selenium.common.exceptions import WebDriverException, TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#from selenium.webdriver.support.wait import WebDriverWait


class Waits:
    def __init__(self, locator, attr, value):
        self._locator = locator
        self._attribute = attr
        self._attribute_value = value

    def __call__(self, driver):
        element = driver.find_element_by(self._locator)
        if element.get_attribute(self._attribute) == self._attribute_value:
            return element
        else:
            return False
