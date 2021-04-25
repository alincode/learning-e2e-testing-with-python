from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome("./chromedriver")
driver.get("https://demoqa.com/alerts")
assert "ToolsQA" in driver.title

driver.maximize_window()

try:
    driver.find_element_by_id("alertButton").click()
    alert = driver.switch_to.alert
    text = alert.text
    print(text)
    alert.accept()

    driver.find_element_by_id("timerAlertButton").click()
    alert2 = WebDriverWait(driver, 6).until(expected_conditions.alert_is_present())
    text2 = alert.text
    print(text2)
    alert2.accept()

finally:
    driver.quit()
