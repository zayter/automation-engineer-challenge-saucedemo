from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

class Form(Group):
  username = InputText(By.CSS_SELECTOR, '[data-test=username]')
  password = InputText(By.CSS_SELECTOR, '[data-test=password]')
  login_button = Button(By.CSS_SELECTOR, '[data-test=login-button]')

class LoginPageObject(PageObject):
    def init_page_elements(self):
      self.form  = Form(By.XPATH, '//form')
      self.error = Text(By.CSS_SELECTOR, '[data-test=error]')  
      return self

    def wait_until_loaded(self):
      self.form.wait_until_visible()
      return self

    def login(self, user):
      self.form.username.text = user['username']
      self.form.password.text = user['password'] 
      self.form.login_button.click()
      return self
