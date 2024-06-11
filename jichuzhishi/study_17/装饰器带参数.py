# 装饰器带参数
'''
带参数的装饰器时三层的
最外层的函数负责接收装饰器的参数
里面的内容还是原装饰器的内容
'''


def outter(a):  # 第一层：负责接收装饰器参数的
    def decorate(func):  # 第二层：负责接收函数的
        def wrapper(*args, **kwargs):  # 第三层：负责接收函数的实参的
            func(*args, **kwargs)
            print('铺地板砖{}块'.format(a))

        return wrapper  # 返回的是：第三层

    return decorate  # 返回的是：第二层


@outter(a=10)
def fang_zi(time):
    print("我在{}是一个毛坯房！".format(time))


fang_zi('2021-05-05')


@outter(100)
def xiu_lu():
    print('新修街道：北京路')


xiu_lu()
