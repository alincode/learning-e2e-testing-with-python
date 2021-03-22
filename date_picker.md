# 日期選擇器

## 日期

```py
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()
driver.get("https://demoqa.com/date-picker")

select_date = driver.find_element_by_id("datePickerMonthYearInput")

select_date.click()
select_year = Select(driver.find_element_by_css_selector('.react-datepicker__year-select'))
select_year.select_by_value('1999')

select_date.click()
select_month = Select(driver.find_element_by_css_selector('.react-datepicker__month-select'))
select_month.select_by_value('0')

select_date.click()
day = driver.find_element_by_css_selector("[aria-label='Choose Sunday, January 3rd, 1999']")
day.click()
driver.quit()
```

## 時間

```py
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://demoqa.com/date-picker")
driver.maximize_window()

select_date = driver.find_element_by_id("dateAndTimePickerInput")
select_date.click()

time = driver.find_elements_by_css_selector('.react-datepicker__time-list-item')[3]
time.click()
```

## 參考文獻

- [MDN Web Docs | <input type="date">](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date)
