# 練習題： behave

## Step1

1. 建立 `features/` 和 `features/steps/` 資料夾
1. 建立 feature 檔案，例如 `logo.feature`。
1. 執行 `behave`

<!--
````
Feature: OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM home page
     Given launch chrome browser
      When open orange hrm homepage
      Then verify that the logo present on page
      And close browser
``` -->

## Step2

1. 建立 step 檔案，例如 `features/steps/logo.py`。
1. 添加 `behave` 和 `selenium` 模組

## Step3

1. 實作 `logo.py` 細節

<!--
```py
from behave import *
from selenium import webdriver

@given(u'launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome("../chromedriver")


@when(u'open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'verify that the logo present on page')
def step_impl(context):
    status = context.driver.find_element_by_css_selector("#divLogo img").is_displayed()
    assert status is True


@then(u'close browser')
def step_impl(context):
    context.driver.close()

``` -->
