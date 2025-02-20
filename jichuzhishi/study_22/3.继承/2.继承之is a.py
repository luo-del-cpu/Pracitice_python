"""
继承之is a :base class 父类，基类
    1.举例
        子类：
        Student Employee Doctor
        父类：
        Person
    2.定义
        1.原则：将子类相同的代码提取至父类，让三个子类继承父类
        2.格式：
            class Person:
                pass
            class Student(Person):
                pass
    3.特点：
        1.init调用问题：
            a:如果子类中不定义__init__，则调用父类super_class的init
            b:如果子类继承了父类，但是子类也需要定义自己的__init__，就需要在当前子类中也调用一下父类__init__
                如何调用父类__init__:
                    super().__init__(参数)
                    super(类名，对象).__init__(参数)
"""

"""
子类重写init方法之继承父类的init方法
    注意:如果父类中有私有属性，那么子类也不可继承
"""


class Person:
    # 父类初始化了参数，那么子类继承时也必须传入参数，如54行
    def __init__(self, name):
        self.name = name

    def run(self):
        print('{}正在跑步'.format(self.name))


class Student(Person):
    # 只要是子类继承了父类且子类重写了init方法，那么父类的init方法就不会调用，只会调用子类的init方法
    # 通常子类定义了自己的init方法，都需要继承一下父类的init方法
    def __init__(self, name):
        # 其实此处也可以通过self初始化属性，但是因为继承的思想，父类init方法已经有了，所以最好直接继承，如下super()
        # self.name = name
        print('--->子类的init')
        # 使用super()将父类的init全部继承,父类传参，这里也必须传参，【实际上是在子类创建对象的时候将参数传进来，然后通过super()在将参数传回给父类使用】
        super().__init__(name)


class Doctor(Person):
    pass


s = Student('tom')
s.run()  # 得出：tom正在跑步

# 此处Doctor类中实际没有定义自己的init方法，所以就直接继承了父类的init方法，父类定义必须传参，所以此处就必须传递参数
d = Doctor('jack')
d.run() # 得出：jack正在跑步
