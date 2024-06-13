# is a :base class 父类，基类
"""
子类重写init方法之定义自己独有的属性
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


class Doctor(Person):
    def __int__(self, name, patients):
        super().__init__(name)
        self.patients = patients


s =Student('tom',10) # 此处传参就需要根据student类中定义的init方法来传参
s.run()