# 練習題：單元測試

- 消費滿一千，打九折。
- 若是 VIP 客戶，在打 95 折。

```py
# order.py
max_range = 1000
vip_discount = 0.95
rebate_discount = 0.9

def calculate_order(original_amount, is_vip):
    amount = original_amount
    if original_amount >= max_range:
        if is_vip:
            amount = original_amount * rebate_discount * vip_discount
        else:
            amount = original_amount * rebate_discount
    else:
        if is_vip:
            amount = original_amount * vip_discount
    return amount
```

### 答案

```py
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
```
