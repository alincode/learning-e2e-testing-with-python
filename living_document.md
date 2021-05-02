# 活文件 (living document)

- 所謂的活文件 Living Document 意思是說，文件的會隨著時間、處境而跟著改變的。
- 在軟體上；一份活的文件或動態文件就是一份不斷修改和更新的文件。

### 支援活文件的框架

- behave: <https://behave.readthedocs.io/en/stable/>
- cucumber: <https://cucumber.io/>
- ...

## behave

```
pip install git+https://github.com/behave/behave
```

`/features/tutorial.feature`

```
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!
```

`features/steps/tutorial.py`

```py
from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
```

![](assets/behave.png)

## 延伸閱讀

- <https://www.youtube.com/results?search_query=python+cucumber>
- <https://www.tenlong.com.tw/products/9789862019481>

![](assets/spec_by_example.png)
