"""
多态：
Python中，在类中接收的其它“大”类型的对象，可以传这个“大”的类型（父类）对象和可以传它下面的所有“小”的类型（子类）的对象，
也可以传不是它的“小”类型的对象；例如下述所示：在Person类中的feed_pet方法中接收了一个pet,此处的pet就可以
接受“大”类型（Pet）的对象，也可以接受“小”类型（子类）cat,dog的对象，也可以接收不是它的子类tiger对象,只不过
要用if isinstance(obj,类)来判断一下，传入的参数是否是“大”类型或者“大”类型下“小”类型的对象；但是在其它语言中，这里就不能实现
"""
class Person():
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):  # 此处定义的pet是用于接收方法调用时传进来的对象，既可以接收cat，dog,也可以接收tiger
        # if isinstance(obj,类)--->判断obj是不是类的对象或者判断obj是不是该类子类的对象
        if isinstance(pet, Pet):
            print()
            print('{}喜欢养宠物：{}，昵称是：{}'.format(self.name, pet.role, pet.nickname))  # 此处打印不能使用self
            # 来调用其它类里的方法，只能使用对象.属性来调用
        else:
            print('不是宠物类型')


class Pet():
    role = 'pet'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show_name(self):
        print('昵称：{}，年龄：{}'.format(self.nickname, self.age))


class Cat(Pet):
    role = '猫'

    def cat_mouse(self):
        print('抓老鼠')


class Dog(Pet):
    role = '狗'

    def watch_house(self):
        print('看家')


class Tiger():  # 此处没有继承父类Pet,没有父类初始化的类属性和无法使用类里的方法
    def eat(self):
        print('吃人')


# 创建对象：
cat = Cat('花花', 2)
dog = Dog('大黄', 2)
person = Person('张三')
person.feed_pet(cat)  # 此处传值传的是一个对象
print('-------------------')
tiger = Tiger()
person = Person('李四')
person.feed_pet(tiger)
