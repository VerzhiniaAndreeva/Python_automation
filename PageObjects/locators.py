from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    GO_LINK = (By.CSS_SELECTOR, 'click')
    GO_DDL = (By.CLASS_NAME, 'select')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass