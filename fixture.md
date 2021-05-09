# fixture 模組

fixture 模組，常使用於放置固定配置、常用配置，例如啟動 API Server、連接 DB、載入假資料等等。

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
