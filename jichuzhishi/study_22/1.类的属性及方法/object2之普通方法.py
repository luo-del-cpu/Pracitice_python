# 类中方法：动作
# 种类：普通方法 类方法 静态方法 魔术方法
"""
普通方法格式：
    def 方法名（self[参数，参数]）：
    pass
"""


class Phone:
    brand = 'xiaomi'
    price = 2000
    type = 'k30'

    # Phone类里面方法：call
    def call(self):  # 注意：实际此处的self就是在创建对象时传过来的自身
        print('self------>', self)
        print('打电话...')



phone1 = Phone()
print(phone1)  # 得出：<__main__.Phone object at 0x000002131F5EE280>
phone1.call()  # 得出：self------> <__main__.Phone object at 0x000002131F5EE280>
# 打电话...（此处说明只要对象调用类中的方法，就会将对象本身当做参数传递给self）

"""
解释：
从上面打印出来的phone1对象的内存地址和在调用call()方法时，方法内部打印的self的内存地址看出，
两个内存地址相同，表示实际类中的self就是代表要传入的对象
"""
