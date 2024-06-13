# is a :base class 父类，基类
'''
继承：
    子类：
    Student Empioyee Doctor
    父类：
    Person
将子类相同的代码提取至父类，让三个子类继承父类
格式：
    class Student(Person):
        pass
特点：
    1.init调用问题：
        a:如果子类中不定义__init__，则调用父类super class的init
        b:如果子类继承了父类，但是子类也需要定义自己的__init__，就需要在当前子类中也调用一下父类__init__
            如何调用父类__init__:
                super().__init__(参数)
                super(类名，对象).__init__(参数)
    2.方法调用问题：
        a:如果父类有eat(),子类也定义一个eat(),默认搜索的原则：先找当前类，再去找父类；此种行为就叫重写（override）
            父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写
    3.子类的方法中也可以调用父类方法：
        super().方法名（参数）

复习顺序：
1.init方法
2.重写方法
'''

"""
子类重写init方法之继承父类的init方法
"""
class Person:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('{}正在跑步'.format(self.name))


class Student(Person):
    def __init__(self,name):
        print('--->子类的init')
        # 使用super()将父类的init全部继承,父类传参，这里也必须传参
        super().__init__(name)

class Doctor(Person):
    pass
s = Student('tom')
s.run()  # 得出：tom正在跑步

d = Doctor('jack')
d.run()
