# 私有化
# 封装：1.私有化属性 2.定义公有的set和get方法
'''
dir():
函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
带参数时，返回参数的属性、方法列表。
如果参数包含方法__dir__()，该方法将被调用。
如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
'''
'''
私有化的好处：
1.隐藏属性，不被外界随意修改
2.也可以修改：通过函数完成
    def setXXX（self,xxx）
        3.筛选赋值内容：
            if xxx:
                pass
            else:
                pass
4.如果想获得具体的某一属性
    使用getxxx函数
        def getxxx(self,xxx)
            return self.__xxx

'''


class Person():
    def __init__(self, name, age):
        self.__name = name  # 加了__以后表示将属性私有化,访问范围仅仅在类中
        self.__age = age

    # 定义公有set和get方法
    # set为了赋值
    def setAge(self, age):
        if age < 100:
            self.__age = age
            print("修改成功，年龄是：", self.__age)
        else:
            print('超出年龄范围')

    def setName(self, name):
        if len(name) == 6:
            self.__name = name
            print("修改成功，名字是：", self.__name)
        else:
            print('名字不是六位')

    # get为了取值
    def getAge(self):  # 注意：此处getxxx必须使用return返回
        return self.__age

    def __str__(self):  # 注意：此处使用str必须使用return且返回的是字符串
        return '姓名：{} 年龄：{} '.format(self.__name, self.__age)


p1 = Person('张三', 18)
print(p1)
# print(p1.__age)#此处想访问内部的私有化属性，无法访问
p1.setAge(20)
p1.setName('aaaaaa')
print(p1)
print(p1.getAge())  # 通过getxxx方法拿到私有化属性的值
print(dir(Person))
print(dir(p1))
