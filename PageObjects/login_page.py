class LoginPage:

    header = "h1"

    def __init__(self, driver):
        self.driver = driver

    def getHeaderText(self):
        element = self.driver.find_element_by_css_selector(self.header)
        return element.text
