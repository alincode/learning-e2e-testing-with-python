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

### until / until_not

直到調用的方法返回值為 True

until(method, message='')

method：expected_conditions 庫中定義的方法

### 預期條件 (Expected Conditions)

內建的檢查條件有以下幾個內建的判斷

#### title_is

判斷當前頁面標題是否為 title

```py
EC.title_is("Google")
```

#### title_contains

判斷當前頁面標題是否包含 title

```py
EC.title_contains("Google")
```

#### presence_of_element_located

判斷此定位的元素是否存在

presence_of_all_elements_located(locator)

```py
EC.presence_of_element_located((By.ID, "enableAfter"))
```

#### url_contains

判斷頁面網址中是否包含 url

```py
EC.url_contains(url)
```

#### url_to_be

判斷頁面網址是否為 url

```py
EC.url_to_be(url)
```

#### url_changes(url)

判斷頁面網址不是 url

```py
EC.url_changes(url)
```

#### visibility_of_element_located(locator)

判斷此定位的元素是否可見

#### visibility_of

判斷此元素是否可見

#### presence_of_all_elements_located(locator)

判斷此定位的一組元素至少有一個可見

#### visibility_of_all_elements_located(locator)

判斷此定位的一組元素全部可見

#### text_to_be_present_in_element(locator, text)

判斷此定位中是否包含 text 的內容

#### text_to_be_present_in_element_value(locator, text)

判斷此定位中的 value 屬性中是否包含 text 的內容

#### frame_to_be_available_and_switch_to_it(locator)

判斷定位的元素是否為 frame，並直接切換到這個 frame 中

#### invisibility_of_element_located(locator)

判斷定位的元素是否不可見

#### invisibility_of_element(element)

判斷此元素是否不可見

#### element_to_be_clickable(locator)

判斷所定位的元素是否可見且可點擊

#### element_to_be_selected(element)

判斷該元素是否被選中

#### element_located_to_be_selected(locator)

判斷該元素被選中狀態是否和期望狀態相同

#### element_located_selection_state_to_be(locator,Boolean)

判斷定位的元素被選中狀態是否和期望狀態相同

#### number_of_windows_to_be(num)

判斷當前瀏覽器頁簽數量是否為 num

#### new_window_is_opened(handles)

判斷此 handles 頁簽不是唯一打開的頁簽

#### alert_is_present()

判斷是否會出現 alert 窗口警報

- [官方 API 文件](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected_conditions)

### 完整範例

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

- 設置全局元素查找的超時時間
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
- [Web 自动化测试：WebDriverWait 元素等待和全局设置](https://zhuanlan.zhihu.com/p/143357537)
