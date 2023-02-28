Feature: Cart
  Scenario Outline: Add Single Product from ProductList  
    Given user is signed in
    When user adds product "<product_name>" into the cart
    Then cart number is "1" 
  Examples: Products
      | product_name             |
      | Sauce Labs Bike Light    |
      | Sauce Labs Fleece Jacket |      

  Scenario: Add Multiple Products from ProductList  
    Given user is signed in
    When user adds the following products into the cart
        | product_name              | 
        | Sauce Labs Onesie         | 
        | Sauce Labs Fleece Jacket  |
        | Sauce Labs Bike Light     |
    Then cart number is "3"

  Scenario Outline: Add Single Product from ProductDetail  
    Given user is signed in
    When user visits "<product_name>" product details
    And user adds product "<product_name>" into the cart from detail page
    Then cart number is "1" 
  Examples: Products
      | product_name             |
      | Sauce Labs Onesie        |
