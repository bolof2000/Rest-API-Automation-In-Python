import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]
@pytest.fixture(scope='module')
def my_setup():
    print("")
    print(">>>> MY SETUP <<<<")

    return {'id': 20, 'name': 'Admas'}

@pytest.mark.abc
class TestCheckout(object):

    def test_checkout_as_guest(self, my_setup):
        print("checkout as guest")
        print("Class: 11111111")

    def test_checkout_with_existing_user(self):
        print("Checkout with existing user")
        print("Class: 22222222222")