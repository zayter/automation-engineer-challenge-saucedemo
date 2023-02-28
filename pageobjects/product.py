from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.header import HeaderPageObject

class ProductItem(Group):
  def init_page_elements(self):
    self.title = Link(By.CLASS_NAME, 'inventory_item_name')
  
  def add_to_cart(self): 
     button = Button(By.CSS_SELECTOR, "[data-test=add-to-cart-{}]".format(self.title.text.replace(' ','-').lower()))
     button.click()

class ProductItems(PageElements):
    page_element_class = ProductItem

class ProductListPageObject(PageObject):
  def init_page_elements(self):
    self.header = HeaderPageObject()
    self.products = ProductItems(By.CLASS_NAME, 'inventory_item')

  def find_product(self, product_name):
    filtered_product = filter(lambda product: product.title.text == product_name, self.products)
    product = list(filtered_product)[0]
    return product

class ProductDetailPageObject(PageObject):
  def init_page_elements(self):
    self.header = HeaderPageObject()
    self.title = Text(By.CLASS_NAME, 'inventory_details_name')
    self.add_to_cart = Button(By.CSS_SELECTOR, "[data-test=add-to-cart-{}]".format(self.title.text.replace(' ','-').lower()))
