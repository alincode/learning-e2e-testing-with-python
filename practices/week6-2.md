# POM 練習題

```
.
└── features
    ├── environment.py
    ├── login.feature
    └── steps
        ├── login.py
        └── page.py
```

- 講 Login 的程式，改寫成 POM 的格式。
  - 建立 environment.py
  - 建立 BasePage class
  - 建立個別的 Page class

## 答案

features/login.feature

```
Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    When I open orange HRM Homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard Page
```

features/environment.py

```py
from selenium import webdriver

def before_feature(context, feature):
    context.driver = webdriver.Chrome("../chromedriver")


def after_feature(context, feature):
    print("=== after_feature ===")
    context.driver.close()

```

features/steps/login.py

```py
from behave import *
from page import *

@when(u'I open orange HRM Homepage')
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.go()
    context.main_page = main_page

@when(u'Enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.main_page.set_username(username)
    context.main_page.set_password(password)

@when(u'Click on login button')
def step_impl(context):
    context.main_page.click_submit_button()

@then(u'User must successfully login to the Dashboard Page')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    assert dashboard_page.is_title_matches() == True

```

features/steps/page.py

```py
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
```
