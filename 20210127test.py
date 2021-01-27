# ###列表list
# list_a=[1,2,3,'a']
# print(type(list_a))
# print(list_a[2])
# # list_a.append(4)
#
# ##给list_a添加元素
# # for i in range(5):
# #     list_a.append(i)
# #     i+=1
#
# ##☆☆☆循环生成list，注意 一定要用{}！！！
# list_b={i**2 for i in range(1,4)}
# print(list_b)

# ###元祖tuple
# tuple_a=(3,4,8,5,['q','d',8])
# print(type(tuple_a))
# #统计7在tuple_a中出现的次数
# print(tuple_a.count(8))
# print(tuple_a[4])
# ##☆☆☆元祖中的list可以修改
# tuple_a[4][1]='xzz'
# print(tuple_a)


# ##集合set
# set_a= {1,2,3,4,5}
# set_b={3,5,6,7}
# print(type(set_a))
# print(set_a.union(set_b))
# set_a.add('f')
# print(set_a)


##字段dic
dic_a={'a':1,'b':2,'c':3}
print(type(dic_a))
##删除key为a的值
print(dic_a.pop('a'))
print(dic_a)
print(dic_a.fromkeys('b'))
##用for循环构造个字典
print({i: i ** 2 for i in range(1, 4)})