# 訊息框

<https://www.selenium.dev/documentation/en/webdriver/js_alerts_prompts_and_confirmations/>

### 使用情境

- 跳離本站警告
- 動作前警告提示

## 警告訊息框 (Alert)

```py
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

```

## 確認訊息框 (Confirm)

```py
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
```

## 提示訊息對話 (Prompts)

```py
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
```
