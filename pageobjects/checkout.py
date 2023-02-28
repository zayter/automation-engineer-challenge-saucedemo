from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.header import HeaderPageObject

class LineItem(Group):
  def init_page_elements(self):
    self.title = Text(By.CLASS_NAME, 'inventory_item_name')

class YourInformationForm(Group):
  first_name = InputText(By.CSS_SELECTOR, '[data-test=firstName]')
  last_name = InputText(By.CSS_SELECTOR, '[data-test=lastName]')
  zip_code = InputText(By.CSS_SELECTOR, '[data-test=postalCode]')
  continue_button = Button(By.CSS_SELECTOR, '[data-test=continue]')

class CheckoutYourInformationPageObject(PageObject):
    def init_page_elements(self):
      self.form  = YourInformationForm(By.XPATH, '//form')
      return self
      self.header = HeaderPageObject()

    def wait_until_loaded(self):
      self.form.wait_until_visible()
      return self

    def complete_checkout(self, user_info):
      self.form.first_name.text = user_info['first_name']
      self.form.last_name.text = user_info['last_name'] 
      self.form.zip_code.text = user_info['zip_code'] 
      self.form.continue_button.click()
      return CheckoutOverviewPageObject()

class CheckoutOverviewPageObject(PageObject):
    def init_page_elements(self):
      self.header = HeaderPageObject()
      self.item_total = Text(By.CLASS_NAME, 'summary_subtotal_label')
      self.finish_button = Button(By.CSS_SELECTOR, '[data-test=finish]')
      self.line_items = PageElements(By.CLASS_NAME, 'cart_item', page_element_class=LineItem)
      return self

class CheckoutCompletePageObject(PageObject):
    def init_page_elements(self):
      self.header = HeaderPageObject()
      self.title = Text(By.CLASS_NAME, 'complete-header')
      self.back_home_button = Button(By.CSS_SELECTOR, '[data-test=back-to-products]')      
      return self
