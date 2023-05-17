# 猫
class Cat():
    type = '猫'  # 注意：类属性一般是不变的;类属性就是给类对象定义的属性,通常用来记录与这个类相关的特征,
                 # 类属性不会用于记录具体对象的特征。

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def eat(self, food):
        print('{}吃了{}'.format(self.name, food))

    def catch_mouse(self, color, weight):
        print('{}抓了一只{}kg的{}大老鼠'.format(self.name,weight, color))

    def sleep(self, hour):
        if hour < 5:
            print('不能睡了！')
        else:
            print('继续睡吧！')

    def show(self):
        print('猫的信息：')
        print(self.color)
        print(self.age)


# 创建对象
cat1 = Cat('小白', '白色', 2)

# 通过对象调用方法
cat1.eat('小金鱼')
cat1.catch_mouse('黑色',2)
