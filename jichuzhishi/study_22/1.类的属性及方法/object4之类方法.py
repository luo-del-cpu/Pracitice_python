# 类方法
"""
特点：
    1.定义需要依赖装饰器：@classmethod
    2.类方法中参数不是一个对象，而是当前的这个类（cls）
    3.类方法中只可以使用类属性，不可以使用对象属性（因为类方法在对象加载前就已经产生了）
    4.类方法中不可调用普通方法

作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些动作（功能）可以使用此方法
"""


class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{}在吃饭'.format(self.name))

    def run(self):
        print('{}在跑步'.format(self.name))
        # self.eat()  # 类中的【普通方法】相互调用，需要通过self.方法名（）

    # 看见有这个装饰器，就会自动将类传入方法
    @classmethod
    def test(cls):  # 此处的cls实际是一个类，这个就是Dog类
        print(cls)  # <class '__main__.Dog'>
        # print(cls.name)#报错，因为类中没有name属性，只有对象有这个属性


dog1 = Dog('大黄')
dog1.run()
dog1.test() # 也可使用对象调用类方法

print("*"*20+"类方法的补充"+"*"*20)

class Person:
    age = 19

    def show(self):
        print('年龄是：', Person.age) # 在使用类属性的时候，使用：类名.属性的方式调用

    @classmethod
    def update_age(cls):
        cls.age = 20
        print('---->类方法')

p = Person()
p.age = p.age + 1
print(p.age) # 打印出来时20，在对象中已经对age做了+1操作，如上一步
p.show() # 打印出来依然是19，因为类属性没有改变
Person.update_age()
print(Person.age) # 打印出来时20，因为上一步调用了类方法，类方法中将age属性改为了20

print("*"*20+"类属性的私有化"+"*"*20)

class Person1:
    __age = 19  # 加了__以后，就变成了私有化，就无法在类以外的地方访问；例如无法在使用Person.age进行访问

    def show(self):
        print('年龄是：', Person1.__age) # 在使用类属性的时候，使用：类名.属性的方式调用

    @classmethod
    def update_age(cls):
        cls.__age = 20
        print('---->类方法')

    @classmethod
    def show_age(cls):
        print('修改后的年龄：', cls.__age)


Person1.update_age() # print(Person1.__age) # 无法访问，因为属性已经被私有化了
Person1.show_age() # 输出年龄为20
