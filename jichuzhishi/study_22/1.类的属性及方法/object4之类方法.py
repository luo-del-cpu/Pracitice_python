# 类方法
'''
特点：
    1.定义需要依赖装饰器：@classmethod
    2.类方法中参数不是一个对象，而是当前的这个类
    3.类方法中可以使用类属性
    4.类方法中不可使用普通方法

作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些动作（功能）
'''


class Dog():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{}在吃饭'.format(self.name))

    def run(self):
        print('{}在跑步'.format(self.name))
        # self.run()  # 类中的【普通方法】相互调用，需要通过self.方法名（）

    @classmethod
    def test(cls):  # 此处的cls实际是一个类，这个就是Dog类
        print(cls)  # <class '__main__.Dog'>
        # print(cls.name)#报错


dog1 = Dog('大黄')
dog1.run()
dog1.test()


class Person():
    __age = 19  # 加了__以后，就无法在类以外的地方访问；例如无法在使用Person.age进行访问

    def show(self):
        print('年龄是：', Person.__age)

    @classmethod
    def test(cls):
        cls.__age = 20
        print('---->类方法')

    @classmethod
    def show_age(cls):
        print('修改后的年龄：', cls.__age)


# p = Person()
# # p.age = p.age + 1
# p.show_age
Person.test()
Person.show_age()
