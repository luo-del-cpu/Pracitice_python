# @Time : 2023/11/22 22:14
# @Author : luoxin


"""
返回值：通过return关键字将想要返回的参数"扔"出去
return
"""


def add(a, b):
    result = a + b
    return "aaa", 100


x = add(1, 2)  # return的值必须得有一个参数接着
print(x)  # 得出：('aaa', 100),如果是返回了两个值，那么就会放到元组中

x, y = add(1, 2)
print(x, y)  # 得出：aaa 100；也可以是两个值来接收，分别赋值


def add1(a, b):
    result = a + b
    return result

x = add1(1,2)
print(x) #得出：3
