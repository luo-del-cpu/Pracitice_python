"""
匿名函数：简化匿名函数(没有函数名的函数)
匿名函数的作用就是在不丧失代码可读性的前提下为精简代码提供的一种方式。一般是用来操作可迭代数据中的元素
注意：需要按照条件查找字典中的元素时，lambda必须和key使用
"""
# 格式：  lambda 参数1，参数2... : 运算

s = lambda a, b: a + b #相当于把函数赋值给s，必须要赋值给一个值
print(s(1, 2))


# 匿名函数作为参数
def func(x, y, func):
    print(x, y)
    print(func)
    s = func(x, y)
    print(s)


func(1, 2, lambda a, b: a + b)

# 找出price最大的
lst = [
    {'name': 'egon', 'price': 100},
    {'name': 'rdw', 'price': 666},
    {'name': 'zat', 'price': 1}
]
ret = max(lst, key=lambda dic: dic['price'])  # 指定比较内容
print(ret) # {'name': 'rdw', 'price': 666}



