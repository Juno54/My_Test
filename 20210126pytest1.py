import pytest


def func(x):
    return x+1

##参数化
@pytest.mark.parametrize('a,b',[(1,2),(2,3),(20,40),('a','a1'),(5,9)])
def test_answer1(a,b):
    assert func(a)== b

def test_answer2():
    assert func(3) == 4

def test_answer3():
    assert func(3)== 3

###装饰器
@pytest.fixture()
def login():
    print("登录操作")
    username='JunoXu'
    return username

class TestDemo:
    def test_a(self,login):
        ##前面加个f是什么意思？？？？
        print(f"a   username={login}")

    def test_b(self):
        print("b")

    def test_c(self,login):
        print("c  username={login}")