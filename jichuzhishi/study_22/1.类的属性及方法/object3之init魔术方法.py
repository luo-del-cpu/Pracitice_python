# 类里面定义的函数就叫方法,类外的叫函数
"""
魔术方法之一：只要是__名字__()这种格式的就是系统内置的魔术方法:
    __init__(self)方法:初始化对象属性
"""


class Phone:
    # 保证每个对象中都有初始化的属性;执行时间是在将内存空间给对象之前，此时的self是开辟出来准备给对象的内存地址，还没有赋值给对象
    def __init__(self):
        # 可以在控制台看到，此处是最先打印出来的
        print('--->init方法')
        # 动态的给self（马上要赋值给的对象）空间中添加了两个固定的属性：brand price；类中没有这些参数
        self.brand = 'xiaomi'
        self.price = 1000

    def call(self):
        print('---->call')
        # 初始化中的属性必须使用self.xxx来使用
        print('price:', self.price)
        print('brand:', self.brand)


p1 = Phone()
print(p1)
p1.call()  # 注意：此处对象在调用方法的执行顺序是：先创建一个对象（申请一个照着Phone“模子”一样的内存空间,如上一步）-->去找Phone类中
# 是否有__init__(self)方法【用于初始化】-->如果有，执行init中的代码，然后在将内存空间分配给p1;如果没有，直接将内存空间给p1

print("*"*50)

"""
方法使用补充说明:
1：可以在初始化方法中传入参数，用于在【创建对象时要求传参】
2：可以在类中的普通方法中定义参数，用于在【对象调用方法时要求传参】
"""


class People:
    # 此处写了两个参数,用于定义在创建对象时，【必须传递两个参数】；方便对象初始化属于自己的属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 此处定义了一个food参数，用于在对象调用方法时必须传递参数
    def eat(self, food):
        # 在使用初始化的属性【必须使用self.xxx调用】；类中的方法参数可直接使用
        print('{}吃了{}'.format(self.name, food))

    # 此方法没有定义参数，所以在使用时不用传递参数
    def run(self):
        print('{}今年{}岁，正在跑步！'.format(self.name, self.age))


people1 = People('张三', 18)
print(people1.name) # 张三
people1.name = 'lisi' # 对象属性修改
people1.eat('红烧肉') # 使用eat方法必须传递参数，得出：lisi吃了红烧肉
people1.run() # 使用run方法可以不传递参数，得出：lisi今年18岁，正在跑步！

people2 = People('王五', 18)
people2.age = '10'
people2.eat('鱼香肉丝')
people2.run()

people3 = People('赵四', 10)
people3.run()
