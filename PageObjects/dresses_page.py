from PageObjects import webElements_manipulations

class Dresses:

    title = "Dresses"
    tabDress = "DRESSES"

def __init__(self, driver):
    self.driver = driver

def getElementTittle(self):
    element = self.driver.find_element_by_css_selector(self.title)
    return element.tittle

def selectDressTab(self, tabDresses):
    webElements_manipulations.Maniplations.click_button(tabDresses)
    return tabDresses
