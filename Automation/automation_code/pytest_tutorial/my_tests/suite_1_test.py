
import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke
def test_login_page_valid_user():
    print("Login with valid user")
    print("Function: aaaaaaa")

@pytest.mark.regression
def test_login_page_wrong_password():
    print("Login with wrong password")
    print("Function: bbbbbbbbb")
    # assert 1==2, 'One is not two'