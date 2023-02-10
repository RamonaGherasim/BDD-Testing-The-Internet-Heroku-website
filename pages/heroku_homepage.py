from selenium.webdriver.common.by import By
from basepage import BasePage


class HomePage(BasePage):
    # LOGIN_PAGE_LINK = (By.LINK_TEXT, link_name)
    # INPUTS_PAGE_LINK = (By.XPATH, '//*[@href="/inputs"]')
    # STATUS_CODES_PAGE_LINK = (By.XPATH, '//*[@href="/status_codes"]')

    def navigate_to_homepage(self):
        self.chrome.get('https://the-internet.herokuapp.com/')

    def click_page_link(self, link_name):
        self.chrome.find_element(By.LINK_TEXT, link_name).click()
        # self.wait_and_click_element((By.LINK_TEXT, link_name))

    # def click_inputs_page_link(self):
    #     self.chrome.find_element(*self.INPUTS_PAGE_LINK).click()
    #
    # def click_status_codes_page_link(self):
    #     self.chrome.find_element(*self.STATUS_CODES_PAGE_LINK).click()
