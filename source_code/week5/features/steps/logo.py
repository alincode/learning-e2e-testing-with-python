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
    status = context.driver.find_element_by_css_selector(
        "#divLogo img").is_displayed()
    assert status is True


@then(u'close browser')
def step_impl(context):
    context.driver.close()
