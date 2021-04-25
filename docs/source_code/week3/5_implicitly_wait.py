from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(5)
driver.get("https://demoqa.com/dynamic-properties")
assert "ToolsQA" in driver.title
try:
    element = driver.find_element_by_id("visibleAfter")
    print(element.text)
finally:
    driver.quit()
