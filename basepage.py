from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Browser):
    def wait_and_click_element(self, selector):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(selector))
        self.chrome.find_element(*selector).click()

    def get_page_url(self):
        url = self.chrome.current_url
        return url

    def get_page_header(self):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//h3')))
        header = self.chrome.find_element(By.XPATH, '//h3').text
        return header
