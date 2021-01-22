from selenium.webdriver.common.by import By
from Common.do import Do
from Common.get import Get
from Common.wait import Wait
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

    @property
    def icon_twitter(self):
        return By.CLASS_NAME, 'icon-twitter'

    @property
    def product_img_link(self):
        return By.CLASS_NAME, 'product-container'
    
    @property
    def icon_large(self):
        return By.CLASS_NAME, 'icon-th-large'

    def select_tab_dressesTab(self):
        Do().click(self.tab_dressesTab)
        return self

    def categoriesBlock_is_displayed(self):
        Get().elementDisplayed(self.categoriesBlock)
        return self

    def select_lnk_casualDresses(self):
        Do().click(self.lnk_casualDresses)
        return self

    def select_product(self):
        Wait().ForElementDisplayed(self.icon_large)
        Do().scrollToElement(self.product_img_link)
        Do().click(self.product_img_link)
        Wait().ForElementPresent(self.icon_twitter)
        return self
