from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
assert "The Internet" in driver.title

try:
    result = driver.find_element_by_css_selector('h3')
    assert "Basic Auth" in result.text
finally:
    driver.quit()
