from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")
driver.get("https://demoqa.com/slider")
assert "ToolsQA" in driver.title

try:
    input_range = driver.find_element_by_css_selector("[type='range']")
    move = ActionChains(driver)
    move.click_and_hold(input_range).move_by_offset(10, 0).release().perform()
finally:
    driver.quit()