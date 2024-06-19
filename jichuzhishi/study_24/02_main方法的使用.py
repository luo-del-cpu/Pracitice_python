__all__ = ['add', 'number', 'test2']  # 此处限制了可被引用的东西，在列表里的都是可以被调用的
# 变量
number = 100


# 函数
def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum

    else:
        print('至少传入两个参数！')


def minus(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m -= i
        return m
    else:
        print('至少传入两个参数！')


# 类
class Caculate():
    def __init__(self, num):
        self.num = num

    def show(self):
        print('caculate中的类')

    @classmethod
    def test1(cls):
        print('caculate中的类方法')


def test2():
    print('我是测试')


if __name__ == '__main__':
    """
     此处定义了这个以后，在其他模块中调用此模块（caculate）时就不会调用下方的内容；
     原理：
         在本模块中调用此__name__得到的就是__main__;就会执行下方内容；
         如果是其它模块调用此__name__,得到的就是其它模块的名字；
         例如：定义了A模块，并且写了__name__,B模块导入了A模块；
         在B模块执行时，A模块下方的内容不会执行，只有在A模块本身执行时，才会执行下方的内容，因为在本模块中
         打印出来的__name__就是等于__main__,在其他模块执行时，__name__是等于A且不等于__main，所以不会执行
    """
    test2()
