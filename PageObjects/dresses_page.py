from selenium.webdriver.support.wait import WebDriverWait


class Dresses:

    def __init__(self, driver):
        self.driver = driver

        # self._dressesTab = driver.find_element_by_css_selector("#block_top_menu > ul > li:nth-of-type(2)"),
        # self._cotegoriesBlock = driver.find_element_by_css_selector("h2.title_block"),
        # self._casualDressesCategory = driver.find_element_by_css_selector("#categories_block_left div > ul> li:nth-of-type(1) a"),


    # def selectDressTab(self):
    #     self._dressesTab.click()
    #
    # def categoriesBlockIsPresent(self):
    #     self._cotegoriesBlock.is_displayed()
    #     return True
    #
    # def selectCasualDressesCategory(self):
    #     WebDriverWait().until(self.categoriesBlockIsPresent())
    #     self._casualDressesCategory.click()

    def selectDressTab(self):
        dressesTab = self.driver.find_element_by_css_selector("#block_top_menu > ul > li:nth-of-type(2)")
        dressesTab.click()

    def categoriesBlockIsPresent(self):
        cotegoriesBlock = self.driver.find_element_by_css_selector("h2.title_block")
        cotegoriesBlock.is_displayed()
        return True

    def selectCasualDressesCategory(self):
        #WebDriverWait().until(self.categoriesBlockIsPresent())
        casualDressesCategory = self.driver.find_element_by_css_selector("#categories_block_left div > ul> li:nth-of-type(1) a")
        casualDressesCategory.click()
