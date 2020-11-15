from selenium.webdriver.common.by import By
from PageObjects.basePage import BasePage

class Dresses(BasePage):

    @property
    def tab_dressesTab(self):
        return BasePage().findElement(By.CSS_SELECTOR, '#block_top_menu > ul > li:nth-of-type(2)')

    @property
    def categoriesBlock(self):
        return BasePage().findElement(By.CSS_SELECTOR, 'h2.title_block')

    @property
    def lnk_casualDresses(self):
        return BasePage().findElement(By.CSS_SELECTOR, '#categories_block_left div > ul> li:nth-of-type(1) a')

    def select_tab_dressesTab(self):
        return self.tab_dressesTab.click()

    def categoriesBlock_is_displayed(self):
        return self.categoriesBlock.is_displayed()

    def select_lnk_casualDresses(self):
        return self.lnk_casualDresses.click()
