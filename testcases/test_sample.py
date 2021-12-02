import pytest
def test_1():
    print('测试用例1')

def test_2(login):
    print('测试用例2')

if __name__ =="__main__":
    pytest.main(['test_sample.py','-s'])
