
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger

class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")

    def call_create_product(self, payload):
        return self.requests_utility.post('products', payload=payload, expected_status_code=201)

    def call_list_products(self, payload=None):

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f"List products page number: {i}")

            if not payload:
                payload = {}

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            # add the current page number to the call
            payload['page'] = i
            rs_api = self.requests_utility.get('products', payload=payload)

            # if there is not response then stop the loop b/c there are no more products
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages.")

        return all_products

    def call_retrieve_product(self, product_id):
        return self.requests_utility.get(f'products/{product_id}')

    def call_update_product(self, product_id, payload=None):
        return self.requests_utility.put(f'products/{product_id}', payload=payload)