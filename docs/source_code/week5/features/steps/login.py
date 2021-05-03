from behave import *
from selenium import webdriver

@given(u'I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome("../chromedriver")


@when(u'I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter username "{user}" and password "{password}"')
def step_impl(context, user, password):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'User must successfully login to the Dashboard Page')
def step_impl(context):
    page_title = context.driver.find_element_by_css_selector("h1").text
    assert page_title == "Dashboard"
    context.driver.close()
