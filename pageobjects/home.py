from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

class HomePageObject(PageObject):
    def init_page_elements(self):
        self.root = PageElement(By.ID, 'root')

    def wait_until_loaded(self):
        self.root.wait_until_visible()
        return self

    def open(self):
      self.driver.get('{}/'.format(self.config.get('Server', 'url')))
      return self
  
