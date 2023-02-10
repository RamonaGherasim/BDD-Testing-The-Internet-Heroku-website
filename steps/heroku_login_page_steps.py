from behave import *


@given('Login page: I have successfully logged in')
def step_impl(context):
    context.login_page_object.enter_username("tomsmith")
    context.login_page_object.enter_pass("SuperSecretPassword!")
    context.login_page_object.click_login_btn()


@given('Login page: I am on Login Page')
def step_impl(context):
    context.login_page_object.navigate_to_login_page()


@when('Login page: I type "{username}" in the Username form field')
def step_impl(context, username):
    context.login_page_object.enter_username(username)


@when('Login page: I type "{password}" in the Password form field')
def step_impl(context, password):
    context.login_page_object.enter_pass(password)


@when('Login page: I click on the Login button')
def step_impl(context):
    context.login_page_object.click_login_btn()


@then('Login page: I will be taken back on the Login Page (URI: "{uri}")')
def step_impl(context, uri):
    base_url = "https://the-internet.herokuapp.com"
    expected_url = base_url + uri
    current_url = context.home_page_object.get_page_url()
    assert current_url == expected_url, f"Current url {current_url}, expected url {expected_url}"
