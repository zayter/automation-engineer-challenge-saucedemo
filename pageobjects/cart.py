from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.header import HeaderPageObject

class LineItem(Group):
  def init_page_elements(self):
    self.title = Text(By.CLASS_NAME, 'inventory_item_name')
    self.remove_button = Button(By.CSS_SELECTOR, "[data-test=remove-{}]".format(self.title.text.replace(' ','-').lower()))

class CartPageObject(PageObject):
  def init_page_elements(self):
    self.header = HeaderPageObject()
    self.line_items = PageElements(By.CLASS_NAME, 'cart_item', page_element_class=LineItem)
    self.checkout_button = Button(By.CSS_SELECTOR, '[data-test=checkout]')
