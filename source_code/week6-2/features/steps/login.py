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
