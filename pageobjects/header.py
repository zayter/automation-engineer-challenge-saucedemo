from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

class Cart(Group):
  badge = Text(By.CLASS_NAME, 'shopping_cart_badge')
  link = Link(By.CLASS_NAME, 'shopping_cart_link')

class HamburgerMenu(Group):
  burger_button = Button(By.ID, 'react-burger-menu-btn')
  log_out_link = Link(By.ID, 'logout_sidebar_link')
  reset_link = Link(By.ID, 'reset_sidebar_link')
  
  def reset_and_log_out(self):
    self.burger_button.click()
    self.reset_link.click()
    self.log_out_link.click()

class HeaderPageObject(PageObject):
    def init_page_elements(self):
        self.root = PageElement(By.ID, 'header_container')
        self.title = PageElement(By.CLASS_NAME, 'title', parent=self.root)
        self.cart  = Cart(By.ID, 'shopping_cart_container', parent=self.root)
        self.hambuger_menu = HamburgerMenu(By.ID, 'menu_button_container', parent=self.root)
  
