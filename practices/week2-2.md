# 練習題：上傳檔案

<https://the-internet.herokuapp.com/upload>

![](assets/file_uploader.png)

### 練習目標

- 上傳檔案
- 取得元素文字
- 驗證上傳成功

### 解答

```py
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://the-internet.herokuapp.com/upload")
assert "The Internet" in driver.title

try:

    file = driver.find_element_by_css_selector("[type='file']")
    file.send_keys('/Users/alin/PycharmProjects/demo/screenshot.png')
    submit_button = driver.find_element_by_css_selector("#file-submit")
    submit_button.submit()

    result = driver.find_element_by_css_selector("h3")
    assert "File Uploaded!" in result.text

finally:
    driver.quit()

```
