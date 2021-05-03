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