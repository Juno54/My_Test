#测试用例命名规范
#文件要以test_开头，或者_test结尾
#类要以Test开头，方法要以test_开头

import sys
import pytest
from pythoncode.Caculator import Calculator01
from decimal import Decimal
import yaml

def get_datas():
    with open('./datas/calc.yaml') as f:
        datas = yaml.safe_load(f)
    return datas(['add1'][datas],datas['add1']['ids'])


class Test_caculator:

    #在类执行执行前执行一次,这样可以避免每个test方法都调用一次Calculator类。setup是个方法
    def setup_class(self):
        print('开始测试...')
        #初始化1个实例calc
        self.calc = Calculator01()

    def teardown_class(self):
        print('测试结束...')



    #注意，c,a,b要用1个引号括起来，代表1个参数
    @pytest.mark.parametrize('c,a,b',[[10,2,8],[-6,-2,-4],[0,9,-9],[1024,1000,24],[0.3,0.1,0.2]])
    def test_add1(self,c,a,b):
        print(f'c=a+b: c={c}  a={a}  b={b}')
        assert  ('%f' %c) == self.calc.add1(a,b)

    @pytest.mark.parametrize('c,a,b', [[10.013, 2.005, 8.007], [-6.4449, -2.3333, -4.1116], [0, 9, -9], [1024, 1000, 24], [0.3, 0.1, 0.2]])
    def test_add2(self, c, a, b):
        print(f'c=a+b: c={c}  a={a}  b={b}')
        assert (Decimal(c).quantize(Decimal('1.000000'))) == self.calc.add2(a, b)



    # 注意，c,a,b要用1个引号括起来，代表1个参数
    @pytest.mark.parametrize('c,a,b', [[2, 4, 2], [-3, -9, 3], [10, -20, -2], [0.6, 3.6, 6],[2.666667, 8, 3],[4,20,0]])
    def test_division(self, c, a, b):
        try:
            print(f"c=a/b: c={c}  a={a}  b={b}")
            assert (Decimal(c).quantize(Decimal('1.000000'))) == self.calc.division(a, b)
        except ZeroDivisionError:
            print('分子不能为0')




