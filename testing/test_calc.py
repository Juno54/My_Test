#测试用例命名规范
#文件要以test_开头，或者_test结尾
#类要以Test开头，方法要以test_开头
# -*- coding: utf-8 -*-
import sys
import pytest
from pythoncode.Caculator import Calculator
from decimal import Decimal
import yaml

##读取calc.yaml文件中的数据
def get_data1():
    with open('./datas/calc.yaml',encoding='utf-8') as f:
        data1 = yaml.safe_load(f)
    return (data1['add']['datas'],data1['add']['ids'])

def get_data2():
    with open('./datas/calc.yaml',encoding='utf-8') as f:
        data2 = yaml.safe_load(f)
    return (data2['division']['datas'],data2['division']['ids'])



class Test_caculator:
    #把输出值变成list
    data1: list = get_data1()
    data2: list = get_data2()

    #在类执行执行前执行一次,这样可以避免每个test方法都调用一次Calculator类。setup是个方法
    def setup_class(self):
        print('开始测试...')
        #初始化1个实例calc
        self.calc = Calculator()

    def teardown_class(self):
        print('测试结束...')


    #加法和除法分别使用了3种格式数据进行测试，一种直接输出结果，一种保留小数点后6位，一种使用decimal格式
    #注意，c,a,b要用1个引号括起来，代表1个参数
    @pytest.mark.parametrize('c,a,b',data1[0],ids=data1[1])
    def test_add1(self,c,a,b):
        print(f'c=a+b: c={c}  a={a}  b={b}')
        assert c == self.calc.add1(a,b)

    @pytest.mark.parametrize('c,a,b',data1[0],ids=data1[1])
    def test_add2(self, c, a, b):
        print(f'c=a+b: c={c}  a={a}  b={b}')
        if self.calc.add2(a,b) is None:
            assert c == self.calc.add2(a,b)
        else:
            assert (Decimal(c).quantize(Decimal('1.000000'))) == self.calc.add2(a, b)

    @pytest.mark.parametrize('c,a,b',data2[0],ids=data2[1])
    def test_division1(self,c,a,b):
        if self.calc.division1(a,b) is None:
            assert c == self.calc.division1(a,b)
        else:
            assert ('%f' % c) == self.calc.division1(a, b)



    # 注意，c,a,b要用1个引号括起来，代表1个参数
    @pytest.mark.parametrize('c,a,b',data2[0],ids=data2[1])
    def test_division2(self, c, a, b):
        print(f"c=a/b: c={c}  a={a}  b={b}")
        if self.calc.division2(a,b) is None:
            assert  c == self.calc.division2(a,b)
        else:
            assert (Decimal(c).quantize(Decimal('1.000000'))) == self.calc.division2(a, b)



