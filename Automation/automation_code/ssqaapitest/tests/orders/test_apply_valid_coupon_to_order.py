
from ssqaapitest.src.helpers.orders_helper import OrdersHelper
from ssqaapitest.src.helpers.products_helper import ProductsHelper
import pytest
import random


@pytest.fixture(scope='module')
def my_setup_teardown():
    # hard code 50% coupon
    coupon_code = 'xevfex50off'
    discount_pct = '50.00'

    # get a random product for order
    rand_products = ProductsHelper().call_list_products()
    rand_product = random.choice(rand_products)

    info = dict()
    info['order_helper'] = OrdersHelper()
    info['coupon_code'] = coupon_code
    info['discount_pct'] = discount_pct
    info['product_id'] = rand_product['id']
    info['product_price'] = rand_product['price']

    return info



@pytest.mark.tcid60
def test_apply_valid_coupon_to_order(my_setup_teardown):
    """
    Validates when x% coupon is applied to an order, the 'total' amount is reduced by x%
    """
    # coupon info and product info in setup

    # create payload and make call to create order
    order_helper = OrdersHelper()
    order_payload_addition = {
        "line_items": [{"product_id": my_setup_teardown['product_id'], "quantity": 1}],
        "coupon_lines": [{"code": my_setup_teardown['coupon_code']}],
        "shipping_lines": [{"method_id": "flat_rate", "method_title": "Flat Rate", "total": "0.00"}]
        }

    rs_order = order_helper.create_order(additional_args=order_payload_addition)

    # calculate expected total price based on coupon and product price
    expected_total = float(my_setup_teardown['product_price']) * (float(my_setup_teardown['discount_pct'])/100)

    # get total from order response and verify
    total = round(float(rs_order['total']), 2)
    expected_total = round(expected_total, 2)

    assert total == expected_total, f"Order total is not reduced after applying 50% coupon. Expected cost: {expected_total}, Actual: {total}"
