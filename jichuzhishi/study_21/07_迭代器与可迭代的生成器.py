"""
可迭代的对象：1.生成器 2.元组，列表，字典，集合，字符串
"""
from collections import Iterable

# 如何判断一个对象是否可迭代？通过isinstance方法得出
# list = [1, 2, 3, 4]
# f = isinstance(list, Iterable)
# print(f)  # 得到：True
#
# str_1 = 'abc'
# f = isinstance(str_1, Iterable)
# print(f)  # 得到：True
#
# g = (x for x in range(10))
# f = isinstance(g, Iterable)
# print(f)  # 得到：True
#
# int_1 = 10
# f = isinstance(int_1, Iterable)
# print(f)  # 得到：False


'''
迭代器：可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

概念：
    迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。
    
特点：
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
    迭代器只能往前不会后退。
    
问题：可迭代的是不是肯定就是迭代器？
    生成器是可迭代的，也是迭代器
    list是可迭代的，但不是迭代器，如果想把list变成一个迭代器，那么可以通过：iter（list）变成一个迭代器
    同理，元组，字典等也是
'''

list = [1,2,3,4]

list1 = iter(list)  # 这样list1就变成了一个迭代器
print(next(list1))
print(next(list1))

'''
生成器与迭代器：
1.可以理解生成器时迭代器的一种
2.只要能够使用next()调用获取值的就是迭代器
'''