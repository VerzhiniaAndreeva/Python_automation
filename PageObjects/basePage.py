from PageObjects.HomePage import HomePage

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

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

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine

        return "No results found." not in self.driver.page_source