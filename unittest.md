# 與測試框架整合

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```

輸出的結果

```python
python test_python_org_search.py
.
----------------------------------------------------------------------
Ran 1 test in 15.566s

OK
```

## 補充：常見專有名詞

- Test Suite
- Test Case
- Test Step
- Test Run

## 參考文獻

- [我整理了一些 Python 測試的庫，看看有沒有你想要的 | 每日頭條](https://kknews.cc/zh-tw/code/9oay3gl.html)
- [Running First PyUnit Script](https://www.lambdatest.com/blog/using-pyunit-for-testing-a-selenium-python-test-suite/)
- [unittest | Python 官方文件](https://docs.python.org/zh-tw/3/library/unittest.html)
- [Python 2 Tutorial 第六堂（1）使用 unittest 單元測試](https://openhome.cc/Gossip/CodeData/PythonTutorial/UnitTest.html)
