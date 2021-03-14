# 準備開發環境

- Python
- PyCharm IDE
- 安裝瀏覽器驅動
- 安裝 Selenium Webdriver 模組

## 安裝

### 安裝 Python

- 下載安裝檔：<https://www.python.org/downloads/>
- 目前範例使用 Python 3.8

### PyCharm IDE

- 下載安裝檔：<https://www.jetbrains.com/pycharm/download/#section=mac>
- 安裝 Community 版本

### 安裝 Driver Binaries

- Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
- Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Internet Explorer: https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver
- Firefox: https://github.com/mozilla/geckodriver/releases
- Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/

或

從 <https://www.selenium.dev/downloads/> 找到 Platforms Supported by Selenium 的位址，並下載對應的驅動程式。

或

從 <https://github.com/christian-bromann/awesome-selenium#driver> 找到

### 測試環境準備完成

新增一個檔案叫 test.py

```python
# test.py
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.python.org")
```

在 Windows 上執行

```
C:\Python38\Scripts\pip.exe install selenium
C:\Python38\python.exe C:\test.py
```

在 Mac 上執行

```
python3 -m pip install --upgrade selenium
python test.py
```

## 練習題 😎

1. 試著將上面的步驟完成
1. 試著改用其他瀏覽器

## 補充

### 環境常見問題

- 瀏覽器版本跟驅動程式不一致

```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of MSEdgeDriver only supports MSEdge version 91
Current browser version is 89.0.774.50 with binary path C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
```

- 驅動程式的版本一直更新

可以使用 <https://www.npmjs.com/package/selenium-standalone> 來讓自己省點力

## 參考文獻

- <https://selenium-python.readthedocs.io/installation.html>
