# API 測試

```py
import unittest
import requests

class ApiTest(unittest.TestCase):

    def test_get_user(self):
        url = "https://reqres.in/api/users/2"
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)
        body = res.json()
        # data = body["data"]
        self.assertEqual(body["data"]["id"], 2)


if __name__ == '__main__':
    unittest.main()
```

## 練習題

- 測試 `https://reqres.in/api/users?page=2` API

### 延伸閱讀

- <https://github.com/public-apis/public-apis>
- <https://reqres.in/>
