from behave import given, when, then
from hamcrest import *
from pageobjects.product import (ProductListPageObject, ProductDetailPageObject)

@when('user adds product "{product_name}" into the cart')
def step_impl(context, product_name):
  context.current_page = ProductListPageObject()
  product = context.current_page.find_product(product_name)
  product.add_to_cart()

@when('user adds product "{product_name}" into the cart from detail page')
def step_impl(context, product_name):
  context.current_page = ProductDetailPageObject()
  context.current_page.add_to_cart.click()

@when('user visits "{product_name}" product details')
def step_impl(context, product_name):
   context.current_page = ProductListPageObject()
   product = context.current_page.find_product(product_name)
   product.title.click()

@then('cart number is "{counter}"')
def step_impl(context, counter):
  if int(counter) > 0:
    assert_that(context.current_page.header.cart.badge.text, equal_to(counter))
  else:
    assert_that(context.current_page.header.cart.badge.is_present(), equal_to(False))      

@when('user adds the following products into the cart')
def step_impl(context):
  context.current_page = ProductListPageObject()
  products_to_be_added = context.table
  for product_name in products_to_be_added:
    product = context.current_page.find_product(product_name[0])
    product.add_to_cart()

@step('user clicks on cart button')
def step_impl(context):
  context.current_page = ProductListPageObject()
  context.current_page.header.cart.link.click()
