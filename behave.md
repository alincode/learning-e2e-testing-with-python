# behave

官方文件：<https://behave.readthedocs.io/en/stable/>

## 安裝

```
pip install behave
pip install behave2cucumber
```

## 配置

### 最低限制

```
features/
features/everything.feature
features/steps/
features/steps/steps.py
```

### 更複雜的例子

```
features/
features/signup.feature
features/login.feature
features/account_details.feature
features/environment.py
features/steps/
features/steps/website.py
features/steps/utils.py
```

## 完整範例

### feature 範例

`/features/tutorial.feature`

```
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!
```

### step 範例

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

```
Feature: Scenario Outline
 Scenario Outline: Blenders
    Given I put <thing> in a blender
    When I switch the blender on
    Then it should transform into <other thing>
  Examples: Amphibians
    | thing         | other thing |
    | Red Tree Frog | mush        |
    | apples        | apple juice |
  Examples: Consumer Electronics
    | thing         | other thing |
    | iPhone        | toxic waste |
    | Galaxy Nexus  | toxic waste |
```

### 執行

```
behave
behave /features/tutorial.feature
```

<!-- ```
behave --lang-list
behave --lang-help zh-TW
``` -->

![](assets/behave.png)

## step 參數

```
# feature
When Enter first name "AILIN" and last name "LIOU"
```

```
@when(u'Enter first name "{first_name}" and last name "{last_name}"')
def step_impl(context, first_name, last_name):
```

## Environmental Controls

<https://behave.readthedocs.io/en/stable/tutorial.html#environmental-controls>

```py
# -- FILE: features/environment.py
from behave import fixture, use_fixture
from behave4my_project.fixtures import wsgi_server
from selenium import webdriver

@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.browser = webdriver.Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

def before_all(context):
    use_fixture(wsgi_server, context, port=8000)
    use_fixture(selenium_browser_chrome, context)
    # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.

def before_feature(context, feature):
    model.init(environment='test')
```

## 參考文獻

- [Part 1: Selenium with Python Behave (BDD) Introduction - YouTube](https://www.youtube.com/watch?v=JIyvAFBx2Fw)
- [behave.example](https://github.com/behave/behave.example/tree/master/features)
