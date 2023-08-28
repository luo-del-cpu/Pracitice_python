# @Time : 2023/8/27 23:50
# @Author : luoxin

"""
字符串的内建函数：
1：大小写相关
str.capitalize():将首字母转换为大写
str.title():将字符串中的每个单词的首字母转换为大写
str.upper():将字符串中字母转换为大写
str.lower():将字符串中字母转换为小写
"""
s1 = 'abc'
print(s1.capitalize())

s='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0987654321'
code=''

import random
for i in range(4):
    ran = random.randint(0, len(s) - 1)
    code += s[ran]
print("验证码是：",code)

user_input= input("输入验证码:")

#判断用户输入是否与验证码相同，需要都转化为小写已保证兼容性
if user_input.lower() == code.lower():
    print("验证码正确！")
else:
    print("验证码错误！")
"""
2：查找与替换

str.find():查找字符第一次出现的索引，如果没有找到，则返回-1
str.rfind():从右侧开始找第一个字符出现的索引
str.replace(old,new,[max]):替换想要的字符，max为最大替换次数
"""

s='abcdef'
pos = s.find('b')
print(pos)
#输出：1

s='https://blog.csdn.net/qq_44702847/article/details/102663643'
p=s.rfind('/')
print(s[p+1:])
#s输出：102663643


"""
3：编码与解码

str.encode()
str.decode()
"""

"""
4：判断开头与结尾
返回值是布尔类型
str.startswith()
str.endswith()
"""

"""
5：判断字符是否为字母/数字
返回类型是布尔类型

str.isalpha()
str.isdigt()
"""