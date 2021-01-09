from selenium.webdriver.common.by import By

from Common.do import Do
from Common.get import Get
from PageObjects.basePage import BasePage

class Dresses(BasePage):

    @property
    def tab_dressesTab(self):
        return By.CSS_SELECTOR, '#block_top_menu>ul>li:nth-of-type(2)'

    @property
    def categoriesBlock(self):
        return By.CSS_SELECTOR, 'h2.title_block'

    @property
    def lnk_casualDresses(self):
        return By.CSS_SELECTOR, '#categories_block_left div>ul>li:nth-of-type(1) a'

    def select_tab_dressesTab(self):
        Do().click(self.tab_dressesTab)
        return self

    def categoriesBlock_is_displayed(self):
        Get().elementDisplayed(self.categoriesBlock)
        return self

    def select_lnk_casualDresses(self):
        Do().click(self.lnk_casualDresses)
        return self
