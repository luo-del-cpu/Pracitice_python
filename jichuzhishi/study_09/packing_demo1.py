# @Time : 2023/9/17 23:07
# @Author : luoxin

"""
拆包：
在Python中，拆包（unpacking）是一种将可迭代对象（如列表、元组或字典）中的元素解包并赋值给多个变量的操作。
通过拆包，可以方便地将可迭代对象中的元素提取出来，然后分别赋值给对应的变量。
"""

t1 = (1, 2, 3,)
a, b, c = t1
print(a)  # 输出:1
print(b)  # 输出:2
print(c)  # 输出:3

# a,b = t1 # 输出：ValueError: too many values to unpack (expected 2)
# a,b,c,d = t1 #输出：ValueError: not enough values to unpack (expected 4, got 3)

# 变量的个数与元组个数不一致

t1 = (1, 2, 3, 4, 5, 6)
a, *_, c = t1
print(a, c, _)  # 输出：1 6 [2, 3, 4, 5]
a, c, *_ = t1
print(a, c, _)  # 输出：1 2 [3, 4, 5, 6]

t1 = (9,)
a, *b = t1  # "*b"代表未知个数0-n,0--[]  多个元素的话：[1,2,3,4,5,...]
print(a, b)  # 输出：9 []
