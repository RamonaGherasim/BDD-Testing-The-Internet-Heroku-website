Feature: Test the login success and logout button on the Secure Page
  Background:
    Given Login page: I am on Login Page
    Given Login page: I have successfully logged in

  Scenario: Check that the success message is displayed
    Then Secure page: I can see the success message

  Scenario Outline: Check that I can click on the logout button
    When Secure page: I click on the "Logout" button
    Then Login page: I will be taken back on the Login Page (URI: "<uri>")

    Examples:
      | uri     |
      | /login |