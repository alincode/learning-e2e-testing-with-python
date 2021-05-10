# 練習題：API 測試

- 測試 GET `https://reqres.in/api/users?page=1` API

```json
{
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    {
      "id": 2,
      "email": "janet.weaver@reqres.in",
      "first_name": "Janet",
      "last_name": "Weaver",
      "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    {
      "id": 3,
      "email": "emma.wong@reqres.in",
      "first_name": "Emma",
      "last_name": "Wong",
      "avatar": "https://reqres.in/img/faces/3-image.jpg"
    },
    {
      "id": 4,
      "email": "eve.holt@reqres.in",
      "first_name": "Eve",
      "last_name": "Holt",
      "avatar": "https://reqres.in/img/faces/4-image.jpg"
    },
    {
      "id": 5,
      "email": "charles.morris@reqres.in",
      "first_name": "Charles",
      "last_name": "Morris",
      "avatar": "https://reqres.in/img/faces/5-image.jpg"
    },
    {
      "id": 6,
      "email": "tracey.ramos@reqres.in",
      "first_name": "Tracey",
      "last_name": "Ramos",
      "avatar": "https://reqres.in/img/faces/6-image.jpg"
    }
  ],
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
```

### 答案

```py
import unittest
import requests

class ApiTest(unittest.TestCase):

    def test_get_users(self):
        url = "https://reqres.in/api/users?page=1"
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)
        body = res.json()

        for body_key in body.keys():
            self.assertIn(body_key, ['page', 'per_page', 'total', 'total_pages', 'data', 'support'])
        for support_key in body["support"]:
            self.assertIn(support_key, ['url', 'text'])

        self.assertEqual(len(body["data"]), 6)
        row = body["data"][1]
        for row_key in row:
            self.assertIn(row_key, ['id', 'email', 'first_name', 'last_name', 'avatar'])
        self.assertIsInstance(row["id"], int)
        self.assertEqual(row["id"], 2)

if __name__ == '__main__':
    unittest.main()
```

- 測試 POST `https://reqres.in/api/login` API

### 解答

```py
import unittest
import requests

class ApiTest(unittest.TestCase):

    def test_login(self):
        url = "https://reqres.in/api/login"
        req_body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        res = requests.post(url, req_body)
        self.assertEqual(res.status_code, 200)
        body = res.json()
        print(body)

        for body_key in body.keys():
            self.assertIn(body_key, ['token'])

        self.assertIsInstance(body['token'], str)

if __name__ == '__main__':
    unittest.main()
```
