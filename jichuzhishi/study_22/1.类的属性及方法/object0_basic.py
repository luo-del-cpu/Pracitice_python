"""
面向对象：把构成问题事务分解成各个对象，建立对象的目的不是为了完成一个步骤，而是为了描叙某个事物在整个解决问题的步骤中的行为。
    四大关键：类，属性，方法，对象
    三大特性：封装、继承、多态
    具象理解：
        程序---->     现实中
        对象---->     具体的事物
    好处：
        曹操做匾，改一处不会影响其他的地方
    举例：
        对象：
            张三的手机
            李四的手机
            王五的手机
            ...
            以上就是对象的集合  --->共同特征：品牌 颜色 大小 价格  动作：打电话 发短信 上网 打游戏

        类别：学生类
        特征：姓名 年龄 性别...---->属性
        动作：打篮球 听音乐...---->方法

    总结：多个对象--->提取对象的共同特征和动作--->封装到一个类中
    重点：类中放的属性只放对象共有的属性和方法

    命名：所有的类名要求首字母大写，多个单词使用驼峰式命名，例如People,RequestUntil
    注意：在python中要求所有的类都继承于object类，在python3中默认继承，可以不写
    格式：
        class 类名[(父类)]
            属性：特征
            方法：动作
"""

class Phone:
    pass
    # 属性：此处在类中可以不定义任何属性与方法，格式正确即可
    brand = 'Huawei'


# 使用类创建对象
phone1 = Phone()  # 创建一个手机对象
phone2 = Phone()
print(phone1)  # 得出：<__main__.Phone object at xxxxxxxx>；为创建的对象分配一个内存空间
print(phone1.brand)  # 得出：Huawei；从类中找出对应的属性
phone1.brand = 'oppo' # 修改phone1对象中的brand为oppo
print(phone1.brand)  # 得出：oppo；修改phone1的属性，只是修改自己的属性，并不会影响类中的属性和其它对象的属性
print(Phone.brand)  # 得出：Huawei，类中的属性依然是Huawei
print(phone2.brand) # 得出：Huawei，phone2对象中的属性依然是Huawei
