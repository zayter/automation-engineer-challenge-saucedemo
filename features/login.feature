Feature: Login
  Background:
    Given home page is open
    When page loads
  Scenario Outline: Valid Login  
    Given login form is visible
    When the user logs in with valid username "<username>" and password "<password>"
    Then the user is redirected to the products homepage
  Examples: Credentials
      | username      | password    |
      | standard_user | secret_sauce|
