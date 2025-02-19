# 装饰器
"""
特点：
1.函数A是作为参数出现的（函数B就接收函数A作为参数）
2.要有闭包的特点
"""


def decorator(f):
    def wrapper(*args, **kwargs):  # 万能装饰器：使用可变参数来定义,可以在被装饰函数传参过来的时候可以接到
        print('这是一个装饰器！')
        print("内部函数*args的值:",*args)
        print("内部函数**kwargs的值:", kwargs)
        f(*args,**kwargs)

    return wrapper


@decorator
def func1(n):  # 在被装饰函数有传参的时候，要记得在装饰器中的内层函数中同样传参，如上装饰器所示
    print('----这是第一个测试函数！----')
    print('打印n的值：', n)
func1(2)

print("*"*50)

@decorator
def func2(a, b):
    print('----这是第二个测试函数！----')
    print('打印a和b的值：', a, b)
func2(1, 2)
print("*"*50)
#
#
@decorator
def func3(m):
    print('----这是第三个测试函数！----')
    print("m:",m)
    for stu in m:
        print('打印学生姓名：', stu)

studerts = ['张三', '李四']

func3(studerts)
print("*"*50)

@decorator
def func4(studerts, clazz='101'):
    print('----这是第四个测试函数！----')
    for i in studerts:
        print('{}的班级是{}'.format(i, clazz))

studerts = ['张三', '李四']
func4(studerts,clazz='102')