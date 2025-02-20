# is a :base class 父类，基类
"""
子类重写init方法之定义自己独有的属性与方法:
    1:定义独有的属性：
        class A:
            def __init__(self,name):
                self.name=name

        class B(A):
            def __init__(self,name,clazz):
            super().__init__(name)
    2:定义独有的方法
        class A:
            def __init__(self,name):
                self.name=name
            def aaa(self):
                pass

        class B(A):
            def __init__(self,name,clazz):
            super().__init__(name)

            def bbb(self,arg):
                pass
"""


class Person:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('{}正在跑步'.format(self.name))


class Student(Person):
    # student自己特殊的属性（clazz）也可以单独定义
    def __init__(self, name, clazz):
        super().__init__(name)
        self.clazz = clazz

    # 可以定义独属于自己类的方法
    def study(self,course):
        print(f"{self.name}正在{self.clazz}班学习{course}")


class Doctor(Person):
    def __int__(self, name, patients):
        super().__init__(name)
        self.patients = patients

s =Student('tom',10) # 此处传参就需要根据student类中定义的init方法来传参
s.run() # 得出：tom正在跑步
s.study("python") # 得出：tom正在10班学习python