# 導航 (Navigating)

## get

在瀏覽器載入指定網頁

```py
driver.get("http://www.google.com")
```

![](assets/get.png)

<!-- 說明怎麼看 API 文件和 source code -->

## 與表單互動

### send_keys

模擬輸入值到元素中

![](assets/input_text.png)

```html
<form action="/action_page.php">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" /><br />
  <label for="pwd">Password:</label>
  <input type="password" id="pwd" name="pwd" /><br /><br />
  <input type="submit" value="Submit" />
</form>
```

```py
form_textfield = driver.find_element_by_name('username')
form_textfield.send_keys("admin")
```

### select

```py
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
```

```
options = select.options
```

```py
select = Select(driver.find_element_by_id('id'))
select.deselect_all()
```

### submit

```py
driver.find_element_by_id("submit").click()
element.submit()
```

### 拖放 (Drag And Drop)

```py
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
```

### 在 window 和 frame 之間切換

```html
<a href="somewhere.html" target="windowName">Click here to open a new window</a>
```

```py
driver.switch_to_window("windowName")
driver.switch_to_frame("frameName")
driver.switch_to_default_content()
```

### 與彈跳視窗互動 (Popup dialogs)

```
alert = driver.switch_to.alert
```

### Navigation: history and location

```py
driver.forward()
driver.back()
```

### Cookies

```py
# Go to the correct domain
driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain
cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
driver.get_cookies()
```

## 參考文獻

- [3.1. Interacting with the page](https://selenium-python.readthedocs.io/navigating.html#interacting-with-the-page)
- [3.2. Filling in forms](https://selenium-python.readthedocs.io/navigating.html#filling-in-forms)
- [3.3. Drag and drop](https://selenium-python.readthedocs.io/navigating.html#drag-and-drop)
- [3.4. Moving between windows and frames](https://selenium-python.readthedocs.io/navigating.html#moving-between-windows-and-frames)
- [3.5. Popup dialogs](https://selenium-python.readthedocs.io/navigating.html#popup-dialogs)
- [3.6. Navigation: history and location](https://selenium-python.readthedocs.io/navigating.html#navigation-history-and-location)
- [3.7. Cookies](https://selenium-python.readthedocs.io/navigating.html#cookies)
