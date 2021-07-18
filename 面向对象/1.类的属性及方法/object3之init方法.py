# 函数 和 类里面定义的：方法  区别就是在类里面定义的函数就叫方法
# class Phone:
#     # 魔术方法之一：只要是__名字__()这种格式的就是系统内置的魔术方法
#     def __init__(self):#保证每个对象中都有初始化的属性;执行时间是在将内存空间给对象之前；
#                         #此时的self是开辟出来准备给对象的内存地址，还没有赋值给对象
#         print('--->init方法')
#         self.brand = 'xiaomi'
#         self.price = 1000  #动态的给self（马上要赋值给的对象）空间中添加了两个属性：brand price
#
#     def call(self):
#         print('---->call')
#         print('price:', self.price)
#
#
# p1 = Phone()
# p1.call() #注意：此处对象在调用方法的执行顺序是：先创建一个对象（申请一个照着Phone“模子”一样的内存空间）-->去找Phone类中
#           #是否有__init__(self)方法【用于初始化】-->如果有，执行init中的代码，然后在将内存空间分配给p1;如果没有，
#           #直接将内存空间给p1
#
# p2 = Phone()
# p2.call()

#方法使用补充说明

class test():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self,food):
        print('{}吃了{}'.format(self.name,food))
    def run(self):
        print('{}今年{}岁，正在跑步！'.format(self.name,self.age))

a1 = test('张三',18)
a1.name = 'lisi'
a1.eat('红烧肉')
a1.run()

a2 = test('王五',18)
a2.age = '10'
a2.eat('鱼香肉丝')
a2.run()

a3 = test('赵四',10)
a3.run()



