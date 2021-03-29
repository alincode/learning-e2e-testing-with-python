# 練習題：等待

```py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

## 顯式等待

- <https://demoqa.com/dynamic-properties>
- 會用到的語法
  - WebDriverWait
    - until
  - expected_conditions
    element_to_be_clickable

### 解答

```py
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
```

## 隱式等待

- <https://demoqa.com/dynamic-properties>
- 會用到的語法
  - implicitly_wait(time_to_wait)

### 解答

```py
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(5) # 單位是秒
driver.get("https://demoqa.com/dynamic-properties")
assert "ToolsQA" in driver.title
try:
    element = driver.find_element_by_id("visibleAfter")
    print(element.text)
finally:
    driver.quit()
```
