from browser import Browser
from pages.heroku_homepage import HomePage
from pages.heroku_secure_page import SecurePage
from pages.heroku_login_page import LoginPage


def before_all(context):
    context.browser = Browser()
    context.home_page_object = HomePage()
    context.secure_page_object = SecurePage()
    context.login_page_object = LoginPage()


def after_all(context):
    context.browser.close()