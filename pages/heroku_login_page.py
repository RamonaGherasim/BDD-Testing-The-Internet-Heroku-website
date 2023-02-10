from selenium.webdriver.common.by import By
from basepage import BasePage
from pages.heroku_homepage import HomePage


class LoginPage(BasePage):
    USER = (By.ID, 'username')
    PASS = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')

    def navigate_to_login_page(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")

    def enter_username(self, username):
        self.chrome.find_element(*self.USER).send_keys(username)

    def enter_pass(self, password):
        self.chrome.find_element(*self.PASS).send_keys(password)

    def click_login_btn(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()


