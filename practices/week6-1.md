# 練習題：登入

## Step1

```
pip install behave
pip install selenium
```

## Step2

1. 建立 `features/` 和 `features/steps/` 資料夾
1. 建立 feature 檔案，例如 `login.feature`。
1. 執行 `behave`

![](assets/login_feature.png)

```
Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open orange HRM Homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard Page
```

## Step3

1. 建立 step 檔案，例如 `features/steps/login.py`。
1. 添加 `behave` 和 `selenium` 模組

## Step4

1. 實作 `login.py` 細節
1. 執行 `behave`

```py
# featurs/steps/login.py
from behave import *
from selenium import webdriver


@given(u'I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome("../chromedriver")


@when(u'I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element_by_id("txtUsername").send_keys(username)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'User must successfully login to the Dashboard Page')
def step_impl(context):
    page_title = context.driver.find_element_by_css_selector("h1").text
    assert page_title == "Dashboard"
    context.driver.close()

```
