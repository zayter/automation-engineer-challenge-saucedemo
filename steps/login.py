from behave import given, when, then
from hamcrest import *
from pageobjects.login import LoginPageObject
from pageobjects.product import ProductListPageObject
from pageobjects.home import HomePageObject

@given('home page is open')
def step_impl(context):
  context.current_page = HomePageObject()
  context.current_page.open()

@when('page loads')
def step_impl(context):
  context.current_page.wait_until_loaded()

@given('login form is visible')
def step_impl(context):
  context.current_page = LoginPageObject()
  context.current_page.wait_until_loaded()
  assert_that(context.current_page.form.username.is_present(), equal_to(True))

@when('the user logs in with valid username "{username}" and password "{password}"')
def step_impl(context, username, password):
  user = {'username': username, 'password': password}
  context.current_page.login(user)
  
@step('the user is redirected to the products homepage')
def step_impl(context):
  context.current_page = ProductListPageObject()
  assert_that(context.current_page.header.title.web_element.text, equal_to("Products"))

@given('user is signed in')
def step_impl(context):
  context.execute_steps(u"""
  Given home page is open
  When page loads
  Given login form is visible
  When the user logs in with valid username "standard_user" and password "secret_sauce"
    """)
