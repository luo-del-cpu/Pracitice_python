# @Time : 2025/2/22 04:18
# @Author : luoxin

"""
函数调用时的拆包:
    将容器（列表/元组/字典）拆包为独立的参数传递给函数。
"""

# 将列表或元组拆包为位置参数
def func(a, b, c):
    print(a, b, c)

"""
* 拆包位置参数
    将列表或元组拆包为位置参数。
"""
args = [1, 2, 3]
func(*args)  # 等价于 func(1, 2, 3)

"""
* 拆包字典
    很少用
"""
args1 = {"a": 1, "b": 2, "c": 3}
func(*args1) # 等价于 func('a','b','c')，默认拆字典的键放入

"""
** 拆包关键字参数
    将字典拆包为关键字参数。很少用
"""
func(**args1) # 等价于 func(a=1, b=2, c=3)，默认拆字典的值放入



"""
混合使用
"""
def func1(a, b, c, d):
    print(a, b, c, d)

args = (2, 3)
kwargs = {"d": 4}
func1(1, *args, **kwargs)  # 等价于 func(1, 2, 3, d=4)


"""
必须保持数量一致,否则会报错
"""
def func2(a, b):
    print(a, b)

args = [1, 2, 3]
# func1(*args)  # 报错：TypeError: func1() takes 2 positional arguments but 3 were given

"""
重点：函数调用字典时，需要使用**拆包成关键字参数时，才能传递给**kwargs使用，因为只接收关键字参数
"""
def merge_params(*args, **kwargs):
    combined = {
        "positional_args": args,
        "keyword_args": kwargs
    }
    return combined

dict = {"a": 1, "b": 2, "c": 3}
print(merge_params(1, 2, a=3, b=4)) # 输出：{'positional_args': (1, 2), 'keyword_args': {'a': 3, 'b': 4}}

print(merge_params(**dict)) # 输出：{'positional_args': (), 'keyword_args': {'a': 1, 'b': 2, 'c': 3}}


