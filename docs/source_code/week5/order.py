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
