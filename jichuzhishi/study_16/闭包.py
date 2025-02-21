# 闭包
# 在函数中提出的概念
"""
条件：
1.外部函数中定义了内部函数
2.外部函数是有返回值的
3.返回的值是：内部函数名
4.内部函数引用了外部函数的变量

格式：
def 外部函数（）：
    ...
    def 内部函数（）：
        ...
    return 内部函数
"""


# def func():
#     a = 100
#
#     def inner_func():
#         b = 99
#         print(a, b)  # 在此内部函数中使用了外部函数中的a变量
#
#     return inner_func  # 在此返回了内部的函数，注意返回的是函数的名称，不能加（）
#
#
# x = func()  # 将return返回的值赋值给一个变量
# x()  # 直接使用x（）即调用了inner_func()的函数


# 案例
def func1(a, b):
    c = 10

    def inner_func1():
        s = a + b + c
        print('s的值：', s)

    return inner_func1


x = func1(2, 3)  # x就是inner_func1
x()  # 调用返回出来的内部函数
