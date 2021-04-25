from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://demoqa.com/alerts")
assert "ToolsQA" in driver.title

try:
    driver.find_element_by_id('promtButton').click()
    alert = driver.switch_to.alert
    alert.send_keys("AILIN LIOU")
    print(alert.text)
    alert.accept()
finally:
    driver.quit()
