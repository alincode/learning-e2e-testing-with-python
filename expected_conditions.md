# 預期條件 (Expected Conditions)

內建的檢查條件，有以下幾個內建的判斷，除了這些之外，也可以自訂預期條件。

### title_is

判斷當前頁面標題是否為 title

```py
EC.title_is("Google")
```

### title_contains

判斷當前頁面標題是否包含 title

```py
EC.title_contains("Google")
```

### presence_of_element_located

判斷此定位的元素是否存在

presence_of_all_elements_located(locator)

```py
EC.presence_of_element_located((By.ID, "enableAfter"))
```

### url_contains

判斷頁面網址中是否包含 url

```py
EC.url_contains(url)
```

### url_to_be

判斷頁面網址是否為 url

```py
EC.url_to_be(url)
```

### url_changes(url)

判斷頁面網址不是 url

```py
EC.url_changes(url)
```

### visibility_of_element_located(locator)

判斷此定位的元素是否可見

### visibility_of

判斷此元素是否可見

### presence_of_all_elements_located(locator)

判斷此定位的一組元素至少有一個可見

### visibility_of_all_elements_located(locator)

判斷此定位的一組元素全部可見

### text_to_be_present_in_element(locator, text)

判斷此定位中是否包含 text 的內容

### text_to_be_present_in_element_value(locator, text)

判斷此定位中的 value 屬性中是否包含 text 的內容

### frame_to_be_available_and_switch_to_it(locator)

判斷定位的元素是否為 frame，並直接切換到這個 frame 中

### invisibility_of_element_located(locator)

判斷定位的元素是否不可見

### invisibility_of_element(element)

判斷此元素是否不可見

### element_to_be_clickable(locator)

判斷所定位的元素是否可見且可點擊

### element_to_be_selected(element)

判斷該元素是否被選中

### element_located_to_be_selected(locator)

判斷該元素被選中狀態是否和期望狀態相同

### element_located_selection_state_to_be(locator,Boolean)

判斷定位的元素被選中狀態是否和期望狀態相同

### number_of_windows_to_be(num)

判斷當前瀏覽器頁簽數量是否為 num

### new_window_is_opened(handles)

判斷此 handles 頁簽不是唯一打開的頁簽

### alert_is_present()

判斷是否會出現 alert 窗口警報

- [官方 API 文件](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected_conditions)
