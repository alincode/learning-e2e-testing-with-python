# 導航 (Navigating)

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
