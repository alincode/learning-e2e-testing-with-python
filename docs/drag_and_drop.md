# 拖拉

<http://sahitest.com/demo/dragDropMooTools.htm>

```py
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/dragDropMooTools.htm')

dragger = driver.find_element_by_id('dragger')
item1 = driver.find_element_by_xpath('//div[text()="Item 1"]')
item2 = driver.find_element_by_xpath('//div[text()="Item 2"]')
item3 = driver.find_element_by_xpath('//div[text()="Item 3"]')
item4 = driver.find_element_by_xpath('//div[text()="Item 4"]')

action = ActionChains(driver)
# 1. 移動 dragger 到目標一
action.drag_and_drop(dragger, item1).perform()
sleep(2)

# 2. 效果與上句相同，也能起到移動效果
action.click_and_hold(dragger).release(item2).perform()
sleep(2)

# 3.效果与上两句相同，也能起到移动的效果
action.click_and_hold(dragger).move_to_element(item3).release().perform()
sleep(2)
# action.drag_and_drop_by_offset(dragger, 400, 150).perform()

# 4.移动到指定坐标
action.click_and_hold(dragger).move_by_offset(400, 150).release().perform()
# 5.与上一句相同，移动到指定坐标
sleep(2)
driver.quit()
```
