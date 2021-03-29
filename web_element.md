# 元素的狀態與屬性

## get_attribute("attr_name")

取得元素指定的屬性值

### 範例

```py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

# Get attribute of current active element
attr = driver.switch_to.active_element.get_attribute("title")
print(attr)
```

## isEnabled()

元素是否是 Enable 的狀態，回傳值為 Boolean。

### 範例

```py
  driver.get("https://www.google.com/");
  boolean value = driver.findElement(By.name("btnK")).isEnabled();
```

## is_selected()

元素是否被選取，回傳值為 Boolean。

### 範例

```py
driver.get("https://the-internet.herokuapp.com/checkboxes")
value = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type").is_selected()
```

## tag_name

元素的 tag 名稱

### 範例

```py
attr = driver.find_element(By.CSS_SELECTOR, "h1").tag_name
# 結果回傳：h1
```

## rect

取得元素的 height, width, x 和 y 值。

### 範例

```py
rest = driver.find_element(By.CSS_SELECTOR, "h1").rect
```

## value_of_css_property('css_attr_name')

取得元素的 CSS 的屬性值

### 範例

```py
cssValue = driver.findElement(By.LINK_TEXT, "More information...").value_of_css_property('color')
```

## text

取得元素的文字

### 範例

```py
text = driver.find_element(By.CSS_SELECTOR, "h1").text
```

## 補充：判斷元素是否存在

> 注意這裡是 `elements`，如果是呼叫 `element` 會丟出 error。

```py
elements = driver.find_elements_by_css_selector("h4")
elements_size = len(elements)

if(elements_size > 0):
  print("元素存在 " + elements.text)
else:
   print("元素不存在")
```

## 參考文獻

- <https://www.selenium.dev/documentation/en/webdriver/web_element/>
