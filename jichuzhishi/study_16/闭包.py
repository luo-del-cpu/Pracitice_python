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


def func():
    a = 100

    def inner_func():
        b = 99
        print(a, b)  # 在此内部函数中使用了外部函数中的a变量

    return inner_func  # 在此返回了内部的函数，注意返回的是函数的名称，不能加（）

# 调用函数，将return返回的值赋值给一个变量,其实返回的就是内部函数inner_func()
x = func()
x()  # 直接使用x(),就相当于调用了inner_func()的函数


# 案例
def func1(a, b):
    c = 10

    def inner_func1():
        s = a + b + c
        print('s的值：', s)
        print(f"inner_func1的内存地址是:{id(inner_func1)}")
    return inner_func1


x = func1(2, 3)  # x就是inner_func1
x()  # 调用返回出来的内部函数
print(f"外部x的内存地址是:{id(x)}")


"""
从打印结果可以看出，实际他们就是一个函数，使用的一个内存地址
    inner_func1的内存地址是:4331122400
    外部x的内存地址是:4331122400
"""


funcs = []

for i in range(3):
    def f(i=i):
        return i
    funcs.append(f)

print(funcs[0]())  # ❗ 0
print(funcs[1]())  # ❗ 1
print(funcs[2]())  # ❗ 2
