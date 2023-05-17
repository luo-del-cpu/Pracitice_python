# 静态方法
'''
静态方法：很类似于类方法
1.需要装饰器#staticmethod
2.静态方法是无需传递参数（cls,self都是不需要的）
3.也只能访问类的属性和方法，对象的是无法访问的
4.加载时机同类方法

总结类方法和静态方法：
不同之处：
1.装饰器不同
2.类方法有参数，静态方法无参数

相同之处：
1.只能访问类的属性和方法，对象的是无法访问的
2.都可以通过类名调用访问
3.都可以在创建之前使用，因为是不依赖于对象的

普通方法与上述两者的区别：
不同之处：
1.普通方法不依赖于装饰器
2.普通方法永远要依赖对象，因为每个普通方法都有一个self
3.只有创建了对象才可以调用普通方法，否则无法调用
'''


class Person():
    __age = 19  # 加了__以后，就无法在类以外的地方访问；例如无法在使用Person.age进行访问

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
        print('修改后的年龄：', cls.__age)

    @staticmethod
    def test2():
        # print(self.name)  # 语法的错误，静态方法是无法访问对象的属性的
        print('--->静态方法')
        print(Person.__age)


Person.test()
Person.show_age()
Person.test2()
