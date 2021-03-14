# 快速入門

## 第一個最簡單的範例

建立一個檔案，檔名叫 `python_org_search.py`。

```python
# python_org_search.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

執行測試程式

```bash
python3 -m pip install --upgrade selenium
python python_org_search.py
```

## 一步一步解說

### Step1: 匯入模組

- webdriver 可模擬操作瀏覽器，目前支援 Firefox, Chrome, IE 等等。
- 而 Keys 類別，提供了模擬鍵盤操作 (e.g. RETURN, F1, ALT)

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

### Step2: 建立 webdriver 的 instance

```python
driver = webdriver.Chrome("./chromedriver")
```

### Step3: 前往給定的 URL 網頁

driver.get 方法的用途是前往給定的 URL 網頁

```python
driver.get("http://www.python.org")
```

### Step4: 斷言 - 確認標題中包含 Python

```python
assert "Python" in driver.title
```

### Step5: 查找元素

```python
elem = driver.find_element_by_name("q")
```

### Step6: 執行模擬鍵盤的送出行為 + 提交頁面

```python
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
```

### Step7: 斷言

提交頁面後，如果有的話應該得到結果。為了確保找到一些結果，請聲明：

```python
assert "No results found." not in driver.page_source
```

### Step8: 關閉瀏覽器視窗

你也可以使用 quit() 替代 close()

```python
driver.close()
```
