# 元素的狀態與屬性

## Get Active Element

```py

  from selenium import webdriver
  from selenium.webdriver.common.by import By

  driver = webdriver.Chrome()
  driver.get("https://www.google.com")
  driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

  # Get attribute of current active element
  attr = driver.switch_to.active_element.get_attribute("title")
  print(attr)

```

## Is Element Enabled

```py
  driver.get("https://www.google.com/");

  //returns true if element is enabled else returns false
  boolean value = driver.findElement(By.name("btnK")).isEnabled();

```

## Is Element Selected

```py
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Returns true if element is checked else returns false
value = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type").is_selected()

```

## Get Element TagName

```py
driver.get("https://www.example.com")

# Returns TagName of the element
attr = driver.find_element(By.CSS_SELECTOR, "h1").tag_name

```

## Get Element Rect

```py
driver.get("https://www.example.com")

# Returns height, width, x and y coordinates referenced element
res = driver.find_element(By.CSS_SELECTOR, "h1").rect
```

## Get Element CSS Value

```py
# Navigate to Url
driver.get('https://www.example.com')

# Retrieves the computed style property 'color' of linktext
cssValue = driver.findElement(By.LINK_TEXT, "More information...").value_of_css_property('color')
```

## Get Element Text

```py
driver.get("https://www.example.com")

# Retrieves the text of the element
text = driver.find_element(By.CSS_SELECTOR, "h1").text
```

## 練習題

<https://the-internet.herokuapp.com/dynamic_controls>

## 參考文獻

- <https://www.selenium.dev/documentation/en/webdriver/web_element/>
