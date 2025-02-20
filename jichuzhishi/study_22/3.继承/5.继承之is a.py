# is a :base class 父类，基类
"""
子类重写与父类的同名方法方法 之 子类中和父类中的方法参数不一致
    子类的方法中也可以调用父类方法：
            super().方法名（参数）
"""


class Person:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('{}正在跑步'.format(self.name))


class Student(Person):
    def __init__(self, name, clazz):
        super().__init__(name)
        # student自己特殊的属性也可以单独定义
        self.clazz = clazz

    def run(self,student_method): # 这里只是警告，并不代表有错误

        # 继承父类的方法：实际先会执行父类的方法，在执行子类自己的方法
        super().run()
        print('{}：学生类自己的跑步方法:{}'.format(self.name,student_method))
# is a :base class 父类，基类
"""
子类重写与父类的同名方法方法 之 子类中和父类中的方法参数不一致
    子类的方法中也可以调用父类方法：
            super().方法名（参数）
"""


class Person:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('{}正在跑步'.format(self.name))


class Student(Person):
    def __init__(self, name, clazz):
        super().__init__(name)
        # student自己特殊的属性也可以单独定义
        self.clazz = clazz

    def run(self,student_method): # 这里只是警告，并不代表有错误

        # 继承父类的方法：实际先会执行父类的方法，在执行子类自己的方法
        super().run()
        print('{}：学生类自己的跑步方法:{}'.format(self.name,student_method))


s =Student('tom',10)
s.run('子类自己方法的参数') # 得出:tom正在跑步
                        # tom：学生类自己的跑步方法:子类自己方法的参数


s =Student('tom',10)
s.run('子类自己方法的参数') # 得出:tom正在跑步
                        # tom：学生类自己的跑步方法:子类自己方法的参数
