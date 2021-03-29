# 常見錯誤訊息

```py
try:
  l = driver.find_element_by_css_selector("h4")
  # NoSuchElementException thrown if not present
except NoSuchElementException:
  print("Element does not exist")
```
