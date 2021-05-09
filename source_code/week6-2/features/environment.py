from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome("../chromedriver")


def after_feature(context, feature):
    print("=== after_feature ===")
    context.driver.close()
