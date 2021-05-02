# API 測試

## API 範例

<https://reqres.in/api/users/2>

```json
{
  "data": {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver",
    "avatar": "https://reqres.in/img/faces/2-image.jpg"
  },
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
```

### 測試應該驗證什麼？

- 結構
- 資料型別
- 值的正確性

## 完整的測試程式

```py
import unittest
import requests

class ApiTest(unittest.TestCase):

    def test_get_user(self):
        url = "https://reqres.in/api/users/2"
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)
        body = res.json()

        for body_key in body.keys():
            self.assertIn(body_key, ['data', 'support'])
        for data_key in body["data"]:
            self.assertIn(data_key, ['id', 'email', 'first_name', 'last_name', 'avatar'])
        for support_key in body["support"]:
            self.assertIn(support_key, ['url', 'text'])

        self.assertIsInstance(body["data"]["id"], int)
        self.assertEqual(body["data"]["id"], 2)

if __name__ == '__main__':
    unittest.main()
```

### 測試程式邏輯說明

1. 首先繼承 unittest 模組的 TestCase 類別
1. 然後再使用 test 作為前置命名，例如 test_1, test_2。
1. 最後在實作測試細節

### 延伸閱讀

- <https://github.com/public-apis/public-apis>
- <https://reqres.in/>
