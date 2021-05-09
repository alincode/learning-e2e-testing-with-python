# environment 模組

environment 模組顧名思義就是集中定義特定環境行為的地方，常使用於在執行測試之前或之後的，預載或卸除。此模組主要是定義測試跑之前或之後的特定事件，如下所示：

- before_step(context, step), after_step(context, step)
- before_scenario(context, scenario), after_scenario(context, scenario)
- before_feature(context, feature), after_feature(context, feature)
- before_tag(context, tag), after_tag(context, tag)
- before_all(context), after_all(context)

### 範例一

```py
# features/environment.py
def before_all(context):
    print ('=====Before ALL=====')


def after_all(context):
    print ('=====After ALL=====')


def before_feature(context, feature):
    if 'Decorators feature 2' in str(feature):
        print ('====Before Feature====' + str(feature))


def after_feature(context, feature):
    if 'Decorators feature 2' in str(feature):
        print ('====After Feature====' + str(feature))


def before_scenario(context, scenario):
    if 'Decorators check case 4' in str(scenario):
        print ('===Before Scenario===' + str(scenario))


def after_scenario(context, scenario):
    if 'Decorators check case 4' in str(scenario):
        print ('===After Scenario===' + str(scenario))


def before_step(context, step):
    if 'I start decorators check case 2' in str(step):
        print ('==Before Step==' + str(step))


def after_step(context, step):
    if 'I start decorators check case 2' in str(step):
        print ('==After Step==' + str(step))


def before_tag(context, tag):
    if 'tag1' in str(tag):
        print ('=Before Tag=' + str(tag))


def after_tag(context, tag):
    if 'tag1' in str(tag):
        print ('=After Tag=' + str(tag))


```

### 範例二

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

- <https://behave.readthedocs.io/en/stable/tutorial.html#environmental-controls>
- [environment.py](https://github.com/behave/behave.example/blob/master/features/environment.py)
