'''
通过列表生成式(列表推导式)，我们可以直接创建一个列表，
但是，收到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的列表，从而节省大量的空间。在python中，这种一边循环一边计算的机制，称为”生成器“，generator

得到列表生成器的方式：
1.通过列表推导式得到生成器

'''


# 得到生成器
# 1.通过列表推导式得到生成器
# g = (x * 3 for x in range(10))  # 将以前的列表推导式的[]换为（），就是一个生成器
# print(g)  # 得到<generator object <genexpr> at 0x000001DD55C67900>
#
# # 得到元素的方法
# # 1.通过调用__next__()方式得到元素
# print(g.__next__())  # 得到0
# print(g.__next__())  # 得到3；调用一次，通知生成器产生一个元素
#
# # 2.next(生成器对象)builtins系统内置函数
# # 每调用一次next()就产生一个元素
# print(next(g))  # 得到6
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  # 得到24
# print(next(g))  # 得到27
# print(next(g))  # 得到：StopIteration；超出生成器的范围，报错

# 2.定义生成器的方式二：借助函数完成
# 只要函数中出现了yield关键字，说明函数就不是函数了，变成了一个生成器

# def func():
#     n = 0
#     while True:
#         n += 1
#         yield n
#
#
# x = func()
# print(x)  # 得到：<generator object func at 0x0000020E65519510>
# print(next(x))  # 得到：1


# 斐波那契数列
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b
        a, b = b, a + b
        n += 1
    return '没有更多元素了'  # 此处往往放报错的提示


x = fib(5)
print(next(x))  # 得到：1
print(next(x))  # 得到：1
print(next(x))  # 得到：2
print(next(x))  # 得到：3
print(next(x))
print(next(x))
