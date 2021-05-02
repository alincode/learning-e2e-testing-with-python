# HTTP 基本認證 (Basic Http Authentication)

- 你可以透過將帳號密碼透過 URL 傳遞來完成認證程序

```py
driver.get("https://<username>:<password>@www.example.com/index.html")
```

## 練習題

![](assets/basic_auth.png)

- <http://the-internet.herokuapp.com/basic_auth>
  - 帳號 admin
  - 密碼 admin

### 答案

```py
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
assert "The Internet" in driver.title

try:
    result = driver.find_element_by_css_selector('h3')
    assert "Basic Auth" in result.text
finally:
    driver.quit()
```

### 參考文獻

- Basic HTTP Authentication for Selenium tests - BrowserStack: <https://www.browserstack.com/docs/automate/selenium/basic-http-authentication>
