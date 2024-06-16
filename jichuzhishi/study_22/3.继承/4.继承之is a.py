# is a :base class 父类，基类
"""
子类重写方法之定义自己独有的方法
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

        # 定义自己的同名方法，叫重写；实际先会执行父类的方法，在执行子类自己的方法
    def run(self,student_method): # 这里只是警告，并不代表有错误

        # 继承父类的方法
        super().run()
        print('{}：学生类自己的跑步方法:{}'.format(self.name,student_method))


s =Student('tom',10) # 此处传参就需要根据student类中定义的init方法来传参
s.run('子类自己方法的参数')
