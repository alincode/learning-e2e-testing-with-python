# 等待 (Waits)

因為現在大多數網站都使用大量的 Ajax，當頁面載入時，透過非同步動態載入的元素，可能尚未存在而引發 `ElementNotDisableException`，可使用 Waits 語法來解決這個問題。

Selenium Webdriver 提供兩種類型的 Wait：

- 顯示等待
- 隱式等待

### 模擬情境說明

<https://demoqa.com/dynamic-properties>

因為第一個按鈕一開始是被 disable，需要等到五秒後，才會被 enable，所以如果我們要點擊第一個按鈕，必需要等到五秒之後。

### WebDriverWait 語法

```
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
```

- driver：WebDriver 的驅動程式(Ie, Firefox, Chrome 或遠端)
- timeout：最長超時時間，預設以秒為單位。
- poll_frequency：休眠時間的間隔（步長）時間，預設為 0.5 秒。
- ignored_exceptions：超時後的異常資訊，預設情況下拋 NoSuchElementException 異常。

## 顯式等待 (Explicit Waits)

顯示等待是指明確的等到某個元素的出現，或者是某個元素的可點選等條件符合，等不到就一直等，直到規定的時間之內都沒找到，則跳出 Exception。顯式等待需等特定條件發生時，在執行後面的程序，常與 `until()` 和 `until_not()` 搭配使用。

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

在上面的範例 Selenium 最多等待 10 秒，若元素則拋出 `TimeoutException`。在預設情況下，每 500 ms 會檢查一次條件，如果成功 `ExpectedCondition` 會返回 `true`，找不到元素，則返回 `null`。

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

- [官方 API 文件](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected_conditions)

### 自訂等待條件

```py
class element_has_css_class(object):
  """An expectation for checking that an element has a particular css class.

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)   # Finding the referenced element
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False

# Wait until an element with id='myNewInput' has class 'myCSSClass'
wait = WebDriverWait(driver, 10)
element = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))
```

## 隱式等待 (Implicit Waits)

- 隱式等待是代表建立一個最長等待時間，這個方法是得不到某個元素就等待，直到拿到元素位置(如果一直拿不到就等到時間截止)，再執行下一步。
- 隱式等待對整個 driver 週期都起作用，所以只要設定一次即可。

```python
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

## 補充：強制等待

```python
from time import sleep
sleep(3)
```

> 盡量不要使用，如果真的使用需小心謹慎。

## 練習題

<https://demoqa.com/dynamic-properties>

- 顯式等待
- 隱式等待

## 參考文獻

- [5. Waits](https://selenium-python.readthedocs.io/waits.html)
- [Python selenium — 一定要会用 selenium 的等待，三種等待方式解讀](https://huilansame.github.io/huilansame.github.io/archivers/sleep-implicitlywait-wait)
