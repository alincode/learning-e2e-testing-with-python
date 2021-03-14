# 選取元素 (Locating Elements)

有多種策略可以找到元素，你可以跟自己的情況選擇使用。

## 單一元素

即使有多個也只返回一個

```
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
```

## 多個元素

如果是要一次取多個元素，則要加 `s`。

```
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
```

### 另一種寫法

```
find_element
find_elements
```

### 使用範例

```python
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
```

```
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

## 透過 ID 來選取

常見於選取唯一的元素

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
<html/>
```

```python
login_form = driver.find_element_by_id('loginForm')
```

## 透過 Class Name 來選取

比較常見於一次選取多個元素

```html
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
<html>
```

```python
content = driver.find_element_by_class_name('content')
```

## 透過 Name 來選取

常見於選取表單元素

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
</html>
```

```python
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
```

## 透過 CSS_SELECTOR 來選取

```html
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
<html>
```

```python
content = driver.find_element_by_css_selector('p.content')
```

- [CSS Selectors Reference](https://www.w3schools.com/cssref/css_selectors.asp)
- [CSS Diner 小遊戲](https://flukeout.github.io/)

## 總結

- 有這麼多種，到底該用哪一種？
- 其他不常使用的，下週再說明。
