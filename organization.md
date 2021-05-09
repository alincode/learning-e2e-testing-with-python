# 組織測試專案

大到小 all -> feature -> scenario -> step

- feature 1：搜尋功能
  - scenario 1: 書名搜尋
    - step1: 前往搜尋頁
    - step2: 填寫想搜尋的書名
    - step3: 按下搜尋按鈕
    - etc...
  - scenario 2: 作者名搜尋
  - scenario 3: 關鍵字搜尋

## environment

`environment.py` 模組主要是定義測試跑之前或之後的特定事件，如下所示：

- before_step(context, step), after_step(context, step)
- before_scenario(context, scenario), after_scenario(context, scenario)
- before_feature(context, feature), after_feature(context, feature)
- before_tag(context, tag), after_tag(context, tag)
- before_all(context), after_all(context)

```py
# -- FILE: features/environment.py
from behave import *

def before_tag(context, tag):

```

### environment 範例

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

## Fixtures

### 範例一

```py
# -- FILE: behave4my_project/fixtures.py  (or in: features/environment.py)
from behave import fixture
from somewhere.browser.firefox import FirefoxBrowser

# -- FIXTURE: Use generator-function
@fixture
def browser_firefox(context, timeout=30, **kwargs):
    # -- SETUP-FIXTURE PART:
    context.browser = FirefoxBrowser(timeout, **kwargs)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.shutdown()
```

### 範例二

```py
# -- FILE: behave4my_project/fixtures.py
# ALTERNATIVE: Place fixture in "features/environment.py" (but reuse is harder)
from behave import fixture
import threading
from wsgiref import simple_server
from my_application import model
from my_application import web_app

@fixture
def wsgi_server(context, port=8000):
    context.server = simple_server.WSGIServer(('', port))
    context.server.set_app(web_app.main(environment='test'))
    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()
    yield context.server
    # -- CLEANUP-FIXTURE PART:
    context.server.shutdown()
    context.thread.join()
```

- <https://behave.readthedocs.io/en/stable/fixtures.html#docid-fixtures>

## Controlling Things With Tags

steps/testutil.py

```py
# -*- coding: UTF-8 -*-
"""
Test utility support.
"""

# @mark.test_support
# ----------------------------------------------------------------------------
# TEST SUPPORT:
# ----------------------------------------------------------------------------
class NamedNumber(object):
    """Map named numbers into numbers."""
    MAP = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four":  4,
        "five":  5,
        "six":   6,
    }

    @classmethod
    def from_string(cls, named_number):
        name = named_number.strip().lower()
        return cls.MAP[name]
```

### 測試帳號與資料的管理
