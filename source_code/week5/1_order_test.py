import unittest
import order

class TestOrder(unittest.TestCase):
    def test_calculate_order_not_vip(self):
        self.assertEqual(order.calculate_order(100, False), 100)
        self.assertEqual(order.calculate_order(1100, False), 990)

    def test_calculate_order_vip(self):
        self.assertEqual(order.calculate_order(100, True), 95)
        self.assertEqual(order.calculate_order(1100, True), 940.5)

if __name__ == '__main__':
    unittest.main()