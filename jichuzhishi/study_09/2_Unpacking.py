# @Time : 2025/2/22 03:25
# @Author : luoxin
"""
拆包（Unpacking）
    将容器中的元素解构为独立的元素
"""

# 拆包元组
x, y, z = (1, 2, 3)     # x=1, y=2, z=3
print(x, y, z)

# 拆包字典（默认拆包键）
key1, key2 = {"a": 1, "b": 2}  # key1="a", key2="b"
print(key1, key2)

# 当拆包的元素与赋值的元素不一致时，会报错
t1 = (1, 2, 3,)
# a,b = t1 # 输出：ValueError: too many values to unpack (expected 2)
# a,b,c,d = t1 #输出：ValueError: not enough values to unpack (expected 4, got 3)

# 当需要赋值的变量的个数与要拆的包的个数不一致时,可以使用*b来接收未知个数的数，并且放入列表（0-n,0--[]）
t2 = (1, 2, 3, 4)
a, *b, c = t2
print(a, b, c)  # 输出：1 [2, 3] 4；当拆包t2的值2,3，发现赋值给*b时，因为有*，所以就会将2,3装包成列表赋值给b
print(a, *b, c) # 输出：1 2 3 4；当在打印时，发现有*，就进行拆包，把b=[2,3]拆包为2 3

t3 = (9,)
a, *b = t3
print(a, b)  # 输出：9 []

"""
总结：
1:当在赋值时：装包
*y=4,6,8：会将散列的4，6，8准备好一个容器[],进行装包操作赋值给y--->[4,6,8]

2:当在打印时：拆包
print(*y)，发现有*，就进行拆包操作--->4，6，8
"""

