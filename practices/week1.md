# 練習題：測試計算機

![](week1.png)

### 構思程式碼的行為

1. import 要使用的類別
1. 建立模擬人的行為的瀏覽器的物件
1. 前往特定的網址 <http://juliemr.github.io/protractor-demo/>
1. 驗證是不是在對的頁面
1. 選取元素
  - 選取第一個 input 欄位元素
  - 選取第二個 input 欄位元素
  - 選取按鈕元素
1. 操縱元素
  - 第一個欄位給值為 1
  - 第二個欄位給值為 2
  - 觸發按鈕

### 解答

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("http://juliemr.github.io/protractor-demo/")
assert "Super Calculator" in driver.title
input1 = driver.find_element_by_css_selector("[ng-model='first']")
input2 = driver.find_element_by_css_selector("[ng-model='second']")
button = driver.find_element_by_id("gobutton")

input1.send_keys("1")
input2.send_keys("2")
button.send_keys(Keys.ENTER)
```