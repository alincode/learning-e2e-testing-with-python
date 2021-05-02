# behave

## 安裝

```
pip install behave
pip install behave2cucumber
```

## feature 範例

`/features/tutorial.feature`

```
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!
```

## step 範例

`features/steps/tutorial.py`

```py
from behave import *

@given('we have behave installed')
def step_given(context):
    pass

@when('we implement a test')
def step_when(context):
    assert True is not False

@then('behave will test it for us!')
def step_then(context):
    assert context.failed is False
```

- context: 可以用來...

## 執行

```
behave
```

<!-- ```
behave --lang-list
behave --lang-help zh-TW
``` -->

![](assets/behave.png)

## 參考文獻

- [Part 1: Selenium with Python Behave (BDD) Introduction - YouTube](https://www.youtube.com/watch?v=JIyvAFBx2Fw)
