from behave import *


@given('Home page: I am on Heroku Homepage')
def step_impl(context):
    context.home_page_object.navigate_to_homepage()


@when('Home page: I click on "{link_name}" link')
def step_impl(context, link_name):
    context.home_page_object.click_page_link(link_name)


@then('"{page_name}" page: I will be taken to the "{page_name}" Page (URI: "{uri}")')
def step_impl(context, page_name, uri):
    base_url = "https://the-internet.herokuapp.com"
    expected_url = base_url + uri
    current_url = context.home_page_object.get_page_url()
    assert current_url == expected_url, f"Current url {current_url}, expected url {expected_url}"
