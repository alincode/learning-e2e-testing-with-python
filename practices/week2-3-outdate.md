# 練習題： TextBox 表格

<https://demoqa.com/text-box>

練習

<!--
### 答案

```py
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://demoqa.com/text-box")
assert "ToolsQA" in driver.title

try:
    user_name = driver.find_element_by_css_selector("#userName")
    user_name.send_keys("AILIN LIOU")

    user_email = driver.find_element_by_css_selector("#userEmail")
    user_email.send_keys("ooxx@ooxx.com")

    current_address = driver.find_element_by_css_selector("#currentAddress")
    current_address.send_keys("TAiWAN")

    permanent_address = driver.find_element_by_css_selector("#permanentAddress")
    permanent_address.send_keys("台灣")

    submit_button = driver.find_element_by_css_selector("#submit")
    submit_button.click()

    output = driver.find_element_by_css_selector("#name")
    assert "Name:AILIN LIOU" in output.text

finally:
    driver.quit()

``` -->
