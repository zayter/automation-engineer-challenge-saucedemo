from behave import given, when, then
from hamcrest import *
from pageobjects.login import LoginPageObject
from pageobjects.product import ProductListPageObject
from pageobjects.home import HomePageObject

@step('user logs out')
def step_impl(context):
  context.current_page.header.hambuger_menu.reset_and_log_out()

@then('the user is redirected to the login')
def step_impl(context):
  context.current_page = LoginPageObject()
  assert_that(context.current_page.form.username.is_present(), equal_to(True))

@then('I shouldn not be able to visit the products page')
def step_impl(context):
  context.driver.get('https://www.saucedemo.com/inventory.html')
  assert_that(context.current_page.error.text, contains_string("You can only access '/inventory.html' when you are logged in."))
