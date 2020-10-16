
import logging as logger
import pytest
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():

    req_helper = RequestsUtility()
    rs_api = req_helper.get('customers')

    assert rs_api, f"Response of list all customers is empty."
