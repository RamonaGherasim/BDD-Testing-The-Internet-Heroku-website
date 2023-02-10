Feature: Test the form functionality of the Login Page

  Scenario Outline: Check that the user can login using correct credentials
    Given Login page: I am on Login Page
    When Login page: I type "<username>" in the Username form field
    When Login page: I type "<password>" in the Password form field
    When Login page: I click on the Login button
    Then Secure page: I will be taken to the Secure Area page (URI: "<uri>")

    Examples:
      | username | password             | uri     |
      | tomsmith | SuperSecretPassword! | /secure |
