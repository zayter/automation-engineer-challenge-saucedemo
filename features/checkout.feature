Feature: Checkout
  Scenario Outline: Checkout Multiple Products
    Given user is signed in
    When user adds the following products into the cart
        | product_name              | 
        | Sauce Labs Fleece Jacket  |
        | Sauce Labs Onesie         |        
        | Sauce Labs Bike Light     |
    And user clicks on cart button
    And user clicks on checkout button 
    And user fills out checkout step first name "<first_name>" last name "<last_name>" zip_code "<zip_code>"
    And user clicks on finish button
    Then user sees "Thank you for your order!" message  
    And user click on Back Home
    And cart number is "0"
    Examples: Users
        | first_name  | last_name | zip_code |
        | Zayter      | Munive    | 94102    |
        | Tenchi      | Gonzalez  | 777532   |

  Scenario Outline: Checkout Multiple Products - Overview
    Given user is signed in
    When user adds the following products into the cart
        | product_name              | 
        | Sauce Labs Fleece Jacket  |
        | Sauce Labs Bolt T-Shirt   |        
        | Sauce Labs Bike Light     |
    And user clicks on cart button
    And user clicks on checkout button 
    And user fills out checkout step first name "<first_name>" last name "<last_name>" zip_code "<zip_code>"
    Then order item total is "Item total: $75.97"
    And order line number is "3"  
    Examples: Users
        | first_name  | last_name | zip_code |
        | Zayter      | Munive    | 94102    |


  Scenario Outline: Checkout Single Product from Detail Page
    Given user is signed in
    When user visits "<product_name>" product details
    And user adds product "<product_name>" into the cart from detail page
    And user clicks on cart button
    And user clicks on checkout button 
    And user fills out checkout step first name "<first_name>" last name "<last_name>" zip_code "<zip_code>"
    And user clicks on finish button
    Then user sees "Thank you for your order!" message  
    And user click on Back Home
    And cart number is "0"
    Examples: Users
        | first_name  | last_name | zip_code | product_name      |  
        | Zayter      | Munive    | 94102    | Sauce Labs Onesie |
        | Tenchi      | Gonzalez  | 777532   | Sauce Labs Onesie |
