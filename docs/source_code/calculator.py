from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.get("http://juliemr.github.io/protractor-demo/")
assert "Super Calculator" in driver.title
input1 = driver.find_element_by_css_selector("[ng-model='first']")
input2 = driver.find_element_by_css_selector("[ng-model='second']")
button = driver.find_element_by_id("gobutton")

input1.send_keys("1")
input2.send_keys("2")
button.send_keys(Keys.ENTER)
