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


if __name__ == '__main__':  # 此处定义了这个以后，在caculate中就不会调用以下的内容；在本模块中调用此__name__
    # 得到的就是__main__;如果是其它模块调用此__name__,得到的就是其它模块的名字
    test2()
