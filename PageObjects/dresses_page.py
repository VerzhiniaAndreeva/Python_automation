from selenium.webdriver.support.ui import WebDriverWait
from PageObjects import page

class Dresses:
    tittle = "Dresses"
    tabDress = "DRESSES"

    def __init__(self, driver):
        self.driver = driver
        tabDresses = self.driver.find_element_by_css_selector("[title='Dresses']")

  #  def getElementTittleDisplay(self, tabDresses):
   #     return

    def selectDressTab(self, tabDresses):
        self.tabDresses = tabDresses
        page.MainPage.click_button(tabDresses)
##        WebDriverWait.until(self.getElementTittleDisplay())
        return tabDresses
