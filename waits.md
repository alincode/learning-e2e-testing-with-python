# 等待 (Waits)

因為現在大多數網站都使用大量的 Ajax，當頁面載入時，透過非同步動態載入的元素，可能尚未存在而引發 `ElementNotDisableException`，可使用 Waits 語法來解決這個問題。

Selenium Webdriver 提供兩種類型的 Wait：

- 顯示等待
- 隱式等待

### 模擬情境說明

<https://demoqa.com/dynamic-properties">

因為第一個按鈕一開始是被 disable，需要等到五秒後，才會被 enable，所以如果我們要點擊第一個按鈕，必需要等到五秒之後。

### 語法

```
WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
```

> 這裡需要特別注意的是 until 或 until_not 中的可執行方法 method

## 顯式等待 (Explicit Waits)

顯式等待需等特定條件發生時，在執行後面的程序，常與 until() 和 until_not() 搭配使用。

```python
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

在上面的範例 Selenium 最多等待 10 秒，若元素則拋出 `TimeoutException`。在預設情況下，每 500 ms 會檢查一次條件，如果成功 `ExpectedCondition` 會返回 true，找不到元素，則返回 null。

### 預期條件 (Expected Conditions)

內建的檢查條件有：

```
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
```

## 隱式等待 (Implicit Waits)

- 隱式等待不用設定任何符合條件，會強制等待到指定的秒數才執行後面的指令。
- 隱式等待對整個 driver 週期都起作用，所以只要設定一次即可

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10) # 單位是秒
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
```

## 補充：強制等待

```python
from time import sleep
sleep(3)
```

## 參考文獻

[5. Waits](https://selenium-python.readthedocs.io/waits.html)
