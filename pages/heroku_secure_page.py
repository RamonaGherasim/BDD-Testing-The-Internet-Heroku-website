from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basepage import BasePage


class SecurePage(BasePage):
    SUCCESS_MESSAGE = (By.ID, "flash")
    LOGOUT_BTN = (By.XPATH, '//a[@href="/logout"]')

    def check_success_message_display(self):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        return self.chrome.find_element(*self.SUCCESS_MESSAGE).is_displayed()

    def click_logout_button(self):
        self.chrome.find_element(*self.LOGOUT_BTN).click()
