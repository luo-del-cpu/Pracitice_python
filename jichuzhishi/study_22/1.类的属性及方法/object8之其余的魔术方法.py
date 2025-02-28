"""
魔术方法：
1.__init__：初始化魔术方法
触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）
参数：至少有一个self，接收对象
返回值：无
作用：初始化对象的成员
注意：使用该方式初始化的成员都是直接写入对象当中，类中无法具有

2.__new__方法：实例化魔术方法
触发时机： 在实例化对象时触发
参数：至少一个cls 接收当前类
返回值：必须返回一个对象实例
作用：实例化对象
注意：实例化对象是Object类底层实现，其他类继承了Object的__new__才能够实现实例化对象。
没事别碰这个魔术方法，先触发__new__才会触发__init__

3.__del__:析构魔术方法
触发时机：当对象没有用（没有任何变量引用）的时候被触发
参数：一个self
返回值：无
作用：使用完对象是回收资源
注意：del不一定会触发当前方法，只有当前对象没有任何变量接收时才会触发

4.__call__:调用对象的魔术方法
触发时机:将对象当作函数调用时触发
参数:至少一个self接收对象，其余根据调用时参数决定
返回值：根据情况而定
作用：可以将复杂的步骤进行合并操作，减少调用的步骤，方便使用
注意：无

5.__str__:
触发时机:使用print(对象)或者str(对象)的时候触发
参数：一个self接收对象
返回值：必须是字符串类型
作用：print（对象时）进行操作，得到字符串，通常用于快捷操作
注意：一定要return值
作用的解释：单纯打印对象名称，出来的是一个地址，地址对于开发者来说没有太大意义
    如果想在打印对象名的时候能够给开发者多一些信息
"""

"""
__init__(self),__str__(self)重点关注。
"""

class Stu:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

stu = Stu("tom")
# 如果不加str方法，则打印：<__main__.Stu object at 0x105bbcdf0>
# 加了str方法，则打印：tom
print(stu)


