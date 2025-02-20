# is a :base class 父类，基类
"""
子类重写方法之重写父类中的同名方法
    方法调用问题：
            a:如果父类有eat(),子类也定义一个eat(),默认搜索的原则：先找当前类，当前类没有再去找父类；此种行为就叫重写（override）
                父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写
"""


class Person:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('{}正在跑步'.format(self.name))


class Student(Person):
    def __init__(self, name, clazz):
        super().__init__(name)
        self.clazz = clazz

        # 定义与父类中同名的方法，叫重写；
    def run(self):
        print('{}：学生类自己的跑步方法:{}'.format(self.name,"子类自己方法的参数"))


s =Student('tom',10)
# 只会去找里自己类中最近的方法
s.run() # 得出：tom：学生类自己的跑步方法:子类自己方法的参数
