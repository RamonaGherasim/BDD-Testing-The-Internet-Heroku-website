Feature: Test the page links of the Heroku Homepage

  Background:
    Given Home page: I am on Heroku Homepage

  Scenario Outline: Check that the user can navigate to different pages using the links on the Heroku Homepage
    When Home page: I click on "<link_name>" link
    Then "<page_name>" page: I will be taken to the "<page_name>" Page (URI: "<uri>")

    Examples:
      | link_name           | page_name    | uri           |
      | Form Authentication | Login        | /login        |
      | Inputs              | Inputs       | /inputs       |
      | Status Codes        | Status Codes | /status_codes |



