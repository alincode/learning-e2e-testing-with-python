# 練習題：檢查 Tab 是否可以正常切換

![](asserts/nav_tab.png)

- <https://demoqa.com/tabs>
- 會用到的語法
  - element.get_attribute("attr_name")
  - string.split()
  - element.text

<!--
### 解答

```py
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://demoqa.com/tabs")
assert "ToolsQA" in driver.title

try:
    driver.find_element_by_id("demo-tab-origin").click()
    origin_tab_content = driver.find_element_by_id("demo-tabpane-origin")
    class_names = origin_tab_content.get_attribute("class")
    assert "active" in class_names.split()
    assert "Contrary to popular belief" in origin_tab_content.text
finally:
    driver.quit()

``` -->
