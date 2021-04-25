from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://demoqa.com/alerts")
assert "ToolsQA" in driver.title

try:
    driver.find_element_by_id('confirmButton').click()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    # alert.dismiss()
finally:
    driver.quit()
