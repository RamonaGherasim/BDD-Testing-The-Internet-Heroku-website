from behave import *


@when('Secure page: I click on the "Logout" button')
def step_impl(context):
    context.secure_page_object.click_logout_button()


@then('Secure page: I will be taken to the Secure Area page (URI: "{uri}")')
def step_impl(context, uri):
    base_url = "https://the-internet.herokuapp.com"
    expected_url = base_url + uri
    current_url = context.home_page_object.get_page_url()
    assert current_url == expected_url, f"Current url {current_url}, expected url {expected_url}"


@then('Secure page: I can see the success message')
def step_impl(context):
    is_displayed = context.secure_page_object.check_success_message_display()
    assert is_displayed, f"Is displayed {is_displayed}, expected True"
