from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    # Navigation Bar

    def go(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def is_title_matches(self):
        return "OrangeHRM" in self.driver.title

    def set_username(self, username):
        self.driver.find_element_by_id("txtUsername").send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id("txtPassword").send_keys(password)

    def click_submit_button(self):
        self.driver.find_element_by_id("btnLogin").click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_submit_button()


class DashboardPage(BasePage):
    def is_title_matches(self):
        return self.get_title() == "Dashboard"

    def get_title(self):
        h1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return h1.text
        # return self.driver.find_element_by_css_selector("h1").text
