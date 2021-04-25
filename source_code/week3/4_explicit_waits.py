from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("./chromedriver")
driver.get("https://demoqa.com/dynamic-properties")
assert "ToolsQA" in driver.title

try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "enableAfter"))
    )

finally:
    driver.quit()
