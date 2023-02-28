Feature: Logout
  Background:
    Given home page is open
    When page loads
  Scenario Outline: Logut  
    Given login form is visible
    When the user logs in with valid username "<username>" and password "<password>"
    And the user is redirected to the products homepage
    And user logs out
    Then the user is redirected to the login
    But I shouldn not be able to visit the products page
  Examples: Credentials
      | username      | password    |
      | standard_user | secret_sauce|
