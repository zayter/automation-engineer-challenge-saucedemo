from behave import given, when, then
from hamcrest import *
from pageobjects.checkout import (CheckoutYourInformationPageObject, CheckoutOverviewPageObject, CheckoutCompletePageObject)
from pageobjects.cart import CartPageObject
from pageobjects.product import ProductListPageObject

@step('user clicks on checkout button')
def step_impl(context):
  context.current_page = CartPageObject()
  context.current_page.checkout_button.click()

@step('user clicks on finish button')
def step_impl(context):
  context.current_page = CheckoutOverviewPageObject()
  context.current_page.finish_button.click()

@step('user fills out checkout step first name "{first_name}" last name "{last_name}" zip_code "{zip_code}"')
def step_impl(context, first_name, last_name, zip_code):
  user_info = {'first_name': first_name, 'last_name': last_name,'zip_code': zip_code}
  context.current_page = CheckoutYourInformationPageObject()
  context.current_page = context.current_page.complete_checkout(user_info)

@step('user sees "{message}" message')
def step_impl(context, message):
  context.current_page = CheckoutCompletePageObject()
  assert_that(context.current_page.title.text, equal_to(message))

@step('user click on Back Home')
def step_impl(context):
  context.current_page = CheckoutCompletePageObject()
  context.current_page.back_home_button.click()
  context.current_page = ProductListPageObject()

@then('order item total is "{total}"')
def step_impl(context, total):
  assert_that(context.current_page.item_total.text, equal_to(total))

@then('order line number is "{counter}"')
def step_impl(context, counter):
  assert_that(len(context.current_page.line_items), equal_to(int(counter)))
   
