# @Time : 2025/2/22 03:46
# @Author : luoxin
"""
函数定义时的 **kwargs
    用于接受不定数量的参数，实现参数装包。
"""

# 这里**kwargs在函数调用时，可传参数也可以不传；会准备一个字典{};若要传参，必须是关键字参数:key=value
def test(**kwargs):
    print(kwargs)
    # print(**kwargs) print()函数里**kwargs不能拆包

"""
不传参:
    得出：{}
"""
test()

"""
传递关键字参数:
    得出：{'a': 1, 'b': 2}
"""
test(a=1, b=2)  # 得出：{'a': 1, 'b': 2}

"""
直接传值:
    无法接收，必须使用关键字参数进行传递
"""
test(1)
test(1, 2, 3)

"""
通过实参int传递:
    无法接收，必须使用关键字参数进行传递
"""
x = 2
test(x)

"""
通过实参str传递:
    无法接收，必须使用关键字参数进行传递
"""
a = 'll'
test(a)

"""
通过列表传递:
    无法接收，必须使用关键字参数进行传递
"""
l = [1,2,3]
test(l)

"""
通过字典传递:
   无法接收，必须使用关键字参数进行传递
"""
d = {"a":"1"}
test(d)

"""
不可变参数，可变参数组合使用
"""
def func(a, *args, b=0, **kwargs):
    print(f"a={a}, args={args}, b={b}, kwargs={kwargs}")

func(1, 2, 3, b=4, c=5, d=6) # 输出：a=1, args=(2, 3), b=4, kwargs={'c': 5, 'd': 6}

