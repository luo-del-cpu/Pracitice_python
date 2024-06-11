# 装饰器
'''
特点：
1.函数A是作为参数出现的（函数B就接受函数A作为参数）
2.要有闭包的特点
'''


def decorater(f):
    def wrapper(*args, **kwargs):  # 万能装饰器：使用可变参数来定义,可以在被装饰函数传参过来的时候可以接到
        print('这是一个装饰器！')
        print("内部函数*args的值",*args)
        print("内部函数**kwargs的值", **kwargs)
        f(*args,**kwargs)

    return wrapper


# @decorater
# def func1(n):  # 在被装饰函数有传参的时候，要记得在装饰器中的内层函数中同样传参，如上装饰器所示
#     print('----这是第一个测试函数！----')
#     print('打印n的值：', n)
# func1(2)
# print("*"*50)
#
# @decorater
# def func2(a, b):
#     print('----这是第二个测试函数！----')
#     print('打印a和b的值：', a, b)
# func2(1, 2)
# print("*"*50)
#
#
# @decorater
# def func3(m):
#     print('----这是第三个测试函数！----')
#     print("m:",m)
#     for stu in m:
#         print('打印学生姓名：', stu)
#
# studerts = ['张三', '李四']
#
# func3(studerts)
# print("*"*50)

@decorater
def func4(studerts, clazz='101'):
    print('----这是第四个测试函数！----')
    for i in studerts:
        print('{}的班级是{}'.format(i, clazz))

print('------这是第一遍执行结果开始--------')
studerts = ['张三', '李四']
func4(studerts)
print('------这是第一遍执行结果结束---------')
#
# '''
# 如果装饰器是多层的，那么谁离函数最近就优先使用哪个装饰器，装饰完成后在使用下一个装饰器
# '''
# def zhuang_1(func5):
#     print('----这是第一个装饰器开始！----')
#     def wrapper_1(*args,**kwargs):
#         func5()
#         print('刷漆')
#     print('----第一个装饰器状装饰完成！----')
#     return wrapper_1
#
# def zhuang_2(func6):
#     print('----这是第二个装饰器开始！----')
#     def wrapper_2(*args,**kwargs):
#         func6()
#         print('装地板')
#         print('房子装修完毕！')
#
#     print('----第二个装饰器状装饰完成！----')
#     return wrapper_2
#
# @zhuang_2
# @zhuang_1
# def fang_zi():
#     print('我是一个毛坯房！')
# fang_zi()