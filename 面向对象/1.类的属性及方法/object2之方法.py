# 类中方法：动作
# 种类：普通方法 类方法 静态方法 魔术方法
'''
普通方法格式：
    def 方法名（self[参数，参数]）：
    pass
'''


class Phone():
    brand = 'xiaomi'
    price = 2000
    type = 'k30'
    def __init__(self,note,address_book):
        self.note = note
        self.address_book = address_book
    # Phone类里面方法：call
    def call(self):
        print('self------>', self)
        print('打电话...')
        print('留言：', self.note)  # 注意：实际此处的self就是对象调用方法时传进来的对象
        print('正在访问通讯录...')
        for person in self.address_book:#注意：此处有阴影是因为在phone2对象中没有address_book属性
            print(person.items())

phone1 = Phone('1',[{'121212':'zhangsan'},{'323232':'lisi'}])
#print(phone1)  # 得出：<__main__.Phone object at 0x000002131F5EE280>
phone1.note = '这是phone1的note'
phone1.address_book = [{'121212':'zhangsan'},{'323232':'lisi'}]
phone1.call()  # 得出：self------> <__main__.Phone object at 0x000002131F5EE280>
                    # 打电话...（此处说明只要对象调用类中的方法，就会将对象本身当做参数传递给self）
print('*'*60)

# phone2 = Phone()
# #print(phone2)
# phone2.note = '这是phone2的note'
# phone2.call()