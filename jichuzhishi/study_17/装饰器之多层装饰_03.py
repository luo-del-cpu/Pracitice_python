# @Time : 2025/2/19 21:21
# @Author : luoxin

"""
如果装饰器是多层的，那么谁离函数最近就优先使用哪个装饰器，装饰完成后在使用下一个装饰器
"""
def zhuang_1(func5):
    print('----这是第一个装饰器开始！----')
    def wrapper_1(*args,**kwargs):
        func5()
        print('刷漆')
    print('----第一个装饰器状装饰完成！----')
    return wrapper_1

def zhuang_2(func6):
    print('----这是第二个装饰器开始！----')
    def wrapper_2(*args,**kwargs):
        func6()
        print('装地板')
        print('房子装修完毕！')

    print('----第二个装饰器状装饰完成！----')
    return wrapper_2

@zhuang_2
@zhuang_1
def fang_zi():
    print('我是一个毛坯房！')
fang_zi()