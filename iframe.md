# IFrame

## 切換 Iframe

語法ㄧ：透過 ID

```html
<iframe id="ifr" name="demo" src="demo.html" height="200" width="300"></iframe>
```

```py
driver.switch_to_frame("ifr")
```

語法二：透過 Name

```html
<iframe id="ifr" name="demo" src="demo.html" height="200" width="300"></iframe>
```

```py
driver.switch_to_frame("demo")
```

語法三：透過 index

```
<iframe id="ifr" name="demo" src="demo.html" height="200" width="300"></iframe>
<iframe id="ifr" name="demo" class='second' src="width.html" height="200" width="300"></iframe>
<iframe id="ifr" name="demo" src="width.html" height="200" width="300"></iframe>
```

```py
driver.switch_to_frame(1)
```

語法四：透過元素

```py
iframe = driver.find_element_by_css_selector('iframe')
driver.switch_to.frame(iframe)
```

## 回到預設頁面區塊

```
driver.switch_to.default_content()
```

## 練習題

![](asserts/TinyMCE.png)

- <http://the-internet.herokuapp.com/iframe>
  - driver.switch_to.frame(iframe)
  - driver.switch_to.default_content()

<!-- ### 答案

```py
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("./chromedriver")
driver.get("http://the-internet.herokuapp.com/iframe")
assert "The Internet" in driver.title

try:
    iframe = driver.find_element_by_css_selector('iframe')
    driver.switch_to.frame(iframe)
    editor = driver.find_element_by_css_selector('body')
    editor.clear()
    editor.send_keys("123")
    # sleep(5)
    driver.switch_to.default_content()
    title = driver.find_element_by_css_selector('h3')
    assert "An iFrame containing the TinyMCE WYSIWYG Editor" in title.text
finally:
    driver.quit()

``` -->

## 延伸閱讀

- [Select iframe using Python and Selenium](https://www.tutorialspoint.com/select-iframe-using-python-and-selenium)
