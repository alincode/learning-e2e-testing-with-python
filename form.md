# 表單操作

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

## 練習題 - 登入頁

- <https://opensource-demo.orangehrmlive.com/>

### 測試登入失敗

我們會練習到 send_keys 和 submit 語法

### 測試登入成功

我們會練習到 clear 語法
