# 在开发中看到一些私有化处理：装饰器

class Person():
    def __init__(self, name, age):
        self.name = name  # 加了__以后表示将属性私有化,访问范围仅仅在类中
        self.__age = age

    # 定义公有set和get方法:使用装饰property装饰器
    # 必须先定义get,在定义set
    @property  # 使用此装饰器的好处是可以像没有私有化属性一样，直接使用“对象.方法名”直接调用方法
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 100:
            self.__age = age
            print("修改成功，年龄是：", self.__age)
        else:
            print('超出年龄范围')

    # set为了赋值
    # def setAge(self, age):
    #     if age < 100:
    #         self.__age = age
    #         print("修改成功，年龄是：", self.__age)
    #     else:
    #         print('超出年龄范围')

    # get为了取值
    # def getAge(self):  # 注意：此处getxxx必须使用return返回
    #     return self.__age

    def __str__(self):  # 注意：此处使用str必须使用return且返回的是字符串
        return '姓名：{} 年龄：{} '.format(self.name, self.__age)


p1 = Person('张三', 18)
print(p1)
print(p1.age)  # 得出：18
p1.age = 90
print(p1.age)
