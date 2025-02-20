"""
静态方法：很类似于类方法
1.需要装饰器@staticmethod
2.静态方法是无需传递参数（cls,self都是不需要的）
3.也只能访问类的属性和方法，对象的是无法访问的
4.加载时机同类方法
"""


class Person:
    __age = 19

    def __init__(self, name):
        self.name = name

    def show(self):
        print('年龄是：', Person.__age)

    @classmethod
    def test(cls):
        cls.__age = 20
        print('---->类方法')

    @classmethod
    def show_age(cls):
        print('显示类属性的年龄：', cls.__age)

    @staticmethod
    def test2():
        # print(self.name)  # 语法的错误，静态方法是无法访问对象的属性的
        print('--->静态方法')
        print(Person.__age) # 直接使用：类名.属性访问
        # Person.show_age() # 可以通过类访问到类方法

Person.show_age() # 输出：19
Person.test() # 修改类属性age为20
Person.test2() # 输出：20
p = Person("tom")
p.test2() # 也可使用对象调用静态方法
