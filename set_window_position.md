# 設定視窗位置

我們只能測試我們看得到的區域，所以最後在一開始測試時，把視窗展開到最大。

### Maximize window

最大化視窗 (工具列還會存在)

```py
driver.maximize_window()
```

### Minimize window

最小化視窗

```
driver.minimize_window()
```

> Note: This feature works with Selenium 4 and later versions.

### Fullscreen window

全螢幕

```
driver.fullscreen_window()
```

### TakeScreenshot

擷取螢幕畫面

```py
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.example.com")

# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')
driver.quit()
```

<!--
### TakeElementScreenshot

### Execute Script

### Print Page
-->
