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