#被测类：计算器
from decimal import Decimal
class Calculator:
    def add1(self,a,b):
        return ('%f' %(a+b))

    def add2(self,a,b):
        return (Decimal(a+b).quantize(Decimal('1.000000')))

    def division(self,a,b):
        return (Decimal(a/b).quantize(Decimal('1.000000')))

