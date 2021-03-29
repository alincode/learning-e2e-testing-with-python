# 練習題：檢查欄位是否能被輸入

- <https://the-internet.herokuapp.com/dynamic_controls>
- 會用到的語法
  - is_enabled()

## 解答

```py
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
assert "The Internet" in driver.title

try:
    is_enable = driver.find_element_by_css_selector("[type='text']").is_enabled()
    print(is_enable)
    assert False == is_enable
finally:
    driver.quit()
```
