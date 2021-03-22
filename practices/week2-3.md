# 練習題：填寫表單

<https://demoqa.com/automation-practice-form>

![](assets/week2-3.png)

### 練習目標

- 控制 radio, checkbox 元素
- 控制 modal

### 解答

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.get("https://demoqa.com/automation-practice-form")
print(driver.title)
assert "ToolsQA" in driver.title

driver.maximize_window()

try:

    first_name = driver.find_element_by_css_selector("#firstName")
    first_name.send_keys("AILIN")
    last_name = driver.find_element_by_css_selector("#lastName")
    last_name.send_keys("LIOU")
    user_email = driver.find_element_by_css_selector("#userEmail")
    user_email.send_keys("aaa@aaa.com")
    user_number = driver.find_element_by_css_selector("#userNumber")
    user_number.send_keys("0123456789")

    # radio
    male_radio = driver.find_element_by_css_selector("[for='gender-radio-1']")
    male_radio.click()

    # checkbox
    sports_checkbox = driver.find_element_by_css_selector("[for='hobbies-checkbox-1']")
    sports_checkbox.click()

    reading_checkbox = driver.find_element_by_css_selector("[for='hobbies-checkbox-2']")
    reading_checkbox.click()

    current_address = driver.find_element_by_css_selector("#currentAddress")
    current_address.send_keys("TAIPEI")

    # file
    picture = driver.find_element_by_css_selector("[type='file']")
    picture.send_keys('/Users/alin/PycharmProjects/demo/screenshot.png')

    submit_button = driver.find_element_by_css_selector("#submit")
    submit_button.submit()

    # modal
    close_large_modal = driver.find_element_by_css_selector("#closeLargeModal")
    close_large_modal.click()
finally:
    driver.quit()

```
