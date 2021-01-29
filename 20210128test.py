# #格式化输出，使用F方法，:10表示将改了输出框的大小设定为10，可以帮助对齐
# table={'Juno':'female','Alex':'male','Mars':'mail'}
# for name,gender in table.items():
#     print(f'{name:10}====>    {gender}')
#
# a='Python'
# print(f'I am learning {a.upper()!r}')
#
#
# #异常处理
# def division_test(a,b):
#    return a/b
#
# try:
#     x = 5
#     y = int(input('请输入分母:'))
#     print(division_test(x, y))
# except ZeroDivisionError:
#         print('这是个异常')
# finally:
#     print('这是finally')
#
import yaml

def get_datas():
    with open('E:/LearningPython/My_Test/testing/datas/calc.yaml') as f:
        datas = yaml.safe_load(f)
    return datas(['add1'][datas],datas['add1']['ids'])

print(get_datas())