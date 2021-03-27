# 動作鏈 (action chains)

模擬滑鼠操作

```
class selenium.webdriver.common.action_chains.ActionChains(driver)
```

## 使用範例

```py
menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
```

## API

### click(on_element = None)

點擊一下滑鼠左鍵

> 解說 `on_element = None` 的意思

### click_and_hold(on_element = None)

單擊滑鼠左鍵，然後不鬆開。

### context_click(on_element = None)

點擊滑鼠右鍵

### double_click(on_element = None）

點擊滑鼠左鍵兩下

### drag_and_drop(source，target）

拖拽 A 元素到 B 個元素區域，然後鬆開。

### drag_and_drop_by_offset(source, xoffset, yoffset)

拖拽元素位移到某個坐標，然後鬆開。

### key_down(value, element = None)

點擊某個鍵盤上的鍵

### key_up(value, element = None)

鬆開某個鍵

### move_by_offset(xoffset, yoffset)

滑鼠從當前位置移動到某個坐標

### move_to_element(to_element)

滑鼠移動到某個元素

### move_to_element_with_offset（to_element, xoffset, yoffset）

移動到距離某個元素（左上角坐標）多少距離的位置

### pause(seconds)

暫停所有輸入至 n 秒

Pause all inputs for the specified duration in seconds

### perform()

執行鏈中的所有動作

### release(on_element = None)

在某個元素位置鬆開滑鼠左鍵

### reset_actions()

清除已經存儲的操作

### send_keys(keys_to_send)

發送某個鍵到當前焦點的元素

### send_keys_to_element(element, keys_to_send)

發送某個鍵到指定元素

## 練習題

### Range Sliders

- 這個練習題會用到 click_and_hold, move_by_offset, release, perform，這四個動作。

## 參考文獻

- [7.2. Action Chains](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains)
- [selenium.webdriver.common.action_chains](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html)
