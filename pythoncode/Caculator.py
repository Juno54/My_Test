#被测类：计算器
from decimal import Decimal
class Calculator:
    #直接输出结果比较，测试小数点后n位
    def add1(self,a,b):
        return (a+b)

    #保留小数点后6位
    def add2(self,a,b):
        return (Decimal(a+b).quantize(Decimal('1.000000')))

    def division1(self,a,b):
        return ('%f' %(a/b))

    def division2(self,a,b):
        return (Decimal(a/b).quantize(Decimal('1.000000')))

