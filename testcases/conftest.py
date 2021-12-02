import pytest

@pytest.fixture(scope='function')
def login():
    print("登录")