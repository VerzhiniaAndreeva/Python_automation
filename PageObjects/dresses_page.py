class Dresses:

    def __init__(self, driver):
        self.driver = driver

        self._dressesTab = driver.find_element_by_css_selector("#block_top_menu > ul > li:nth-of-type(2)")

    # def getElementTittleDisplay(self, tabDresses):
    #     pass

    def selectDressTab(self):
        self._dressesTab.click()
