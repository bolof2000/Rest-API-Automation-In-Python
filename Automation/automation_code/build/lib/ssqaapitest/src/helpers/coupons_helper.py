

from ssqaapitest.src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger

class CouponsHelper(object):

    def __init__(self):
        self.woo_helper = WooAPIUtility()

    def call_create_coupon(self, payload):
        logger.debug("Calling 'Create Coupon'.")
        return self.woo_helper.post('coupons', params=payload, expected_status_code=201)

    def call_retrieve_coupon(self, coupon_id):
        logger.debug("Calling retrieve a coupon. Coupon id: {}")
        return self.woo_helper.get(f'coupons/{coupon_id}')

